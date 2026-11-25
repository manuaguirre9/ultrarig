# Monophonic Analog Bass Synth (Moog Ladder & Oscillator) Modeling Guide

This guide details the pitch-tracking architecture, anti-aliased VCO waveform generation, 4-pole resonant **Moog Ladder Filter** modeling, and practical preset design for **Monophonic Analog Bass Synthesis** within UltraRig for M-VAVE hardware (Tank-B, Tank-G v1/v2, and Black Box).

---

## 1. Principles & DSP Architecture of Guitar/Bass-to-Synth Tracking

Synthesizing rich analog bass tones from an electric bass or guitar requires locking onto the incoming pitch without octave jumping, harmonic glitching, or excessive tracking latency. Because low $E_1$ ($41.2\text{ Hz}$) has a waveform period of $24.27\text{ ms}$, conventional frequency-domain FFT pitch trackers suffer sluggish tracking.

```
Bass / Guitar In
   │
   ├───► [ Tracking Pre-Filter (LPF @ 160 Hz) ] ──► [ Hybrid YIN / Zero-Crossing Pitch Tracker ]
   │                                                               │ (Frequency f0 & Gate)
   ├───► [ Amplitude Envelope Follower ]                           ▼
   │           │                                   [ PolyBLEP VCO1 (Saw) + VCO2 (PWM Pulse) ]
   │           │                                   [ Sub-Octave Flip-Flop Divider (-12 st) ]
   │           │                                                   │
   │           ▼                                                   ▼
   │     [ VCF Envelope Contour ] ────────────────► [ 4-Pole 24 dB/oct Moog Ladder Filter ]
   │                                                (With Non-Linear tanh Saturation & Bass Comp)
   │                                                               │
   └───► [ Clean Direct Blend ] ───────────────────────────────────┴──► Master Output
```

### 1.1 Low-Latency Pitch & Fundamental Extraction

1. **Tracking Pre-Filter:** Real bass strings contain strong 2nd and 3rd harmonics that often exceed the fundamental in amplitude—causing false "octave-up" pitch jumps. UltraRig feeds the tracker through a steep 4th-order low-pass filter at $160\text{ Hz}$, isolating the pure fundamental waveform.
2. **Wave-Cycle Zero-Crossing + YIN Lock:** Estimates pitch period $T_0$ within the first cycle and validates harmonic consistency, delivering responsive synth tracking without chordal "flutter" when playing single-note grooves.
3. **Dynamic Tracking Gate:** Automatically mutes the internal oscillators below $-45\text{ dBFS}$ so string handling noise and dampened fret muting never trigger spurious glitch notes.

### 1.2 Anti-Aliased PolyBLEP Oscillators & Moog Ladder Filter

- **Sawtooth & PWM Square VCOs:** Generated mathematically using **PolyBLEP (Polynomial Band-Limited Step)** correction to eliminate harsh high-frequency digital aliasing distortion. Dual oscillators can be slightly detuned ($\pm 8\text{ cents}$) or modulated via PWM (Pulse Width Modulation) for lush analog movement.
- **24 dB/oct Transistor Ladder Filter:** Models four cascaded non-linear one-pole low-pass stages using $\tanh(x)$ hyperbolic tangent soft-clipping. Unlike thin digital IIR filters that lose all sub-bass power when Resonance is turned up, UltraRig injects low-end feedback compensation so high-Q resonant sweeps maintain earth-shaking low-end chest punch.

---

## 2. DSP Signal Chain & Processing Topology

```
Instrument Input (4/5-String Bass or Electric Guitar)
   │
   ├───► [ Clean Direct Path (Optional Low-End Retention) ] ───────────────────────┐
   │                                                                               │
   ▼                                                                               │
[ Pitch & Envelope Extraction Engine ]                                             │
   │ (Tracks f0, Velocity Attack, Gate Threshold)                                  │
   ▼                                                                               │
[ Dual Anti-Aliased Oscillators: Sawtooth + PWM Pulse + -12 st Sub-Octave ]        │
   │                                                                               │
   ▼                                                                               │
[ 4-Pole 24 dB/oct Resonant Moog Ladder VCF ] ◄── [ Envelope Follower / ADSR Mod ] │
   │                                                                               │
   ▼                                                                               │
[ Ladder Overdrive / Analog Saturation Stage ]                                     │
   │                                                                               │
   ▼                                                                               │
[ Stereo High-Frequency Chorus (> 150 Hz Mono-Safe Crossover) ] ───────────────────┴──► Output
```

---

## 3. Parameter Specifications

