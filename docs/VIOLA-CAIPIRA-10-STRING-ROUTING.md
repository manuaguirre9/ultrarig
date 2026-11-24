# Viola Caipira (10-String) Electroacoustic Routing & Tone Guide

This guide details the acoustic profile, frequency management, dynamic response shaping, and DSP preset architecture for the **10-String Viola Caipira** (Brazilian 10-string folk guitar) within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Acoustic & Harmonic Profile of the 10-String Viola

The Viola Caipira features 10 steel strings arranged in 5 double courses (pares de cordas). Its distinctive timbre combines metallic brilliance, resonant acoustic chamber chime, and rich octave harmonic reinforcement.

```
Pair 1 (1º Par - Cantadeiras):  E4 + E4   (Unison - High Plain Steel)
Pair 2 (2º Par - Turinas):      B3 + B3   (Unison - Plain Steel)
Pair 3 (3º Par - Meio-Corpo):   G#3 + G#4 (Octave - Wound Low + Plain High)
Pair 4 (4º Par - Canotilho):    E3 + E4   (Octave - Wound Low + Plain High)
Pair 5 (5º Par - Toero):        B2 + B3   (Octave - Wound Low + Plain High)
```
*(Standard Cebolão in E major tuning; alternative tunings include Cebolão in D, Rio Abaixo in G, and Boiadeira).*

### 1.1 Acoustic Challenges with Piezo & Magnetic Pickups

1. **Pick & Dedeira Transient Spikes (3.5 kHz – 6.5 kHz):** Traditional Brazilian *ponteado* utilizes a steel or plastic thumb pick (*dedeira*) and fingerpicks. This generates intense, ultra-fast transients that cause piezo transducer clipping and abrasive acoustic "clack".
2. **Body Resonance Boom (210 Hz – 280 Hz):** The small-bodied acoustic chamber resonates sharply in the lower midrange, leading to acoustic feedback during live stage monitoring.
3. **Phase Beating in Unison Pairs:** Minute pitch deviations between the two unisons in Pairs 1 and 2 create natural acoustic chorusing, which can sound phase-smeared or metallic if processed through poorly aligned digital filters.
4. **Octave Balance Imbalance (Pairs 3, 4, and 5):** The wound lower string carries heavy low-mid fundamental weight, while the unwound octave string possesses cutting high-mid energy. Improper compression can over-accentuate the octave string or muddle the bass fundamentals.

---

## 2. DSP Signal Chain & Processing Topology

```
Viola Caipira In (Piezo / Mic)
   │
   ▼
[ High-Z Input Buffer & Low-Cut (75 Hz 18dB/oct) ]
   │
   ▼
[ Fast Peak Limiter & Transient Tamer ] (Softens harsh dedeira clicks)
   │
   ▼
[ Parametric Surgical EQ ]
   ├── Band 1: Notch @ 235 Hz (Body cavity resonance boom)
   ├── Band 2: Dip @ 3.4 kHz (Piezo nasal bite)
   └── Band 3: High Shelf @ 10 kHz (Air and chime smoothness)
   │
   ▼
[ Acoustic Body IR Convolution ] (Brazilian Cedar / Jacarandá Body Resonance)
   │
   ▼
[ Dual-Band Dynamic Compressor ] (Balances low-mid wound strings vs. high plain octaves)
   │
   ▼
[ Subtle Micro-Stereo Widener / Ambient Space ]
   │
   ▼
[ Studio Ambience / Plate Reverb ] ──► Stereo Output
```

---

## 3. Parameter Specifications

