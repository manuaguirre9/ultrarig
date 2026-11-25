# Roland JC-120 Jazz Chorus Stereo Amplifier Routing Guide

This guide details the solid-state JFET high-headroom preamp, **Dual-Power-Amp Acoustic-Air Chorus** architecture, **MN3002 BBD modulation**, aluminum dust-cap **Silver Cone 2x12** speaker profiles, and preset configuration for the **Roland JC-120 Jazz Chorus** within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Circuit & Spatial Architecture of the 1975 Roland JC-120

Introduced in 1975, the **Roland JC-120 Jazz Chorus** remains the most celebrated solid-state electric guitar amplifier in recording history. Delivering immediate transient snap, crystal-clear headroom at high volumes, and the world's first integrated Bucket Brigade (BBD) stereo chorus, it forged the signature clean tones of **Andy Summers** (The Police), **Johnny Marr** (The Smiths), **Robert Smith** (The Cure), and **James Hetfield / Kirk Hammett** (Metallica ballads).

```
Instrument In
   │
   ▼
[ High-Headroom Solid-State JFET Preamp + Bright Switch + 3-Band EQ ]
   │
   ├─────────────────────────────────────────────► [ Left 60W Power Amp ] ──► [ Left 12" Silver Cone IR ] (100% PURE DRY)
   │
   └──► [ MN3002 BBD Delay Line & LFO Modulator ] ► [ Right 60W Power Amp ] ─► [ Right 12" Silver Cone IR ] (100% WET PITCH MOD)
```

### 1.1 The Secret of "Acoustic-Air" True Stereo Chorus

Conventional mono chorus pedals mix the dry signal and the pitch-modulated BBD signal *electronically* inside the pedal before sending the summed result to one speaker. This creates static phase cancellation notches (comb filtering) that can sound thin or metallic.

The **JC-120** solves this architecturally using a **Dual-Amp Split**:
1. **Left Channel (Dry Power Amp):** Outputs strictly the unmodulated dry signal through the Left 12" Silver Cone speaker.
2. **Right Channel (Wet BBD Power Amp):** Outputs strictly the modulated pitch-shifted BBD delay signal through the Right 12" Silver Cone speaker.
3. **Result:** The dry and modulated sound waves combine **acoustically in open air**! Zero electronic comb filtering occurs inside the amp, yielding immense, wide, glassy 3D spatial separation while keeping chord fundamentals tight and solid.

### 1.2 Solid-State Headroom & Silver Cone 12" Speakers

- **Zero Tube Rectifier Sag:** Discrete transistors and solid-state power rails refuse to compress on hard chord attacks, giving funk strums, jazz comping, and clean arpeggios razor-sharp immediacy.
- **Aluminum-Dome 12" Silver Cones:** Unlike traditional paper-cone guitar speakers that roll off steeply above $4.5\text{ kHz}$, the JC-120's original Roland drivers feature stiff aluminum center dust caps extending glassy clean sparkle smoothly up to $6.5\text{ kHz}$.

---

## 2. DSP Signal Chain & Processing Topology

```
Guitar / Bass In (Single-Coils / Active EMG Humbuckers / Hollowbody)
   │
   ▼
[ High-Z 1MΩ JFET Preamp Emulation + Bright Switch (+4 dB @ 4.5 kHz) ]
   │
   ▼
[ 3-Band Solid-State EQ (Bass / Middle / Treble) ]
   │
   ├──► [ Path L: Pure Dry 60W Solid-State Power Section ] ──► [ Left 12" Silver Cone IR ] ──► Stereo L
   │
   └──► [ Path R: MN3002 BBD Chorus / Manual Vibrato ] ──────► [ Right 12" Silver Cone IR ] ─► Stereo R
                                                                      │
[ Built-In Accutronics Spring Reverb + Optional Stereo Tape Delay ] ◄─┘
```

---

## 3. Parameter Specifications

