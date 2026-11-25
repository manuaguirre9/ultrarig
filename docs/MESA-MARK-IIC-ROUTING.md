# Mesa/Boogie Mark IIC+ & IV Preamp Routing & 5-Band EQ Guide

This guide details the iconic **Pre-Distortion Tonestack**, **Post-Distortion 5-Band Graphic Equalizer ("V-Scoop")**, **Simul-Class Hybrid Power Section**, and practical preset configuration for the **Mesa/Boogie Mark IIC+** and **Mark IV** within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Circuit Architecture of the Mesa/Boogie Mark Series

Developed by Randall Smith in Petaluma, California, the Mark IIC+ (1984) and Mark IV represent the pinnacle of cascading American high-gain tube engineering. Their unmistakable voice—championed by **Carlos Santana**, **James Hetfield** (*Master of Puppets*), and **John Petrucci**—stems from a radically different signal layout compared to British amplifiers or the later Dual Rectifier.

```
Instrument In
   │
   ▼
[ V1A Input Stage ] ──► [ Pull Bright Switch ]
   │
   ▼
[ PRE-DISTORTION Fender-Style Passive Tonestack (Treble / Bass / Mid) ] <=== Must Keep Rotary Bass LOW!
   │
   ├── (Clean Rhythm Channel) ─────────────────────────────────────────────────────┐
   │                                                                               │
   ▼                                                                               │
[ V3 & V4 Cascading Lead Drive Stages ] (Extreme High-Gain Harmonic Compression)   │
   │                                                                               │
   ▼                                                                               │
[ POST-DISTORTION 5-Band LC Graphic EQ (80 / 240 / 750 / 2200 / 6600 Hz) ] ◄───────┘
   │ (The Iconic "V-Scoop" Re-Injects Massive Tight Sub-Bass After Clipping)
   ▼
[ Simul-Class Hybrid Power Amp: 2x EL34 (Class A) + 2x 6L6 (Class AB) ] ◄── [ Pull Deep / Presence ]
   │
   ▼
[ 4x12 Celestion Vintage 30 / EVM-12L Speaker IR Convolution ] ──► Stereo Output
```

### 1.1 The Pre-Distortion Tonestack Secret

In British designs (Marshall JCM800, Friedman, Soldano), the Treble/Middle/Bass tonestack sits *after* all distortion tubes. In the **Mark IIC+**, the rotary Bass, Middle, and Treble knobs are located **before** the Lead Drive cascade:
- **Rotary Bass Trap:** Turning the rotary **Bass** knob above 2 or 3 ($> 25\%$) injects massive low-frequency energy *directly into the high-gain clipping stages*, resulting in uncontrollable muddy flub and blocking distortion. Keeping rotary Bass low ($10\% - 20\%$) yields razor-sharp palm mutes.
- **Rotary Treble as Gain & Bite:** Because Treble drives the input into the Lead stages, setting Treble high ($70\% - 85\%$) tightens the distortion grain, boosts upper harmonics, and increases pick-attack immediacy.

### 1.2 The Post-Distortion 5-Band Graphic EQ ("V-Scoop")

To restore massive chest-pounding low end without muddying the preamp distortion, Mesa placed an active 5-band LC gyrator graphic equalizer **after** all Lead gain stages:
- **80 Hz:** Re-injects thunderous, ultra-tight sub-bass thump.
- **240 Hz:** Controls lower-mid cabinet warmth or boxiness.
- **750 Hz:** The crucial "honky" nasal midrange pivot; scooping this band deeply creates the iconic *Master of Puppets* aggressive thrash rhythm scoop, while leaving it near flat or slightly boosted gives John Petrucci's vocal liquid lead sustain.
- **2200 Hz & 6600 Hz:** Restore cutting pick articulation and sparkling top-end air.

### 1.3 Simul-Class Hybrid Power Stage

Unlike standard all-6L6 or all-EL34 output sections, **Simul-Class** runs two distinct tube architectures simultaneously:
- Inner pair (**EL34 in Class A / Triode**): Provides warm, creamy midrange harmonic compression.
- Outer pair (**6L6 in Class AB / Pentode**): Provides huge dynamic headroom, tight bottom-end punch, and sparkling treble snap.

