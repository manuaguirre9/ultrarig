# Arabic & Turkish Oud (Alaúde Oriental) Electroacoustic Routing Guide

This guide details the acoustic physics of the pear-shaped wooden bowl, fretless microtonal sustain dynamics, *risha* plectrum transient control, and preset configuration for the **Arabic and Turkish Oud** within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Acoustic Profile & Heritage of the Fretless Oud

The **Oud** (meaning "wood" in Arabic) is the ancestral precursor to the European lute and guitar. Characterized by a fretless neck, deep ribbed bowl back (*qas'ah*), thin spruce soundboard with ornate rosettes (*shamsiyat*), and 11 strings (five double courses plus one single bass string), it is played with a long flexible plectrum called a **risha** (historically an eagle quill).

```
Course 1 (1º Par - Zir):   C4 + C4 (High Plain Nylon / Fluorocarbon)
Course 2 (2º Par - Mathna): G3 + G3 (Nylon)
Course 3 (3º Par - Mathlath): D3 + D3 (Silverplated Wound Nylon)
Course 4 (4º Par - Bamm):  A2 + A2 (Silverplated Wound Nylon)
Course 5 (5º Par - Qarar): F2 + F2 (Heavy Wound Nylon)
String 6 (Single Bass):    C2      (Low Single Drone / Bass String: ~65.4 Hz)
```
*(Standard Arabic C-to-C tuning; Turkish tuning frequently employs $D_2, A_2, B_2, E_3, A_3, D_4$ for brighter pitch projection).*

### 1.1 Fretless Mechanics & Electroacoustic Obstacles

1. **Deep Ribbed Bowl Resonance (160 Hz – 240 Hz):** The massive hemispherical wooden bowl creates powerful acoustic amplification centered around 190 Hz. Under stage monitors or PA reinforcement, internal microphones and bridge transducers trigger severe low-mid boom and feedback.
2. **Fretless String Damping & Glissando Loss:** Because fingers press strings directly against an unfretted hardwood fingerboard (ebony or rosewood) rather than metal frets, soft fingertips absorb high-frequency overtones and reduce mechanical sustain during slow *maqam* glissandos.
3. **Aggressive *Risha* Pick Attack (3.2 kHz – 5.8 kHz):** Rapid tremolo picking (*fardah*) and sharp downward strokes near the bridge produce loud transient clicks on glued-bridge piezo pickups.
4. **Double-Course Beating:** Natural micro-pitch variations across paired nylon strings add warmth acoustically, which must be preserved cleanly without comb-filter phase smearing.

---

## 2. DSP Signal Chain & Processing Topology

```
Oud In (Floating / Under-Bridge Piezo OR Internal Condenser Mic)
   │
   ▼
[ High-Pass Filter (55 Hz, 18 dB/oct Butterworth) ] (Retains low C2 = 65.4 Hz while blocking stage thump)
   │
   ▼
[ Fast Transient Limiter ] (Clamps sharp risha plectrum strikes)
   │
   ▼
[ Parametric Surgical Notch EQ ]
   ├── Band 1: Notch @ 190 Hz (Hemispherical bowl boom / stage feedback)
   ├── Band 2: Dip @ 3.6 kHz (Bridge piezo synthetic click)
   └── Band 3: Upper-Mid Air (+2.0 dB @ 6.5 kHz for fingerboard glide clarity)
   │
   ▼
[ Oud Acoustic Bowl IR Convolution ] (Walnut Bowl & European Spruce Soundboard)
   │
   ▼
[ Transparent Optical Sustainer Compressor ] (Extends fretless note sustain smoothly)
   │
   ▼
[ Acoustic Courtyard / Stone Chamber Reverb ] ──► Stereo Output
```

---

## 3. Parameter Specifications

| Module | Parameter | Recommended Value | Purpose |
| :--- | :--- | :--- | :--- |
| **Input Filter** | High-Pass Filter | `55 Hz` (18 dB/oct) | Preserves low $C_2$ bass string ($65.4\text{ Hz}$) while eliminating thumps. |
| **Peak Limiter** | Attack / Release | `1.0 ms` / `40 ms` | Smooths abrupt *risha* tremolo strikes without dulling attack. |
| **Bowl Notch** | Freq / Q / Gain | `190 Hz` / `Q=6.0` / `-7.5 dB` | Tames deep wooden bowl acoustic resonance and stage feedback. |
| **Piezo Tamer** | Freq / Q / Gain | `3.6 kHz` / `Q=3.0` / `-3.5 dB` | Softens dry bridge transducer hardness. |
| **Body IR** | Impulse Response | `Oud_Walnut_Spruce_Mic.wav`| Emulates warm, spacious ribbon-mic soundboard bloom. |
| **Optical Comp** | Ratio / Attack / Rel | `2.6:1` / `28 ms` / `190 ms` | Sustains fretless slides (*glissandos*) smoothly. |
| **Clarity Shelf**| Freq / Gain | `7.2 kHz` / `+2.0 dB` | Enhances *risha* string detail and subtle double-course shimmer. |
| **Reverb** | Type / Decay / Mix | `Stone Courtyard` / `2.2 s` / `22%` | Evokes authentic acoustic halls and Mediterranean courtyards. |

---

## 4. Factory Scene Presets

### Scene A: Classical Arabic Taksim Solo (Munir Bashir / Farid al-Atrash)
- **Concept:** Intimate, organic, and expressive solo tone tailored for contemplative microtonal *maqam* improvisations.
- **Filtering:** `HPF = 55 Hz`, bowl notch @ 188 Hz (-8 dB), mild high roll-off above 10 kHz.
- **Dynamics:** Gentle optical sustain (`2.2:1`, `30 ms` attack) allowing seamless glissandos and quarter-tone vibrato.
- **Space:** Intimate Wooden Chamber Reverb (`1.9 s`, `24%` mix).

### Scene B: Modern Mediterranean Fusion (Anouar Brahem / Rabih Abou-Khalil)
- **Concept:** Polished, focused electroacoustic timbre engineered to sit effortlessly alongside upright bass, jazz piano, and frame drums.
- **Filtering:** Tighter `HPF = 75 Hz`, crisp mid clarity (+2 dB @ 1.4 kHz), piezo dip @ 3.6 kHz.
- **Modulation:** Subtle stereo micro-widening (`+4 cents` left, `-4 cents` right) expanding double-course depth.
- **Space:** Studio Plate Reverb (`2.1 s`, `20%` mix) with `30 ms` pre-delay.

### Scene C: Turkish Fast Risha Taqsim (High Articulation)
- **Concept:** Crisp, snappy, forward midrange attack designed for blistering Turkish-style alternate picking and fast rhythmic ornamentation.
- **Dynamics:** Fast limiter (`0.8 ms` attack) controlling heavy strikes + tight compression (`3.2:1`).
- **EQ:** Slight low-mid cleanout (-3 dB @ 280 Hz) and upper-mid boost (+2.5 dB @ 2.8 kHz).
- **Space:** Short Stone Room (`1.1 s`, `14%` mix).

### Scene D: Ambient Mystical Oud (Desert Courtyard Reverb)
- **Concept:** Atmospheric, cinematic desert soundscape weaving slow rhythmic repeats into vast cavernous stone reverberation.
- **Delay & Space:** Stereo Warm Tape Delay (`dotted 8th`, `440 ms`, `30%` feedback) feeding Stone Cathedral Reverb (`5.0 s` decay, `38%` mix).

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (Classical Taksim) / Scene B (Mediterranean Fusion).
- **Footswitch B:** Scene C (Turkish Fast Taqsim).
- **Footswitch C:** Scene D (Ambient Mystical Oud) / Tuner (calibrated for quarter-tone offsets).
- **Knob 1 (EQ):** Sweepable Bowl Notch frequency (`150 Hz` to `260 Hz`) for soundcheck feedback control.
- **Knob 2 (COMP):** Fretless Optical Sustain depth.
- **Knob 3 (REVERB):** Courtyard Ambience mix.

### Tank-B Control Assignments
- Tank-B excels at capturing the deep $C_2$ and $F_2$ fundamentals of bass-heavy Arabic ouds, providing clean headroom and responsive low-end limiting.

### Black Box Desktop Configuration
- **High-Z Buffer:** Essential when using passive soundboard transducers (e.g. K&K, Shadow, or Schertler Dyn-Oud) without an external preamp.
- **Dual-Source Blending:** Connect an internal mini-condenser mic to Channel R and a bridge piezo to Channel L, blending both inside UltraRig with phase inversion calibration.
