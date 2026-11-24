# Backup, Tone Library Export & Recovery Guide for UltraRig

This guide explains how to safeguard, back up, export, and restore your **Factory Firmware**, **User Presets (1–32)**, **NAM Neural Models**, and **Cabinet IRs** in **UltraRig**.

---

## 1. The Two Distinct Types of Backups

Understanding the difference between **Hardware Flash Backups** and **User Preset Exports** is critical to avoid accidental data loss or security issues:

| Backup Type | What It Contains | Where It Is Stored | Can It Be Shared Publicly? |
|---|---|---|---|
| **Hardware Factory Backup** | Complete binary dump of your pedal's flash chips, device serial numbers, calibration values, and encryption keys. | `Documents\tankg_installer\backup_<date>` | ❌ **NEVER.** Contains unique cryptographic keys tied to your physical device. |
| **User Tone Library Backup** | Preset configurations, scene parameters, custom `.nam` amp models, and `.wav` cabinet IRs. | Exported `.json` / `.urp` files on your computer. | ✅ **YES.** Safe to share with bandmates and the community. |

---

## 2. Managing Your Factory Hardware Backup

When you first install UltraRig using `UltraRig-Installer.exe`, the installer automatically reads and backs up the entire pedal before writing a single byte of firmware.

### Location:
```text
C:\Users\<YourUsername>\Documents\tankg_installer\backup_<YYYYMMDD_HHMMSS>\
```

### Safety Rules:
1. **Create Off-Site Copies:** Immediately copy this entire folder to a secure location (e.g. an external USB drive or private cloud storage like Google Drive / OneDrive).
2. **Never Rename Files:** Keep all `.bin` and `.json` files inside the folder untouched.
3. **Restoring Factory Firmware:**
   - To remove UltraRig and return to 100% official M-VAVE factory state, launch `UltraRig-Installer.exe` and click **"Go back to the factory firmware"**.
   - The installer selects your latest backup and restores the bootloader, partition table, and factory presets.

---

## 3. Backing Up & Exporting User Presets (Tone Library)

Before updating to a new UltraRig alpha or sharing your tone collection:

### Single Preset Export:
1. Open the UltraRig Web Editor (`web\index.html`) in Chrome or Edge and connect your pedal.
2. Select the preset you want to save.
3. Click the **"..." (More Options)** icon next to the preset name.
4. Select **Export Preset**. The browser will download a `.json` file containing all routing blocks, scene parameters, and associated NAM/IR references.

### Bulk Backup of All 32 Presets:
1. In the Web Editor, navigate to **Settings > Presets & Storage**.
2. Click **Backup All Presets (Full Library)**.
3. The editor dumps all 8 banks (32 preset slots) into an archive file: `UltraRig-Library-<date>.json`.
4. Store this file alongside your collection of `.nam` captures and `.wav` impulse responses.

---

## 4. Restoring Presets to Your Pedal

### Restoring a Single Preset into an Empty Slot:
1. In the Web Editor, click on an empty preset slot (or an existing preset you wish to replace).
2. Click the **"..."** menu and select **Import Preset**.
3. Select your `.json` preset file.
4. The editor loads the signal chain into RAM.
5. If the preset references custom NAM models or IRs not currently on the pedal, the editor will prompt you to upload the missing `.nam` or `.wav` files.
6. Click **Save Preset** to write the imported tone into non-volatile flash.

### Full Library Restore:
1. Under **Settings > Presets & Storage**, select **Restore Full Library**.
2. Select your `UltraRig-Library-<date>.json` file.
3. Confirm the prompt to overwrite user preset memory.
4. The editor writes all 32 slots sequentially over Web MIDI. Keep the USB cable connected until the progress bar reaches 100%.

---

## 5. Upgrading to New UltraRig Releases

When a new version is released (e.g. upgrading from Alpha 13 to Alpha 13.1):

1. Unzip the new `UltraRig-<version>-win.zip` package.
2. Connect your pedal, switch it on, and close all audio/MIDI software.
3. Run `UltraRig-Installer.exe`.
4. Click **"Update UltraRig"** (or "Install UltraRig" on Alpha 13.1+, which automatically proceeds as an update if an existing install is detected).
5. **Your presets, NAM captures, and IRs are preserved in flash.** The installer only updates the executable code partition and leaves user storage intact.
