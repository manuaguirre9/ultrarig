# Stereo Comb Filter & Tuned Resonator Modeling Guide

This guide details the mathematical principles, fractional delay line interpolation, physical modeling synthesis, and practical preset configuration for the **Stereo Comb Filter & Tuned Acoustic Resonator** within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Principles & Mathematics of Comb Filtering and Resonators

A comb filter combines an audio signal with a delayed copy of itself. When implemented with high positive or negative feedback, it ceases to be a simple spatializer or chorus and transforms into an **acoustic resonator**—the mathematical foundation of physical modeling synthesis (such as Karplus-Strong string synthesis).

```
Audio Input x(n) ───────────────────► [ + ] ──────────────────────────────────────────► Output y(n)
                                       ▲                 │
                                       │                 ▼
                         [ Soft-Saturation Limiter ] [ Fractional Delay Line: D samples ]
                                       ▲                 │
                                       │                 ▼
                         [ Loop Feedback Gain: g ] ◄── [ Loop Damping LPF ]
```

### 1.1 Fundamental Resonant Frequencies

In a feedback comb filter, constructive interference occurs at integer multiples of the fundamental frequency determined by the delay time $D$:

$$f_0 = \frac{f_s}{D}$$

Where:
- $f_s$ is the audio sampling rate ($48\,000\text{ Hz}$).
- $D$ is the delay length in samples ($D = f_s / f_0$).

For musical tuning across the chromatic scale, $D$ must not be restricted to integer sample values; it requires **fractional delay interpolation** (using all-pass filters or cubic Hermite polynomials) to avoid pitch stepping and to track exact musical frequencies with sub-cent accuracy.

### 1.2 Material Emulation via Loop Damping

The character of the synthesized resonator is governed by a one-pole low-pass filter inserted directly into the feedback path:

$$H_{\text{damp}}(z) = \frac{1 - d}{1 - d \cdot z^{-1}}$$

- **Low Damping ($d \to 0$):** High frequencies circulate for many cycles, producing ringing metallic timbres, silver chimes, and steel pipes.
- **High Damping ($d \to 0.7$):** High frequencies decay almost instantaneously while fundamental frequencies sustain, perfectly emulating plucked nylon strings, acoustic marimbas, and wooden resonance chambers.

---

## 2. DSP Signal Chain & Topology

```
Input Audio (Guitar / Bass / Percussion)
   │
   ├───► [ Dry Direct Signal Level ] ──────────────────────────────────────────┐
   │                                                                           │
   ▼                                                                           │
[ Input Transient Exciter / Soft Clipper ]                                     │
   │                                                                           │
   ├───► [ Resonator Channel Left (Delay: D_L, Feedback: g) ]                  │
   │           │                                                               │
   │           └──► [ Loop Damping Filter L & Soft Limiter ] ──┐               │
   │                                                           │               │
   └───► [ Resonator Channel Right (Delay: D_R, Feedback: g) ] │               │
               │                                               │               │
               └──► [ Loop Damping Filter R & Soft Limiter ] ──┤               │
                                                               ▼               │
[ Stereo Panning & Detune Matrix (Unison / Octave / 5th) ] ──► [ Wet Level ] ──┴──► Master Output
```

---

## 3. Parameter Specifications

| Parameter | Range | Default | Unit | Description |
| :--- | :--- | :--- | :--- | :--- |
| `RESONATOR_MODE`| `TUNED_NOTE` / `CHORUS_COMB` / `METALLIC` | `TUNED_NOTE` | mode | Resonator mode: Tuned Note tracks musical pitch; Metallic provides industrial ring. |
| `ROOT_NOTE` | `C1` to `C6` | `A2 (110 Hz)` | note | Fundamental resonance frequency of the comb filter. |
| `FINE_TUNE` | `-50` to `+50`| `0` | cents | Micro-pitch tuning offset for exact calibration. |
| `RESONANCE (Q)` | `0` - `99.5` | `88` | % | Feedback recirculation gain $g$; controls sustain duration. |
| `MATERIAL_DAMP` | `1.0` - `18.0`| `6.5` | kHz | High-frequency damping inside the feedback loop (wood vs. metal). |
| `STEREO_OFFSET` | `0` - `100` | `25` | % | Frequency difference between Left and Right resonators (octave/fifth/detune). |
| `PITCH_TRACK` | `OFF` / `ON` | `OFF` | bool | Automatically shifts resonator pitch to track played monophonic notes. |
| `SAT_LIMIT` | `0` - `100` | `60` | % | Non-linear soft-saturation threshold preventing feedback runaway. |
| `MIX_WET_DRY` | `0` - `100` | `45` | % | Parallel balance between raw direct instrument and resonant acoustic body. |