| Parameter | Range | Default | Unit | Description |
| :--- | :--- | :--- | :--- | :--- |
| `BRIGHT_SW` | `OFF` / `ON` | `ON` | bool | Classic JC bright switch boosting crisp upper-treble chime. |
| `PREAMP_GAIN` | `0` - `100` | `32` | % | Input level (JC-120 stays dead-clean up to ~85%). |
| `BASS` | `0` - `100` | `52` | % | Solid-state low-end fullness without tube flub. |
| `MIDDLE` | `0` - `100` | `46` | % | Midrange focus (lower slightly for scooped 80s shimmer). |
| `TREBLE` | `0` - `100` | `64` | % | Crystalline top-end clarity. |
| `CHORUS_MODE` | `OFF` / `FIXED_CHORUS` / `MANUAL_VIB`| `FIXED_CHORUS`| mode | Classic fixed-rate JC-120 chorus OR adjustable rate/depth Vibrato. |
| `VIBRATO_RATE` | `0.2` - `8.0` | `0.8` | Hz | LFO speed when Manual Vibrato mode is selected. |
| `VIBRATO_DEPTH`| `0` - `100` | `60` | % | Pitch modulation depth in Manual mode. |
| `REVERB_MIX` | `0` - `100` | `22` | % | Internal clean spring reverb tank blend. |
| `STEREO_WIDTH` | `0` - `100` | `100` | % | Separation between Dry Left Silver Cone and Wet Right Silver Cone. |

---

## 4. Factory Scene Presets

### Scene A: 80s Solid-State Crystal Clean (Pure Unmodulated JC-120)
- **Concept:** Ultra-fast, glassy, hi-fi clean guitar tone engineered for studio funk comping, neo-soul, and crisp jazz chord melodies.
- **Preamp & EQ:** `BRIGHT_SW = ON`, `PREAMP_GAIN = 28%`, `BASS = 54%`, `MIDDLE = 52%`, `TREBLE = 62%`.
- **Modulation:** `CHORUS_MODE = OFF` (Pure dual Silver Cone dry stereo).
- **Dynamics & Space:** Fast optical limiter (`2.2:1`) + clean Spring Reverb (`1.6 s`, `18%` mix).

### Scene B: True Stereo Acoustic-Air Chorus (Fixed Chorus Mode)
- **Concept:** The unmistakable 1980s stereo chorus signature—wide, lush, and completely free of mono comb-filter phase cancellations.
- **Preamp & Mod:** `BRIGHT_SW = ON`, `CHORUS_MODE = FIXED_CHORUS` (Left = 100% Dry Silver Cone; Right = 100% MN3002 BBD Modulated Silver Cone), `STEREO_WIDTH = 100%`.
- **Space:** Warm Studio Plate Reverb (`2.0 s`, `20%` mix).

### Scene C: Master of Puppets Ballad Clean (Metallica Clean Intro)
- **Concept:** Cavernous, shimmering arpeggio clean tone paired with active/passive humbuckers and mild midrange scoop (*Fade to Black*, *Sanitarium*, *One*).
- **Preamp & EQ:** `BRIGHT_SW = ON`, `BASS = 58%`, `MIDDLE = 36%`, `TREBLE = 68%`, `CHORUS_MODE = FIXED_CHORUS`.
- **Space:** Subtle Analog Delay (`380 ms`, `20%` feedback) + Deep Hall Reverb (`2.8 s`, `28%` mix).

### Scene D: Johnny Marr / Andy Summers Vibrato Swirl (Lush Modulated)
- **Concept:** Hypnotic, swirling chorus-vibrato texture designed for sparkling arpeggios and rhythmic 8th-note delay patterns.
- **Modulation:** `CHORUS_MODE = MANUAL_VIB`, `VIBRATO_RATE = 1.6 Hz`, `VIBRATO_DEPTH = 68%`.
- **Space:** Modulated Dotted-8th Tape Delay (`375 ms`, `30%` feedback) + Spring Tank.

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (Crystal Clean) / Scene B (True Stereo Fixed Chorus).
- **Footswitch B:** Scene C (Metallica Ballad Clean).
- **Footswitch C:** Scene D (Johnny Marr Swirl) / Chorus Bypass.
- **Knob 1 (EQ):** Midrange Focus (turn down for 80s ballad scoop, up for jazz warmth).
- **Knob 2 (MOD FX):** Manual Vibrato Rate & Depth.
- **Knob 3 (REVERB):** Built-in Spring Tank & Hall ambient blend.

### Tank-B Control Assignments
- Bassists seeking bright, punchy 1980s slap-funk or melodic New Wave bass (Peter Hook / Joy Division / Duran Duran style!) can run the JC-120 Fixed Chorus above a $160\text{ Hz}$ mono crossover, preserving rock-solid sub-bass while projecting lush stereo Silver Cone shimmer!

### Black Box Desktop Configuration
- **True Stereo Direct Outputs (L + R):** Essential for experiencing the JC-120's defining Dry-Left / Wet-Right **acoustic-air summing** across stereo studio monitors or live stereo PA channels without mono collapse.
