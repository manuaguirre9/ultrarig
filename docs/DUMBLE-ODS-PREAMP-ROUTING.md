# Dumble Overdrive Special (ODS) Preamp Routing & Modeling Guide

This guide details the circuit architecture, cascading gain stages, tone-shaping switches, and preset design for emulating the legendary **Dumble Overdrive Special (ODS)** tube amplifier within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Circuit Architecture of the Dumble Overdrive Special

The Dumble Overdrive Special (ODS)—custom-built by Alexander "Howard" Dumble—is universally regarded as the holy grail of boutique tube amplifiers. Unlike typical high-gain amps that rely on harsh clipping diodes or extreme multi-stage preamplification, the ODS relies on a meticulously calibrated **cascading triode architecture**.

```
Instrument In
   │
   ▼
[ Bright & Deep Filter Network ]
   │
   ▼
[ V1A Clean Triode Stage ] (High-Headroom 12AX7)
   │
   ▼
[ Passive Tonestack (Bass / Mid / Treble) & Rock/Jazz Switch ] ◄───► [ PAB (Preamp Boost) Bypass ]
   │
   ▼
[ Clean Channel Master / Send ]
   │
   ├── (Clean Mode Direct) ────────────────────────────────────────────────────────┐
   │                                                                               │
   ▼                                                                               │
[ Overdrive Input Trimmer ]                                                        │
   │                                                                               │
   ▼                                                                               │
[ V2A & V2B Overdrive Triode Cascade ] (Soft Grid Conduction & Plate Saturation)    │
   │                                                                               │
   ▼                                                                               │
[ Overdrive Output Level & Ratio ] ────────────────────────────────────────────────┴──► Sum to Power Amp
```

### 1.1 Cascading Overdrive Stage

The signature feature of the ODS is that its **Overdrive channel does not replace the Clean channel; it cascades off it**:
1. The guitar signal first flows through the Clean preamp stage (V1) and tone stack.
2. When the Overdrive channel is engaged, this already-sculpted signal is fed directly into an additional dual-triode tube circuit (V2A and V2B).
3. Because the overdrive stage receives a pre-shaped, tone-filtered signal, the distortion is exceptionally smooth, vocal, and free from the fizzy raspy highs typical of standard master-volume amplifiers.

### 1.2 Essential Tone-Shaping Switches

- **Rock / Jazz Switch:**
  - **Rock Mode:** Introduces an aggressive midrange contour and higher gain structure, tailored for biting blues, funk, and rock solos.
  - **Jazz Mode:** Flattens the midrange frequency response and increases headroom, producing an open, hi-fi, acoustic-like clean tone.
- **Preamp Boost (PAB):** Disconnects the tone stack resistors and capacitors from ground, lifting the passive EQ insertion loss (~12 dB to 14 dB). This sends a massive, full-frequency midrange punch directly into the overdrive cascade for singing lead sustain.
- **Bright Switch:** Places a 120 pF capacitor across the clean volume potentiometer, adding sparkling glass harmonics that diminish as volume increases.
- **Deep Switch:** Shifts the bottom-end corner frequency downward, adding foundational cabinet resonance.

---

## 2. DSP Signal Chain & Topology

```
Guitar In (Single-Coils / Humbuckers)
   │
   ▼
[ Input Voicing: Bright / Deep Switches ]
   │
   ▼
[ V1A Clean Tube Stage Emulation ]
   │
   ▼
[ 3-Band Passive Tonestack + Rock/Jazz Contour ]
   │
   ▼
[ PAB Preamp Boost Latch ]
   │
   ▼
[ V2 Overdrive Cascade (Drive / Ratio / Edge Trim) ]
   │
   ▼
[ Power Amp Sag & Negative Feedback (6L6 / 6V6 Push-Pull) ]
   │
   ▼
[ Dual IR Convolution: Celestion G12-65 / Electro-Voice EVM-12L ]
   │
   ▼
[ Stereo Ambient Tape Delay & Studio Room Reverb ] ──► Stereo Output
```

---

## 3. Parameter Specifications

| Parameter | Range | Default | Unit | Description |
| :--- | :--- | :--- | :--- | :--- |
| `PREAMP_MODE` | `CLEAN` / `OD` | `OD` | mode | Toggles between Clean preamp and Cascaded Overdrive channel. |
| `TONE_VOICING` | `ROCK` / `JAZZ` | `ROCK` | mode | Rock: punchy mid focus; Jazz: flat hi-fi transparent headroom. |
| `PAB_BOOST` | `OFF` / `ON` | `ON` | bool | Preamp Boost: lifts tone stack for thick mid push and infinite sustain. |
| `BRIGHT_SW` | `OFF` / `ON` | `ON` | bool | High-frequency shelf bypass for chime and glassy string attack. |
| `DEEP_SW` | `OFF` / `ON` | `OFF` | bool | Extends low-end resonance for 1x12 open-back cabinet fullness. |
| `CLEAN_GAIN` | `0` - `100` | `45` | % | Input gain feeding V1 stage; controls edge-of-breakup clean tone. |
| `OD_DRIVE` | `0` - `100` | `65` | % | Cascaded overdrive gain feeding V2 tube stage. |
| `OD_RATIO` | `0` - `100` | `55` | % | Output level balance of overdrive stage relative to clean channel. |
| `TREBLE` | `0` - `100` | `58` | % | Passive treble tone stack control. |
| `MIDDLE` | `0` - `100` | `62` | % | Passive middle tone stack control (critical for vocal lead tone). |
| `BASS` | `0` - `100` | `42` | % | Passive bass tone stack control (kept tight to prevent muddy overdrive). |
| `POWER_SAG` | `0` - `100` | `35` | % | Emulation of power supply voltage droop under heavy transients. |

