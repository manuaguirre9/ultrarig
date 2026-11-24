# Granular Synthesis, Reverse Cloud & Infinite Freeze Guide

This guide details the theoretical principles, algorithmic architecture, and practical preset configuration for real-time **Granular Micro-Acoustic Synthesis**, **Reverse Cloud Diffusion**, and **Infinite Buffer Freeze** within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Principles of Real-Time Granular Audio Processing

Granular synthesis deconstructs incoming continuous instrument audio into tiny micro-acoustic fragments called **grains** (typically ranging from 15 ms to 150 ms in duration). These grains are windowed, independently modulated in pitch, time, amplitude, and stereo panorama, and subsequently overlapped to generate complex textural soundscapes, ambient pads, micro-glitches, and atmospheric clouds.

```
Incoming Audio (Guitar / Bass / Synth)
   │
   ▼
[ Circular Ring Buffer ] (128 KB - 256 KB SDRAM / Internal SRAM)
   │
   ├── Grain Voice 1 ──► [ Hann Window ] ──► [ Reverse / Forward ] ──► [ Pitch Shift ] ──► [ Pan L ] ──┐
   ├── Grain Voice 2 ──► [ Hann Window ] ──► [ Reverse / Forward ] ──► [ Pitch Shift ] ──► [ Pan R ] ──┤
   ├── Grain Voice 3 ──► [ Hann Window ] ──► [ Reverse / Forward ] ──► [ Pitch Shift ] ──► [ Pan C ] ──┼──► Summing Bus & Cloud Reverb
   └── Grain Voice N ──► [ Hann Window ] ──► [ Reverse / Forward ] ──► [ Pitch Shift ] ──► [ Pan L/R] ─┘
```

### 1.1 Grain Architecture and Windowing

Without proper windowing, extracting slices of audio waveforms causes sharp step discontinuities at the grain boundaries, producing audible clicks and high-frequency digital artifacts. UltraRig implements a smooth **Hann (Raised Cosine)** or **Tukey window** envelope for every spawned grain:

$$w(n) = 0.5 \cdot \left(1 - \cos\left(\frac{2\pi n}{N - 1}\right)\right), \quad 0 \le n \le N-1$$

Where:
- $N$ is the grain length in samples ($N = \text{Grain Size (ms)} \times f_s / 1000$).
- $n$ represents the discrete sample index inside the active grain.

### 1.2 Reverse Grain Playback (*Reverse Cloud*)

In a traditional reverse delay, an entire musical phrase (500 ms to 2000 ms) is buffered and played backwards, introducing substantial rhythmic latency. In **Granular Reverse Mode**, reverse playback happens at the *micro-grain level* (30 ms to 100 ms):
- The macroscopic timeline moves forward in real time with zero perceptual latency.
- Individual grains read backwards from their local buffer pointer.
- This creates the distinctive shimmering, bowed, cello-like textures of reverse audio while maintaining immediate transient responsiveness to playing dynamics.

### 1.3 Pitch Scattering & Micro-Detuning

Each grain voice can be transposed independently using cubic Hermite interpolation:
- **Octave Up (+12 st):** Grains played at $2.0\times$ speed produce celestial, crystalline shimmer without dedicated feedback loops.
- **Octave Down (-12 st):** Grains played at $0.5\times$ speed yield deep, cavernous sub-harmonic drones.
- **Random Pitch Scatter ($\pm 15$ to $\pm 50$ cents):** Introduces organic chorusing, tape flutter, and orchestral detuning.

### 1.4 Infinite Buffer Freeze (*Freeze Latch*)

When the **Freeze** function is engaged (via hardware footswitch or MIDI CC):
1. **Buffer Write Pointer Halts:** Incoming instrument signal is disconnected from writing into the circular ring buffer, preventing old samples from being overwritten.
2. **Infinite Grain Re-circulation:** The granular engine continues to read, window, transpose, and scatter grains from the frozen audio slice indefinitely.
3. **Dry Signal Bypass / Solo:** The player's dry instrument signal can play dynamically over the stationary frozen pad without altering the background cloud.

