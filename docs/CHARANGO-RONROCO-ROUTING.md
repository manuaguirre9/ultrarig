# Andean Charango & Ronroco Electroacoustic Routing & Tone Guide

This guide details the acoustic profile, double-course string balance, percussive rasgueado transient management, and preset architecture for the **Andean Charango** and **Ronroco** (baritone charango) within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Acoustic Profile & Heritage of the Charango & Ronroco

Originating in the Andean Altiplano (Bolivia, Peru, Argentina, and Chile), the **Charango** and its baritone sibling, the **Ronroco**, are 10-string instruments arranged in 5 double courses. Their distinctive sound combines crystalline, harp-like chime, rapid percussive rasgueados, and re-entrant octave cascades.

```
--- CHARANGO (Standard Tuning: 5 Double Courses) ---
Course 1 (1º Orden): E5 + E5 (High Unison Nylon)
Course 2 (2º Orden): A4 + A4 (Unison Nylon)
Course 3 (3º Orden): E5 + E4 (Octave Pair - High E5 + Low E4 Wound)  <=== Re-entrant Anchor
Course 4 (4º Orden): C5 + C5 (Unison Nylon)
Course 5 (5º Orden): G4 + G4 (Unison Nylon)

--- RONROCO (Baritone Tuning - Santaolalla Style) ---
Course 1 (1º Orden): B4 + B4 (Unison)
Course 2 (2º Orden): E4 + E4 (Unison)
Course 3 (3º Orden): B4 + B3 (Octave Pair)
Course 4 (4º Orden): G4 + G4 (Unison)
Course 5 (5º Orden): D4 + D4 (Unison Wound / Nylon)
```

### 1.1 Charango vs. Ronroco Sonic Distinction

- **The Charango (~37 cm scale length):**
  - High-pitched, vibrant, and energetic.
  - Historically constructed from armadillo carapace (*quirquincho*) or solid one-piece carved hardwoods (*naranjillo*, *jacarandá*).
  - Primary playing styles include the *repique* (rapid 5-finger tremolo) and *chullu* (rhythmic muted rasgueado).
  - Main acoustic issue: Brittle, ear-piercing transient clack (4.5 kHz – 7 kHz) through piezo pickups, and boxy cavity resonance around 480 Hz – 620 Hz.
- **The Ronroco (~48 cm to 52 cm scale length):**
  - Pioneered by the Cavour brothers and popularized globally by two-time Academy Award-winning composer **Gustavo Santaolalla** (*The Last of Us*, *Brokeback Mountain*, *Babel*, *Motorcycle Diaries*).
  - Boasts a larger, deeper soundbox producing melancholic, haunting, cello-like warmth and singing sustain.
  - Main acoustic issue: Boomy lower-mid buildup (180 Hz – 260 Hz) and piezo nasal quack.

---

## 2. DSP Signal Chain & Processing Topology

```
Charango / Ronroco In (Piezo / Under-saddle Transducer)
   │
   ▼
[ Switchable High-Pass Filter: Charango (150 Hz) / Ronroco (75 Hz) ]
   │
   ▼
[ Fast Peak Limiter & Transient Tamer ] (Clamps aggressive repique & rasgueado clack)
   │
   ▼
[ 3-Band Parametric Surgical Notch EQ ]
   ├── Band 1: Notch @ 220 Hz (Ronroco body boom) OR 520 Hz (Charango cavity)
   ├── Band 2: Dip @ 3.4 kHz (Piezo under-saddle hardness)
   └── Band 3: Air Polish @ 11 kHz (Smooth acoustic shimmer)
   │
   ▼
[ Dual Body IR Convolution: Hardwood Charango vs. Deep Cedar Ronroco ]
   │
   ▼
[ Optical Leveler Compressor ] (Smooths volume disparities between fingerpicking and strumming)
   │
   ▼
[ Stereo Ambient Reverb & Shimmer Matrix ] ──► Stereo Output
```

---

## 3. Parameter Specifications

