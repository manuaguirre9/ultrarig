# Auto-Swell & Slow Gear Volume Envelope Modeling Guide

This guide details the algorithmic principles, transient flux re-triggering, logarithmic gain ramping, and preset design for **Auto-Swell & Reverse Dynamic Expansion** (inspired by the vintage **Boss SG-1 Slow Gear**) within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Principles of Dynamic Auto-Swell (Reverse Expansion)

Traditional volume swells—famously executed by Roy Buchanan, Jeff Beck, and David Gilmour—require rolling a guitar's volume knob or rocking a physical volume pedal simultaneously with every pick attack. An **Auto-Swell** automates this gesture through **inverted dynamic expansion**.

```
Instrument In ───────┬───────────────────────────────────────────────► [ Pre-Sustain Compressor ]
                     │                                                          │
                     ▼                                                          ▼
[ Transient Flux & Envelope Detector ] ──► [ Ramp Generator (ADSR) ] ───► [ VCA Gain Stage ] ──► Output
      (Triggers on Attack Spike)          (Rise Time: 50 - 1200 ms)      (-90 dB -> 0 dB)
```

### 1.1 Envelope Ramp Curves & Acoustic Perception

When a pick strike exceeds the trigger threshold, the VCA momentarily mutes the initial attack transient (dropping gain to $-90\text{ dB}$) and smoothly ramps back to $0\text{ dB}$ over a user-defined **Rise Time**:
- **Linear Ramp:** Gains linearly in voltage, which can feel too fast initially in logarithmic decibels.
- **Exponential / S-Curve Ramp:** Smoothly accelerates in amplitude, mirroring human auditory loudness curves and producing authentic bowed string (cello/violin) phrasing.

### 1.2 Intelligent Spectral Flux Re-Triggering

The primary flaw of vintage analog SG-1 pedals is **re-trigger lockup**: if a previous chord is still ringing out above the threshold, playing a new note fails to reset the swell envelope.
UltraRig resolves this using **High-Frequency Spectral Flux Detection**:
1. Even while low-frequency chord fundamentals are decaying slowly, a new pick attack produces an unmistakable spike in upper-mid spectral energy ($2\text{ kHz} - 6\text{ kHz}$).
2. The detector recognizes this rapid positive derivative ($dE/dt > \text{Sensitivity}$) and cleanly resets the swell ramp to $-90\text{ dB}$ via a $4\text{ ms}$ anti-click fade, allowing fluid chord changes and arpeggio phrasing.

### 1.3 Post-Swell Sustain Compensation

Long swell times ($>600\text{ ms}$) naturally consume a guitar string's peak energy before reaching full volume. Integrating a clean **Optical Sustain Booster** in the signal path maintains string energy during the ramp-up, ensuring notes bloom into full, resonant pads instead of fading prematurely.

---

## 2. DSP Signal Chain & Processing Topology

```
Guitar / Bass In
   │
   ├───► [ Spectral Flux Trigger & Hysteresis Detector ]
   │           │ (Sensitivity, Re-trigger Threshold, Anti-Click Ramp Reset)
   │           ▼
   │     [ Swell Envelope Generator (Log / Exp / S-Curve, 50-1200 ms) ]
   │           │
   ▼           ▼
[ Clean Sustainer & Optical Comp ] ──► [ VCA Swell Attenuator ]
                                             │
                                             ▼
[ Optional Pre-Delay Tube Warmth / Overdrive ]
                                             │
                                             ▼
[ Stereo Modulation (Dimension Chorus) + Shimmer / Tape Delay ] ──► Stereo Output
```

---

## 3. Parameter Specifications

