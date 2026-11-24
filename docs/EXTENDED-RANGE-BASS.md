# UltraRig Extended-Range (6-String) & Down-Tuned Bass Guide

Modern bass players frequently perform on **Extended-Range Basses (ERB)** — 5-string basses with a low B string, 6-string basses featuring both a low B and high C string, and down-tuned 4/5-string instruments tuned to **Drop A (27.50 Hz)**, **Drop G# (25.96 Hz)**, or lower.

Managing an instrument spanning over 7 octaves poses severe DSP challenges:
* **Subsonic Overload (The Sub-30 Hz Trap):** Notes below 30 Hz carry massive acoustic energy that human ears perceive more as physical vibration than musical pitch. Unchecked sub-frequencies rob amplifier headroom, cause subwoofer voice-coil over-excursion, and turn venue mixes into muddy rumble.
* **The High C String Sizzle:** Solos, chords, and tapping passages on the high C string can sound harsh, brittle, or thin when routed through standard bass overdrives and bright cabinet IRs.
* **String Compression Imbalance:** Because low B/A strings produce three to four times more electrical voltage than high C strings, standard compressors clamp down heavily on low notes while completely ignoring high-register fills.

This guide details calibration procedures for high-pass sub filtering, sidechain-compensated compression, cabinet IR selection, and 4-scene setups tailored for the M-VAVE Tank-B and Tank-G running UltraRig.

---

## 1. Extended Frequency Spectrum Reference

```
 Frequency (Hz)      Fundamental Pitch               Musical Function
 ──────────────────────────────────────────────────────────────────────────
 25.96 Hz            Drop G#0                        Modern Metal Sub-Rumble
 27.50 Hz            Drop A0 (Low A)                 Heavy Djent / Metalcore
 30.87 Hz            Standard B0 (Low B)             5-String & 6-String Foundation
 41.20 Hz            Standard E1 (Low E)             Traditional 4-String Bass Low
 130.81 Hz           C3 (Mid-range octave)           Slap Thumb & Low-Mids
 261.63 Hz           Middle C (C4)                   6-String High C String Open
 500 - 1,500 Hz      Midrange Growl                  Fretless & Fingerstyle Bite
 2,500 - 4,000 Hz    Attack & Clack                  Metallic Pick Attack / Slap Pop
 5,000 - 8,000 Hz    String Air & Sizzle             Harmonics & High C Sparkle
```

---

## 2. Eliminating Subsonic Flap (Master High-Pass Filtering)

Subwoofer cones in live venues and studio monitors struggle to reproduce frequencies below 30 Hz accurately. Frequencies below your lowest fundamental waste amplifier wattage and blur the kick drum transient.

```
       Gain (dB)
         0 dB ────┐           ┌────────────────────────────┐
                  │          /                              \
                  │         /                                \
        -6 dB ────┤        /                                  \
                  │       /                                    \
       -18 dB ────┴──────/                                      \──────
                         ▲                                       ▲
                  Master HPF                              Master LPF
                  Standard B0: 28 - 32 Hz                 High C Control: 5.5 - 6.5 kHz
                  Drop A0:     24 - 26 Hz
```

### HPF Calibration Rules in UltraRig:
* **Standard 5-String & 6-String (Low B0 = 30.9 Hz):**
  - Set Master High-Pass Filter (HPF) to **28 Hz – 32 Hz** (18 dB or 24 dB/octave slope).
  - Eliminates mechanical stage rumble and handling thumps without thinning out the fundamental low B.
