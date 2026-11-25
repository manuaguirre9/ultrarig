# Friedman BE-100 (Brown Eye) High-Gain British Routing Guide

This guide details the circuit architecture, hot-rodded British gain cascade, signature voicing switches (**HBE**, **C45**, **SAT**, **Fat**), and preset configuration for the **Friedman BE-100 (Brown Eye)** amplifier within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Circuit Architecture of the Friedman BE-100

Designed by master amp builder Dave Friedman, the BE-100 takes the classic modified 1970s/1980s British Marshall Plexi and JCM800 lineage—famously associated with the early "Brown Sound"—and refines it with tighter low-end tracking, noise-free operation, and immense tonal versatility.

```
Instrument In
   │
   ├── (Clean Channel: 3-Way Bright Switch) ───────────────────────────────────────────┐
   │                                                                                   │
   ▼                                                                                   │
[ Fat Switch & Input Gain ]                                                            │
   │                                                                                   │
   ├──► [ Optional Extra Gain Stage: HBE (Hairy Brown Eye) ]                           │
   │           │                                                                       │
   ▼           ▼                                                                       │
[ BE Preamp Cascade (12AX7 Triodes) ] ◄───► [ C45 Switch: Upper-Mid Grind Cap ]        │
   │                                                                                   │
   ├──► [ SAT Switch: Asymmetric Clipping Diodes (Lead Compression) ]                  │
   │                                                                                   │
   ▼                                                                                   │
[ Passive British Tonestack (Bass / Middle / Treble) ] ◄───────────────────────────────┘
   │
   ▼
[ 4x EL34 Power Amp Emulation (Thump Resonance & Presence Feedback Loop) ]
   │
   ▼
[ Mixed 4x12 Cabinet IR (2x Greenback G12M-25 Top + 2x Vintage 30 Bottom) ] ──► Stereo Output
```

### 1.1 BE vs. HBE (Hairy Brown Eye) Gain Cascade

- **BE (Brown Eye) Channel:** Delivers classic, open, dynamic hard-rock crunch. It exhibits massive touch sensitivity—clean up effortlessly by rolling back the guitar's volume knob, or dig in for roaring 1980s arena rock rhythm chords.
- **HBE (Hairy Brown Eye) Channel:** Inserts an additional 12AX7 triode gain stage directly in front of the BE circuit. This saturates the harmonic spectrum further, delivering aggressive, saturated high-gain lead sustain and tight modern metal tracking.

### 1.2 The Essential Voicing Switches (C45, SAT, Fat, Voice)

- **C45 Switch (The "Steve Stevens" Mod):** Switches an extra treble/upper-mid peaking capacitor into the early preamp stage, adding sharp pick-attack "sizzle," cutting bite, and aggressive high-mid grind.
- **SAT (Saturation) Switch:** Introduces asymmetrical clipping diodes across the gain path. This produces a slight volume drop alongside immediate, singing compression and harmonic richness—perfect for smooth, effortless solo playing at lower volumes.
- **Fat Switch:** Increases low-mid coupling capacitance at the input, fattening up thin single-coil Stratocaster or Telecaster pickups.
- **Voice Switch:** Shifts the power amp negative feedback contour between open vintage Plexi chime and tight modern focus.

### 1.3 Mixed 4x12 Speaker Complement

The classic Friedman 4x12 cabinet utilizes an **X-pattern or Top/Bottom split**:
- **Top Pair (Celestion G12M-25 Greenbacks):** Imparts vintage woody crunch, soft high-end breakup, and rich midrange bloom.
- **Bottom Pair (Celestion Vintage 30s):** Delivers tight low-end thump, aggressive projection, and upper-mid cut.

---

## 2. DSP Signal Chain & Processing Topology

```
Guitar In (Humbuckers / Single-Coils)
   │
   ▼
[ Fast Downward Expander / Noise Gate ] (Tames high-gain idle hiss)
   │
   ▼
[ Preamp Channel Selector: Clean / BE / HBE ]
   │
   ▼
[ Switch Matrix: C45 Grind | SAT Diode Clip | Fat Input | Voice Switch ]
   │
   ▼
[ 3-Band British Passive Tonestack (Bass / Mid / Treble) ]
   │
   ▼
[ 100W EL34 Power Amp Model (Presence & Thump Resonance Feedback) ]
   │
   ▼
[ Dual Speaker IR Convolution: Greenback G12M-25 + Vintage 30 ]
   │
   ▼
[ Stereo FX Loop: Warm Tape Delay & Studio Plate Reverb ] ──► Stereo Output
```

---

## 3. Parameter Specifications

