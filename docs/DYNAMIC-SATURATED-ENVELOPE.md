# Dynamic Saturated Envelope Filter Guide

This guide details the architectural principles, DSP implementation, and practical preset configuration for a **Dynamic Envelope Filter with Pre-Filter Harmonic Saturation** within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Principles of Pre-Filter Dynamic Envelope Filtering

Classic envelope-controlled filters (such as the Mu-Tron III, Electro-Harmonix Q-Tron, and vintage analog synth VCFs) sweep a resonant filter cutoff frequency in direct proportion to the player's picking attack and volume envelope.

```
Instrument In ───────────────────────► [ Pre-Filter Saturation ] ──► [ Resonant Filter (SVF) ] ──┐
      │                                 (Diode / Tube Drive)           (LPF / BPF / HPF)         │
      │                                                                                          │
      └───► [ Sidechain Envelope Follower ] ───────────────────────────────┘ (Cutoff Mod)       │
            (Attack / Decay / Sensitivity)                                                       │
                                                                                                 ▼
Instrument In ───────────────────────► [ Parallel Clean Blend ] ──────────────────────────► Sum Out
```

### 1.1 The Crucial Role of Pre-Filter Saturation

Placing harmonic saturation *before* the filter is vastly superior to post-filter distortion for dynamic filtering:
1. **Spectral Enrichment:** A pure clean guitar or bass string produces mostly fundamental and lower-order harmonics. Introducing non-linear diode or tube saturation *prior* to the filter injects dense odd and even harmonics across the entire audio bandwidth.
2. **Resonant Accentuation:** When the resonant filter peak sweeps through this harmonic-rich spectrum, the "quack", "vocal talk", and vocal-like formants become dramatically more pronounced, dynamic, and vocal.
3. **Dynamic Touch Sensitivity:** Soft fingerpicking keeps the signal below the saturation threshold for mellow, warm filtering; dig in with a pick, and the signal pushes into harmonic saturation, making the filter sweep explode with aggressive bite and presence.

### 1.2 Envelope Ballistics & Sweep Direction

The sidechain envelope detector tracks the instantaneous audio amplitude $x(t)$:

$$v_{\text{env}}(n) = \alpha \cdot v_{\text{env}}(n-1) + (1 - \alpha) \cdot |x(n)|$$

Where the smoothing coefficient $\alpha$ changes dynamically based on attack ($\alpha_{\text{att}}$) or release ($\alpha_{\text{rel}}$) conditions.

- **UP Sweep:** As input attack increases, the cutoff frequency sweeps *upwards* towards the treble, mimicking a traditional wah pedal pushed forward (classic 70s funk quack).
- **DOWN Sweep:** As input attack increases, the cutoff starts high and plunges *downwards* into the bass frequencies, producing synthesizer laser sweeps and dark bubbly filter dips.

---

## 2. DSP Signal Chain & Topology

```
Input Audio (Guitar / Bass / Keys)
   │
   ├───► [ Sidechain Rectifier & Envelope Detector ] ──► [ Sweep Mod: UP / DOWN ]
   │                                                               │
   ▼                                                               │
[ Pre-Filter Overdrive & Harmonic Generator ]                      │
      │ (Germanium Diode Soft-Clip / Tube Asymmetric)             │
      ▼                                                            │
[ 2-Pole 12dB / 4-Pole 24dB State Variable Filter (SVF) ] ◄────────┘
      │ (Mode: Low-Pass / Band-Pass / High-Pass)
      ▼
[ Resonance Peak Limiter / Soft-Saturation Tamer ]
      │ (Prevents ear-fatiguing resonant squeals)
      ▼
[ Parallel Clean Dry / Saturated Wet Summing ] ──► Master Output
```

---

## 3. Parameter Specifications

| Parameter | Range | Default | Unit | Description |
| :--- | :--- | :--- | :--- | :--- |
| `SENSITIVITY` | `0` - `100` | `65` | % | Determines how readily the envelope detector reacts to picking attack. |
| `SWEEP_DIR` | `UP` / `DOWN` | `UP` | mode | Direction of cutoff frequency excursion upon transient detection. |
| `FILTER_MODE` | `LPF` / `BPF` / `HPF` | `BPF` | mode | Filter curve topology: BPF = vocal quack; LPF = synth bass fatness. |
| `PRE_DRIVE` | `0` - `100` | `40` | % | Amount of pre-filter harmonic saturation injected into the signal. |
| `DRIVE_VOICING`| `GERM` / `TUBE` | `GERM` | mode | Saturation character: Germanium (soft, fuzzy) vs. Tube (punchy, gritty). |
| `BASE_CUTOFF` | `40` - `2000` | `280` | Hz | Resting resting cutoff frequency when no envelope modulation is present. |
| `SWEEP_DEPTH` | `0` - `100` | `75` | % | Maximum frequency excursion range driven by the envelope. |
| `RESONANCE (Q)`| `0.7` - `18.0` | `7.5` | - | Sharpness of the resonant peak at the cutoff frequency. |
| `ATTACK_TIME` | `1.0` - `60.0`| `8.0` | ms | Speed at which the filter opens upon transient strike. |
| `DECAY_TIME` | `40` - `800` | `180` | ms | Speed at which the filter returns to its resting base cutoff frequency. |
| `MIX_WET_DRY` | `0` - `100` | `75` | % | Balance between raw direct input and filtered/saturated output. |

