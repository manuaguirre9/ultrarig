# Soldano Super Lead Overdrive (SLO-100) Preamp & High-Gain Routing Guide

This guide details the circuit architecture, cascading high-gain triode stages, interstage de-fuzzing filters, and practical preset design for emulating the legendary **Soldano Super Lead Overdrive (SLO-100)** within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Circuit Architecture of the Soldano SLO-100

Introduced in 1987 by Mike Soldano, the Super Lead Overdrive (SLO-100) fundamentally redefined high-gain electric guitar amplification. Its cascading preamp topology served as the architectural benchmark for virtually all modern high-gain amplifiers that followed (including the 5150, Dual Rectifier, and modern boutique designs).

```
Instrument In
   │
   ▼
[ Input Voicing & Bright Switch ]
   │
   ├── (Normal Channel: Clean / Crunch) ───────────────────────────────────────────┐
   │                                                                               │
   ▼                                                                               │
[ V1A Stage ] ──► [ Interstage High-Pass Filter (Cuts flubby bass < 120 Hz) ]      │
   │                                                                               │
   ▼                                                                               │
[ V1B Stage ] ──► [ Gain / Distortion Cascade ]                                    │
   │                                                                               │
   ▼                                                                               │
[ V2A & V2B High-Gain Lead Stages ] (Cold Clipper & Progressive Tube Saturation)   │
   │                                                                               │
   ▼                                                                               │
[ Cathode Follower Driven Tonestack (Bass / Middle / Treble) ] ◄───────────────────┘
   │
   ▼
[ Effects Loop Send / Return ]
   │
   ▼
[ 5881 / 6L6 Power Section with Presence & Depth Negative Feedback ]
   │
   ▼
[ 4x12 Speaker Cabinet IR Convolution (Celestion Vintage 30) ] ──► Master Output
```

### 1.1 The High-Gain Cascade & Interstage "De-Fuzzing"

The major engineering breakthrough of the SLO-100 was solving the "muddy low-end" dilemma inherent in high-gain tube circuits:
1. **Pre-Distortion Bass Rolloff:** When high-gain stages clip low frequencies, they create "blocking distortion" and flubby, mushy bass. The SLO-100 implements steep high-pass coupling capacitors between early triodes, stripping away frequencies below 120 Hz *before* heavy saturation occurs.
2. **Post-Distortion Tonestack:** Once the signal is saturated with rich, focused harmonics, the full low end is reintroduced at the tone stack and power amplifier's **Depth (Resonance)** control. This yields the SLO-100's iconic tight, percussive palm-muted chug combined with rich, singing lead sustain.
3. **Cold Clipper Stage:** One of the intermediate 12AX7 triodes is biased unusually cold (39k cathode resistor), creating asymmetric waveform clipping that mimics power tube saturation at the preamp stage while generating rich even-order harmonics.

### 1.2 Channel Voicings

- **Normal Channel (Clean Mode):** Pristine, dynamic clean tone with high headroom and bell-like chime (famously used by Eric Clapton on the *Journeyman* album).
- **Normal Channel (Crunch Mode):** Roaring vintage British plexi-style overdrive with immediate touch sensitivity for classic rock and blues (favored by Warren Haynes).
- **Overdrive / Lead Channel:** Massive, smooth liquid high-gain distortion with incredible note separation in complex chords and effortless singing sustain on solo lines.

---

## 2. DSP Signal Chain & Processing Topology

```
Guitar In (Humbuckers / Single-Coils)
   │
   ▼
[ Input Noise Gate / Downward Expander ] (Silences high-gain idle hiss)
   │
   ▼
[ Preamp Mode: Clean / Crunch / Overdrive Lead ]
   │
   ▼
[ 4-Stage Cascading Triode Emulation & Asymmetric Cold-Clipper ]
   │
   ▼
[ 3-Band Passive Tonestack (Bass / Mid / Treble) ]
   │
   ▼
[ Power Amp Emulation (4x 5881/6L6 Push-Pull + Presence & Depth Controls) ]
   │
   ▼
[ Dual IR Cabinet Convolution: Soldano 4x12 (Celestion V30 + EVM-12L) ]
   │
   ▼
[ Stereo FX Loop: Studio Modulated Delay & Plate Reverb ] ──► Stereo Output
```

---

## 3. Parameter Specifications