---

## 2. DSP Topology & Signal Flow

```
Instrument In ───────────────────────► [ Dry Level ] ──────────────────────────────────────────┐
      │                                                                                        │
      ▼                                                                                        │
[ Input Soft-Limiter & HPF (60 Hz) ]                                                           │
      │                                                                                        │
      ├───► (Freeze Trigger Latch: Write Disable / Hold)                                       │
      ▼                                                                                        │
[ Circular Audio Buffer (250 ms) ]                                                             │
      │                                                                                        │
      ▼                                                                                        │
[ Multi-Voice Granular Engine ] (Grain Size: 20-120 ms | Density: 4-16x | Reverse % | Pitch)   │
      │                                                                                        │
      ▼                                                                                        │
[ Stereo Spatial Diffuser / Binaural Spread ]                                                 │
      │                                                                                        │
      ▼                                                                                        │
[ Multi-Tap Cloud Reverb & Space Matrix ]                                                      │
      │                                                                                        │
      ▼                                                                                        │
[ 3-Band Parametric Post-EQ ] ──► [ Wet Level ] ───────────────────────────────────────────────┴──► Output
```

---

## 3. Parameter Specifications

| Parameter | Range | Default | Unit | Description |
| :--- | :--- | :--- | :--- | :--- |
| `GRAIN_SIZE` | `15` - `200` | `45` | ms | Duration of individual audio slices. Short = metallic/glitch; Long = smooth pad. |
| `GRAIN_DENSITY` | `2` - `16` | `8` | voices | Number of concurrent overlapping grain streams in the synthesis cloud. |
| `GRAIN_REVERSE_PCT` | `0` - `100` | `40` | % | Probability of an individual grain playing in reverse. |
| `PITCH_SCATTER` | `0` - `100` | `25` | % | Amount of random pitch variation applied across consecutive grains. |
| `PITCH_SHIFT` | `-24` to `+24`| `0` | st | Fixed harmonic pitch transposition (+12 = octave up shimmer, -12 = sub drone). |
| `STEREO_SPREAD` | `0` - `100` | `85` | % | Binaural panning offset alternating across stereo left and right channels. |
| `BUFFER_FREEZE` | `OFF` / `ON` | `OFF` | bool | Freezes current circular audio buffer into an infinite sustained pad. |
| `CLOUD_DECAY` | `0.1` - `20.0`| `4.5` | s | Diffusion and decay time of the post-granular multi-tap cloud reverb. |
| `POST_DAMPING` | `1.0` - `16.0`| `6.5` | kHz | High-frequency damping filter to control harsh high-end grain accumulation. |
| `MIX_WET_DRY` | `0` - `100` | `50` | % | Parallel blend between raw direct instrument signal and granular cloud. |

---

## 4. Factory Scene Presets

### Scene A: Granular Stardust Cloud (Ambient Shimmer)
- **Concept:** Ethereal, floating ambient texture where guitar chords dissolve into an angelic, sparkling cloud of micro-particles.
- **Grain Settings:** `GRAIN_SIZE = 40 ms`, `GRAIN_DENSITY = 10`, `GRAIN_REVERSE_PCT = 35%`, `PITCH_SHIFT = +12 st`, `PITCH_SCATTER = 15%`.
- **Spatial:** `STEREO_SPREAD = 90%`, `CLOUD_DECAY = 6.0 s`, `POST_DAMPING = 7.5 kHz`.
- **Mix:** `MIX_WET_DRY = 45%` (Dry retains melodic clarity; wet blooms behind notes).

### Scene B: Reverse Shimmer Swell (Bowed Cello & Pad)
- **Concept:** 100% reverse grain texture that removes percussive pick attack and transforms plucked strings into sweeping orchestral pads.
- **Grain Settings:** `GRAIN_SIZE = 95 ms`, `GRAIN_DENSITY = 12`, `GRAIN_REVERSE_PCT = 100%`, `PITCH_SHIFT = 0 st`, `PITCH_SCATTER = 30%`.
- **Spatial:** `STEREO_SPREAD = 95%`, `CLOUD_DECAY = 8.5 s`, `POST_DAMPING = 5.2 kHz`.
- **Mix:** `MIX_WET_DRY = 70%` (Soft pick attack with lush swell response).

