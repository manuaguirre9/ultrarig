# Analog BBD Chorus & Dimension Spatializer Modeling Guide

This guide details the circuit architecture, clock-driven delay line physics, non-linear companding, and practical preset design for emulating **Analog Bucket Brigade Device (BBD) Chorus** and the **Dimension Spatializer** (Boss CE-1 and Roland Dimension D SDD-320) within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Principles & Circuitry of Analog BBD Chorus

Before digital DSP delays, analog chorus and flanging relied on charge-coupled **Bucket Brigade Device (BBD)** integrated circuits (such as the Panasonic MN3002, MN3007, and MN3207).

```
Audio In ──► [ Pre-Emphasis ] ──► [ 2:1 Compander Compressor ] ──► [ Anti-Aliasing LPF ] ──┐
                                                                                           │
                                                                                           ▼
[ LFO: Sine / Triangle ] ──► [ Clock Gen (50 kHz - 150 kHz) ] ──► [ BBD Analog Delay Line (MN3007) ]
                                                                                           │
                                                                                           ▼
Audio Out ◄── [ Stereo Matrix ] ◄── [ 1:2 Compander Expander ] ◄── [ Reconstruction LPF ] ─┘
```

### 1.1 The Anatomy of BBD Warmth and Character

1. **Capacitive Bucket-to-Bucket Losses:** As the analog voltage charge is transferred down a chain of 512 or 1024 capacitive storage stages, slight high-frequency loss and non-linear distortion accumulate, imparting a warm, velvety timbre.
2. **Anti-Aliasing & Reconstruction Filters:** Because the clock rates typically run between 40 kHz and 150 kHz, steep multi-pole analog low-pass filters (typically 7 kHz to 10 kHz) are required at both input and output to prevent clock bleed. This rolls off extreme top-end fizz, ensuring the chorus sits naturally behind the dry signal.
3. **NE570 / NE571 Compander Dynamics:** To overcome the inherent thermal noise of hundreds of MOS transistors, analog chorus units implement a 2:1 dynamic compressor before the delay line and a 1:2 expander after it. This introduces a subtle, musical "breathing" and soft-knee compression on pick transients.

### 1.2 The Dimension Architecture (Spatial Spread Without Wobble)

Traditional single-delay chorus pedals (like the CE-1 or Small Clone) modulate a single delay time with an LFO, causing a prominent pitch-bending "seasick" vibrato.

The **Dimension D (Roland SDD-320)** solves this with a sophisticated **dual anti-phase delay line topology**:
- **Delay Line 1** is modulated by LFO $\phi(t)$.
- **Delay Line 2** is modulated by inverted LFO $-\phi(t)$ ($180^\circ$ out of phase).
- When Delay 1 is cross-mixed into the Left channel and Delay 2 into the Right channel alongside inverted phase-inverted dry signals, the pitch variations cancel each other psychoacoustically in the center while creating an immense, static stereo image with **zero perceptible pitch wobble**.

---

## 2. DSP Signal Chain & Topology

```
Instrument In ───────────────────────► [ Direct Dry Level ] ───────────────────────────────────┐
      │                                                                                        │
      ▼                                                                                        │
[ Dynamic Pre-Compander (2:1 Soft Knee) ]                                                      │
      │                                                                                        │
      ▼                                                                                        │
[ Anti-Aliasing Analog LPF (8.5 kHz, 24 dB/oct) ]                                              │
      │                                                                                        │
      ├───► [ BBD Delay Line A ] ◄── [ Dual Anti-Phase LFO Engine ] ──► [ BBD Delay Line B ]   │
      │     (Clock Delay: 5-25 ms)                                     (Clock Delay: 5-25 ms)  │
      │           │                                                          │                 │
      │           ▼                                                          ▼                 │
      │     [ Reconstruction LPF ]                                     [ Reconstruction LPF ]  │
      │           │                                                          │                 │
      │           ▼                                                          ▼                 │
      │     [ De-Compander Expander ]                                  [ De-Compander Expander ]
      │           │                                                          │                 │
      └───────────┼───────────────────────────┬──────────────────────────────┘                 │
                  ▼                           ▼                                                │
          [ Channel Left Mix ]        [ Channel Right Mix ]                                    │
                  │                           │                                                │
                  ▼                           ▼                                                │
         [ Stereo Output L ]          [ Stereo Output R ] ◄────────────────────────────────────┘
```

---

## 3. Parameter Specifications

