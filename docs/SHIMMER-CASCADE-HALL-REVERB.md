# Stereo Shimmer & Cascade Hall Reverb Modeling Guide

This guide details Feedback Delay Network (FDN) reverb diffusion, **in-loop regenerative pitch-shift cascades** ($+12\text{ st}$, $+7\text{ st}$, $-12\text{ st}$), adaptive high-frequency damping, and preset configuration for **Stereo Shimmer & Cascade Hall Reverb** within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Algorithmic Principles of Regenerative Shimmer Reverb

Originally crafted in the 1980s by ambient pioneers **Brian Eno** and **Daniel Lanois** (heard on *Apollo* and U2's *The Unforgettable Fire*), **Shimmer Reverb** achieves its unmistakable celestial pad quality not merely by adding an octave pedal before a reverb, but by embedding a pitch shifter **directly inside the reverb's regenerative feedback loop**.

```
Instrument In ──► [ Pre-Delay (0 - 150 ms) ] ──► [ + ] ──► [ 8-Channel Hadamard FDN Diffusion Matrix ] ──► Stereo Wet Out
                                                   ▲                          │
                                                   │                          ▼
                   [ Adaptive Cascade Damping LPF ] ◄── [ In-Loop Polyphonic Pitch Shifter ]
                                                       (+12 st Octave / +7 st Fifth / -12 st Sub)
```

### 1.1 Pre-Reverb Pitch vs. In-Loop Regenerative Cascade

1. **Standard External Pitch + Reverb:** Simply yields a single static octave voice washed into normal room decay.
2. **In-Loop Regenerative Cascade:** Feeding the output of the reverb tank *through* a polyphonic pitch shifter and back into the tank input creates recursive harmonic transposition:
   - Pass 1: Fundamental note ($0\text{ st}$)
   - Pass 2: Octave up ($+12\text{ st}$)
   - Pass 3: Two octaves up ($+24\text{ st}$)
   - Pass 4: Three octaves up ($+36\text{ st}$)
   Each iteration blurs dynamically through the multi-tap FDN diffuser, smoothly morphing single guitar plucks into soaring, rising orchestral string and pipe-organ clouds.

### 1.2 Cascade Damping & FDN Orthogonal Diffusion

Without careful spectral control, recursive upward transposition ($+12\text{ st} \to +24\text{ st} \to +36\text{ st}$) rapidly pushes acoustic energy above $6\text{ kHz}$, turning pleasant harmonics into shrill metallic ringing. UltraRig solves this via:
- **Adaptive In-Loop Low-Pass Damping:** Gently rolls off upper reflections between $4.2\text{ kHz}$ and $7.5\text{ kHz}$ on every pass, turning harsh upper octaves into silky cello-like clouds.
- **Hadamard / Householder FDN Matrix:** Uses modulated prime-length delay lines inside an orthogonal feedback matrix to eliminate rhythmic flutter and metallic comb echoes.

---

## 2. DSP Signal Chain & Processing Topology

```
Guitar / Bass / Synth In ──────────────► [ Dry Direct Level ] ─────────────────────────────────┐
      │                                                                                        │
      ▼                                                                                        │
[ Soft Attack Pre-Filter & Pre-Delay (0 - 150 ms) ] (Separates dry attack from blooming shimmer)
      │                                                                                        │
      ▼                                                                                        │
[ Modulated 8-Line Feedback Delay Network (FDN Hall Matrix) ] ◄────────────────────────┐       │
      │                                                                                │       │
      ├───► [ Pitch Voice A (+12 st) ] ──┐                                             │       │
      │                                  ├──► [ Loop Damping LPF & Soft Limiter ] ─────┘       │
      └───► [ Pitch Voice B (+7 st / -12 st) ] ┘                                               │
      │                                                                                        │
      ▼                                                                                        │
[ Stereo High/Low-Cut Post-EQ ] ──► [ Wet Level ] ─────────────────────────────────────────────┴──► Stereo Output
```

---

## 3. Parameter Specifications

| Parameter | Range | Default | Unit | Description |
| :--- | :--- | :--- | :--- | :--- |
| `SHIMMER_MODE` | `OCTAVE_UP` / `FIFTH_CASCADE` / `SUB_ABYSS` | `OCTAVE_UP` | mode | Harmonic interval architecture inside the feedback loop. |
| `PITCH_1_ST` | `-12` to `+12`| `+12` | st | Primary harmonic transposition inside the FDN loop. |
| `PITCH_2_ST` | `-12` to `+12`| `0` (Off) | st | Optional secondary voice (e.g. $+7\text{ st}$ perfect fifth). |
| `SHIMMER_REGEN`| `0` - `100` | `55` | % | Amount of reverb energy routed through the pitch-shift feedback path. |
| `FDN_DECAY` | `1.5` - `25.0` | `8.5` | s | Overall decay length of the modulated hall matrix. |
| `PRE_DELAY` | `0` - `150` | `55` | ms | Delays shimmer onset behind dry pick transients for melodic clarity. |
| `CASCADE_DAMP` | `2.5` - `12.0` | `5.2` | kHz | Critical damping filter keeping cascading octaves warm and organic. |
| `MOD_DEPTH` | `0` - `100` | `40` | % | Subtle FDN delay line chorus modulation preventing metallic stasis. |
| `FREEZE_LATCH` | `OFF` / `ON` | `OFF` | bool | Locks FDN feedback at 100% while muting input, holding infinite pads. |
| `MIX_WET_DRY` | `0` - `100` | `45` | % | Balance between raw direct instrument signal and ambient shimmer hall. |

---

## 4. Factory Scene Presets

### Scene A: Eno / Lanois Classic Octave Shimmer (Apollo Pad)
- **Concept:** The authentic 1980s ambient benchmark: warm, majestic ascending octaves blooming slowly behind delicate clean notes.
- **Shimmer & FDN:** `SHIMMER_MODE = OCTAVE_UP`, `PITCH_1_ST = +12 st`, `SHIMMER_REGEN = 58%`, `FDN_DECAY = 9.0 s`.
- **Damping & Pre-Delay:** `PRE_DELAY = 65 ms`, `CASCADE_DAMP = 5.0 kHz`, `MOD_DEPTH = 45%`.
- **Mix:** `MIX_WET_DRY = 45%`.

### Scene B: Fifth-Up Celestial Pad (`+7 st` & `+12 st` Harmonics)
- **Concept:** Stacked intervals of perfect fifths and octaves creating an immersive cathedral choir / string orchestra synthesis.
- **Shimmer & FDN:** `SHIMMER_MODE = FIFTH_CASCADE`, `PITCH_1_ST = +12 st`, `PITCH_2_ST = +7 st`, `SHIMMER_REGEN = 50%`.
- **Damping & Decay:** `FDN_DECAY = 7.5 s`, `CASCADE_DAMP = 4.6 kHz`.
- **Mix:** `MIX_WET_DRY = 48%`.

### Scene C: Sub-Octave Dark Abyss (`-12 st` Cavern)
- **Concept:** Inverted atmospheric pitch cascade that sinks notes downward into vast, brooding, cinematic sub-bass shadows.
- **Shimmer & FDN:** `SHIMMER_MODE = SUB_ABYSS`, `PITCH_1_ST = -12 st`, `SHIMMER_REGEN = 65%`, `FDN_DECAY = 11.0 s`.
- **EQ:** Subsonic protection HPF at `45 Hz`, dark damping at `3.4 kHz`.
- **Mix:** `MIX_WET_DRY = 52%`.

### Scene D: Infinite Ambient Freeze Bloom (Footswitch Pad Hold)
- **Concept:** Instantly captures any strummed chord into an endless, evolving ambient pad while leaving dry guitar completely free for soloing over top.
- **Shimmer & Freeze:** `FREEZE_LATCH = ON` (toggled via Footswitch B), `PITCH_1_ST = +12 st`, `SHIMMER_REGEN = 35%`, `MOD_DEPTH = 60%`.
- **Mix:** `MIX_WET_DRY = 50%`.

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (Eno/Lanois Octave Shimmer) / Scene B (Fifth-Up Celestial Pad).
- **Footswitch B (Hold / Latch):** Engages **Infinite Ambient Freeze Bloom** (locks chord pad cleanly for live soloing).
- **Footswitch C:** Scene C (Sub-Octave Dark Abyss) / Reverb Bypass.
- **Knob 1 (REVERB):** FDN Decay Time (`2.0 s` to `20.0 s`).
- **Knob 2 (MOD / SHIMMER):** Shimmer Regeneration Feed (`0%` normal hall to `85%` cascading waterfall).
- **Knob 3 (BLEND):** Wet / Dry ambient balance.

### Tank-B Control Assignments
- Bassists can utilize Scene A with an internal wet-only high-pass filter set to `180 Hz`, allowing shimmering $+12\text{ st}$ ambient clouds to float high above crisp, unclouded sub-bass grooves.

### Black Box Desktop Configuration
- **Expression Pedal 1:** Continuous control over `SHIMMER_REGEN` or `MIX_WET_DRY`, enabling seamless emotional swells into cascading octave clouds during song climaxes.
- **Stereo Outputs:** Essential to appreciate the full 8-channel Hadamard FDN stereo diffusion.
