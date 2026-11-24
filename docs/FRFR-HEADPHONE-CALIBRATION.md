# UltraRig FRFR Speaker & Studio Headphone Calibration Guide

One of the most frustrating experiences for guitarists and bassists using digital modelers is the **monitoring discrepancy trap**:
* Presets dialed at home on studio headphones sound muddy, dark, and buried when plugged into a live PA system.
* Presets dialed on a stage floor wedge sound harsh, shrill, and thin when recorded into a DAW or monitored through headphones.

The culprit is rarely the preset itself. Instead, it is caused by the **pronounced frequency colorations of popular studio headphones** and the **acoustic boundary loading (floor reflections)** of Full-Range Flat-Response (FRFR) active stage monitors.

By applying targeted acoustic compensation curves at UltraRig's **Global Output EQ** stage, your saved presets remain objectively neutral, translating with 1:1 accuracy across recording headphones, live stage monitors, and front-of-house PA systems.

---

## 1. Popular Studio Headphone Coloration & Global EQ Profiles

Most studio headphones are not acoustically flat. Manufacturers design specific curves for tracking drums, broadcasting speech, or casual listening:

```
  Frequency Response Colorations:
  ──────────────────────────────────────────────────────────────────────────
  Beyerdynamic DT 770 / 990:   Aggressive +5 to +7 dB treble spike at 8.5 kHz ("Beyer Peak")
  Audio-Technica ATH-M50x:     V-shaped; pronounced +4 dB bump in low-mids (200–250 Hz)
  Sony MDR-7506:               Piercing upper-mid bite (+4 dB at 3.5–4.5 kHz)
  Sennheiser HD 600 / 650:     Neutral midrange; natural sub-bass roll-off below 60 Hz
```

### The "Beyer Peak" Trap (Beyerdynamic DT 770 Pro / DT 990 Pro)
* **The Problem:** The aggressive 8.5 kHz treble spike causes guitarists to cut presence and treble inside their presets to avoid ear fatigue during late-night headphone practice. When plugged into a flat stage PA, the guitar sounds dark, muffled, and lifeless.
* **Global Output EQ Calibration Profile for DT 770 / 990:**
  - **Band 1 (Sub Tame):** `60 Hz`, Gain: `-2.0 dB`, Q: `1.0` (Low Shelf)
  - **Band 2 (Beyer Peak Notch):** `8,500 Hz (8.5 kHz)`, Gain: `-4.5 dB`, Q: `3.0` (Parametric Notch)

---

### The Low-Mid Mud Trap (Audio-Technica ATH-M50x)
* **The Problem:** The heavy 200–250 Hz resonance causes presets to sound boomy in the headphones, prompting players to scoop low-mids. On stage through a neutral PA, the guitar loses all its body and punch.
* **Global Output EQ Calibration Profile for ATH-M50x:**
  - **Band 1 (Low-Mid Mud Dip):** `220 Hz`, Gain: `-3.5 dB`, Q: `1.6` (Parametric Dip)
  - **Band 2 (Mid Body Lift):** `500 Hz`, Gain: `+1.5 dB`, Q: `1.4` (Parametric Peak)
  - **Band 3 (Treble Smooth):** `9,000 Hz`, Gain: `-2.0 dB`, Q: `2.0` (High Shelf)

---

### The Broadcast Bite Trap (Sony MDR-7506)
* **The Problem:** Designed for vocal broadcast monitoring, the MDR-7506 has an aggressive 3.5 kHz – 4.5 kHz upper-mid bump that exaggerates overdrive raspiness.
* **Global Output EQ Calibration Profile for MDR-7506:**
  - **Band 1 (Presence Tame):** `4,200 Hz (4.2 kHz)`, Gain: `-3.5 dB`, Q: `2.0` (Parametric Dip)
  - **Band 2 (Sub-Bass Warmth):** `100 Hz`, Gain: `+1.5 dB`, Q: `1.0` (Low Shelf)

---

### The Reference Standard (Sennheiser HD 600 / HD 650 / HD 560S)
* **The Profile:** Known for exceptional midrange linearity. Requires minimal correction:
  - **Band 1 (Sub Extension):** `50 Hz`, Gain: `+2.0 dB`, Q: `1.0` (Low Shelf)
  - **Bands 2–4:** Flat (`0.0 dB`)

---

