# 12-String Craviola (Brazilian Acoustic Harpsichord-Guitar) Routing Guide

This guide details the asymmetric acoustic physics, 12-string double-course dynamic balancing, piezo metallic transient taming, and preset architecture for the **Brazilian 12-String Craviola** within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Acoustic Heritage & Asymmetric Chamber Physics

Invented in the late 1960s by legendary Brazilian guitarist **Paulinho Nogueira** in collaboration with luthier **Giannini**, the **Craviola** takes its name from *Cravo* (harpsichord) and *Viola* (guitar). Distinguished by its radical asymmetric teardrop body shape and dual/offset soundholes, it was designed specifically to bridge classical acoustic guitar warmth with harpsichord-like crystalline overtone shimmer—even earning admiration from rock legends such as **Jimmy Page** (Led Zeppelin) and **Toquinho**.

```
12-String Craviola Double-Course Configuration:
 Course 1 (1º Par): E4 + E4   (Unison - Plain Steel)
 Course 2 (2º Par): B3 + B3   (Unison - Plain Steel)
 Course 3 (3º Par): G3 + G4   (Octave Pair - Thin Wound + High Plain G4) <=== Crystalline Harpsichord Bite
 Course 4 (4º Par): D3 + D4   (Octave Pair - Wound + Plain Steel)
 Course 5 (5º Par): A2 + A3   (Octave Pair - Wound + Plain Steel)
 Course 6 (6º Par): E2 + E3   (Octave Pair - Heavy Wound + Plain Steel)
```

### 1.1 Electroacoustic Engineering Challenges

1. **Asymmetric Chamber Resonance (185 Hz – 265 Hz):** Unlike symmetrical figure-8 dreadnought guitars, the elongated asymmetric upper/lower bout shifts the primary Helmholtz air mode ($A_0$) and soundboard modes into staggered frequency peaks between $185\text{ Hz}$ and $265\text{ Hz}$, triggering localized low-mid feedback on amplified stages.
2. **Octave Pair Harshness (3.8 kHz – 6.2 kHz):** Four of the six courses feature an ultra-thin plain steel octave string sitting adjacent to a thick wound bass string. Under-saddle piezo pickups disproportionately amplify the metallic scratch and high-frequency transient spikes of the octave strings, especially the high $G_4$ ($392\text{ Hz}$ fundamental with piercing harmonics).
3. **Massive 12-String Pick Transients:** Simultaneous strumming of twelve high-tension steel strings hits digital converters with high crest-factor spikes that cause premature input clipping unless managed by fast transparent peak limiting.

---

## 2. DSP Signal Chain & Processing Topology

```
12-String Craviola In (Piezo / Dual-Source Mic)
   │
   ▼
[ High-Z 1MΩ Buffer & High-Pass Filter (65 Hz, 18 dB/oct) ]
   │
   ▼
[ Fast Transient Peak Limiter (Attack: 0.8 ms) ] (Clamps 12-string rasgueado spikes)
   │
   ▼
[ Dual-Band Dynamic Split (Crossover @ 240 Hz) ]
   ├── Low Band (< 240 Hz: Bass Fundamentals) ───► [ Tight Optical Comp & Asymmetric Notch @ 215 Hz ]
   │                                                                   │
   └── High Band (> 240 Hz: Unison & Octave Pairs)► [ Piezo Harshness Dip @ 4.4 kHz + Gentle Leveler ]
                                                                       │
                                   ┌───────────────────────────────────┘
                                   ▼
[ Asymmetric Rosewood / Spruce Body IR Convolution ] (Giannini Jacarandá Craviola IR)
                                   │
                                   ▼
[ Micro-Stereo Spatializer & Acoustic Hall Reverb ] ──► Stereo Output
```

---

## 3. Parameter Specifications