| Parameter | Range | Default | Unit | Description |
| :--- | :--- | :--- | :--- | :--- |
| `OSC_WAVE` | `SAW` / `PULSE` / `DUAL_MIX` | `DUAL_MIX` | mode | Oscillator shape: Saw (brassy, rich), Pulse (hollow), or Dual Blend. |
| `PWM_MOD` | `0` - `100` | `35` | % | Pulse-width LFO modulation depth for thick dual-oscillator animation. |
| `SUB_OCT_MIX` | `0` - `100` | `50` | % | Level of phase-locked $-12\text{ st}$ sub-octave square wave divider. |
| `FILTER_CUTOFF` | `40` - `4500` | `320` | Hz | Base cutoff frequency of the 4-pole 24 dB/oct Moog ladder VCF. |
| `RESONANCE` | `0` - `95` | `55` | % | Filter Q emphasis / squelch peak at the cutoff point. |
| `ENV_MOD_DEPTH` | `0` - `100` | `75` | % | Amount the player's picking attack sweeps the ladder cutoff upward. |
| `ENV_DECAY` | `50` - `1200` | `240` | ms | Speed at which the filter sweep closes after initial pluck. |
| `LADDER_DRIVE` | `0` - `100` | `40` | % | Non-linear $\tanh$ drive saturating the filter transistor core. |
| `TRACKING_GATE` | `-60` to `-20` | `-44` | dBFS | Gate floor preventing fret noise from triggering oscillators. |
| `MIX_WET_DRY` | `0` - `100` | `85` | % | Balance between clean instrument signal and synthesized waveforms. |

---

## 4. Factory Scene Presets

### Scene A: Moog Taurus Sub Pedal Bass (Rush / The Police Weight)
- **Concept:** Colossal, chest-rattling sustained bass pedals inspired by the legendary Moog Taurus I.
- **Oscillators:** `OSC_WAVE = SAW`, `DETUNE = +10/-10 cents`, `SUB_OCT_MIX = 75%` ($-12\text{ st}$ sub-fundamental).
- **VCF Filter:** `FILTER_CUTOFF = 180 Hz`, `RESONANCE = 25%`, `ENV_MOD_DEPTH = 40%`, `LADDER_DRIVE = 55%`.
- **Mix:** `MIX_WET_DRY = 90%` (10% clean string blend for tactile finger phrasing).

### Scene B: Funk Sawtooth Envelope Synth (Stevie Wonder / Herbie Hancock)
- **Concept:** Expressive, vocal "Superstition" / "Chameleon" clav-bass synth with elastic resonant filter squelch.
- **Oscillators:** `OSC_WAVE = DUAL_MIX` (75% Sawtooth + 25% Pulse), `SUB_OCT_MIX = 30%`.
- **VCF Filter:** `FILTER_CUTOFF = 240 Hz`, `RESONANCE = 72%`, `ENV_MOD_DEPTH = 90%`, `ENV_DECAY = 160 ms`.
- **Mix:** `MIX_WET_DRY = 100%`.

### Scene C: Woolly Mammoth Gated Fuzz Synth (Muse / Royal Blood)
- **Concept:** Aggressive, pinched square-wave synth fuzz with razor-sharp gated silence between riffs.
- **Oscillators:** `OSC_WAVE = PULSE` (Duty Cycle squeezed to 18%), `SUB_OCT_MIX = 80%`.
- **VCF Filter & Drive:** `LADDER_DRIVE = 85%`, `TRACKING_GATE = -32 dBFS` (instant gated silence).
- **Mix:** `MIX_WET_DRY = 80%`.

### Scene D: Electro-Square Lead & Sub Drop (Daft Punk / Synthwave)
- **Concept:** Futuristic 1980s arpeggio bass synth with stereo width above 150 Hz and punchy sub-bass anchor.
- **Oscillators:** `OSC_WAVE = DUAL_MIX`, `PWM_MOD = 65%`, `SUB_OCT_MIX = 45%`.
- **VCF Filter:** `FILTER_CUTOFF = 450 Hz`, `RESONANCE = 60%`, `ENV_DECAY = 120 ms`.
- **Space:** Dimension Stereo Chorus (> 150 Hz crossover) + Tight Studio Room Reverb.

---

## 5. Hardware Setup & Mapping

### Tank-B Control Assignments
- **Primary Bass Platform:** Designed natively for 4-string and 5-string bassists! Use neck pickup exclusively with tone rolled slightly back (~60%) to feed a clean, fundamental-heavy signal into the pitch tracker.
- **Footswitch 1:** Scene A (Moog Taurus Sub) / Scene B (Funk Sawtooth Synth).
- **Footswitch 2:** Scene C (Woolly Mammoth Gated Fuzz) / Synth Bypass.
- **Knob 1 (MOD / CUTOFF):** Real-time manual Filter Cutoff sweep.
- **Knob 2 (RESONANCE / DRIVE):** Ladder Q and Saturation grit.

### Tank-G (v1 / v2) Control Assignments
- Guitarists can transform standard 6-string guitars into thunderous octave-down synth bass lines by selecting Scene A or Scene C with `SUB_OCT_MIX = 85%` (instant keyboard-bass simulation without needing a bass guitar).

### Black Box Desktop Configuration
- **Expression Pedal 1:** Continuous control over `FILTER_CUTOFF` (functions like a classic Moog expression filter sweep across live synth bass grooves).
- **MIDI Clock Sync:** Locks LFO PWM modulation rate cleanly to live drummer click tracks.
