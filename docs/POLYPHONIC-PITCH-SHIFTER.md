# Polyphonic Pitch Shifter & Chord Intelligence Modeling Guide

This guide details the algorithmic principles, transient preservation techniques, spectral phase-locking, and practical preset configuration for **Real-Time Polyphonic Pitch Shifting** within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Principles of Real-Time Polyphonic Pitch Shifting

Monophonic pitch shifters rely on time-domain autocorrelation or zero-crossing detection to estimate a single fundamental frequency ($f_0$). When presented with chords, intervals, or ringing open strings, monophonic algorithms experience frequency ambiguity, resulting in violent glitching, phase tremolo, and audible "gargle."

UltraRig's **Polyphonic Pitch Shifting Engine** utilizes a hybrid **Phase Vocoder with Transient Detection & Identity Phase Locking**:

```
Audio In (Polyphonic Chords / Notes)
   │
   ├───► [ Transient Transient Detector ] (Energy Flux / High-Frequency Content)
   │           │
   │           ▼ (Transient Event Trigger: Bypass Phase Smearing)
   ▼           │
[ Short-Time Fourier Transform (STFT) Analysis ] ◄─┘
   │
   ▼
[ Spectral Peak Tracking & Identity Phase-Locking ]
   │ (Maintains phase coherence across adjacent frequency bins)
   ▼
[ Pitch Transposition & Resampling Engine ] (Ratio: 2^(semitones / 12))
   │
   ▼
[ Inverse FFT (IFFT) / Overlap-Add (OLA) Synthesis ]
   │
   ▼
[ Polyphonic Chroma Analysis & Intelligent Scale Quantizer ] ──► Stereo Summing & Output
```

### 1.1 Transient Preservation (Anti-Smearing)

The primary audible drawback of traditional frequency-domain phase vocoders is transient "smearing"—the softening of pick attacks into mushy, hollow thuds. UltraRig implements a parallel time-domain transient detector:
1. When a pick attack is detected via high spectral flux, the transient slice is passed with minimal phase modification.
2. The sustained portion (tail) of the chord is then smoothly crossfaded into the phase vocoder engine.
3. This guarantees crisp, percussive string articulation even when transposing dense bar chords.

### 1.2 Identity Phase-Locking

In polyphonic audio, individual harmonics from different notes interact within the same FFT bins. Without phase-locking, the vocoder recalculates each bin's phase independently, causing phase dispersion (the classic "underwater / metallic" vocoder artifact). 

By grouping adjacent spectral bins around local amplitude peaks and locking their phase differences:

$$\Delta \phi_k = \phi_k - \phi_{\text{peak}}$$

The harmonic relationship of each chord tone is preserved, delivering an organic, natural instrument timbre.

### 1.3 Polyphonic Virtual Drop-Tuning & Capo

By applying uniform polyphonic pitch shifting without harmonic distortion, guitarists can alter their instrument's tuning digitally in real time:
- **Virtual Drop Tuning:** Shifts incoming audio down by 1 to 7 semitones (e.g., E Standard to Drop D, D Standard, C Standard, or B Standard) without string flabbiness or intonation issues.
- **Virtual Capo:** Transposes upward by 1 to 7 semitones, emulating a mechanical capo without altering neck reach or fret accessibility.

---

## 2. DSP Signal Chain & Topology

```
Input Audio (Polyphonic Chords / Solos)
   │
   ├───► [ Dry Direct Signal Level ] ──────────────────────────────────────────┐
   │                                                                           │
   ▼                                                                           │
[ Transient Energy Detector ]                                                  │
   │                                                                           │
   ▼                                                                           │
[ Polyphonic Pitch Shifter Core ]                                              │
   ├── Engine Mode: Vocoder Poly / Resample                                    │
   ├── Semitone Shift: -24 to +24 st                                           │
   ├── Fine Detune: -50 to +50 cents                                           │
   └── Tracking Filter: Low / High Frequency Cut                               │
   │                                                                           │
   ▼                                                                           │
[ Intelligent Scale & Key Harmony Matrix ] (Optional Diatonic Mode)             │
   │                                                                           │
   ▼                                                                           │
[ Stereo Panning & Detune Spread ] ──► [ Wet Level ] ──────────────────────────┴──► Master Output
```

---

## 3. Parameter Specifications

