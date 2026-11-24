# UltraRig Chromatic Tuner & Intonation Guide

UltraRig features a built-in, studio-grade **Chromatic Tuner** with sub-cent precision running directly on the M-VAVE pedal's hardware DSP. It supports 6, 7, and 8-string electric and acoustic guitars, as well as 4, 5, and 6-string basses down to the low B fundamental (30.87 Hz).

This guide covers activation shortcuts, reference frequency calibration (A4 = 432 Hz – 445 Hz), visual needle versus strobe emulation display modes, and pro stage techniques for setting bridge saddle intonation.

---

## 1. Quick Reference: Tuner Controls & Activation

```
 ┌────────────────────────────────────────────────────────────────────────┐
 │                      Tuner Activation Methods                          │
 ├───────────────────┬────────────────────────────────────────────────────┤
 │ Hardware Switch   │ Press and hold Footswitch B for 1.5 seconds        │
 │ Web / Mobile App  │ Click the "Tuner" (Fork) icon in the top toolbar   │
 │ MIDI Controller   │ Send MIDI CC #68 (Value 127 = On, 0 = Off)         │
 └───────────────────┴────────────────────────────────────────────────────┘
```

| Action | Hardware Pedal | Web / Android Editor | MIDI CC |
| :--- | :--- | :--- | :--- |
| **Enter Tuner** | Hold Footswitch B (1.5 sec) | Click Tuner icon (top right) | Send `CC #68` (Val 127) |
| **Exit Tuner** | Tap any footswitch | Click Tuner icon again | Send `CC #68` (Val 0) |
| **Toggle Mute / Thru** | Tap Footswitch A while in tuner | Toggle `Mute` / `Thru` switch | Send `CC #69` |

---

## 2. Audio Output Behavior (Mute vs. Thru)

When the tuner engages, you can choose how UltraRig handles the audio output:

```
                  ┌──> [ MUTE MODE (Default) ] ──> Silent Stage Outputs (FOH / IEM)
 [ Guitar Input ] ┤
                  └──> [ THRU / BYPASS MODE ]   ──> Dry Unprocessed Audio (Soundcheck)
```

1. **Mute Mode (Recommended for Live Stage):**
   - Completely silences the main 6.35 mm output, 3.5 mm headphone jack, and USB audio monitoring.
   - Allows silent tuning between songs without broadcasting string plucking or tuning peg adjustments to the audience.
2. **Thru / Bypass Mode:**
   - Routes the pristine, dry guitar signal directly to outputs at unity gain (bypassing all amps, drives, and delays).
   - Useful during rehearsals, soundchecks, or when you want to verify guitar volume while checking tuning.

---

## 3. Reference Pitch Calibration (A4 = 432 Hz – 445 Hz)

While the worldwide standard concert pitch is **A4 = 440 Hz**, certain musical genres, acoustic instruments, or historical temperaments require custom pitch standards.

```
 432 Hz ───────────── 436 Hz ───────────── 440 Hz ───────────── 442 Hz ───────────── 445 Hz
 (Verdi Tuning)       (Baroque / Horns)    (Concert Pitch)      (European Symphony)  (Bright Acoustic)
```

### Changing Reference Pitch:
1. Open the UltraRig Editor and click the **Settings** gear icon (or the frequency badge next to the Tuner).
2. Use the slider or numeric input to set the reference frequency between **432.0 Hz and 445.0 Hz** in 0.1 Hz increments.
3. The selected calibration is saved to pedal flash memory and remains persistent across reboots.
4. To reset to standard concert pitch, double-click the frequency badge or click **Reset to 440 Hz**.

---

## 4. Visual Display Modes: Needle vs. Strobe Emulation

UltraRig provides two distinct visual rendering modes designed for different performance scenarios:

### 1. Needle / Cent Meter Mode (Stage Playing)
```
          Flat (-50)             In Tune (0)            Sharp (+50)
              [ ◄ ◄ ◄ ◄ ◄ ◄ ◄ ◄ ─── [ E ] ─── ► ► ► ► ► ► ► ► ]
                                     ▲ (Green Lock)
```
* **Best for:** Fast tuning adjustments between songs under glaring stage lights.
* **How it works:** Displays the detected pitch letter (`E`, `A`, `D`, `G`, `B`, `e`) with a ±50 cent arc. When pitch is within **±1 cent**, the center target glows solid neon green.

### 2. Virtual Strobe Emulation (Setup & Intonation)
```
     Rotating Counter-Clockwise (Flat)            Stationary (Exact 0.1 Cent Lock)
            ◄── ▓ ▓ ▓ ▓ ▓ ▓ ◄──                                ▓   ▓   ▓   ▓
```
* **Best for:** Guitar bridge saddle intonation adjustment, truss rod setups, and recording studio tracking.
* **How it works:** A rotating visual strobe band moves across the display. The speed of rotation indicates the degree of pitch discrepancy; the direction indicates whether the note is flat (left) or sharp (right). When the strobe **stands completely still**, the string is in absolute mathematical alignment down to **0.1 cent resolution**.

---

## 5. Setting Bridge Saddle Intonation (Step-by-Step)

Proper intonation ensures your instrument stays in tune across the entire fretboard, from open chords to solos above the 12th fret.

```
  [ Nut ]                                  [ 12th Fret ]                    [ Bridge Saddle ]
     |                                           |                                  |
     ▼                                           ▼                                  ▼
   Open String Pluck ───────────────> Compare Natural Harmonic <───────────> Compare Fretted Note
                                      to Fretted 12th Fret
```

1. **Tune the Open String:** Tune the open string until the strobe display is completely stationary.
2. **Play the 12th Fret Natural Harmonic:** Lightly touch the string directly above the 12th fret wire (do not press down) and pluck. Note the pitch reading.
3. **Fret and Pluck at the 12th Fret:** Press the string down normally at the 12th fret and pluck with medium pressure.
4. **Compare & Adjust Bridge Saddle Screws:**
   - **If the fretted note is SHARP (strobe drifts right):** The string speaking length is too short. Move the bridge saddle **backward** (away from the pickups, toward the bridge end).
   - **If the fretted note is FLAT (strobe drifts left):** The string speaking length is too long. Move the bridge saddle **forward** (toward the neck/pickups).
5. **Re-tune Open String:** Re-tune the open string to pitch and repeat until both the 12th-fret harmonic and the 12th-fret fretted note stand perfectly still on the strobe tuner.

---

## 6. Pro Stage Tuning Techniques

1. **Select the Neck Pickup:**
   - Always switch your guitar pickup selector to the **Neck pickup** before tuning.
   - Neck pickups capture greater string fundamental excursion and significantly fewer harsh, metallic harmonic overtones than the bridge pickup, resulting in instantaneous, non-jumpy pitch detection.
2. **Roll the Tone Knob Down to 50%:**
   - Cutting treble frequencies eliminates pick strike scraping and fret noise from confusing the detection algorithm.
3. **Pluck with the Pad of Your Thumb:**
   - Plucking gently with the fleshy pad of your thumb produces a clean sinusoidal wave rather than the aggressive high-frequency transient of a plastic pick.
4. **Tuning 5-String Basses (Low B):**
   - Low B strings vibrate at a very low frequency (~30.87 Hz). If the needle fluctuates on the open low B, play the **12th fret natural harmonic** instead for instant, steady pitch locking.
5. **Always Tune UP to Pitch:**
   - If a string is sharp, detune it below pitch first, then tune **upward** into pitch. This ensures proper string tension over the nut slots and prevents tuning slippage when bending strings.