---

## 4. Factory Scene Presets

### Scene A: Classic Funk Quack (Mu-Tron III Up-Sweep)
- **Concept:** Iconic 1970s funk and disco auto-wah with singing harmonic bite.
- **Filter & Mod:** `FILTER_MODE = BPF`, `SWEEP_DIR = UP`, `SENSITIVITY = 68%`, `SWEEP_DEPTH = 80%`, `RESONANCE = 8.5`.
- **Pre-Drive:** `PRE_DRIVE = 35%`, `DRIVE_VOICING = GERM`.
- **Ballistics:** `ATTACK_TIME = 6.0 ms`, `DECAY_TIME = 160 ms`.
- **Mix:** `MIX_WET_DRY = 85%`.

### Scene B: Laser Synth Bass Down-Sweep (Moog Style Bass Drops)
- **Concept:** Punchy sub-heavy synth filter plunge designed for bass guitar or drop-tuned rhythm.
- **Filter & Mod:** `FILTER_MODE = LPF`, `SWEEP_DIR = DOWN`, `SENSITIVITY = 72%`, `SWEEP_DEPTH = 85%`, `BASE_CUTOFF = 1600 Hz`, `RESONANCE = 9.0`.
- **Pre-Drive:** `PRE_DRIVE = 55%`, `DRIVE_VOICING = TUBE`.
- **Ballistics:** `ATTACK_TIME = 2.0 ms`, `DECAY_TIME = 260 ms`.
- **Mix:** `MIX_WET_DRY = 70%` (Retains 30% unadulterated low-end fundamental).

### Scene C: Saturated Lead Vocal-Wah (Jerry Garcia / Bootsy Collins)
- **Concept:** Warm, singing envelope lead that tracks expressive vibrato and solo articulation.
- **Filter & Mod:** `FILTER_MODE = BPF`, `SWEEP_DIR = UP`, `SENSITIVITY = 60%`, `SWEEP_DEPTH = 70%`, `RESONANCE = 6.8`.
- **Pre-Drive:** `PRE_DRIVE = 65%`, `DRIVE_VOICING = TUBE`.
- **Post FX:** Analog Warm Delay (`380 ms`, `25%` feedback) + Mild Spring Reverb.
- **Mix:** `MIX_WET_DRY = 80%`.

### Scene D: Dynamic Ambient Dub Sweep (Deep Resonant Echo)
- **Concept:** Atmospheric dub filter with long decay times that swells into tape delay spaces.
- **Filter & Mod:** `FILTER_MODE = LPF`, `SWEEP_DIR = UP`, `SENSITIVITY = 50%`, `SWEEP_DEPTH = 65%`, `RESONANCE = 11.5`.
- **Pre-Drive:** `PRE_DRIVE = 25%`, `DRIVE_VOICING = GERM`.
- **Ballistics:** `ATTACK_TIME = 25.0 ms`, `DECAY_TIME = 550 ms`.
- **Space:** Tape Delay (`dotted 8th`, `450 ms`, `45%` feedback) + Dark Hall Reverb.
- **Mix:** `MIX_WET_DRY = 60%`.

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (Classic Funk Quack) / Scene B (Laser Synth Bass).
- **Footswitch B:** Scene C (Saturated Vocal Lead).
- **Footswitch C:** Scene D (Dynamic Dub Sweep) / Bypass.
- **Knob 1 (GAIN):** Pre-Filter Drive & Saturation level.
- **Knob 2 (MOD FX):** Sensitivity & Sweep Depth.
- **Knob 3 (REVERB/DELAY):** Wet/Dry Parallel Balance.

### Tank-B Control Assignments
- Dedicated Low-Pass Filter configuration for bass players: retains full sub-bass fundamental weight using parallel clean path while sweeping mid-range drive harmonics.
- **Footswitch 1 / 2:** Toggle between Up-Sweep and Down-Sweep modes on the fly.

### Black Box Desktop Configuration
- **Expression Pedal 1:** Continuous manual control over `BASE_CUTOFF` (acts as hybrid foot wah).
- **MIDI CC #70:** Dynamic Sensitivity adjustment according to song section.
