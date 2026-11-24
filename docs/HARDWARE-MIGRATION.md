# Hardware Migration & Upgrade Checklist for UltraRig

This guide provides a safe, step-by-step checklist for migrating your tones and settings when upgrading or switching hardware (e.g. from **Tank-G v1 to v2**, between **Tank-G and Tank-B**, to the **Black Box**, or between OEM rebrands like **Ziron** and **Lekato**).

---

## 1. The Cardinal Rule: Never Swap Hardware Backups

> [!CAUTION]
> ### CRITICAL HARDWARE SAFETY RULE
> **NEVER attempt to flash or copy the `Documents\tankg_installer\backup_<date>` folder from one pedal onto another pedal.**
> 
> The hardware backup created by `UltraRig-Installer.exe` is a raw binary dump containing:
> - The physical device serial number and hardware board revision.
> - Factory analog-to-digital calibration constants.
> - Chip-level cryptographic keys unique to the specific microcontroller.
> 
> Flashing unit A's backup onto unit B will corrupt unit B's bootloader and cause an unrecoverable brick.
> 
> **To transfer tones, migrate your PRESET JSON LIBRARY, not hardware flash backups.**

---

## 2. Phase 1: Exporting Tones from the Source Pedal

Before disconnecting or resetting your current pedal:

1. Connect your source pedal to your computer via USB and open the **UltraRig Web Editor** (`web\index.html`).
2. Go to **Settings > Presets & Storage**.
3. Click **Backup All Presets (Full Library)** to save `UltraRig-Library-<date>.json`.
4. Ensure you have the original `.nam` neural amp model files and `.wav` cabinet impulse responses saved in a folder on your computer.
5. In the Web Editor, note down any custom **Footswitch Mappings** or **Expression Pedal Calibration** settings.

---

## 3. Phase 2: Restoring the Source Pedal to Factory (If Selling or Trading)

If you are selling, returning, or giving away your old pedal:

1. Close all DAWs and MIDI programs.
2. Run `UltraRig-Installer.exe` on your computer.
3. Select **"Go back to the factory firmware"**.
4. The installer locates the original backup in `Documents\tankg_installer\backup_<date>` corresponding to that unit's ID and flashes the factory firmware back to the pedal.
5. Disconnect the pedal, power cycle it, and open M-VAVE's official `M-EFCS` software to verify it is recognized as a 100% factory unit.

---

## 4. Phase 3: Preparing and Installing UltraRig on the New Pedal

1. **Verify Factory Firmware on the New Pedal:**
   - Connect the new unit and inspect its firmware version in `M-EFCS` or `M-UPGRADE`.
   - **Recommended:** Version **97** or **98** (or **99** on Tank-G v2).
   - If the new unit arrived on firmware **96 or 53**, update it first to 98 using M-VAVE's official `M-UPGRADE` tool from [m-vave.com/download](https://m-vave.com/download).
2. **Run UltraRig Check (Read-Only):**
   - Run `UltraRig-Check.exe` on the new unit to ensure the board and partition table are identified as `READY`.
3. **Install UltraRig:**
   - Run `UltraRig-Installer.exe` for the new pedal.
   - Click **"Install UltraRig"**.
   - If Windows asks to format a disk, click **Cancel**.
   - The installer creates a brand new, unique backup for the new pedal in `Documents\tankg_installer\backup_<new_date>`. Keep this safe!

---

## 5. Phase 4: Restoring Tone Library to the New Pedal

1. Open the Web Editor (`web\index.html`) in Chrome or Edge and connect to the new pedal.
2. Go to **Settings > Presets & Storage**.
3. Select **Restore Full Library** and choose your exported `UltraRig-Library-<date>.json`.
4. Allow the editor to write the 32 preset slots over Web MIDI.
5. Upload any `.nam` captures or `.wav` IRs that were used in your presets.
6. Navigate to **Settings > Expression & Controllers** to recalibrate your external expression pedal for the new unit's analog inputs.
7. Test your main presets and fine-tune output volume levels.

---

## 6. Model Compatibility Matrix

| Migration Path | Preset Compatibility | Special Considerations |
|---|---|---|
| **Tank-G v1 $\to$ Tank-G v2** | 100% Seamless | Same DSP architecture and signal blocks. |
| **Tank-G $\to$ Tank-B (Bass)** | 100% Compatible | Presets load cleanly; you may want to re-balance EQ frequencies and add clean parallel splits for bass. |
| **Tank-G/B $\to$ Black Box** | 100% Compatible | Black Box features a built-in display; custom footswitch assignments will adapt to the Black Box interface. |
| **OEM Rebrand $\to$ M-VAVE** | 100% Compatible | Hardware under the hood is identical (e.g. Ziron Station G/B, Lekato). |
