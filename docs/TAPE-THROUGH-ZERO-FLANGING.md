# Tape Through-Zero Flanging (TZF) & Tape Saturation Modeling Guide

This guide details the physical principles, tape reel deceleration mechanics, complete destructive phase cancellation at the **Through-Zero Point (TZP)**, and practical preset configuration for **Tape Through-Zero Flanging** within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Physical Origins & Physics of True Tape Flanging

Flanging was invented in recording studios during the 1960s (pioneered by Ken Townsend at Abbey Road with The Beatles, and refined by Eddie Kramer with Jimi Hendrix on *Axis: Bold as Love* and *Electric Ladyland*). The effect was physically produced using two synchronized reel-to-reel tape recorders playing identical audio.

```
Audio Input ───────────────────────────────────┬────────────────────────────────────────────────────────┐
                                               │                                                        │
                                               ▼                                                        ▼
                                    [ Tape Deck A (Reference) ]                              [ Tape Deck B (Modulated) ]
                                    (Fixed Delay: τ_ref = 5.0 ms)                            (Varying Delay: τ_mod = 0 to 10 ms)
                                               │                                                        │
                                               ▼                                                        ▼
                                    [ Tape Oxide Saturation ]                                [ Tape Oxide Saturation ]
                                               │                                                        │
                                               │                                                        ▼
                                               │                                             [ Polarity Invert (180°) ]
                                               │                                                        │
                                               └─────────────────────────┬──────────────────────────────┘
                                                                         ▼
                                                           [ Summing Bus: At τ_mod = τ_ref ]
                                                           ===> TOTAL PHASE CANCELLATION (ZERO VOID) <===
```

### 1.1 Conventional BBD Flanging vs. Through-Zero Flanging (TZF)

Standard analog BBD pedals (such as the EHX Electric Mistress, MXR Flanger, or Boss BF-2) modulate a single delay line between approximately $1.0\text{ ms}$ and $10.0\text{ ms}$:
- The delayed audio is **always strictly behind** the direct dry signal in time.
- The delay difference $\Delta t$ never reaches zero ($\Delta t > 0$).
- Consequently, full destructive cancellation across all frequencies can never occur.

In **True Through-Zero Flanging (TZF)**:
1. Both signals are delayed relative to the input. Deck A has a fixed reference delay $\tau_{\text{ref}} = 5.0\text{ ms}$.
2. Deck B modulates from $10.0\text{ ms}$ down through $5.0\text{ ms}$ to $0.0\text{ ms}$.
3. At the exact moment where $\tau_{\text{mod}}(t) = \tau_{\text{ref}}$, the relative delay between the two paths is **exactly zero** ($\Delta t = 0\text{ ms}$).
4. With Deck B phase-inverted by $180^\circ$, **100% complete destructive phase cancellation occurs across the entire audio spectrum**.
5. The audio momentarily vanishes into an eerie "black hole" / void, inverts phase, and emerges on the other side with an explosive, soaring jet-plane rush.

### 1.2 Magnetic Tape Non-Linearities

In addition to phase cancellation, authentic tape flanging incorporates:
- **Magnetic Hysteresis & Oxide Saturation:** Soft-knee compression and rich 3rd-order harmonic distortion that smooths harsh pick attacks.
- **Tape Head Bump:** A gentle low-frequency resonance boost ($+1.5\text{ dB}$ to $+3.0\text{ dB}$) between $50\text{ Hz}$ and $90\text{ Hz}$.
- **Tape Wow & Flutter:** Microscopic motor variations that add subtle organic randomness to the LFO modulation sweep.

---

## 2. DSP Signal Chain & Processing Topology

```
Guitar / Bass In
   │
   ▼
[ Tape Input Preamp & Head-Bump Low Boost (65 Hz) ]
   │
   ▼
[ Magnetic Oxide Saturation & Soft-Clipper ]
   │
   ├───► [ Reference Delay Line: τ_ref (Fixed 4.5 ms) ] ─────────────────────────┐
   │                                                                             │
   ▼                                                                             │
[ Modulated Delay Line: τ_mod (0.0 ms - 9.0 ms) ] ◄── [ Dual-Stage LFO + Flutter ]
   │                                                                             │
   ▼                                                                             │
[ Polarity Inverter: Phase Null Latch (180°) ]                                   │
   │                                                                             │
   ▼                                                                             │
[ Tape Feedback Matrix (Regeneration with HF Damping) ]                          │
   │                                                                             │
   └───────────────────────────────┬─────────────────────────────────────────────┘
                                   ▼
[ Stereo Summing & Cross-Coupled Spatial Diffuser ] ──► Master Output
```

---

## 3. Parameter Specifications