### Scene C: Infinite Frozen Ambient Pad (Hold Drone)
- **Concept:** Instant footswitch latching that captures any single chord or note and holds it indefinitely as an evolving synthesizer pad while allowing soloing over top.
- **Grain Settings:** `GRAIN_SIZE = 75 ms`, `GRAIN_DENSITY = 14`, `GRAIN_REVERSE_PCT = 50%`, `PITCH_SHIFT = 0 st`, `PITCH_SCATTER = 8%` (gentle chorus drift).
- **Freeze State:** `BUFFER_FREEZE = ON` (toggled via Footswitch B / MIDI CC #64).
- **Spatial:** `STEREO_SPREAD = 100%`, `CLOUD_DECAY = 15.0 s`, `POST_DAMPING = 6.0 kHz`.
- **Mix:** `MIX_WET_DRY = 50%` (50% frozen cloud / 50% live dry soloing).

### Scene D: Glitched Granular Delay Cascade (IDM / Micro-Loop)
- **Concept:** Rhythmic micro-slicing and random octave transpositions that turn single-note lines into complex polyrhythmic cascades.
- **Grain Settings:** `GRAIN_SIZE = 22 ms`, `GRAIN_DENSITY = 6`, `GRAIN_REVERSE_PCT = 60%`, `PITCH_SHIFT = -12 st / +12 st alternating`, `PITCH_SCATTER = 75%`.
- **Spatial:** `STEREO_SPREAD = 80%`, `CLOUD_DECAY = 1.8 s`, `POST_DAMPING = 9.0 kHz`.
- **Mix:** `MIX_WET_DRY = 55%`.

---

## 5. Hardware Mapping & Real-Time Performance Controls

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (Stardust Cloud) / Scene B (Reverse Swell).
- **Footswitch B (Hold / Tap):** Instant **Buffer Freeze** Latch (Engage hold pad).
- **Footswitch C:** Bypass / Glitched Cascade.
- **Knob 1 (REVERB):** Cloud Decay / Space Matrix Size.
- **Knob 2 (MOD FX):** Grain Density and Reverse Probability %.
- **Knob 3 (BLEND / MIX):** Wet / Dry Balance.

### Tank-B Control Assignments
- **Footswitch 1:** Sub-Drone Granular Cloud.
- **Footswitch 2 (Hold):** Low-Frequency Pad Freeze (sustains pedal-point bass notes).
- **Knob HPF / FREQ:** Low-Cut Filter (prevents sub-bass buildup in dense clouds).

### Black Box Desktop / MIDI Workflow
- **MIDI CC #64 (Sustain Pedal):** Momentary Buffer Freeze.
- **MIDI CC #1 (Modulation Wheel):** Continuous control over `GRAIN_SIZE` and `PITCH_SCATTER`.
- **Expression Pedal 1:** Continuous Wet/Dry blend from 0% (pure dry) to 100% (ambient drone).

---

## 6. CPU & Memory Optimization Strategies

1. **Circular Buffer Memory Footprint:**
   - At 48 kHz / 16-bit mono sampling, a 250 ms ring buffer requires only:
     $$250 \times 10^{-3} \times 48000 \times 2 = 24\,000 \text{ bytes } (\approx 23.4 \text{ KB})$$
   - Fits comfortably into internal L1/L2 SRAM on the MCU/DSP without external SDRAM bus contention.
2. **Fixed-Point Hermite Interpolation:**
   - Grain pitch shifting utilizes 16.16 fixed-point phase accumulators, avoiding floating-point division inside the high-frequency grain rendering loop.
3. **Dynamic Voice Allocation:**
   - In quiet passages or when instrument input drops below -60 dBFS, inactive grain voices enter low-power sleep mode, capping maximum CPU consumption at $\le 14\%$ of available DSP cycles.