| Parameter | Range | Default | Unit | Description |
| :--- | :--- | :--- | :--- | :--- |
| `SHIFT_INTERVAL` | `-24` to `+24`| `+12` | st | Fixed pitch transposition in semitones (-12 = sub octave; +12 = upper octave). |
| `FINE_TUNE` | `-50` to `+50`| `0` | cents | Fine micro-pitch detuning for chorus-like thickness. |
| `POLY_MODE` | `STANDARD` / `PRECISE` | `PRECISE` | mode | Processing precision: Standard (lowest latency, 5 ms) vs. Precise (highest fidelity, 7 ms). |
| `TRANSIENT_TAMER`| `0` - `100` | `75` | % | Transient preservation strength to avoid pick smear during chord strumming. |
| `SCALE_HARMONY` | `OFF` / `DIATONIC` | `OFF` | mode | Diatonic scale tracking based on selected Key (Maj, Min, Dorian, Mixolydian). |
| `KEY_ROOT` | `C` to `B` | `A` | note | Musical root note for intelligent scale harmonization. |
| `SCALE_TYPE` | `MAJOR` / `MINOR` | `MAJOR`| scale | Scale formula used for diatonic voice calculations. |
| `STEREO_SPREAD` | `0` - `100` | `50` | % | Pans transposed voices across the stereo spectrum (+12 left, -12 right). |
| `MIX_WET_DRY` | `0` - `100` | `50` | % | Parallel balance between original dry chord and transposed harmony voices. |

---

## 4. Factory Scene Presets

### Scene A: Polyphonic Drop Tuning (-2 & -5 Semitones)
- **Concept:** Instant digital down-tuning for metal and hard rock without changing guitar gauge or retuning physical pegs.
- **Pitch Shift:** `SHIFT_INTERVAL = -2 st` (D Standard) / `SHIFT_INTERVAL = -5 st` (B Standard).
- **Processing:** `POLY_MODE = PRECISE`, `TRANSIENT_TAMER = 85%`, `SCALE_HARMONY = OFF`.
- **Mix:** `MIX_WET_DRY = 100%` (100% wet replaced signal; dry completely muted).

### Scene B: 12-String & Organ Octave Swell (+12 st & -12 st)
- **Concept:** Transforms a standard 6-string electric or acoustic into a rich, chiming 12-string guitar or lush Hammond organ texture.
- **Pitch Shift:** Dual Voice (`Voice 1 = +12 st`, `Voice 2 = -12 st`), `FINE_TUNE = +6 cents`.
- **Processing:** `POLY_MODE = PRECISE`, `TRANSIENT_TAMER = 70%`, `STEREO_SPREAD = 85%`.
- **Mix:** `MIX_WET_DRY = 45%` (Dry chord anchored in center with wide octaves).

### Scene C: Intelligent Diatonic Chord Harmony (Dual Lead Guitars)
- **Concept:** Automatically harmonizes chords and single-note lines with musically correct thirds and sixths in the chosen key (Boston, Thin Lizzy, Iron Maiden style).
- **Pitch Shift:** `SCALE_HARMONY = DIATONIC`, `KEY_ROOT = E`, `SCALE_TYPE = MINOR`, `SHIFT_INTERVAL = +3rd / +4th Diatonic`.
- **Processing:** `POLY_MODE = PRECISE`, `TRANSIENT_TAMER = 80%`.
- **Mix:** `MIX_WET_DRY = 50%`.

### Scene D: Whammy Style Polyphonic Glissando (Expression Pedal Pitch Sweep)
- **Concept:** Continuous polyphonic pitch bending across whole chords up to +2 octaves or down to 2 octaves drop (Dive Bomb) via expression pedal.
- **Pitch Shift:** `SHIFT_INTERVAL` mapped to Expression Pedal 1 (`0 st` at heel down to `+24 st` at toe down).
- **Processing:** `POLY_MODE = STANDARD` (ultra-low 4.8 ms latency for instant foot responsiveness).
- **Mix:** `MIX_WET_DRY = 100%` (solo whammy) or `50%` (harmonic harmony sweep).

---

## 5. Hardware Setup & Performance Controls

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (Poly Drop Tuning -2 st / -5 st).
- **Footswitch B:** Scene B (12-String & Organ Swell).
- **Footswitch C:** Scene C (Intelligent Diatonic Harmony) / Scene D.
- **Knob 1 (MOD FX):** Semitone Interval Shift (`-12` to `+12`).
- **Knob 2 (TONE):** High-frequency damping on transposed pitch voices.
- **Knob 3 (BLEND):** Wet / Dry Mix balance.

### Tank-B Control Assignments
- **Sub-Octave Tracking:** Dedicated `-12 st` and `-24 st` sub-bass generation with instantaneous chord tracking for 4-string and 5-string bassists.

### Black Box Desktop Configuration
- **Expression Pedal 1:** Continuous polyphonic pitch sweep (Whammy pedal mode).
- **Expression Pedal 2:** Smooth Wet/Dry parallel crossfader.
- **MIDI CC #65:** Instantaneous Key change selector for live diatonic modulation.