| Module | Parameter | Recommended Value | Purpose |
| :--- | :--- | :--- | :--- |
| **Input Filter** | High-Pass Filter | `75 Hz` (18 dB/oct) | Removes stage rumble and handling thump. |
| **Limiter** | Attack / Release | `1.2 ms` / `45 ms` | Clamps instantaneous steel pick clicks without squashing decay. |
| **Limiter** | Threshold | `-6.0 dBFS` | Prevents digital overs on aggressive rasgueado / pagode strums. |
| **Notch EQ** | Freq / Q / Gain | `235 Hz` / `Q=6.5` / `-7.0 dB` | Suppresses body cavity resonance and feedback. |
| **Mid Cut** | Freq / Q / Gain | `3.4 kHz` / `Q=3.0` / `-3.5 dB` | Tames piezo "quack" and metallic harshness. |
| **Body IR** | Model | `Viola_Caipira_Cedar_A.wav` | Restores natural acoustic timber and body bloom. |
| **Dynamic Comp**| Ratio / Knee | `2.8:1` / `Soft` | Smooths dynamic volume range between solo lines and chords. |
| **Spatial Width**| Width % | `40%` | Gives spacious width to unison and octave string spread. |
| **Reverb** | Decay / Pre-delay| `1.6 s` / `24 ms` | Warm studio acoustic room with clear separation. |

---

## 4. Factory Scene Presets

### Scene A: Ponteado Caipira Tradicional (Fingerstyle / Fast Solos)
- **Concept:** Crystal-clear articulation for rapid single-note runs and double-course melodies (*ponteados*).
- **Dynamics:** Fast attack peak limiter (`1.0 ms`), mild compression (`2.2:1`).
- **EQ:** +2.0 dB air shelf at 8.5 kHz, notch at 240 Hz (-6 dB).
- **Space:** Dry/Wet `15%`, Studio Room Reverb (`1.2 s`), preserving rhythmic speed and definition.

### Scene B: Moda de Viola Encorpada (Strummed Rhythm & Vocal Accompaniment)
- **Concept:** Warm, resonant, and balanced sound for rhythmic strumming, cururu, and cana-verde grooves.
- **Dynamics:** Medium-slow compressor (`18 ms` attack, `120 ms` release) for rich sustain.
- **EQ:** Low-mid warmth (+1.5 dB at 380 Hz), high-cut filter at 12 kHz to tame raspiness.
- **Space:** Wooden Chamber Reverb (`2.0 s`), Dry/Wet `25%`.

### Scene C: Viola Espacial Estéreo (Modern Ambient & Instrumental)
- **Concept:** Wide cinematic texture for contemporary acoustic instrumentalists (Almir Sater, Renato Andrade styles).
- **Modulation:** Subtle stereo detune (`+6 cents` left, `-6 cents` right) creating a lush, floating double-course image.
- **Space:** Lush Plate Reverb (`3.2 s`), Stereo Delay (`dotted 8th`, `420 ms`, `20%` feedback).
- **Mix:** Dry/Wet `35%`.

### Scene D: Viola Blues & Folk Saturada (Warm Tube & Tape Character)
- **Concept:** Gritty roots-folk tone featuring gentle tube preamp warmth and tape saturation.
- **Saturation:** Vintage Tube Preamp Drive at `18%`, soft tape compression at `3:1`.
- **EQ:** Warm vintage contour: rolled-off highs above 9 kHz, slight push at 1.8 kHz for midrange bite.
- **Space:** Vintage Spring Reverb (`1.8 s`), Dry/Wet `20%`.

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (Ponteado Tradicional) / Scene B (Moda Encorpada).
- **Footswitch B:** Scene C (Viola Espacial Estéreo).
- **Footswitch C:** Scene D (Viola Blues / Folk).
- **Knob 1 (EQ):** Mid Cut / Notch sweep (`200 Hz` – `400 Hz`).
- **Knob 2 (MOD FX):** Stereo Detune / Chorusing depth.
- **Knob 3 (REVERB):** Space Decay & Mix.

### Tank-B Control Assignments
- **Footswitch 1 / 2:** Toggle between acoustic clarity and warm low-mid body resonance.
- **Compressor Knob:** Adjusts threshold to balance soft fingerpicking against heavy thumbpick strokes.

### Black Box Desktop Configuration
- **Input Impedance:** Set hardware input to **High-Z (1 MΩ)** when plugging passive piezo pickups directly without an external preamp.
- **IR Loader Slot:** Dedicated 1024-sample slot for acoustic body impulse responses (`48 kHz / 24-bit`).