---

## 4. Factory Scene Presets

### Scene A: Smooth Jazz Clean (Carlton / Ford Voice)
- **Concept:** Pristine, bell-like clean with touch responsiveness and extended acoustic dynamic range.
- **Voicing:** `PREAMP_MODE = CLEAN`, `TONE_VOICING = JAZZ`, `BRIGHT_SW = ON`, `DEEP_SW = ON`, `PAB_BOOST = OFF`.
- **Gain & EQ:** `CLEAN_GAIN = 38%`, `BASS = 50%`, `MIDDLE = 55%`, `TREBLE = 60%`.
- **Speaker IR:** Electro-Voice EVM-12L (transparent, neutral, non-coloring speaker).
- **Space:** Warm Plate Reverb (`1.8 s`, `18%` mix).

### Scene B: Texas Blues Edge-of-Breakup (Stevie Ray / Mayer Tone)
- **Concept:** Dynamic semi-clean that remains crystal-clean when played softly and produces rich harmonic bloom when digging in.
- **Voicing:** `PREAMP_MODE = CLEAN`, `TONE_VOICING = ROCK`, `BRIGHT_SW = ON`, `DEEP_SW = OFF`, `PAB_BOOST = OFF`.
- **Gain & EQ:** `CLEAN_GAIN = 62%`, `BASS = 42%`, `MIDDLE = 65%`, `TREBLE = 64%`.
- **Power Amp:** 6L6 push-pull with `POWER_SAG = 45%`.
- **Space:** Spring Reverb (`2.2 s`, `22%` mix).

### Scene C: Singing ODS Lead (Robben Ford / Larry Carlton)
- **Concept:** The quintessential Dumble lead sound: horn-like vocal midrange, velvety top-end roll-off, and feedback-inducing sustain.
- **Voicing:** `PREAMP_MODE = OD`, `TONE_VOICING = ROCK`, `PAB_BOOST = ON` (vital mid punch), `BRIGHT_SW = OFF`.
- **Gain & EQ:** `CLEAN_GAIN = 50%`, `OD_DRIVE = 68%`, `OD_RATIO = 60%`, `BASS = 38%`, `MIDDLE = 75%`, `TREBLE = 52%`.
- **Speaker IR:** Celestion G12-65 (smooth cone breakup with soft high-end rolloff).
- **Space:** Warm Analog Tape Delay (`375 ms`, `28%` feedback, `25%` mix).

### Scene D: High-Gain Fusion Solo (Santana / Dumble #183)
- **Concept:** Ultra-saturated modern fusion tone with effortless legato sustain and rich harmonic overtones.
- **Voicing:** `PREAMP_MODE = OD`, `TONE_VOICING = ROCK`, `PAB_BOOST = ON`, `BRIGHT_SW = ON`.
- **Gain & EQ:** `CLEAN_GAIN = 60%`, `OD_DRIVE = 82%`, `OD_RATIO = 70%`, `BASS = 35%`, `MIDDLE = 80%`, `TREBLE = 55%`.
- **Space:** Stereo Modulated Delay (`dotted 8th`, `440 ms`) + Studio Hall Reverb.

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (Smooth Jazz Clean) / Scene B (Texas Blues Crunch).
- **Footswitch B:** Scene C (Singing ODS Lead).
- **Footswitch C:** PAB (Preamp Boost) Toggle / Scene D.
- **Knob 1 (GAIN):** Clean Gain (in Clean mode) / Cascaded OD Drive (in OD mode).
- **Knob 2 (TONE / EQ):** Midrange Focus and Rock/Jazz Voicing.
- **Knob 3 (REVERB):** Space Matrix / Ambient Delay Mix.

### Tank-B Control Assignments
- Excellent for bassists seeking classic James Jamerson or vintage Motown tube warmth using Clean mode with `TONE_VOICING = JAZZ`.

### Black Box Desktop Configuration
- **MIDI CC #80:** Seamless switching between Clean and Cascaded OD modes without audio drops.
- **MIDI CC #81:** Momentary PAB Boost for instantaneous solo emphasis.
- **IR Slots:** Run dual IR mixing combining Celestion G12-65 (for warmth) with Electro-Voice EVM-12L (for low-end punch).