| Parameter | Range | Default | Unit | Description |
| :--- | :--- | :--- | :--- | :--- |
| `CHANNEL_MODE` | `CLEAN` / `BE` / `HBE` | `BE` | mode | Selects Clean, Brown Eye crunch, or Hairy Brown Eye high-gain channel. |
| `PREAMP_GAIN` | `0` - `100` | `65` | % | Gain level feeding 12AX7 preamp stages. |
| `C45_SWITCH` | `OFF` / `ON` | `OFF` | bool | Boosts upper-mid crunch and sharp pick attack bite. |
| `SAT_SWITCH` | `OFF` / `ON` | `OFF` | bool | Engages asymmetric diode clipping for compressed solo sustain. |
| `FAT_SWITCH` | `OFF` / `ON` | `OFF` | bool | Thickens bottom-end weight (recommended for single-coils). |
| `BASS` | `0` - `100` | `52` | % | Tone stack low-end response. |
| `MIDDLE` | `0` - `100` | `64` | % | Tone stack midrange focus (essential for classic British bark). |
| `TREBLE` | `0` - `100` | `58` | % | Tone stack high-frequency bite. |
| `THUMP` | `0` - `100` | `60` | % | Negative feedback low-end cabinet resonance (80 Hz - 110 Hz punch). |
| `PRESENCE` | `0` - `100` | `55` | % | Power section high-frequency edge and sparkle. |
| `CAB_IR_MIX` | `GREENBACK` / `V30` / `MIXED` | `MIXED` | mode | Mixed 4x12 speaker cabinet impulse response. |

---

## 4. Factory Scene Presets

### Scene A: Plexi Clean-Edge (Sparkling Classic Clean)
- **Concept:** Open, woody, dynamic British clean with responsive chime when dug into.
- **Voicing:** `CHANNEL_MODE = CLEAN`, Bright Pos 2, `PREAMP_GAIN = 40%`.
- **EQ & Power:** `BASS = 55%`, `MIDDLE = 52%`, `TREBLE = 62%`, `THUMP = 40%`, `PRESENCE = 58%`.
- **Cabinet IR:** Celestion Greenback G12M-25 4x12.
- **Space:** Subtle Studio Chorus + Spring Reverb (`1.6 s`, `20%` mix).

### Scene B: Brown Eye Classic 80s Rock (Eddie / George Lynch)
- **Concept:** The iconic hot-rodded Plexi rhythm and lead voice: chewy midrange crunch, harmonic bloom, and articulate chords.
- **Voicing:** `CHANNEL_MODE = BE`, `C45_SWITCH = ON`, `SAT_SWITCH = OFF`, `FAT_SWITCH = OFF`, `PREAMP_GAIN = 68%`.
- **EQ & Power:** `BASS = 50%`, `MIDDLE = 68%`, `TREBLE = 56%`, `THUMP = 62%`, `PRESENCE = 54%`.
- **Cabinet IR:** Mixed Greenback + V30 4x12.
- **Space:** Classic 80s Tape Slap/Delay (`340 ms`, `20%` feedback) + Light Plate Reverb.

### Scene C: HBE Modern Saturated Rhythm (Tight Aggressive Chug)
- **Concept:** Massive modern hard rock and metal rhythm clarity with surgical palm-mute focus and tight bottom end.
- **Voicing:** `CHANNEL_MODE = HBE`, `C45_SWITCH = OFF`, `SAT_SWITCH = OFF`, `PREAMP_GAIN = 72%`.
- **EQ & Power:** `BASS = 46%`, `MIDDLE = 60%`, `TREBLE = 60%`, `THUMP = 75%`, `PRESENCE = 62%`.
- **Cabinet IR:** Celestion Vintage 30 4x12.
- **Space:** Dry & tight (Noise Gate threshold at `-32 dBFS`).

### Scene D: Lead Singing Harmonic Solo (SAT Engaged)
- **Concept:** Effortless, creamy legato sustain with saturated harmonic compression and zero harsh pick clicks.
- **Voicing:** `CHANNEL_MODE = HBE`, `C45_SWITCH = ON`, `SAT_SWITCH = ON`, `FAT_SWITCH = ON`, `PREAMP_GAIN = 78%`.
- **EQ & Power:** `BASS = 44%`, `MIDDLE = 78%`, `TREBLE = 52%`, `THUMP = 55%`, `PRESENCE = 50%`.
- **Space:** Stereo Modulated Delay (`dotted 8th`, `420 ms`, `30%` feedback) + Studio Hall Reverb.

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (Plexi Clean-Edge) / Scene B (Brown Eye Classic Rock).
- **Footswitch B:** Scene C (HBE Modern Rhythm).
- **Footswitch C:** Scene D (SAT Singing Lead) / Solo Volume Boost (+3 dB).
- **Knob 1 (GAIN):** Preamp Gain / Saturation.
- **Knob 2 (EQ / TONE):** Midrange Focus and Presence sweep.
- **Knob 3 (REVERB / DELAY):** Ambient FX Loop level.

### Tank-B Control Assignments
- Rock and metal bassists can employ the BE channel at `PREAMP_GAIN = 38%` paired with `THUMP = 80%` and a parallel clean low-end blend (< 150 Hz) for gritty, grinding Duff McKagan / Billy Sheehan rock bass distortion.

### Black Box Desktop Configuration
- **Stereo Dual-IR Split:** Assign `G12M-25 Greenback` to Left Output and `Celestion V30` to Right Output for wide studio wall-of-sound dispersion.
- **MIDI CC #84:** Real-time switching of `C45` and `SAT` switches on the fly.
