# Community Tone Pack Creation & Distribution Guide for UltraRig

This guide establishes standardized conventions, directory structures, and best practices for musicians, YouTubers, and sound designers creating and sharing **Community Preset Packs** for **UltraRig** (Tank-G, Tank-B, Black Box).

---

## 1. The Challenge: Presets with Dependencies

In UltraRig, a preset (`.json`) references two external audio assets:
1. **A Neural Amp Model:** `.nam` (A2-Lite format).
2. **A Cabinet Impulse Response:** `.wav` (1024-point convolution).

If a creator distributes only the preset `.json` file, users importing it will encounter missing model warnings or silent amplifier blocks. A complete community pack must package all dependencies together into a standardized, easy-to-install bundle.

---

## 2. Standardized Pack Directory Structure

When releasing a preset pack (e.g. as a `.zip` archive on GitHub, Google Drive, or Patreon), organize your files using the following layout:

```text
[Pack-Name]-UltraRig/
├── README.txt                     <-- Crucial: notes, pickup calibration, scene layout
├── presets/                       <-- Exported preset JSON files
│   ├── 01_Vintage_Clean.json
│   ├── 02_Edge_Of_Breakup.json
│   ├── 03_Classic_Crunch.json
│   └── 04_HighGain_Lead.json
├── captures/                      <-- Royalty-free A2-Lite NAM models (.nam)
│   ├── Plexi_Crunch_A2Lite.nam
│   └── JCM800_Lead_A2Lite.nam
└── irs/                           <-- 1024-point mono 24-bit WAV files (.wav)
    ├── 4x12_Greenback_SM57.wav
    └── 2x12_Alnico_R121.wav
```

---

## 3. Mandatory `README.txt` Information

Your pack's `README.txt` should communicate calibration values so users hear the presets exactly as you designed them:

### Essential Fields to Include:
```text
============================================================
Pack Name: [Your Tone Pack Title]
Creator: [Your Name / Channel]
Firmware Target: UltraRig Alpha 13.1 or newer
Hardware Target: Tank-G (v1/v2) / Tank-B / Black Box
============================================================

1. PICKUP & INPUT TRIM CALIBRATION:
   - Tuned using: Passive Humbuckers (Gibson Les Paul, bridge pickup).
   - Recommended Input Trim: 0.0 dB.
   - For Single Coils (Strat/Tele): Boost Input Trim by +2.0 dB to +3.0 dB.
   - For High-Output Actives (EMG/Fishman): Lower Input Trim by -2.5 dB.

2. SCENE BREAKDOWN (Per Preset):
   - Scene 1: Clean (Arpeggios / Verses)
   - Scene 2: Rhythm Crunch (Main Riff)
   - Scene 3: Lead Solo (+3 dB Volume Boost, Delay engaged)
   - Scene 4: Ambient Reverb Swell

3. INSTALLATION:
   1. Open UltraRig Web Editor (web/index.html).
   2. Under 'Cab/IR', upload the files from /irs.
   3. Under 'Amp', upload the files from /captures.
   4. Click 'Import Preset' and select a file from /presets.
   5. Save the preset to your desired slot.
```

---

## 4. Licensing & Copyright Best Practices

When assembling community packs:

* **Neural Amp Captures (`.nam`):**
  * Models created by you from physical tube amplifiers or analog pedals are 100% your own copyright and safe to share or distribute.
  * Captures downloaded from [ToneHunt.org](https://tonehunt.org) must respect the original uploader's license (e.g. Creative Commons CC-BY).
* **Cabinet Impulse Responses (`.wav`):**
  * ⚠️ **Do NOT distribute commercial, proprietary IRs** (such as commercial packs from York Audio, OwnHammer, or Celestion) inside free public packs. Distributing copyrighted IR files violates vendor terms of service.
  * **Solution:** Create your own custom speaker IRs, use open-source/public-domain IR captures, or advise users in your `README.txt` on which specific third-party IR to load.

---

## 5. Gain Staging & Equalization Consistency

To ensure professional quality across your pack:

1. **Volume Level Matching:** Toggle through your presets and scenes using an LUFS meter in your DAW. Rhythm scenes should hover around **-14 dBFS to -12 dBFS peak**, with lead scenes boosting **+2.5 dB to +3.5 dB**.
2. **High-Pass & Low-Pass Filtering:** Apply a **High-Pass Filter (HPF)** around $70\text{ Hz}$ to eliminate stage rumble, and a **Low-Pass Filter (LPF)** around $6.5\text{ kHz}$ on high-gain models to prevent digital fizz on PA systems.
3. **Verify Zero-Gap Scene Switching:** Test switching between all 4 scenes within each preset to confirm that delay and reverb decay trails transition smoothly without clicks.