---

## 2. DSP Signal Chain & Processing Topology

```
Guitar In (High-Output Humbuckers / Single-Coils)
   │
   ▼
[ Fast Downward Noise Gate ] (Tames high-gain Lead Drive hiss)
   │
   ▼
[ Pre-Distortion Tonestack (Rotary Volume 1 / Treble / Bass / Mid) ]
   │
   ▼
[ Lead Drive Harmonic Cascade (V3/V4 Asymmetric Saturation) ]
   │
   ▼
[ Post-Distortion 5-Band Graphic EQ (80 Hz | 240 Hz | 750 Hz | 2200 Hz | 6600 Hz) ]
   │
   ▼
[ Simul-Class Hybrid Power Amp (6L6 + EL34) + Pull Deep & Presence ]
   │
   ▼
[ Speaker IR Convolution: Mesa Traditional 4x12 (V30) OR Thiele 1x12 (EVM-12L) ]
   │
   ▼
[ Stereo Modulated Tape Delay & Studio Room Reverb ] ──► Stereo Output
```

---

## 3. Parameter Specifications

| Parameter | Range | Default | Unit | Description |
| :--- | :--- | :--- | :--- | :--- |
| `CHANNEL_MODE`| `RHYTHM_CLEAN` / `LEAD_IIC` | `LEAD_IIC` | mode | Clean Rhythm vs. Cascaded High-Gain Lead channel. |
| `VOLUME_1` | `0` - `100` | `72` | % | Input gain feeding V1 & Pre-Distortion Tonestack (acts as primary drive control). |
| `ROTARY_BASS` | `0` - `100` | `18` | % | Pre-distortion bass (keep below 25% for tight metal rhythm tracking). |
| `ROTARY_MID` | `0` - `100` | `45` | % | Pre-distortion midrange focus. |
| `ROTARY_TREBLE`| `0` - `100` | `76` | % | Pre-distortion treble (acts as harmonic tightness & gain booster). |
| `LEAD_DRIVE` | `0` - `100` | `75` | % | Saturation amount of the V3/V4 Lead overdrive cascade. |
| `GEQ_80HZ` | `-12` to `+12`| `+6.0` | dB | Post-distortion sub-bass punch slider. |
| `GEQ_240HZ` | `-12` to `+12`| `+1.5` | dB | Post-distortion low-mid warmth slider. |
| `GEQ_750HZ` | `-12` to `+12`| `-8.0` | dB | Post-distortion nasal midrange pivot (scoop for thrash; flat/boost for lead). |
| `GEQ_2200HZ` | `-12` to `+12`| `+4.5` | dB | Post-distortion presence and pick-attack articulation slider. |
| `GEQ_6600HZ` | `-12` to `+12`| `+3.5` | dB | Post-distortion crystalline air and sizzle slider. |
| `SIMUL_CLASS` | `ALL_6L6` / `SIMUL_CLASS` | `SIMUL_CLASS` | mode | Hybrid 6L6 + EL34 output stage emulation. |

---

## 4. Factory Scene Presets

### Scene A: Santana Liquid Mark Lead (Abraxas / Supernatural Sustain)
- **Concept:** Thick, singing, vocal midrange sustain with zero harsh fizz and responsive harmonic feedback.
- **Pre-EQ & Drive:** `CHANNEL_MODE = LEAD_IIC`, `VOLUME_1 = 68%`, `ROTARY_BASS = 28%`, `ROTARY_MID = 68%`, `ROTARY_TREBLE = 62%`, `LEAD_DRIVE = 64%`.
- **5-Band GEQ:** Bypassed (or gentle mid-push: `750 Hz = +2.5 dB`, `240 Hz = +2 dB`).
- **Speaker IR:** Thiele 1x12 Electro-Voice EVM-12L.
- **Space:** Warm Studio Plate Reverb (`2.0 s`, `22%` mix).