| Module | Parameter | Charango Setting | Ronroco Setting | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **Input Filter** | High-Pass Filter | `150 Hz` (18 dB/oct) | `75 Hz` (18 dB/oct) | Removes handling rumble without thinning low string fundamentals. |
| **Peak Limiter** | Attack / Release | `0.6 ms` / `30 ms` | `1.2 ms` / `60 ms` | Tames high-velocity rasgueado transients. |
| **Peak Limiter** | Threshold | `-4.5 dBFS` | `-6.0 dBFS` | Prevents digital input clipping during energetic strums. |
| **Body Notch** | Freq / Q / Gain | `520 Hz` / `Q=6.5` / `-7 dB`| `220 Hz` / `Q=7.0` / `-8 dB`| Suppresses body cavity boom and venue stage feedback. |
| **Mid Dip** | Freq / Q / Gain | `3.6 kHz` / `Q=3.0` / `-4 dB`| `3.2 kHz` / `Q=2.5` / `-3.5 dB`| Eliminates synthetic piezo quack on nylon double courses. |
| **Body IR** | Profile | `Charango_Jacaranda.wav`| `Ronroco_Cedar_Concert.wav`| Restores authentic wooden chamber bloom. |
| **Compressor** | Ratio / Attack | `2.5:1` / `15 ms` | `2.2:1` / `25 ms` | Balances dynamic level between soft arpeggios and loud strikes. |
| **Air Shelf** | Freq / Gain | `11.0 kHz` / `+2.0 dB` | `10.5 kHz` / `+1.5 dB` | Adds delicate air and string breath without harshness. |
| **Reverb** | Decay / Pre-delay | `1.4 s` / `18 ms` | `2.8 s` / `35 ms` | Acoustic room (Charango) vs. Cinematic Space (Ronroco). |

---

## 4. Factory Scene Presets

### Scene A: Charango Tradicional Repicado (Huayno & Carnaval)
- **Concept:** Vibrant, percussive clarity with ultra-fast attack response for traditional Andean huaynos, cuecas, and carnavales.
- **Filtering & Notch:** `HPF = 150 Hz`, notch @ 520 Hz (-7 dB), dip @ 3.6 kHz (-4 dB).
- **Dynamics:** Fast peak limiter (`0.6 ms`), tight optical compression (`3:1`).
- **Space:** Intimate Mountain Room Reverb (`1.2 s`, `15%` mix).

### Scene B: Ronroco Santaolalla Cinematic Warmth (The Last of Us)
- **Concept:** The quintessential Gustavo Santaolalla tone: deep, melancholic, intimate, and organic with velvety note decay.
- **Filtering & Notch:** `HPF = 75 Hz`, notch @ 220 Hz (-8 dB), mild high-frequency smoothing above 8.5 kHz.
- **Dynamics:** Gentle optical leveling (`2.0:1`, `30 ms` attack) preserving delicate fingerpicking nuances.
- **Body IR:** Deep Cedar Ronroco concert impulse response.
- **Space:** Warm Wooden Hall Reverb (`2.6 s`, `25%` mix) with `30 ms` pre-delay.

### Scene C: Andean Folk Stereo Ambient (Inti-Illimani Style)
- **Concept:** Expansive stereo width and sparkling micro-detuning for contemporary world-music ensembles.
- **Modulation:** Subtle stereo micro-detuning (`+5 cents` left, `-5 cents` right) creating a wide double-course image.
- **Space:** Cathedral Space (`3.5 s` decay) + Stereo Modulated Delay (`dotted 8th`, `420 ms`).
- **Mix:** 70% Direct Instrument / 30% Space.

### Scene D: Ronroco Shimmer Cloud (Ethereal Soundtrack)
- **Concept:** Ambient cinematic pad where upper-octave shimmer blossoms softly behind solitary plucked ronroco notes.
- **Modulation:** Upper-octave pitch-shifted reverb (+12 st) with smooth low-pass damping.
- **Space:** Infinite Shimmer Reverb (`7.5 s` decay time, `40%` wet mix).

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (Charango Tradicional) / Scene B (Ronroco Santaolalla).
- **Footswitch B:** Scene C (Andean Folk Ambient).
- **Footswitch C:** Scene D (Ronroco Shimmer Cloud) / Tuner.
- **Knob 1 (EQ):** Body Notch frequency sweep (`180 Hz` to `600 Hz`).
- **Knob 2 (MOD FX):** Stereo Detune and Shimmer Bloom.
- **Knob 3 (REVERB):** Decay Time and Wet/Dry balance.

### Tank-B Control Assignments
- The Tank-B is ideal for processing the Ronroco: its high-headroom input circuitry and dedicated low-frequency shaping prevent the deep baritone fundamentals from overloading the DSP.

### Black Box Desktop Configuration
- **High-Z Input:** Set hardware input to **1 MΩ** to prevent passive piezo loading and treble rolloff.
- **Dual IR Slots:** Load `Charango_Jacaranda.wav` in IR Slot 1 and `Ronroco_Cedar_Concert.wav` in IR Slot 2 for instant footswitch switching between instruments during live sets.