## 2. Active FRFR Stage Monitor Calibration (HeadRush, Line 6, Alto)

FRFR active powered speakers (e.g., HeadRush FRFR-108/112, Alto TS series, Line 6 Powercab) sound dramatically different depending on physical placement.

```
       [ ON A SPEAKER STAND (Free Field) ]               [ ON THE STAGE FLOOR (Half-Space) ]
                 Linear Bass Response                             +6 dB Boundary Low-End Mud
                         ▲                                                   ▲
                         │                                                   │
                   [ Flat Sound ]                                   [ Requires Decoupling EQ ]
```

### 1. Acoustic Boundary Loading (Floor Coupling)
Placing an FRFR wedge directly onto a hollow wooden stage or hard floor reinforces low frequencies below 150 Hz by **+4 dB to +6 dB** (acoustic half-space loading).
* **The Fix:**
  - Engage Master **High-Pass Filter (HPF)** at **85 Hz – 95 Hz** (12 dB/octave).
  - Apply a gentle **Low-Shelf Cut:** `130 Hz`, Gain: `-3.5 dB`.

### 2. Taming High-Frequency Compression Horns
Unlike physical 12-inch guitar speakers that naturally roll off above 5 kHz, FRFR cabinets feature high-frequency compression horn tweeters that can beam harsh digital sizzle directly at ear level.
* **The Fix:**
  - Engage Master **Low-Pass Filter (LPF)** at **6.0 kHz – 6.5 kHz** (12 dB/octave).

---

## 3. The Fletcher-Munson (Equal Loudness) Effect

```
  Audible Perception (dB)
    100 dB SPL (Stage)   ───> Flat, balanced perception of bass, mids, and treble
     70 dB SPL (Bedroom) ───> Human ears lose sensitivity to bass (<150 Hz) & highs (>6 kHz)
```

Human hearing frequency sensitivity changes dramatically with volume:
* When dialing presets at low "bedroom" volumes through headphones (~65 dB SPL), human ears require elevated bass and treble to perceive a balanced tone.
* When that exact same preset is played through an FRFR monitor at full gig volume (~100 dB SPL), the elevated bass sounds boomy and the treble sounds harsh.

### Best Practice:
1. When crafting presets on headphones at low volume, leave tone controls balanced and avoid pushing bass or presence past 60%.
2. Perform final volume and EQ verification at realistic rehearsal loudness.

---

## 4. The Global EQ Workflow: Keeping Presets Objective

```
 [ PRESET 01: Friedman Lead ]  ──┐
 [ PRESET 02: Fender Clean   ]  ──┼──> [ MASTER GLOBAL OUTPUT EQ ] ──> [ Physical Speaker ]
 [ PRESET 03: Modern Crunch  ]  ──┘     • Headphone Profile (DT770 / M50x)
                                       • OR FRFR Floor Profile (-3dB at 130Hz)
```

* **Never alter individual preset knobs to compensate for your headphones.** If you change your preset's treble control to match your headphones, you ruin the tone for every other sound system.
* **Make corrections exclusively inside Global EQ.** When switching from headphone recording to stage gigging, change the Global EQ profile in 5 seconds without touching a single saved preset.

---

## 5. Monitoring Calibration Quick Reference

| Monitoring Environment | Master HPF | Low Correction | High Correction | Master LPF |
| :--- | :---: | :---: | :---: | :---: |
| **Beyerdynamic DT 770 / 990** | 75 Hz | 60 Hz: -2.0 dB | 8.5 kHz: -4.5 dB (Q=3.0) | Bypass |
| **Audio-Technica ATH-M50x** | 75 Hz | 220 Hz: -3.5 dB | 9.0 kHz: -2.0 dB | Bypass |
| **Sony MDR-7506** | 80 Hz | 100 Hz: +1.5 dB | 4.2 kHz: -3.5 dB (Q=2.0) | Bypass |
| **FRFR Floor Wedge (Stage)** | 90 Hz | 130 Hz: -3.5 dB (Shelf) | 3.5 kHz: -2.0 dB | 6.2 kHz |
| **FRFR on Pole Stand** | 80 Hz | Flat (0.0 dB) | Flat (0.0 dB) | 6.5 kHz |
| **FOH Balanced PA (Console)** | 80 Hz | Flat (0.0 dB) | Flat (0.0 dB) | 6.5 kHz |
