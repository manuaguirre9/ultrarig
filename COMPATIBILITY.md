# Hardware & Firmware Compatibility Matrix

This document summarizes hardware support and firmware compatibility across the M-VAVE family and OEM rebrands for **UltraRig**.

UltraRig builds upon reverse-engineered firmware and testing contributions from community members. Before flashing any unit, consult this matrix and run the non-destructive **UltraRig Check** tool.

---

## 1. Supported Devices

| Device | Type | Board Revision | Supported Versions | Notes |
|---|---|---|---|---|
| **M-VAVE Tank-G v1** | Guitar Multi-FX | v1 | FW 97, FW 98 | Run installer as Administrator. FW 99 not supported yet on v1. |
| **M-VAVE Tank-G v2** | Guitar Multi-FX | v2 | FW 97, FW 98, FW 99 | FW 99 support added in Alpha 13.1. |
| **M-VAVE Tank-B** | Bass Multi-FX | v1 / v2 | FW 97, FW 98, FW 100 | Supported in dedicated Bass release packages (`alpha13+`). |
| **M-VAVE Black Box** | Amp / IR Box | All | Current factory FW | Supported in `alpha13.1-blackbox` package. |

### Known OEM Rebrands & Clones

Many vendors rebrand M-VAVE hardware under different names with identical or slightly modified firmware IDs:

| Rebrand Name | Base Hardware | Compatibility Status | Verification Notes |
|---|---|---|---|
| **Ziron Station G** | Tank-G (v1/v2) | Compatible | Run `UltraRig-Check` to verify board revision. |
| **Ziron Station B** | Tank-B | Compatible | Reports as `Station-B_100`. Supported in Tank-B release. |
| **Lekato Tank-G / B** | Tank-G / Tank-B | Likely Compatible | Confirm with `UltraRig-Check` before flashing. |
| **Playwell / Yuimer / NMD** | Tank-G | Likely Compatible | Run `UltraRig-Check` and submit report. |

> [!NOTE]
> Other M-VAVE devices such as **Tank Pro**, **Tank Mini**, **MK-300**, and **Cuvave Cube Baby** feature different DSP boards, memory layouts, or screen controllers. They are currently unsupported, but hardware reports and pedal requests are welcome.

---

## 2. Factory Firmware Requirements

Before running the UltraRig Installer:
- **Recommended Versions:** Factory firmware **97** or **98** (or **99** for Tank-G v2).
- **Firmware 96, 53, or older:** You must update to official firmware 98 first using M-VAVE's official `M-UPGRADE` tool from [m-vave.com/download](https://m-vave.com/download).
  - *Warning:* Updating via M-UPGRADE resets presets, amps, and cabinet IRs to factory defaults. Back up custom presets via M-EFCS first.
- **Firmware 99 on Tank-G v1:** Do not attempt installation yet; the installer will detect the unsupported combination and abort safely.

---

## 3. Pre-Install Verification: UltraRig Check

If you are unsure of your board revision, or if you own a rebranded model, use the read-only check tool:

1. Download **UltraRig Check** from [Releases (tag: check1)](../../releases/tag/check1) (or `check-tankb` for bass units).
2. Connect your pedal via a direct USB data cable (avoid unpowered USB hubs).
3. Close all MIDI/audio programs (`M-EFCS`, `M-UPGRADE`, DAWs).
4. Run `UltraRig-Check.exe`.
5. The tool inspects partition tables, flash IDs, and board signatures without writing anything to the pedal.
6. Check the output verdict:
   - `READY`: Fully supported by the current release package.
   - `READY_WITH_WARNINGS`: Supported, but review notes before proceeding.
   - `NOT_READY`: Unsupported board revision or firmware version.

### Submitting a Check Report

Community check reports allow us to map new hardware IDs and board revisions safely:
1. Locate the generated JSON report: `UltraRig-check-<date>-<id>.json`.
2. Open a [Check report issue](../../issues/new?template=check-report.yml).
3. Fill in the pedal model, factory firmware version, and paste or attach the JSON report.

> [!CAUTION]
> **Never upload your `backup_<date>` folder or any `.bin` file.** Backups contain sensitive, unit-specific data and crypto material unique to your individual pedal. Only share the `.json` report file.

---

## 4. Requesting Support for New Hardware

To request support for an unlisted device (e.g., Tank Pro, MK-300):
- Open a [Pedal / Device request](../../issues/new?template=pedal-request.yml).
- Include the exact model, manufacturer, hardware specifications, and whether you have run `UltraRig-Check`.
