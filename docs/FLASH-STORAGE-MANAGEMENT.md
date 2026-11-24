# UltraRig Onboard Flash Storage & Memory Management Guide

The M-VAVE Tank-G, Tank-B, and Black Box multi-effects pedals rely on high-speed embedded SPI flash memory to store the UltraRig firmware kernel, user presets, neural network NAM captures, cabinet impulse responses (IRs), and system calibration data.

Because embedded microcontroller flash memory has finite capacity (typically 16 MB to 32 MB total hardware partition size), unoptimized user files — such as oversized desktop NAM captures or stereo 4096-point IR files — can exhaust available memory, triggering **"Storage Full"**, **"Write Failed"**, or slow boot times.

This guide details the internal flash memory layout, optimization procedures for NAM models and IRs, flash wear prevention, and safe recovery from corrupted memory states.

---

## 1. Flash Memory Partition Architecture

```
 ┌────────────────────────────────────────────────────────────────────────┐
 │                   ONBOARD SPI FLASH MEMORY MAP                         │
 ├────────────────────────┬───────────────────────────────────────────────┤
 │ Bootloader & Recovery  │ Read-only protected sector; recovery fallback │
 │ UltraRig DSP Kernel    │ Real-time audio engine, block DSP algorithms  │
 │ Preset & Scene DB      │ 32 Presets × 4 Scenes (Routing graphs, params)│
 │ NAM Capture Storage    │ Dedicated memory slots for A2-Lite captures   │
 │ Cabinet IR Convolver   │ 1024-point convolution impulse response slots │
 │ System State NVRAM     │ Tuner A4 pitch, MIDI channel, Bluetooth bonds │
 └────────────────────────┴───────────────────────────────────────────────┘
```

| Memory Partition | Contents | Typical Allocation | User Modifiable |
| :--- | :--- | :--- | :--- |
| **Bootloader** | Hardware initialization & DFU recovery | ~1 MB – 2 MB | No (Protected) |
| **UltraRig Kernel** | Embedded DSP firmware & web server | ~4 MB – 6 MB | Via Installer Update |
| **Preset Database** | 32 presets × 4 scenes, block graphs | ~2 MB | Yes (Web / App) |
| **NAM Model Slots** | Machine learning weight tensors | Dedicated user slots | Yes (Import `.nam`) |
| **Cabinet IR Slots** | 1024-point FFT convolution coefficients| Dedicated user slots | Yes (Import `.wav`) |
| **NVRAM Sector** | System settings & persistent parameters| ~64 KB – 128 KB | Automatic on change |

---

## 2. Common Causes of Flash Memory Exhaustion

```
 ┌────────────────────────────────────────────────────────────────────────┐
 │                      FLASH EXHAUSTION CULPRITS                         │
 ├────────────────────────────────┬───────────────────────────────────────┤
 │ 1. Desktop Standard NAM Models │ 10x larger than allowed A2-Lite models│
 │ 2. 4096-Point Stereo WAV IRs   │ Wastes 8x more RAM than 1024-pt mono  │
 │ 3. Unpurged Deprecated Presets │ Retaining dozens of test presets      │
 │ 4. Interrupted USB Cable Writes│ Leaves partial, orphaned file blocks  │
 └────────────────────────────────┴───────────────────────────────────────┘
```

1. **Importing Standard Desktop NAM Models:**
   - Standard desktop NAM files contain 16+ layers and high channel counts intended for desktop CPUs/GPUs. They are rejected by the validator because they exceed both the flash slot capacity and the real-time DSP cycle budget.
   - **Solution:** Only import captures trained using the lightweight **A2-Lite** architecture.
2. **Uploading Oversized Cabinet IRs:**
   - UltraRig's convolution engine processes **1024 samples** (approx. 21.3 ms at 48 kHz). Uploading 2048-point or 4096-point 32-bit floating-point stereo files wastes flash memory without any auditory benefit, as the DSP engine automatically truncates excess samples.
   - **Solution:** Convert and truncate IRs to **Mono, 24-bit (or 16-bit), 48 kHz, 1024 samples** before uploading.

