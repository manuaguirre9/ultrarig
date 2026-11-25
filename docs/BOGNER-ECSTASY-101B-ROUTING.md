# Bogner Ecstasy 101B 3-Channel High-Gain Routing Guide

This guide details the 3-channel tube topology (**Green, Blue, Red**), gain-shaping switches (**Plexi, Structure, Pre-EQ**), power amp damping (**Excursion, Class A/AB**), and preset configuration for the **Bogner Ecstasy 101B** within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Circuit Architecture of the Bogner Ecstasy 101B

Designed by German amplifier visionary Reinhold Bogner in 1992, the Ecstasy 101B fused vintage British Plexi warmth with modern boutique high-gain fluidity. Renowned for its "chewy," vocal, non-fatiguing midrange (favored by **Steve Vai**, **Jerry Cantrell**, and **Doug Aldrich**), its secret lies in nuanced interstage filtering and extraordinary power-amp flexibility.

```
Instrument In
   │
   ├───► [ Channel 1 (Green): Clean / Vintage Tweed Crunch ] ─────────┐
   │                                                                  │
   ├───► [ Channel 2 (Blue): Plexi Mode OR Hot-Rodded British Crunch ]┼──► [ Structure (H/L) & Pre-EQ ]
   │                                                                  │             │
   └───► [ Channel 3 (Red): Cascaded Triode Liquid High-Gain Lead ] ──┘             ▼
                                                                      [ 3-Band Passive Tonestack ]
                                                                                    │
                                                                                    ▼
[ 4x12 Bogner Cab IR (V30 + G12M-25) ] ◄── [ EL34 Power Amp (Class A/AB + Excursion Damping) ]
```

### 1.1 The Three Signature Channels

- **Green Channel (Clean):** Full-bodied, 3D American/British clean voice with three Pre-EQ brightness voicings (`B1`, `B2`, `N`) and enough clean gain push for crisp edge-of-breakup.
- **Blue Channel (Crunch / Plexi):** The heart of the 101B. Delivers thick, organic midrange growl with exceptional pick dynamics. Engaging the **Plexi Mode** bypasses a gain stage and opens the upper midrange for authentic non-master-volume 1968 British rock grind.
- **Red Channel (Liquid Lead):** Stacks an additional 12AX7 triode stage ahead of the Blue path, producing dense harmonic sustain, violin-like singing legato compression, and smooth high-end rolloff completely free of brittle fizz.

### 1.2 Power Amp Damping: Excursion & Class A / AB

- **Excursion Switch (`LOOSE` / `MEDIUM` / `TIGHT`):** Modifies the negative feedback low-frequency resonance across the EL34 output transformer. `TIGHT` clamps speaker excursion for laser-focused metal palm mutes; `LOOSE` opens the cabinet floor resonance for booming 4x12 air push.
- **Class A / Class AB Mode:** Emulates switching the EL34 output stage from stiff 100W Class-AB headroom into warm, spongy, harmonically rich Class-A cathode-style sag.

---

## 2. DSP Signal Chain & Processing Topology

```
Guitar In (Humbuckers / Single-Coils)
   │
   ▼
[ Fast Downward Expander / Noise Gate ] (Silences Red Channel idle hiss)
   │
   ▼
[ Channel Matrix: Green (Clean) / Blue (Crunch & Plexi) / Red (Liquid Lead) ]
   │
   ▼
[ Structure Switch (High / Low Gain) & Boost Stage (+6 dB Input Push) ]
   │
   ▼
[ Pre-EQ Bright Voicing (N / B1 / B2) & 3-Band British Tonestack ]
   │
   ▼
[ 4x EL34 Power Section Emulation (Excursion Damping + Class A/AB Bias + Presence) ]
   │
   ▼
[ Dual Speaker IR Convolution: Bogner 4x12 (Celestion V30 + Greenback) ]
   │
   ▼
[ Stereo FX Loop: Modulated Tape Delay & Studio Hall Reverb ] ──► Stereo Output
```

---

## 3. Parameter Specifications

| Parameter | Range | Default | Unit | Description |
| :--- | :--- | :--- | :--- | :--- |
| `CHANNEL_MODE`| `GREEN` / `BLUE` / `RED` | `BLUE` | mode | Selects Channel 1 (Clean), Channel 2 (British Crunch), or Channel 3 (Lead). |
| `PLEXI_MODE` | `OFF` / `ON` | `OFF` | bool | Reconfigures Blue/Red stages to classic 1960s Plexi dynamic clipping. |
| `STRUCTURE` | `LOW` / `HIGH` | `HIGH` | mode | Overall gain floor and harmonic saturation density. |
| `BOOST_SW` | `OFF` / `ON` | `OFF` | bool | Engages extra input gain boost stage for lead saturation. |
| `PRE_EQ` | `N` / `B1` / `B2` | `B1` | mode | Bright capacitor voicing (`N` = warm neutral; `B2` = aggressive shimmer). |
| `PREAMP_GAIN` | `0` - `100` | `65` | % | Channel input gain drive. |
| `BASS` | `0` - `100` | `54` | % | Tone stack low-end shelf. |
| `MIDDLE` | `0` - `100` | `68` | % | Tone stack chewy midrange focus (heart of Bogner vocal voice). |
| `TREBLE` | `0` - `100` | `56` | % | Tone stack treble edge. |
| `EXCURSION` | `TIGHT` / `MED` / `LOOSE`| `MED` | mode | Power amp speaker damping / cabinet low-end resonance control. |
| `POWER_CLASS` | `CLASS_AB` / `CLASS_A` | `CLASS_AB`| mode | High-headroom punch (`AB`) vs. spongy sweet compression (`A`). |
| `PRESENCE` | `0` - `100` | `58` | % | High-frequency feedback edge in the EL34 power amp. |

