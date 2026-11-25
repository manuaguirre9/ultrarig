# Stereo Micro-Pitch Detuner (Eventide H3000 Style) Modeling Guide

This guide details the psychoacoustics of **static opposing micro-pitch shifting**, asymmetric Haas-effect pre-delays, mono-sum phase safety, and practical preset configuration for **Stereo Micro-Pitch Detuning** (inspired by the **Eventide H3000** and **Yamaha SPX90**) within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Psychoacoustic Principles of Micro-Pitch Detuning

In the late 1980s and 1990s, studio guitarists and touring players—most famously **Eddie Van Halen** (*5150*, *F.U.C.K.*, *Balance*), **Steve Vai**, **John Petrucci**, and **Zakk Wylde**—replaced traditional LFO chorus pedals on high-gain rigs with studio rack **Micro-Pitch Shifters**.

```
Instrument / Preamp Out
   │
   ├──► [ Path L: Pitch +9 cents | Micro-Delay: 11 ms ] ──► [ HF Damping LPF ] ──► Stereo Left
   │
   ├──► [ Path C: Pure Dry Unshifted (0 cents | 0 ms) ] ─────────────────────────► Center Anchor
   │
   └──► [ Path R: Pitch -9 cents | Micro-Delay: 19 ms ] ──► [ HF Damping LPF ] ──► Stereo Right
```

### 1.1 Why Micro-Pitch Beats Chorus on Distorted & Lead Guitars

1. **Zero LFO Pitch Warble:** Conventional chorus sweeps delay time back and forth via an LFO, causing audible, cyclical pitch wobbling ("seasick vibrato"). Under heavy high-gain distortion, oscillating pitch creates unpleasant dissonance and tuning instability. Micro-pitch uses **completely static pitch offsets** ($\pm 6$ to $\pm 15\text{ cents}$), eliminating cyclical wobble while creating a stable, towering wall-of-sound double-track illusion.
2. **Symmetrical Pitch Balancing:** Shifting Left slightly sharp ($+9\text{ cents}$, pitch ratio $1.00521\times$) and Right equally flat ($-9\text{ cents}$, pitch ratio $0.99481\times$) anchors perceived intonation squarely on the center dry note. The human ear perceives three tightly locked guitars playing in unison!
3. **Asymmetric Haas Micro-Delays ($11\text{ ms}$ vs. $19\text{ ms}$):** Offsetting Left and Right delay times slightly within the $8\text{ ms} - 25\text{ ms}$ Haas psychoacoustic window prevents Left and Right voices from collapsing together, unlocking vast 3D stereo separation without audible rhythmic echoes.

---

## 2. DSP Signal Chain & Processing Topology

```
Dry Input (Post-Amp / Cab IR OR Clean Studio Signal)
   │
   ├───► [ Center Direct Dry Anchor ] ──────────────────────────────────────────────────────┐
   │                                                                                        │
   ▼                                                                                        │
[ High-Pass Filter (140 Hz - 180 Hz) ] (Protects low-end punch during live mono PA collapse)│
   │                                                                                        │
   ├───► [ Fractional Hermite Pitch Shifter Left (+Cents) ] ──► [ Asymmetric Delay L (ms) ] ┼──► Stereo L
   │                                                                                        │
   └───► [ Fractional Hermite Pitch Shifter Right (-Cents) ] ─► [ Asymmetric Delay R (ms) ] ┴──► Stereo R
```

---

## 3. Parameter Specifications

| Parameter | Range | Default | Unit | Description |
| :--- | :--- | :--- | :--- | :--- |
| `DETUNE_LEFT` | `-35` to `+35`| `+9` | cents | Static pitch shift applied to the Left stereo channel. |
| `DETUNE_RIGHT` | `-35` to `+35`| `-9` | cents | Opposing static pitch shift applied to the Right stereo channel. |
| `DELAY_LEFT` | `0.0` - `45.0`| `11.0` | ms | Short Haas micro-delay on Left voice widening spatial separation. |
| `DELAY_RIGHT` | `0.0` - `45.0`| `19.0` | ms | Asymmetric delay on Right voice preventing stereo phase cancellation. |
| `FEEDBACK_CROSS`| `0` - `45` | `12` | % | Gentle cross-channel feedback creating rich studio thickness. |
| `HPF_SAFE_HZ` | `40` - `250` | `140` | Hz | Excludes sub-bass from detuning to preserve tight low-end palm mutes. |
| `HF_DAMPING` | `3.5` - `14.0`| `8.5` | kHz | Smooths shifted voice brightness so dry signal remains crisp in front. |
| `THERMAL_DRIFT`| `0` - `100` | `10` | % | Ultra-subtle analog clock randomness preventing static robotic phasing. |
| `MIX_WET_DRY` | `0` - `100` | `40` | % | Balance between pure center anchor and wide detuned stereo wings. |

