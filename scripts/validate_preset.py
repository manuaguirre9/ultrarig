#!/usr/bin/env python3
"""
UltraRig Preset Validator (scripts/validate_preset.py)
Validates the syntax, schema, DSP routing graph, and parameter ranges
of UltraRig preset JSON files for M-VAVE multi-effects pedals.

Usage:
    python scripts/validate_preset.py path/to/preset.json
    python scripts/validate_preset.py --dir presets/
    python scripts/validate_preset.py preset1.json preset2.json --strict
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

# Terminal color styling
USE_COLOR = sys.stdout.isatty() and os.name != "nt" or "WT_SESSION" in os.environ or "TERM" in os.environ

def color(text: str, code: str) -> str:
    return f"\033[{code}m{text}\033[0m" if USE_COLOR else text

def red(text: str) -> str: return color(text, "31")
def green(text: str) -> str: return color(text, "32")
def yellow(text: str) -> str: return color(text, "33")
def cyan(text: str) -> str: return color(text, "36")
def bold(text: str) -> str: return color(text, "1")

# Recognized hardware targets & DSP limits
VALID_PEDAL_MODELS = {"tank-g", "tank-g v1", "tank-g v2", "tank-b", "black box", "universal"}
VALID_BLOCK_TYPES = {
    "gate", "noise_gate",
    "compressor", "comp",
    "drive", "overdrive", "distortion", "fuzz", "boost",
    "nam", "nam_capture", "amp",
    "ir", "cabinet", "cab",
    "eq", "parametric_eq", "graphic_eq",
    "mod", "chorus", "flanger", "phaser", "tremolo", "vibrato",
    "pitch", "pitch_shift", "octave", "whammy",
    "delay", "analog_delay", "digital_delay", "tape_delay",
    "reverb", "hall_reverb", "plate_reverb", "spring_reverb",
    "volume", "gain",
    "split", "merge"
}

VALID_SCENE_KEYS = {"a", "b", "c", "d", "0", "1", "2", "3", "scene_a", "scene_b", "scene_c", "scene_d"}

class ValidationError:
    def __init__(self, message: str, is_warning: bool = False, key_path: str = ""):
        self.message = message
        self.is_warning = is_warning
        self.key_path = key_path

    def __str__(self) -> str:
        prefix = yellow("[WARN]") if self.is_warning else red("[ERROR]")
        path_str = f" at '{self.key_path}'" if self.key_path else ""
        return f"{prefix}{path_str}: {self.message}"

class PresetValidator:
    def __init__(self, strict: bool = False):
        self.strict = strict
        self.errors: List[ValidationError] = []

    def log_error(self, message: str, key_path: str = "") -> None:
        self.errors.append(ValidationError(message, is_warning=False, key_path=key_path))

    def log_warning(self, message: str, key_path: str = "") -> None:
        self.errors.append(ValidationError(message, is_warning=True, key_path=key_path))

    def validate_file(self, file_path: Path) -> Tuple[bool, List[ValidationError]]:
        self.errors.clear()

        if not file_path.exists():
            self.log_error(f"File not found: {file_path}")
            return False, self.errors

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            self.log_error(f"JSON syntax error: {e.msg} (line {e.lineno}, col {e.colno})")
            return False, self.errors
        except Exception as e:
            self.log_error(f"Failed to read file: {e}")
            return False, self.errors

        if not isinstance(data, dict):
            self.log_error("Root element must be a JSON object (dictionary)")
            return False, self.errors

        self.validate_schema(data)
        self.validate_blocks(data)
        self.validate_routing(data)
        self.validate_scenes(data)

        has_errors = any(not e.is_warning for e in self.errors)
        if self.strict and any(e.is_warning for e in self.errors):
            has_errors = True

        return not has_errors, self.errors

    def validate_schema(self, data: Dict[str, Any]) -> None:
        # Check name
        name = data.get("name") or data.get("preset_name")
        if not name:
            self.log_error("Missing required preset name ('name' or 'preset_name')")
        elif not isinstance(name, str):
            self.log_error("Preset name must be a string", "name")
        else:
            if len(name.strip()) == 0:
                self.log_error("Preset name cannot be empty", "name")
            elif len(name) > 32:
                self.log_warning(f"Preset name '{name}' is {len(name)} chars (display may truncate beyond 16-24 chars)", "name")

        # Check target hardware
        target = data.get("target") or data.get("pedal_model") or data.get("hardware")
        if target and isinstance(target, str):
            if target.strip().lower() not in VALID_PEDAL_MODELS:
                self.log_warning(f"Unknown pedal model target: '{target}'", "target")

        # Check blocks list/dict
        blocks = data.get("blocks")
        if blocks is None:
            self.log_error("Missing 'blocks' array or dictionary defining the DSP chain")
        elif not isinstance(blocks, (list, dict)):
            self.log_error("'blocks' must be a list or dictionary of DSP blocks", "blocks")

    def validate_blocks(self, data: Dict[str, Any]) -> None:
        raw_blocks = data.get("blocks")
        if not isinstance(raw_blocks, (list, dict)):
            return

        blocks: List[Dict[str, Any]] = []
        if isinstance(raw_blocks, dict):
            for block_id, block_data in raw_blocks.items():
                if isinstance(block_data, dict):
                    item = dict(block_data)
                    item.setdefault("id", block_id)
                    blocks.append(item)
        else:
            for i, b in enumerate(raw_blocks):
                if isinstance(b, dict):
                    blocks.append(b)
                else:
                    self.log_error(f"Block at index {i} is not a JSON object", f"blocks[{i}]")

        seen_ids: Set[str] = set()
        nam_count = 0
        ir_count = 0

        for i, b in enumerate(blocks):
            path = f"blocks[{i}]"
            block_id = str(b.get("id") or f"block_{i}")

            if block_id in seen_ids:
                self.log_error(f"Duplicate block ID: '{block_id}'", f"{path}.id")
            seen_ids.add(block_id)

            block_type = b.get("type")
            if not block_type or not isinstance(block_type, str):
                self.log_error("Missing or invalid block 'type'", f"{path}.type")
                continue

            normalized_type = block_type.lower().strip()
            if normalized_type not in VALID_BLOCK_TYPES:
                self.log_warning(f"Unrecognized block type '{block_type}'", f"{path}.type")

            if normalized_type in {"nam", "nam_capture", "amp"}:
                nam_count += 1
            elif normalized_type in {"ir", "cabinet", "cab"}:
                ir_count += 1

            # Validate parameters
            params = b.get("params") or b.get("parameters")
            if params is not None:
                if not isinstance(params, dict):
                    self.log_error("Block parameters must be an object/dict", f"{path}.params")
                else:
                    self.validate_parameters(params, f"{path}.params")

        # Hardware DSP constraints
        if nam_count > 1:
            self.log_warning(
                f"Preset defines {nam_count} NAM/Amp blocks. Tank-G DSP hardware cycle budget supports 1 active NAM A2-Lite model at a time.",
                "blocks"
            )

        if nam_count >= 1 and ir_count == 0:
            self.log_warning(
                "Preset contains a NAM/Amp model without a cabinet IR block. Sound may be harsh/fizzy unless intended for external power-amp.",
                "blocks"
            )

    def validate_parameters(self, params: Dict[str, Any], path: str) -> None:
        for key, val in params.items():
            param_path = f"{path}.{key}"
            if isinstance(val, bool):
                continue
            elif isinstance(val, (int, float)):
                # Normalized 0-127 MIDI values or 0.0-1.0 float ranges or dB (-60 to +24)
                if val < -100 or val > 20000:
                    self.log_warning(f"Parameter '{key}' value {val} is outside conventional ranges", param_path)
            elif isinstance(val, str):
                if len(val) > 128:
                    self.log_warning(f"Parameter string '{key}' unusually long ({len(val)} chars)", param_path)
            elif val is not None and not isinstance(val, (list, dict)):
                self.log_error(f"Invalid parameter value type for '{key}': {type(val).__name__}", param_path)

    def validate_routing(self, data: Dict[str, Any]) -> None:
        routing = data.get("routing") or data.get("graph")
        if routing is None:
            return  # Implicit linear routing is valid

        if isinstance(routing, list):
            # Check for split without merge
            has_split = any("split" in str(node).lower() for node in routing)
            has_merge = any("merge" in str(node).lower() for node in routing)
            if has_split and not has_merge:
                self.log_error("Routing defines a 'split' branch without a corresponding 'merge' node", "routing")
        elif isinstance(routing, dict):
            # Graph adjacency list
            branches = routing.get("branches")
            if isinstance(branches, list) and len(branches) > 2:
                self.log_warning(f"Pedal architecture supports at most 2 parallel branches (found {len(branches)})", "routing.branches")

    def validate_scenes(self, data: Dict[str, Any]) -> None:
        scenes = data.get("scenes")
        if scenes is None:
            return

        if isinstance(scenes, dict):
            for scene_key, scene_val in scenes.items():
                if str(scene_key).lower() not in VALID_SCENE_KEYS:
                    self.log_warning(f"Unusual scene identifier '{scene_key}'. Standard scenes are A, B, C, D (or 0, 1, 2, 3)", f"scenes.{scene_key}")
                if not isinstance(scene_val, dict):
                    self.log_error("Scene definition must be an object", f"scenes.{scene_key}")
        elif isinstance(scenes, list):
            if len(scenes) > 4:
                self.log_warning(f"UltraRig hardware supports 4 scenes per preset (A/B/C/D), but {len(scenes)} were defined", "scenes")
        else:
            self.log_error("'scenes' must be a dictionary or list", "scenes")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate UltraRig preset JSON files for syntax, schema, and DSP constraints."
    )
    parser.add_argument("files", nargs="*", type=str, help="Preset JSON files to validate.")
    parser.add_argument("--dir", "-d", type=str, help="Directory containing preset JSON files.")
    parser.add_argument("--strict", "-s", action="store_true", help="Treat warnings as errors.")
    parser.add_argument("--quiet", "-q", action="store_true", help="Only output errors.")

    args = parser.parse_args()

    target_files: List[Path] = []

    if args.dir:
        dir_path = Path(args.dir)
        if not dir_path.is_dir():
            print(red(f"Error: Directory '{args.dir}' does not exist."))
            return 1
        target_files.extend(dir_path.glob("**/*.json"))

    for f in args.files:
        p = Path(f)
        if p.is_dir():
            target_files.extend(p.glob("**/*.json"))
        else:
            target_files.append(p)

    if not target_files:
        print(yellow("No JSON files specified to validate. Use --help for usage."))
        return 0

    validator = PresetValidator(strict=args.strict)
    total = len(target_files)
    passed = 0
    failed = 0

    print(bold(f"\nUltraRig Preset Validator — Inspecting {total} file(s)...\n"))

    for file_path in target_files:
        is_valid, errors = validator.validate_file(file_path)
        err_count = sum(1 for e in errors if not e.is_warning)
        warn_count = sum(1 for e in errors if e.is_warning)

        if is_valid and (not errors or not args.quiet):
            status = green("PASS")
            if warn_count > 0:
                status += " " + yellow(f"({warn_count} warning{'s' if warn_count > 1 else ''})")
            print(f"[{status}] {file_path}")
            for w in errors:
                if w.is_warning and not args.quiet:
                    print(f"       {w}")
            passed += 1
        else:
            status = red("FAIL")
            print(f"[{status}] {file_path} ({err_count} error{'s' if err_count > 1 else ''}, {warn_count} warning{'s' if warn_count > 1 else ''})")
            for e in errors:
                print(f"       {e}")
            failed += 1

    print("\n" + "=" * 50)
    summary_str = f"Summary: {passed} passed, {failed} failed out of {total} preset(s)."
    if failed > 0:
        print(red(bold(summary_str)))
        return 1
    else:
        print(green(bold(summary_str)))
        return 0

if __name__ == "__main__":
    sys.exit(main())
