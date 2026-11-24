# Contributing to UltraRig

Thank you for your interest in helping improve **UltraRig**!
Because UltraRig is an alternative firmware for embedded hardware, community contributions (especially hardware reports, bug diagnostics, and documentation) play a vital role in expanding support safely.

---

## 1. Safety & Privacy First (Critical)

> [!CAUTION]
> **NEVER upload, commit, or share your `backup_<date>` folder or any `.bin` file.**
> - Backups created by `UltraRig-Installer` and `UltraRig-Check` contain sensitive, unit-specific data and encryption keys unique to your individual hardware.
> - Sharing these files risks compromising your pedal or invalidating your unit.
> - When opening issues or contributing diagnostic data, **only attach the `.json` report file** (`UltraRig-check-*.json`).

---

## 2. Ways to Contribute

### A. Submitting Hardware & Pre-Install Check Reports
If you have a Tank-G, Tank-B, Black Box, or OEM rebrand (e.g. Ziron Station, Lekato):
1. Download **UltraRig Check** from Releases (it only reads partition tables and never writes to flash).
2. Run `UltraRig-Check.exe` with your pedal connected.
3. Open a **Check report** issue and attach `UltraRig-check-<date>-<id>.json`.
4. Mention the exact pedal model and factory firmware version.

### B. Validating Check Reports (`scripts/validate_check.py`)
Contributors and maintainers can use the included Python validation utility to inspect diagnostic reports and detect accidental privacy leaks:

```bash
# Validate a local check report file:
python scripts/validate_check.py path/to/UltraRig-check-example.json

# Inspect and validate an attachment on an open GitHub issue:
python scripts/validate_check.py --issue 251

# Post an automated diagnostic summary to the issue:
python scripts/validate_check.py --issue 251 --comment
```

### C. Reporting Bugs & DSP Anomalies
When reporting a bug:
1. Ensure you are on the latest release (e.g. Alpha 13.1+).
2. Go to **Settings > Pedal > Copy diagnostics** in the web editor and include the output.
3. Clearly state the preset structure (NAM model, IR length, parallel blocks, and whether the chromatic tuner was active).

### D. Feature Requests & UI Proposals
Have an idea for preset management (e.g. preset duplication, Undo/Redo) or stage views?
- Open a **Feature request** issue using the template.
- Describe the musical use case and provide mockups or comparisons where relevant.

---

## 3. Pull Request Guidelines

1. **Branching:** Create a feature branch off `main` (e.g., `feature/my-enhancement` or `docs/update-guide`).
2. **Commit Messages:** Follow standard conventional commit format (`feat: ...`, `fix: ...`, `docs: ...`, `tools: ...`).
3. **No Binary Dumps:** PRs containing firmware `.bin` files, proprietary DSP blobs, or unit-specific dumps will be rejected immediately.