| Module | Parameter | Recommended Value | Purpose |
| :--- | :--- | :--- | :--- |
| **Input Filter**| High-Pass Filter | `65 Hz` (18 dB/oct) | Removes stage handling rumble while preserving $E_2$ ($82.4\text{ Hz}$). |
| **Peak Limiter**| Attack / Ceiling | `0.8 ms` / `-4.5 dBFS`| Clamps explosive 12-string strum transients smoothly. |
| **Asym Notch** | Freq / Q / Gain | `215 Hz` / `Q=6.0` / `-6.5 dB` | Suppresses asymmetric lower-bout cavity boom and stage feedback. |
| **Octave Tamer**| Freq / Q / Gain | `4.4 kHz` / `Q=2.8` / `-4.0 dB` | Smooths brittle metallic piezo bite on high $G_4$ and $E_4$ pairs. |
| **Body IR** | Impulse Response | `Craviola_Jacaranda_1970.wav`| Restores warm Brazilian rosewood acoustic chamber resonance. |
| **Low Comp** | Ratio / Attack | `3.2:1` / `18 ms` | Balances thick wound fundamentals evenly beneath octave chime. |
| **High Comp** | Ratio / Attack | `2.4:1` / `12 ms` | Gently reins in piercing octave string spikes during fingerpicking. |
| **Air Shelf** | Freq / Gain | `11.5 kHz` / `+2.0 dB` | Adds delicate silky air without upper-mid harshness. |
| **Reverb** | Decay / Pre-delay| `1.8 s` / `28 ms` | Classic warm wooden studio concert room. |

---

## 4. Factory Scene Presets

### Scene A: Paulinho Nogueira Clássico Fingerstyle (Harpsichord Warmth)
- **Concept:** Intimate, warm, and intricately articulated solo tone showcasing the Craviola's classical counterpoint clarity.
- **EQ & IR:** `Craviola_Jacaranda_1970.wav` IR, asymmetric notch @ 215 Hz, gentle optical leveling (`2.2:1`), high shelf air at `11 kHz`.
- **Space:** Intimate Wooden Studio Room (`1.5 s`, `18%` mix) keeping rapid fingerstyle arpeggios razor clear.

### Scene B: Craviola Folk Rasgueada (Jimmy Page / Acoustic Rock)
- **Concept:** Big, punchy, chiming strummed 12-string wall engineered for acoustic rock rhythms (*Tangerine* / *Stairway* acoustic layers).
- **Dynamics:** Fast peak limiter (`0.8 ms`), tight dual-band compression (`3.5:1` low / `2.8:1` high).
- **EQ:** Pronounced notch at 4.4 kHz (-5 dB) eliminating metallic pick clack; chest warmth at `160 Hz (+2 dB)`.
- **Space:** Bright Studio Plate Reverb (`2.0 s`, `22%` mix) + subtle stereo tape slap (`95 ms`).

### Scene C: MPB Acústica Estéreo (Toquinho / Bossa Warmth)
- **Concept:** Lush, velvety bossa-nova and MPB accompaniment tone with panoramic acoustic width and rolled-off upper harshness.
- **Modulation:** Ultra-subtle stereo micro-detuning (`+4 cents` left, `-4 cents` right) complementing the natural 12-string chorus beating.
- **EQ:** Smooth low-pass damping above `9.5 kHz`.
- **Space:** Warm Chamber Hall (`2.4 s`, `26%` mix).

### Scene D: Craviola Baroque Shimmer Ambient
- **Concept:** Ethereal ambient texture turning delicate harpsichord-like Craviola arpeggios into soaring orchestral synth clouds.
- **Space:** Modulated Stereo Tape Delay (`440 ms`, `35%` feedback) feeding Cathedral Shimmer Reverb (`5.5 s` decay, `+12 st` damped at `5 kHz`).

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (Paulinho Nogueira Fingerstyle) / Scene B (Folk Rasgueada).
- **Footswitch B:** Scene C (MPB Acústica Estéreo).
- **Footswitch C:** Scene D (Baroque Shimmer) / Tuner (calibrated for 12-string unison/octave verification).
- **Knob 1 (EQ):** Sweepable Asymmetric Body Notch (`180 Hz` to `280 Hz`) for soundcheck feedback suppression.
- **Knob 2 (COMP):** Peak Limiter / Octave Tamer intensity.
- **Knob 3 (REVERB):** Acoustic Room & Shimmer blend.

### Tank-B Control Assignments
- Craviola players needing rock-solid control over low $E_2$ and $A_2$ fundamentals in loud live bands can deploy Tank-B's transparent dual-band compressor and high-headroom input buffer.

### Black Box Desktop Configuration
- **High-Z 1 MΩ Input:** Essential for passive under-saddle piezo bridges (Fishman, LR Baggs, Shadow) to maintain organic transient dynamics.
- **Balanced XLR Direct Out:** Delivers pristine acoustic studio sound straight to live FOH mixing desks without external acoustic DI boxes.
