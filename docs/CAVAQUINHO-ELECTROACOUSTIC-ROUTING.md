# Brazilian Cavaquinho Electroacoustic Routing & Tone Guide

This guide details the acoustic physics, frequency management, transient control, and DSP preset architecture for the **Brazilian Cavaquinho** (4-string steel cavaquinho) within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Acoustic Profile & Dynamic Challenges of the Cavaquinho

The cavaquinho is the rhythmic and harmonic engine of Brazilian Samba, Choro, and Pagode. With its small soundboard and short scale length (~34 cm), its 4 steel strings operate at high physical tension in standard tuning:

```
String 1 (1ª Corda): D5 (Ré)  - High Plain Steel
String 2 (2ª Corda): B4 (Si)  - Plain Steel
String 3 (3ª Corda): G4 (Sol) - Plain Steel / Thin Wound
String 4 (4ª Corda): D4 (Ré)  - Wound Steel
```

### 1.1 Critical Electroacoustic Challenges

1. **Aggressive Pick Attack & Transient Spikes (5 kHz – 8 kHz):** Rapid, continuous sixteenth-note strumming (*palhetada de samba*) using stiff plastic or tortoiseshell picks produces severe high-frequency transient spikes. Through piezo pickups, this results in brittle, harsh "clack" and digital clipping.
2. **Body Cavity Boxiness (380 Hz – 490 Hz):** Due to the compact acoustic resonance chamber, low-mid frequencies build up dramatically, producing a hollow "cardboard" timbre and severe stage feedback in loud live performance environments (*rodas de samba*).
3. **Piezo Transducer Nasal Quack (2.2 kHz – 3.8 kHz):** Direct piezo under-saddle pickups capture string vibration without the natural acoustic wood resonance, resulting in an artificial nasal character.
4. **Lack of Sub-100 Hz Energy:** The fundamental frequency of the lowest string ($D_4$) is ~293.7 Hz. Low-frequency energy below 120 Hz is almost purely handling noise, cable rumble, and stage thumps that steal DSP headroom.

---

## 2. DSP Signal Chain & Processing Topology

```
Cavaquinho In (Piezo / Under-saddle Pickup)
   │
   ▼
[ High-Pass Filter (120 Hz, 18 dB/oct Butterworth) ]
   │
   ▼
[ Fast Peak Limiter & Transient Tamer ] (Clamps aggressive pick spikes)
   │
   ▼
[ 3-Band Parametric Surgical EQ ]
   ├── Band 1: Notch @ 420 Hz (Body cavity boxiness / feedback)
   ├── Band 2: Dip @ 3.1 kHz (Piezo nasal quack)
   └── Band 3: High Shelf @ 10 kHz (Air smoothness vs. harshness control)
   │
   ▼
[ Acoustic Cavaquinho Body IR Convolution ] (Brazilian Rosewood / Spruce Resonance)
   │
   ▼
[ Fast Optical Leveller Compressor ] (Smooths volume disparities between solo and rhythm)
   │
   ▼
[ Micro-Stereo Ambience / Small Wooden Chamber Reverb ] ──► Stereo Output
```

---

## 3. Parameter Specifications

| Module | Parameter | Recommended Value | Purpose |
| :--- | :--- | :--- | :--- |
| **Input Filter** | High-Pass Filter | `120 Hz` (18 dB/oct) | Eliminates body handling thump and stage vibrations. |
| **Peak Limiter** | Attack / Release | `0.8 ms` / `35 ms` | Tames high-velocity pick attacks during aggressive strumming. |
| **Peak Limiter** | Threshold | `-5.0 dBFS` | Prevents input buffer digital clipping during rasgueados. |
| **Notch EQ** | Freq / Q / Gain | `420 Hz` / `Q=6.0` / `-7.5 dB` | Removes hollow body cavity resonance and prevents feedback. |
| **Mid Dip** | Freq / Q / Gain | `3.1 kHz` / `Q=3.5` / `-4.0 dB` | Tames piezo quack and ear-piercing string bite. |
| **Body IR** | Impulse Response | `Cavaquinho_Spruce_Body.wav` | Restores natural wood bloom and acoustic instrument timbre. |
| **Compressor** | Ratio / Attack / Rel | `3.2:1` / `15 ms` / `90 ms` | Tightens rhythm consistency without squashing natural dynamics. |
| **Air Polish** | Freq / Gain | `8.5 kHz` / `+2.0 dB` | Adds sparkle to fingerstyle passages without harshness. |
| **Reverb** | Decay / Pre-delay | `1.1 s` / `18 ms` | Simulates an intimate wooden samba room. |