### Scene B: 80s Thrash Master of Puppets (Classic V-Scoop Rhythm)
- **Concept:** The benchmark 1986 Bay Area thrash rhythm sound: chainsaw-tight palm mutes, cavernous scooped mids, and razor-sharp attack.
- **Pre-EQ & Drive:** `CHANNEL_MODE = LEAD_IIC`, `VOLUME_1 = 78%`, `ROTARY_BASS = 14%`, `ROTARY_MID = 35%`, `ROTARY_TREBLE = 82%`, `LEAD_DRIVE = 76%`.
- **5-Band GEQ ("V"):** `80 Hz = +7.5 dB`, `240 Hz = +1.0 dB`, `750 Hz = -11.0 dB`, `2200 Hz = +5.5 dB`, `6600 Hz = +4.0 dB`.
- **Speaker IR:** Mesa 4x12 Recto Traditional (Celestion Vintage 30).
- **Space:** Dry & tight (Noise Gate at `-30 dBFS`).

### Scene C: Dream Theater Petrucci Singing Lead (Mark IIC+ / IV)
- **Concept:** Ultra-articulate progressive metal lead combining blistering speed tracking with creamy, liquid melodic sustain.
- **Pre-EQ & Drive:** `CHANNEL_MODE = LEAD_IIC`, `VOLUME_1 = 75%`, `ROTARY_BASS = 20%`, `ROTARY_MID = 52%`, `ROTARY_TREBLE = 78%`, `LEAD_DRIVE = 82%`.
- **5-Band GEQ (Smooth Lead):** `80 Hz = +4.5 dB`, `240 Hz = +2.0 dB`, `750 Hz = -3.0 dB`, `2200 Hz = +3.5 dB`, `6600 Hz = +2.0 dB`.
- **Space:** Stereo Modulated Ping-Pong Delay (`dotted 8th`, `420 ms`, `30%` feedback) + Hall Reverb.

### Scene D: Jazz Fusion Clean Rhythm (Pristine Fender-Roots Headroom)
- **Concept:** Sparkling, hi-fi clean tone with massive dynamic headroom and crystalline chord separation.
- **Pre-EQ & Drive:** `CHANNEL_MODE = RHYTHM_CLEAN`, Pull Bright ON, `VOLUME_1 = 42%`, `ROTARY_BASS = 48%`, `ROTARY_MID = 55%`, `ROTARY_TREBLE = 64%`.
- **5-Band GEQ:** Gentle Hi-Fi smile (`80 Hz = +2 dB`, `6600 Hz = +2.5 dB`).
- **Space:** Dimension Stereo Chorus + Natural Spring Reverb (`1.8 s`, `20%` mix).

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (Santana Liquid Lead) / Scene B (80s Thrash V-Scoop).
- **Footswitch B:** Scene C (Petrucci Singing Lead).
- **Footswitch C:** Scene D (Clean Rhythm) / 5-Band Graphic EQ Toggle (Instant Mid-Boost for Solos).
- **Knob 1 (GAIN):** Preamp Volume 1 / Lead Drive saturation.
- **Knob 2 (EQ / SCOOP):** 750 Hz Graphic EQ Midrange Pivot slider (turn left for Thrash V-Scoop, right for Singing Solo Mid-Push).
- **Knob 3 (REVERB / DELAY):** Stereo Delay & Room Ambience level.

### Tank-B Control Assignments
- Bassists can utilize the `RHYTHM_CLEAN` channel paired with the 5-band GEQ (`80 Hz = +6 dB`, `750 Hz = -4 dB`, `2200 Hz = +4 dB`) and `SIMUL_CLASS` drive for punchy, studio-grade progressive rock bass tones (inspired by John Myung).

### Black Box Desktop Configuration
- **MIDI CC #86:** Dedicated footswitch trigger toggling the Post-Distortion 5-Band Graphic EQ on/off cleanly without volume spikes.
- **Dual Cabinet IR Slot:** Combine Mesa 4x12 V30 (punch) with Thiele 1x12 EVM-12L (headroom) for immense stage projection.