| Parameter | Range | Default | Unit | Description |
| :--- | :--- | :--- | :--- | :--- |
| `CHANNEL_MODE`| `CLEAN` / `CRUNCH` / `LEAD` | `LEAD` | mode | Selects the active preamp channel voicing and gain structure. |
| `PREAMP_GAIN` | `0` - `100` | `68` | % | Input gain feeding cascading 12AX7 triodes. |
| `BASS` | `0` - `100` | `48` | % | Tone stack low-frequency shelf (post-distortion). |
| `MIDDLE` | `0` - `100` | `62` | % | Tone stack midrange control (critical for solo cut and punch). |
| `TREBLE` | `0` - `100` | `55` | % | Tone stack high-frequency control. |
| `DEPTH` | `0` - `100` | `60` | % | Negative feedback low-end resonance in the 5881 power section. |
| `PRESENCE` | `0` - `100` | `58` | % | High-frequency bite and cut in the power amplifier feedback loop. |
| `BRIGHT_SW` | `OFF` / `ON` | `OFF` | bool | Treble boost on Normal channel at low gain settings. |
| `NOISE_GATE` | `0` - `100` | `45` | % | Fast downward expander threshold for tight staccato riffs. |
| `CAB_IR` | `IR_SLOT_1` / `IR_SLOT_2` | `V30_412` | file | 4x12 cabinet impulse response profile. |

---

## 4. Factory Scene Presets

### Scene A: SLO Clean Chime (Clapton Journeyman Voice)
- **Concept:** Sparkling, dynamic tube clean with high-headroom snap and touch-sensitive clarity.
- **Voicing:** `CHANNEL_MODE = CLEAN`, `BRIGHT_SW = ON`, `PREAMP_GAIN = 35%`.
- **EQ & Power:** `BASS = 52%`, `MIDDLE = 50%`, `TREBLE = 65%`, `DEPTH = 40%`, `PRESENCE = 55%`.
- **Cabinet IR:** 4x12 open/semi-open EVM-12L.
- **Space:** Warm Studio Room Reverb (`1.4 s`, `18%` mix).

### Scene B: Warren Haynes Blues Crunch (Gov't Mule / Southern Rock)
- **Concept:** Punchy, organic edge-of-breakup and medium-gain crunch with vocal midrange growl.
- **Voicing:** `CHANNEL_MODE = CRUNCH`, `BRIGHT_SW = OFF`, `PREAMP_GAIN = 58%`.
- **EQ & Power:** `BASS = 45%`, `MIDDLE = 70%`, `TREBLE = 52%`, `DEPTH = 55%`, `PRESENCE = 50%`.
- **Cabinet IR:** Soldano 4x12 with Celestion Vintage 30.
- **Space:** Spring Reverb (`1.8 s`, `20%` mix).

### Scene C: Modern High-Gain Rhythm (Tight Palm-Muted Chug)
- **Concept:** Crushing, percussive modern rhythm guitar with laser-focused bass response and aggressive upper-mid bite.
- **Voicing:** `CHANNEL_MODE = LEAD`, `PREAMP_GAIN = 72%`, `NOISE_GATE = 55%`.
- **EQ & Power:** `BASS = 46%`, `MIDDLE = 60%`, `TREBLE = 58%`, `DEPTH = 70%`, `PRESENCE = 65%`.
- **Cabinet IR:** Dual V30 / G12-T75 4x12 impulse response.
- **Space:** Dry / Direct with fast room slapback.

### Scene D: Infinite Liquid Lead (Steve Lukather / Gary Moore)
- **Concept:** The legendary singing Soldano lead tone: endless sustain, velvety top-end compression, and harmonic overtones.
- **Voicing:** `CHANNEL_MODE = LEAD`, `PREAMP_GAIN = 85%`, `NOISE_GATE = 35%`.
- **EQ & Power:** `BASS = 42%`, `MIDDLE = 78%`, `TREBLE = 50%`, `DEPTH = 50%`, `PRESENCE = 52%`.
- **Space:** Stereo Modulated Tape Delay (`420 ms`, `28%` feedback) + Studio Plate Reverb (`2.4 s`).

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (SLO Clean Chime) / Scene B (Warren Haynes Crunch).
- **Footswitch B:** Scene C (Modern High-Gain Rhythm).
- **Footswitch C:** Scene D (Infinite Liquid Lead) / Solo Boost (+3 dB).
- **Knob 1 (GAIN):** Preamp Gain / Overdrive Saturation.
- **Knob 2 (TONE):** Midrange Focus and Presence cut.
- **Knob 3 (REVERB / DELAY):** Ambient FX Loop balance.

### Tank-B Control Assignments
- Use the Normal Crunch channel with `PREAMP_GAIN = 40%` and `BASS = 65%` for aggressive modern rock and metal bass distortion that retains massive low-end authority without flubbing.

### Black Box Desktop Configuration
- **Stereo Cabinet Routing:** Load Celestion Vintage 30 on Left output and Electro-Voice EVM-12L on Right output for huge wall-of-sound live tone.
- **MIDI CC #85:** Instant channel switching between Clean, Crunch, and Lead without audio latency.