* **Down-Tuned Basses (Drop A0 = 27.5 Hz / Drop G#0 = 26.0 Hz):**
  - Set Master HPF to **24 Hz – 26 Hz**.
  - Tightens the transient attack of low chugs, allowing sound engineers to push venue subwoofers louder without distortion.

---

## 3. High C String Conditioning & Harshness Control

When playing chordal voicings or tapping solos on a 6-string bass high C string, guitar-style distortion blocks can introduce piercing, metallic fizz.

### Best Practices for High C:
1. **Master Low-Pass Filter (LPF):** Set to **5.5 kHz – 6.5 kHz**. This preserves pick definition and slap transients while eliminating buzzing speaker tweeter sizzle.
2. **Dynamic High-Frequency Taming:** If soloing above the 12th fret on the high C string sounds shrill, apply a narrow parametric dip (-2.5 dB, Q=2.0) centered at **3.8 kHz**.

---

## 4. Balanced Compression: Solving the Low B vs. High C Imbalance

In standard compressors, a loud low B string pluck triggers -10 dB of heavy compression, while a delicate high C chord triggers 0 dB.

```
 Problem: Low B Pluck ────> Triggers -10 dB Gain Reduction ──> High C completely squashed
 Solution: Sidechain HPF ──> Compressor ignores sub-energy ──> Equal compression on all strings
```

### The Solution: Sidechain Filtered Compression
1. Open the **Compressor** block in the UltraRig Editor.
2. Locate the **Sidechain HPF (SC-HPF)** or Detector Filter parameter.
3. Set the sidechain cutoff to **80 Hz – 100 Hz**.
4. **Why this works:** The compressor's internal detector now ignores sub-bass energy below 80 Hz when calculating gain reduction. Low B, low E, D, and high C strings now trigger balanced, uniform dynamic control across the entire fretboard.
5. **Recommended Settings:**
   - **Ratio:** `3:1` to `4:1`
   - **Attack:** `25 ms` (retains snappy slap attack)
   - **Release:** `100 ms`
   - **Gain Reduction:** Aim for `-4 dB to -6 dB` evenly across all 6 strings.

---

## 5. Cabinet IR Selection for Extended-Range Bass

Not all bass cabinet impulse responses reproduce clean low B and low A fundamentals:

```
 Cabinet Type              Low B Performance                  Recommended Use
 ──────────────────────────────────────────────────────────────────────────────
 Sealed 8x10 (Ampeg SVT)   Tight low-end roll-off below 50Hz  Classic rock, vintage punch
 Ported 4x10 with Tweeter  Extended sub-bass down to 32Hz     Modern rock, slap funk, metal
 Ported 2x12 / 1x15        Warm, deep fundamental down to 28Hz 6-string jazz, neo-soul, R&B
```

* **For Modern Down-Tuned Metal (Drop A / B):** A modern ported 4x10 or blend of 8x10 (for mid punch) with a clean sub direct DI path provides the best balance of attack and earthquake-like low-end.
* UltraRig's **1024-point convolution engine** maintains pristine phase alignment across the entire low-frequency band.

---

## 6. Recommended 4-Scene Layout for 6-String Bassists

| Scene | Name | Description & Block Configuration | Ideal Musical Context |
| :---: | :--- | :--- | :--- |
| **A** | **Hi-Fi Modern Clean** | SC-HPF at 90 Hz, flat EQ, gentle chorus, clean low B anchor | 6-string chord soloing, tapping, gospel, jazz |
| **B** | **Drop-A Modern Metal** | Parallel split (LPF 250 Hz clean sub / HPF 250 Hz Darkglass drive) | Djent, metalcore, heavy pick rhythm |
| **C** | **Neo-Soul Slap** | Scooped 500 Hz, fast peak limiting, +3 dB boost at 3 kHz | Marcus Miller / Thundercat slap grooves |
| **D** | **Sub-Synth Bass** | Monophonic square wave sub-octave, cutoff at 350 Hz | Modern pop, electronic, dubstep drops |

---

## 7. Pre-Gig Extended-Range Bass Checklist

- [ ] Master HPF configured between **25 Hz and 30 Hz** to eliminate subsonic speaker flap.
- [ ] Master LPF set between **5.5 kHz and 6.5 kHz** to smooth out high C string harshness.
- [ ] Compressor detector sidechain HPF active at **80 Hz** to balance low B and high C dynamics.
- [ ] Input trim staged for active 18V onboard preamps (meter verified in editor to prevent clipping).
- [ ] Cabinet IR verified for sub-low frequency reproduction.