---

## 4. Factory Scene Presets

### Scene A: Green Sparkling Clean (Lush Boutique Headroom)
- **Concept:** Deep, glassy, three-dimensional clean with high dynamic headroom and warm low-end bloom.
- **Voicing:** `CHANNEL_MODE = GREEN`, `PRE_EQ = B1`, `PREAMP_GAIN = 38%`, `POWER_CLASS = CLASS_A`.
- **EQ & Power:** `BASS = 58%`, `MIDDLE = 52%`, `TREBLE = 64%`, `EXCURSION = MED`, `PRESENCE = 56%`.
- **Cabinet IR:** Bogner 4x12 Greenback G12M-25.
- **Space:** Dimension Stereo Chorus (`Mode 2`) + Warm Hall Reverb (`2.2 s`, `24%` mix).

### Scene B: Blue Channel Plexi Structure (Chewy British Crunch)
- **Concept:** Open, woody, touch-sensitive classic rock crunch that cleans up seamlessly with guitar volume roll-off.
- **Voicing:** `CHANNEL_MODE = BLUE`, `PLEXI_MODE = ON`, `STRUCTURE = LOW`, `PRE_EQ = B2`, `PREAMP_GAIN = 68%`.
- **EQ & Power:** `BASS = 52%`, `MIDDLE = 72%`, `TREBLE = 58%`, `EXCURSION = MED`, `PRESENCE = 54%`.
- **Cabinet IR:** Mixed Bogner 4x12 (Vintage 30 + Greenback).
- **Space:** Analog Tape Slapback (`135 ms`) + Studio Room Reverb.

### Scene C: Red Liquid Saturation Lead (Steve Vai Singing Sustain)
- **Concept:** Thick, creamy, harmonic-drenched solo voice with endless sustain, soft pick attack, and vocal upper-mids.
- **Voicing:** `CHANNEL_MODE = RED`, `STRUCTURE = HIGH`, `BOOST_SW = ON`, `PRE_EQ = N`, `PREAMP_GAIN = 78%`.
- **EQ & Power:** `BASS = 48%`, `MIDDLE = 76%`, `TREBLE = 52%`, `EXCURSION = LOOSE`, `POWER_CLASS = CLASS_A`.
- **Space:** Stereo Modulated Ping-Pong Delay (`dotted 8th`, `440 ms`, `32%` feedback) + Studio Plate Reverb.

### Scene D: Ecstasy Modern Tight Rhythm (Jerry Cantrell Heavy Crunch)
- **Concept:** Massive, low-tuned alternative rock / grunge rhythm wall with tight bottom tracking and roaring midrange grind.
- **Voicing:** `CHANNEL_MODE = RED`, `STRUCTURE = HIGH`, `BOOST_SW = OFF`, `PRE_EQ = B1`, `PREAMP_GAIN = 68%`.
- **EQ & Power:** `BASS = 54%`, `MIDDLE = 65%`, `TREBLE = 60%`, `EXCURSION = TIGHT`, `POWER_CLASS = CLASS_AB`.
- **Cabinet IR:** Bogner Uberkab 4x12 (Celestion V30 + G12T-75).

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (Green Clean) / Scene B (Blue Plexi Crunch).
- **Footswitch B:** Scene C (Red Liquid Lead).
- **Footswitch C:** Scene D (Modern Tight Rhythm) / Boost Toggle (+6 dB).
- **Knob 1 (GAIN):** Channel Preamp Gain / Red Cascade drive.
- **Knob 2 (EQ / MID):** Chewy Midrange Focus and Pre-EQ presence.
- **Knob 3 (REVERB / DELAY):** Stereo FX Loop mix.

### Tank-B Control Assignments
- Bassists looking for warm, authoritative British EL34 tube grind can run the `BLUE` channel (`PLEXI_MODE = ON`, `EXCURSION = TIGHT`) blended parallel with clean sub-bass below 150 Hz.

### Black Box Desktop Configuration
- **Stereo Dual-IR Split:** Load `Celestion V30` on Left Output and `G12M-25 Greenback` on Right Output for authentic Bogner 4x12 spatial projection.
- **MIDI CC #88:** Real-time switching of `BOOST_SW` and `PLEXI_MODE` across live performance passages.