---

## 4. Factory Scene Presets

### Scene A: 80s Van Halen Balance Micro-Pitch (W/D/W Wall of Sound)
- **Concept:** The quintessential early-1990s Eddie Van Halen Wet/Dry/Wet stereo sound: huge, crystal-clear, thick harmonic width with zero chorus modulation warble.
- **Settings:** `DETUNE_LEFT = +9 cents`, `DETUNE_RIGHT = -9 cents`, `DELAY_LEFT = 12 ms`, `DELAY_RIGHT = 21 ms`, `HPF_SAFE_HZ = 140 Hz`, `MIX_WET_DRY = 42%`.
- **Placement:** Post-Cabinet IR (simulating stereo studio mics behind a dry center cabinet).

### Scene B: Wide Stadium Lead Thickener (John Petrucci / Steve Vai)
- **Concept:** Makes single-note distorted solos soar out of speakers with epic three-dimensional width and subtle feedback shimmer.
- **Settings:** `DETUNE_LEFT = +12 cents`, `DETUNE_RIGHT = -12 cents`, `DELAY_LEFT = 14 ms`, `DELAY_RIGHT = 24 ms`, `FEEDBACK_CROSS = 18%`.
- **Space:** Stereo Modulated Ping-Pong Delay (`dotted 8th`, `420 ms`) + Hall Reverb (`2.4 s`).

### Scene C: Crystal Clean Studio Spread (SPX90 Symphonic Clean)
- **Concept:** Lush, wide, airy 1980s session-player clean arpeggio sound avoiding sea-sick chorus pitch swings.
- **Settings:** `DETUNE_LEFT = +6 cents`, `DETUNE_RIGHT = -6 cents`, `DELAY_LEFT = 9 ms`, `DELAY_RIGHT = 17 ms`, `THERMAL_DRIFT = 25%`.
- **Space:** Studio Plate Reverb (`2.1 s`, `22%` mix).

### Scene D: Bass Fusion Wide Harmonic Width (Mono-Safe > 160 Hz)
- **Concept:** Expands upper midrange harmonics on 4-, 5-, and 6-string electric basses into panoramic stereo while anchoring sub-bass weight dead center.
- **Settings:** `HPF_SAFE_HZ = 175 Hz`, `DETUNE_LEFT = +8 cents`, `DETUNE_RIGHT = -8 cents`, `DELAY_LEFT = 10 ms`, `DELAY_RIGHT = 18 ms`, `MIX_WET_DRY = 38%`.

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (Van Halen W/D/W Wall) / Scene B (Wide Stadium Lead).
- **Footswitch B:** Scene C (Crystal Clean Studio Spread).
- **Footswitch C:** Micro-Pitch Always-On Width Toggle / Bypass.
- **Knob 1 (MOD FX):** Detune Spread (`±3 cents` subtle double to `±20 cents` wide shimmer).
- **Knob 2 (DELAY):** Haas Pre-Delay asymmetry (`5 ms` to `30 ms`).
- **Knob 3 (BLEND):** Wet/Dry Stereo Wing balance.

### Tank-B Control Assignments
- Bassists performing solo fusion, chordal tapping, or studio pop sessions gain enormous spatial presence from Scene D (`HPF_SAFE_HZ = 175 Hz`), ensuring FOH subwoofers receive tight mono low end while stereo mains bloom outward cleanly.

### Black Box Desktop Configuration
- **True Stereo Out (L + R):** Essential for unleashing the Eventide-style stereo separation! Note that collapsing Left and Right to a mono cable turns off spatial widening and yields mild flanging—always feed stereo inputs on PA consoles or audio interfaces.
- **Expression Pedal 1:** Continuous control over `MIX_WET_DRY` (smoothly widening dry riffs into massive stereo stadium choruses!).