---

## 4. Factory Scene Presets

### Scene A: Karplus-Strong Plucked String (Acoustic Chime)
- **Concept:** Transforms pick attacks into ringing, plucked acoustic harp or koto notes using physical modeling.
- **Tuning:** `ROOT_NOTE = D3 (146.8 Hz)`, `RESONANCE = 92%`, `MATERIAL_DAMP = 4.2 kHz` (woody warmth).
- **Spatial:** `STEREO_OFFSET = 12 cents` micro-detune for lush acoustic width.
- **Mix:** `MIX_WET_DRY = 50%`.

### Scene B: Sci-Fi Metallic Cyber Lead (Industrial Talkbox)
- **Concept:** High-Q metallic resonant formant that turns single-coil guitar leads into robotic synth timbres.
- **Tuning:** `ROOT_NOTE = E4 (329.6 Hz)`, `RESONANCE = 96%`, `MATERIAL_DAMP = 14.5 kHz` (pristine steel bite).
- **Saturation:** `SAT_LIMIT = 75%` (warm non-linear clipping).
- **Space:** Fast Stereo Slapback Echo (`120 ms`) + Plate Reverb.
- **Mix:** `MIX_WET_DRY = 65%`.

### Scene C: Tuned Pipe & Flute Resonator (Ethereal Wind Chime)
- **Concept:** Hollow, cylindrical air-column resonance with 5th harmonic stereo spread.
- **Tuning:** `ROOT_NOTE = A3 (220 Hz)` on Left, `E4 (330 Hz)` (Perfect 5th) on Right.
- **Resonance & Damping:** `RESONANCE = 89%`, `MATERIAL_DAMP = 5.8 kHz`.
- **Space:** Ambient Cathedral Hall Reverb (`4.5 s` decay time).
- **Mix:** `MIX_WET_DRY = 40%`.

### Scene D: Deep Resonant Ambient Drone (Sub-Harmonic Space)
- **Concept:** Low-frequency sub-drone that blooms into vast soundscapes behind slow chords or bass notes.
- **Tuning:** `ROOT_NOTE = C2 (65.4 Hz)`, `RESONANCE = 95%`, `MATERIAL_DAMP = 2.8 kHz`.
- **Modulation:** Gentle LFO drift (`0.15 Hz`) modulating resonance cutoff.
- **Space:** Shimmer Reverb (`8.0 s` decay, `35%` mix).
- **Mix:** `MIX_WET_DRY = 55%`.

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (Karplus-Strong Plucked String) / Scene B (Cyber Lead).
- **Footswitch B:** Scene C (Tuned Pipe & Flute) / Scene D (Ambient Drone).
- **Footswitch C:** Resonator Bypass / Tap Pitch.
- **Knob 1 (MOD FX):** Resonator Root Pitch Selection.
- **Knob 2 (TONE):** Material Damping (turn left for wood, right for bright metal).
- **Knob 3 (FEEDBACK / MIX):** Resonance Q and Wet/Dry parallel mix.

### Tank-B Control Assignments
- Bassists can lock the resonator to sub-octave fundamentals ($E_1 = 41.2\text{ Hz}$, $A_1 = 55.0\text{ Hz}$) to generate massive synth-bass sub-drops and filtered resonant growls.

### Black Box Desktop Configuration
- **Expression Pedal 1:** Continuous sweep of `ROOT_NOTE` (acting as a pitch-whammy acoustic resonator).
- **MIDI CC #78:** Direct chromatic note selection via external keyboard or sequencer.