---

## 4. Factory Scene Presets

### Scene A: Samba & Pagode Rítmico (Palhetada Rasgada)
- **Concept:** Maximum clarity and punch for rapid, continuous rhythm strumming in noisy live band environments.
- **Dynamics:** Fast attack limiter (`0.8 ms`), tight optical compression (`3.5:1`, `80 ms` release).
- **EQ:** Aggressive notch at 420 Hz (-8 dB), mild high-shelf cut above 9 kHz to eliminate pick sizzle.
- **Space:** Very dry; Studio Room Reverb (`0.8 s`, `10%` mix) for punch and separation.

### Scene B: Choro Solista Articulado (Waldir Azevedo Style)
- **Concept:** Singing, expressive, and detailed articulation for rapid melodic runs, arpeggios, and counterpoint solos.
- **Dynamics:** Gentle leveling (`2.2:1`, `25 ms` attack) preserving fingerpicking touch dynamics.
- **EQ:** Flat low-mids, +2.5 dB air boost at 9 kHz, notch at 3.1 kHz to soften piezo bite.
- **Space:** Warm Acoustic Chamber Reverb (`1.6 s`, `22%` mix).

### Scene C: Cavaquinho Moderno Estéreo (Live Stage & Studio)
- **Concept:** Spacious modern electroacoustic sound with stereo micro-detuning for expansive acoustic presence.
- **Modulation:** Subtle stereo pitch detuning (`+5 cents` left, `-5 cents` right) for panoramic width.
- **Space:** Small Hall Reverb (`2.2 s`, `25%` mix) with `35 ms` pre-delay.
- **Mix:** 75% Direct Instrument / 25% Ambient Space.

### Scene D: Cavaquinho Vintage & Warm (Samba de Raiz)
- **Concept:** Round, dark, and organic timbre reminiscent of classic 1970s acoustic recordings (Cartola, Beth Carvalho).
- **Saturation:** Subtle warm tube preamp saturation (`15%` drive).
- **EQ:** High-cut filter at 7.5 kHz (12 dB/oct), warm low-mid push at 320 Hz (+1.5 dB).
- **Space:** Vintage Spring Reverb (`1.4 s`, `18%` mix).

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (Samba & Pagode Rítmico) / Scene B (Choro Solista).
- **Footswitch B:** Scene C (Cavaquinho Moderno Estéreo).
- **Footswitch C:** Scene D (Vintage & Warm) / Tuner.
- **Knob 1 (EQ / TONE):** Sweepable mid-notch frequency (`350 Hz` – `550 Hz`) for venue soundcheck feedback tuning.
- **Knob 2 (MOD FX):** Stereo Detune and chorus width.
- **Knob 3 (REVERB):** Ambient Room Decay and Dry/Wet balance.

### Tank-B Control Assignments
- The high-headroom input and robust low-cut filters on Tank-B make it an exceptional acoustic processor for cavaquinho players needing tight low-end control and anti-feedback filtering.

### Black Box Desktop Configuration
- **Input Impedance:** Select **High-Z (1 MΩ)** on channel input to eliminate piezo loading and loss of treble fidelity.
- **IR Loader Slot:** Dedicated 1024-point impulse response slot for authentic cavaquinho acoustic soundboard simulation.