---

## 3. Flash Storage Optimization & Hygiene

### Step 1: Check Memory Status in Diagnostics
1. Open the UltraRig Web Editor (`web/index.html` in Chrome or Edge) and click **Connect**.
2. Click **Copy diagnostics** or open the **Storage Diagnostics** tab.
3. Review total flash utilization. If usage exceeds **90%**, perform an asset audit.

### Step 2: Audit & Remove Unused NAM Models
1. Navigate to the **NAM Captures** library in the editor.
2. Identify user slots with models you no longer use in active setlists.
3. Click **Clear Slot** (or overwrite with a needed A2-Lite model).

### Step 3: Batch Optimize Cabinet IRs Before Upload
Ensure your custom `.wav` IR files adhere to optimal specifications:
```
 Format:       Uncompressed Linear PCM (.wav)
 Channels:     Mono (1 Channel)
 Bit Depth:    24-bit or 16-bit
 Sample Rate:  48,000 Hz (48 kHz) or 44,100 Hz (44.1 kHz)
 Length:       1024 samples (21.3 ms)
 File Size:    ~3 KB to 6 KB per impulse file
```
* Using a free audio editor (Audacity, Reaper) or audio converter, convert stereo 4096-point files to mono 1024-point files. This reduces the storage footprint by over **75%**.

### Step 4: Export Master Backup Before Purging
1. In the Web Editor, click **Settings** → **Backup & Library** → **Export Master Library**.
2. Save your active preset collection (`All_Presets_Backup.json`) to your PC or cloud storage.
3. Delete experimental or duplicate scratch presets from the pedal's 32 onboard slots.

---

## 4. CRITICAL WARNING: Never Format the Pedal Drive on Windows

> [!CAUTION]
> When connecting your pedal via USB in installer/update mode, Windows may display a dialogue box stating:  
> **"You need to format the disk in drive X: before you can use it."**  
> **ALWAYS CLICK CANCEL.**

```
                     ┌──────────────────────────────────────────────┐
                     │            Windows Security Prompt           │
                     ├──────────────────────────────────────────────┤
                     │ You need to format the disk in drive E:      │
                     │ before you can use it.                       │
                     │                                              │
                     │  [ Format disk ]          [ CANCEL ] <───────┼── ALWAYS CLICK CANCEL!
                     └──────────────────────────────────────────────┘
```

### Why Windows Shows This:
The pedal's embedded flash memory uses a raw embedded filesystem format rather than a standard Windows NTFS or FAT32 volume. Windows does not recognize it and assumes the drive is unformatted.

If you click "Format disk", Windows will write a FAT32 partition header across your pedal's raw memory, **destroying the UltraRig bootloader, calibration tables, and preset partitions**.

---

## 5. Recovery from Corrupted Flash or Bad Sectors

If a USB cable was disconnected during a firmware write or preset upload, the pedal may hang on boot or display memory write errors:

### Procedure A: Reset Presets to Factory Defaults (Soft Fix)
1. Open the UltraRig Web Editor.
2. Click **Settings** → **Factory Reset Presets**.
3. This clears corrupted user preset JSON structures while preserving your hardware calibration and NAM slots.

### Procedure B: Re-flash UltraRig via Installer (Hard Fix)
1. Disconnect the pedal and switch it off.
2. Connect the pedal directly to your computer using a verified USB **data** cable.
3. Switch on the pedal.
4. Run `UltraRig-Installer.exe` (as administrator on Windows).
5. Click **Update UltraRig** (or **Re-install UltraRig**).
6. The installer performs a low-level sector check, writes clean partition tables, and restores firmware stability.

### Procedure C: Return to Factory Firmware
1. If the unit behaves erratically after multiple re-flashes, run `UltraRig-Installer.exe`.
2. Click **"Go back to the factory firmware"**.
3. The installer restores your original hardware dump from `Documents\tankg_installer\backup_<date>`.
