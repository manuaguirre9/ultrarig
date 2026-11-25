# Matchless DC-30 & Class-A British Chime Preamp Routing Guide

This guide details the dual-channel circuit architecture, EF86 pentode vs. 12AX7 Top Boost gain structures, cathode-biased EL84 power section dynamics, and practical preset configuration for the **Matchless DC-30** and vintage **Vox AC30 Top Boost** within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Circuit Architecture of the Matchless DC-30

Introduced in 1989 by Mark Sampson and Rick Perrotta, the Matchless DC-30 modernized the legendary 1960s Vox AC30 circuit into the defining standard of boutique Class-A tube amplification. Renowned for its sparkling harmonic "chime," immediate pick attack dynamics, and singing edge-of-breakup saturation, the DC-30 features two entirely distinct preamplifier channels.

```
Instrument In
   │
   ├───► [ Channel 1: 12AX7 Top Boost Channel ] ──► [ Interactive Passive Tonestack (Treble & Bass) ] ──┐
   │                                                                                                    │
   └───► [ Channel 2: EF86 Pentode Channel ] ───► [ 6-Position Rotary Tone Contour Switch ] ────────────┤
                                                                                                        │
                                                                                                        ▼
                                                                                   [ Phase Inverter (12AX7) ]
                                                                                                │
                                                                                   [ Passive High-Cut Control ]
                                                                                                │
                                                                                                ▼
[ 2x12 Mixed Speaker Cabinet IR (Celestion Alnico Blue + G12H30) ] ◄─── [ 4x EL84 Cathode-Biased Power Amp (No NFB) ]
```

### 1.1 Channel 1 (12AX7 Top Boost) vs. Channel 2 (EF86 Pentode)

- **Channel 1 (12AX7 Dual-Triode):**
  - Features an interactive **Treble and Bass tonestack** with no dedicated midrange control.
  - Turning Treble and Bass down causes the midrange to leap forward; turning Treble and Bass up scoops the midrange.
  - Produces sparkling top-end chime, crystalline jangly chords, and percussive single-coil snap (favored by The Edge, Tom Petty, and George Harrison).
- **Channel 2 (EF86 High-Gain Pentode):**
  - Employs a single 9-pin EF86 miniature pentode tube paired with a **6-position rotary tone switch**.
  - Unlike dual-triodes, pentodes deliver immense gain, high transconductance, and huge dynamic headroom.
  - Produces a fat, punchy, immediate midrange thrust that drives power tubes into rich, harmonic overdrive much faster and with greater low-end authority.

### 1.2 The "No Negative Feedback" EL84 Power Section & Cut Control

- **Zero Global Negative Feedback (No NFB):** Unlike Fender (6L6) or Marshall (EL34) designs that feed output voltage back to the phase inverter to tighten bass and stabilize gain, the DC-30 runs open-loop. This produces a raw, touch-sensitive, highly responsive dynamic feel where gentle playing is glassy-clean and digging in yields creamy, singing saturation.
- **Master "Cut" Control:** Rather than filtering high frequencies in the preamp, the Cut control is a reverse low-pass filter placed across the differential outputs of the phase inverter tube. Dialing the Cut knob up gently rolls off harsh top-end fizz without altering preamp gain or touch dynamics.
- **Mixed 2x12 Speaker Complement:** The DC-30 pairs one 30-watt Celestion G12H (for tight, punchy low-end) with one 25-watt Celestion G12M Greenback or Alnico Blue (for creamy, singing midrange and chime).

---

## 2. DSP Signal Chain & Processing Topology

```
Guitar In (Single-Coils / Humbuckers)
   │
   ▼
[ Input Voicing & Channel Selector (Ch 1 Top Boost / Ch 2 EF86 Pentode) ]
   │
   ▼
[ Tonestack Emulation (Interactive Bass/Treble OR 6-Way Rotary Switch) ]
   │
   ▼
[ 4x EL84 Cathode-Biased Class-A Power Amp Emulation (Zero NFB) ]
   │
   ▼
[ Post-Phase Inverter Master "Cut" Filter ]
   │
   ▼
[ Dual IR Convolution: 2x12 Celestion Alnico Blue + G12H30 ]
   │
   ▼
[ Ambient Stereo Modulated Tape Delay & Studio Spring/Plate Reverb ] ──► Stereo Output
```

---

## 3. Parameter Specifications