| Parameter | Range | Default | Unit | Description |
| :--- | :--- | :--- | :--- | :--- |
| `TZF_MODE` | `STANDARD_TZF` / `BARBERPOLE` / `INVERT_NULL` | `INVERT_NULL` | mode | Flanger topology: Invert Null achieves full cancellation at TZP. |
| `RATE` | `0.05` - `8.0` | `0.25` | Hz | Modulation frequency; slow sweeps accentuate the through-zero void. |
| `DEPTH` | `0` - `100` | `85` | % | Modulation excursion across the Through-Zero boundary. |
| `ZERO_OFFSET` | `2.0` - `8.0` | `4.5` | ms | Reference delay time; sets the center frequency of the through-zero crossing. |
| `FEEDBACK` | `-95` to `+95` | `+70` | % | Resonance regeneration; negative values emphasize hollow metallic overtones. |
| `TAPE_DRIVE` | `0` - `100` | `45` | % | Non-linear tape saturation and magnetic oxide compression. |
| `HEAD_BUMP` | `0` - `100` | `35` | % | Low-end analog tape head resonance (55 Hz - 85 Hz). |
| `WOW_FLUTTER` | `0` - `100` | `20` | % | Organic micro-pitch instability from tape transport variations. |
| `MIX_WET_DRY` | `0` - `100` | `50` | % | Must be 50% for 100% destructive phase cancellation at zero point. |

---

## 4. Factory Scene Presets

### Scene A: Abbey Road / Olympic Jet Flange (Hendrix Axis Swirl)
- **Concept:** The authentic 1967 tape flanging sound: dramatic through-zero nulling, rich tape saturation, and cosmic stereo sweep.
- **Flanger:** `TZF_MODE = INVERT_NULL`, `RATE = 0.18 Hz`, `DEPTH = 90%`, `FEEDBACK = +75%`.
- **Tape Profile:** `TAPE_DRIVE = 55%`, `HEAD_BUMP = 40%`, `WOW_FLUTTER = 25%`.
- **Mix:** `MIX_WET_DRY = 50%` (Critical for absolute phase cancellation).

### Scene B: Unchained Metallic Barber-Pole (Van Halen Style)
- **Concept:** Metallic, high-resonance swoosh with biting pick attack and intense harmonic comb-filtering.
- **Flanger:** `TZF_MODE = STANDARD_TZF`, `RATE = 0.45 Hz`, `DEPTH = 80%`, `FEEDBACK = -82%` (Negative feedback for hollow metallic timbre).
- **Tape Profile:** `TAPE_DRIVE = 35%`, `HEAD_BUMP = 15%`.
- **Mix:** `MIX_WET_DRY = 55%`.

### Scene C: Slow Oceanic Tape Swell (Pink Floyd / Gilmour Atmosphere)
- **Concept:** Extremely slow, broad tape drift with warm low-frequency head-bump and velvety top-end roll-off.
- **Flanger:** `TZF_MODE = INVERT_NULL`, `RATE = 0.08 Hz`, `DEPTH = 70%`, `FEEDBACK = +45%`.
- **Tape Profile:** `TAPE_DRIVE = 60%`, `HEAD_BUMP = 50%`, `WOW_FLUTTER = 30%`.
- **Space:** Warm Analog Delay (`440 ms`, `25%` feedback) + Studio Plate Reverb.
- **Mix:** `MIX_WET_DRY = 50%`.

### Scene D: Stereo Biphase Tape Flange (Modern Ambient Width)
- **Concept:** Dual anti-phase tape flanging sweeping oppositely in Left and Right channels for vast, enveloping spatialization.
- **Flanger:** `TZF_MODE = INVERT_NULL`, `RATE = 0.30 Hz`, `DEPTH = 85%`, `FEEDBACK = +65%`.
- **Spatial:** Stereo phase offset $180^\circ$ between Left and Right delay lines.
- **Mix:** `MIX_WET_DRY = 50%`.

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (Olympic Jet Flange) / Scene B (Metallic Barber-Pole).
- **Footswitch B:** Scene C (Oceanic Tape Swell).
- **Footswitch C:** Scene D (Stereo Biphase) / Flanger Bypass.
- **Knob 1 (MOD FX):** Rate / Modulation Speed.
- **Knob 2 (GAIN / TONE):** Tape Drive Saturation and High-Cut Damping.
- **Knob 3 (FEEDBACK / MIX):** Regeneration Resonance and 50% Phase Null balance.

### Tank-B Control Assignments
- Excellent for bassists (Justin Chancellor / Tool style): provides aggressive metallic rasp on pick attacks while the `HEAD_BUMP` parameter preserves foundational low-end punch.

### Black Box Desktop Configuration
- **Expression Pedal 1:** Manual Through-Zero Scrubbing (allows the player to sweep manually through the zero-point void using their foot).
- **Stereo Direct Outputs:** Essential to experience the full cross-phase cancellation of Scene D.