| Parameter | Range | Default | Unit | Description |
| :--- | :--- | :--- | :--- | :--- |
| `SENSITIVITY` | `0` - `100` | `65` | % | Input threshold required for pick attacks to reset and trigger a swell. |
| `RISE_TIME` | `40` - `1500` | `350` | ms | Time required for the VCA to fade from silence up to full 0 dB level. |
| `RAMP_CURVE` | `LIN` / `EXP` / `S_CURVE`| `S_CURVE` | mode | Shape of volume swell curve (S-Curve delivers natural bowed phrasing). |
| `RETRIGGER_MODE`| `STANDARD` / `FLUX_POLY` | `FLUX_POLY` | mode | Spectral Flux mode detects new pick attacks over ringing chord tails. |
| `SUSTAIN_BOOST` | `0` - `100` | `45` | % | Optical sustain compensation keeping long swells blooming cleanly. |
| `HOLD_DECAY` | `0` - `100` | `30` | % | Smooth release hold preventing abrupt choking on staccato notes. |
| `MIX_WET_DRY` | `0` - `100` | `100` | % | Typically 100% wet to completely erase mechanical pick attacks. |

---

## 4. Factory Scene Presets

### Scene A: Bowed Cello Solo Lead (Smooth Violin Swell)
- **Concept:** Expressive melodic phrasing mimicking a bowed orchestral cello or violin without using a volume pedal.
- **Swell Settings:** `RISE_TIME = 260 ms`, `RAMP_CURVE = S_CURVE`, `SENSITIVITY = 70%`, `RETRIGGER_MODE = FLUX_POLY`.
- **Tone & Sustainer:** `SUSTAIN_BOOST = 55%`, gentle tube overdrive warmth (`25%` drive).
- **Space:** Warm Studio Plate Reverb (`2.2 s`, `28%` mix).

### Scene B: Ambient Swell Blooming Cloud (Post-Rock & Worship Pad)
- **Concept:** Slow, colossal ambient synth-like pads created effortlessly from standard strummed chords.
- **Swell Settings:** `RISE_TIME = 780 ms`, `RAMP_CURVE = EXP`, `SENSITIVITY = 60%`, `SUSTAIN_BOOST = 70%`.
- **Space:** Modulated Stereo Tape Delay (`480 ms`, `42%` feedback) into Cathedral Shimmer Reverb (`6.5 s` decay).
- **Mix:** `MIX_WET_DRY = 100%`.

### Scene C: Reverse-Like Volume Ramp (60s Psychedelic Swell)
- **Concept:** Fast rhythmic swells emulating the backwards-tape guitar solos of classic 1960s psychedelic rock.
- **Swell Settings:** `RISE_TIME = 180 ms`, `RAMP_CURVE = EXP`, `SENSITIVITY = 75%`.
- **Tone:** Bright vintage fuzz edge rolled back slightly at the guitar volume pot.
- **Space:** Slapback Tape Echo (`140 ms`) + Vintage Spring Reverb.

### Scene D: Polyphonic Synth Organ Swell (Chordal Pad)
- **Concept:** Transforms triads and 7th chords into lush, breathing pipe-organ and analog pad voicings.
- **Swell Settings:** `RISE_TIME = 450 ms`, `RAMP_CURVE = S_CURVE`, `RETRIGGER_MODE = FLUX_POLY`.
- **Modulation:** Dual-Octave Polyphonic Shifter (`+12 st` / `-12 st` blended at `35%`) + Dimension D Stereo Chorus.
- **Space:** Wide Hall Reverb (`4.0 s` decay).

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (Bowed Cello Lead) / Scene B (Ambient Swell Cloud).
- **Footswitch B:** Scene C (Psychedelic Reverse Swell).
- **Footswitch C:** Scene D (Polyphonic Organ Pad) / Auto-Swell Bypass.
- **Knob 1 (COMP / SENS):** Trigger Sensitivity calibration for different pickups (Single-Coils vs. Humbuckers).
- **Knob 2 (MOD FX):** Rise Time (`100 ms` to `1200 ms`).
- **Knob 3 (REVERB / DELAY):** Ambient Space Mix.

### Tank-B Control Assignments
- Bassists can craft cinematic upright-bowed (*arco*) pads and fretless-style synth bass swells by pairing Scene A (`RISE_TIME = 300 ms`) with mild analog chorus and hall reverb.

### Black Box Desktop Configuration
- **Expression Pedal 1:** Real-time continuous adjustment of `RISE_TIME` during live performances (from quick 150 ms stabs to slow 1.2 s ambient washes).
- **MIDI CC #64:** Momentary hold sustain trigger to lock notes before swelling into reverbs.