| Parameter | Range | Default | Unit | Description |
| :--- | :--- | :--- | :--- | :--- |
| `CHANNEL_MODE`| `CH1_TOPBOOST` / `CH2_EF86` / `LINKED` | `CH1_TOPBOOST` | mode | Active preamp channel topology. |
| `PREAMP_GAIN` | `0` - `100` | `55` | % | Input gain driving 12AX7 triodes or EF86 pentode. |
| `BASS` | `0` - `100` | `48` | % | Ch 1 low-frequency control (interlocks with Treble for mid scoop/boost). |
| `TREBLE` | `0` - `100` | `62` | % | Ch 1 high-frequency chime control. |
| `ROTARY_POS` | `1` to `6` | `3` | pos | Ch 2 EF86 6-position rotary tone capacitor selector (1 = thin; 6 = thick/fat). |
| `MASTER_CUT` | `0` - `100` | `35` | % | Post-phase inverter high-frequency smoothing control. |
| `POWER_SAG` | `0` - `100` | `50` | % | Cathode-biased EL84 power supply compression and bloom. |
| `CAB_IR_MIX` | `ALNICO_BLUE` / `G12H30` / `MIXED_5050`| `MIXED_5050` | mode | Speaker cabinet convolution profile. |
| `PRESENCE` | `0` - `100` | `60` | % | High-frequency acoustic air and pick transient bite. |

---

## 4. Factory Scene Presets

### Scene A: British Jangle & Chime (The Edge / Tom Petty Style)
- **Concept:** Sparkling, pristine Class-A chime with glassy top-end clarity for ringing open chords and 12-string arpeggios.
- **Voicing:** `CHANNEL_MODE = CH1_TOPBOOST`, `PREAMP_GAIN = 42%`.
- **EQ & Cut:** `BASS = 45%`, `TREBLE = 68%` (subtle mid scoop), `MASTER_CUT = 30%`.
- **Cabinet:** Celestion Alnico Blue IR.
- **Space:** Modulated Dotted-8th Tape Delay (`375 ms`, `28%` feedback) + Plate Reverb.

### Scene B: EF86 Fat Punch Crunch (Boutique British Breakup)
- **Concept:** Thick, immediate, and punchy midrange crunch with touch-responsive dynamics that clean up with guitar volume.
- **Voicing:** `CHANNEL_MODE = CH2_EF86`, `ROTARY_POS = 4`, `PREAMP_GAIN = 65%`.
- **Power & Cut:** `POWER_SAG = 55%`, `MASTER_CUT = 42%` (smooth top end).
- **Cabinet:** Mixed 2x12 (Alnico Blue + G12H30).
- **Space:** Natural Spring Reverb (`1.8 s`, `18%` mix).

### Scene C: Harmonic Overdrive Solo (Rory Gallagher / Brian May)
- **Concept:** Singing, creamy Class-A lead sustain with blooming odd harmonics and effortless feedback.
- **Voicing:** `CHANNEL_MODE = LINKED` (Jumping Ch 1 and Ch 2 in parallel), `PREAMP_GAIN = 82%`.
- **Power & Cut:** `POWER_SAG = 70%`, `MASTER_CUT = 48%` (removes harsh fizz while keeping singing sustain).
- **Cabinet:** Dual Alnico Blue 2x12.
- **Space:** Warm Analog Slapback Delay (`140 ms`) + Studio Room Reverb.

### Scene D: Worship & Indie Ambient Chime (Clean Ambient Swell)
- **Concept:** Lush, spatial clean foundation designed to take ambient delays and vast reverbs without muddying.
- **Voicing:** `CHANNEL_MODE = CH1_TOPBOOST`, `PREAMP_GAIN = 38%`, `BASS = 42%`, `TREBLE = 60%`.
- **Master Cut:** `MASTER_CUT = 40%` (warm, non-fatiguing high end).
- **Space:** Stereo Modulated Delay (`500 ms`) into Shimmer Reverb (`5.5 s` decay).
- **Mix:** 50% Direct / 50% Space.

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (British Jangle Chime) / Scene B (EF86 Fat Crunch).
- **Footswitch C:** Scene C (Harmonic Overdrive Solo) / Scene D (Ambient Chime).
- **Footswitch B:** Boost (+3 dB) / Channel Switch.
- **Knob 1 (GAIN):** Preamp Gain / EF86 Drive.
- **Knob 2 (TONE):** Master Cut control (turn clockwise to smooth highs).
- **Knob 3 (REVERB / DELAY):** Ambient FX balance.

### Tank-B Control Assignments
- Bassists seeking vintage Paul McCartney / Beatles *Abbey Road* warm tube bass tone can use Channel 2 (`EF86`) with `ROTARY_POS = 6` and mild power sag for round, woody bass punch.

### Black Box Desktop Configuration
- **Stereo Cabinet Mixing:** Route Celestion Alnico Blue to Left Output and Celestion G12H30 to Right Output for authentic 3D boutique dispersion.
- **MIDI CC #82:** Seamless real-time channel switching between Top Boost and EF86.