| Parameter | Range | Default | Unit | Description |
| :--- | :--- | :--- | :--- | :--- |
| `CHORUS_MODE` | `CE1_CHORUS` / `DIMENSION` / `VIBRATO` | `CE1_CHORUS` | mode | Algorithm topology: Vintage single-LFO vs. Dual Anti-Phase Dimension. |
| `RATE` | `0.1` - `12.0` | `0.85` | Hz | Speed of the low-frequency modulation oscillator. |
| `DEPTH` | `0` - `100` | `65` | % | Modulation width (excursion of delay time). |
| `BBD_STAGES` | `512` / `1024` | `1024` | stages| Number of simulated capacitive bucket stages (affects warmth and delay base). |
| `COMPANDER_DRIVE`| `0` - `100` | `40` | % | Non-linear dynamic compression and harmonic warmth in the delay path. |
| `DAMPING_FREQ` | `3.0` - `12.0` | `8.2` | kHz | Cutoff frequency of the simulated analog reconstruction filter. |
| `DIMENSION_PRESET`| `1` / `2` / `3` / `4` | `3` | mode | Dimension D push-button mode (Mode 4 = maximum stereo width). |
| `STEREO_SPREAD` | `0` - `100` | `100` | % | Phase offset and cross-feed panning between Left and Right outputs. |
| `MIX_WET_DRY` | `0` - `100` | `50` | % | Wet/Dry parallel blend (Set to 100% in Vibrato mode). |

---

## 4. Factory Scene Presets

### Scene A: Boss CE-1 Vintage Chorus (Warm & Organic)
- **Concept:** The authentic 1976 Boss CE-1 sound: lush, analog, slightly dark, and musically warm.
- **Topology:** `CHORUS_MODE = CE1_CHORUS`, `RATE = 0.75 Hz`, `DEPTH = 60%`.
- **Analog Profile:** `BBD_STAGES = 1024`, `DAMPING_FREQ = 7.8 kHz`, `COMPANDER_DRIVE = 45%`.
- **Mix:** `MIX_WET_DRY = 50%` (Classic 1:1 dry to wet analog ratio).

### Scene B: Roland Dimension D Spatializer (Mode 4 Stereo Spread)
- **Concept:** Massive, three-dimensional stereo enlargement without pitch seasickness or comb filtering.
- **Topology:** `CHORUS_MODE = DIMENSION`, `DIMENSION_PRESET = 4`, `STEREO_SPREAD = 100%`.
- **Modulation:** Dual anti-phase LFOs (`0.25 Hz` slow drift), `DEPTH = 40%`.
- **Mix:** `MIX_WET_DRY = 65%` (Cross-coupled stereo imaging).

### Scene C: CE-1 True Pitch Vibrato (Leslie / Rotary Warble)
- **Concept:** 100% wet frequency modulation simulating a spinning Leslie speaker horn or vintage Magnatone pitch vibrato.
- **Topology:** `CHORUS_MODE = VIBRATO`, `RATE = 5.4 Hz`, `DEPTH = 75%`.
- **Analog Profile:** `BBD_STAGES = 512`, `DAMPING_FREQ = 6.5 kHz`.
- **Mix:** `MIX_WET_DRY = 100%` (Dry completely eliminated for pure pitch modulation).

### Scene D: 80s Studio Clean Arpeggio (Police / The Cure Style)
- **Concept:** Shimmering, glassy chorus designed for sparkling single-coil Strat arpeggios and rhythmic funk chords.
- **Topology:** `CHORUS_MODE = DIMENSION`, `DIMENSION_PRESET = 3`, `RATE = 1.2 Hz`, `DEPTH = 55%`.
- **Analog Profile:** `DAMPING_FREQ = 10.5 kHz`, `COMPANDER_DRIVE = 25%`.
- **Space:** Light Stereo Tape Delay (`380 ms`, `20%` feedback) + Studio Plate Reverb.
- **Mix:** `MIX_WET_DRY = 50%`.

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (CE-1 Vintage Chorus) / Scene B (Dimension Spatializer).
- **Footswitch B:** Scene C (CE-1 Pitch Vibrato).
- **Footswitch C:** Scene D (80s Studio Clean) / Bypass.
- **Knob 1 (MOD FX):** Rate / Speed of modulation.
- **Knob 2 (TONE):** High-frequency reconstruction filter damping.
- **Knob 3 (BLEND):** Wet/Dry Mix balance.

### Tank-B Control Assignments
- In Dimension mode with low-end crossover enabled, bassists can add enormous stereo width to mid and high harmonics while keeping frequencies below 150 Hz completely mono and unmodulated to preserve low-end punch.

### Black Box Desktop Configuration
- **Stereo TRS / Dual XLR Outputs:** Essential for experiencing the full psychoacoustic cancellation and spatial enlargement of the Dimension algorithm.
- **MIDI CC #72:** Real-time LFO Rate modulation via expression pedal.
