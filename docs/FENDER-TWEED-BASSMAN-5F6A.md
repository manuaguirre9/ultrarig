# Fender Tweed Bassman 5F6-A (1959 4x10 Tube Combo) Routing Guide

This guide details the landmark **1959 5F6-A** circuit architecture, interactive **Bright/Normal channel jumping**, **cathode-follower driven midrange tonestack**, **5AR4 tube rectifier sag**, and practical preset configuration for the **Fender Tweed Bassman** within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Circuit Heritage & Topology of the 1959 5F6-A Bassman

Originally engineered by Leo Fender's team in Fullerton, California to amplify the Precision Bass, the 1958–1960 **5F6-A Tweed Bassman** quickly became the blueprint for modern rock guitar amplification. Jim Marshall famously used the exact 5F6-A schematic in 1962 to build the JTM45, and boutique builders from Soldano to Bogner still trace their midrange gain structures back to this circuit.

```
Instrument In
   │
   ├──► [ Bright Channel (12AY7 V1A) ] ───► [ Bright Volume ] ──┐
   │                                                           ├──► [ Shared 12AX7 Gain Stage (V2A) ]
   └──► [ Normal Channel (12AY7 V1B) ] ───► [ Normal Volume ] ─┘             │
                                                                             ▼
                                                        [ 12AX7 Cathode Follower (V2B) ]
                                                                             │ (Zero Tonestack Loading)
                                                                             ▼
                                                        [ Passive Tonestack (Bass / Mid / Treble) ]
                                                                             │
                                                                             ▼
[ 4x10 Open-Back Jensen P10R Alnico IR ] ◄── [ 2x 5881 Push-Pull Power Amp + 5AR4 Rectifier Sag + Presence ]
```

### 1.1 Interactive Channels & Cathode-Follower Tonestack

1. **Channel Jumping (Bright + Normal Linked):** Unlike later dual-channel amps with hard relays, both channels sum passively via $270\text{ k}\Omega$ mixing resistors. Blending **Normal Volume** (warm, woody bottom weight) with **Bright Volume** (sparkling glassy chime) allows sculptable harmonic balance directly ahead of the V2 saturation stage.
2. **Cathode Follower Midrange Authority:** Later Blackface Fender amps drove their tone stacks straight off a tube plate, causing severe mid-scoop insertion loss. The 5F6-A buffers its tone stack through a **12AX7 cathode follower**—delivering low output impedance, rich assertive midrange bark, and singing, touch-sensitive compression.
3. **5AR4 / GZ34 Rectifier Sag & Presence Control:** High-output chords momentarily pull down DC power rails across the vacuum rectifier, softening sharp pick attacks before blooming into sustain. The global **Presence** knob controls high-frequency negative feedback right in the phase inverter.

### 1.2 Open-Back 4x10 Jensen P10R Speaker Character

Four 10-inch **Jensen P10R Alnico** speakers mounted in an open-back finger-jointed pine cabinet produce rapid transient snap without 12-inch speaker flub, yet exhibit huge low-mid acoustic warmth when coupled together.

---

## 2. DSP Signal Chain & Processing Topology

```
Guitar / Bass In (Single-Coils / P90s / PAF Humbuckers)
   │
   ▼
[ Channel Linking Matrix: Bright Only / Normal Only / Jumped Parallel Blend ]
   │
   ▼
[ V1/V2 12AY7 + 12AX7 Cascade & Cathode-Follower Saturation ]
   │
   ▼
[ Passive 3-Band Tweed Tonestack (Bass / Middle / Treble) ]
   │
   ▼
[ 2x 5881 / 6L6 Power Section + 5AR4 Tube Rectifier Sag + Presence NFB ]
   │
   ▼
[ 4x10 Open-Back Jensen P10R Alnico Speaker IR Convolution ]
   │
   ▼
[ Vintage Echoplex Slapback & Outboard 6G15 Spring Reverb ] ──► Stereo Output
```

---

## 3. Parameter Specifications

| Parameter | Range | Default | Unit | Description |
| :--- | :--- | :--- | :--- | :--- |
| `CHANNEL_MODE` | `BRIGHT` / `NORMAL` / `JUMPED` | `JUMPED` | mode | Selects single channel or parallel internal patch-cable jumping. |
| `BRIGHT_VOL` | `0` - `100` | `58` | % | Input gain & high-frequency sparkle on the Bright channel. |
| `NORMAL_VOL` | `0` - `100` | `52` | % | Input gain & woody low-mid girth on the Normal channel. |
| `BASS` | `0` - `100` | `46` | % | Tone stack bottom end (keep moderate when pushing high power drive). |
| `MIDDLE` | `0` - `100` | `64` | % | Cathode-follower midrange punch and vocal thickness. |
| `TREBLE` | `0` - `100` | `58` | % | Tone stack top-end snap and chime. |
| `PRESENCE` | `0` - `100` | `55` | % | Negative feedback high-frequency edge in power amp phase inverter. |
| `RECTIFIER_SAG`| `0` - `100` | `60` | % | 5AR4 vacuum rectifier voltage droop compression under transients. |
| `POWER_DRIVE` | `0` - `100` | `62` | % | 2x 5881 output tube push-pull clipping and pine-cab bloom. |
| `CAB_IR` | `JENSEN_P10R_410` / `CELESTION_10` | `JENSEN_P10R_410`| file | 4x10 open-back speaker impulse response. |

---

## 4. Factory Scene Presets

### Scene A: Classic Tweed Clean & Woody Snap (Country / Jump Blues)
- **Concept:** Big, punchy, warm 1950s clean tone with percussive 4x10 Alnico snap and subtle organic compression.
- **Voicing:** `CHANNEL_MODE = JUMPED`, `BRIGHT_VOL = 38%`, `NORMAL_VOL = 34%`, `POWER_DRIVE = 35%`, `RECTIFIER_SAG = 40%`.
- **EQ & Presence:** `BASS = 52%`, `MIDDLE = 56%`, `TREBLE = 62%`, `PRESENCE = 54%`.
- **Space:** Echoplex Slapback (`115 ms`) + Subtle Spring Reverb (`1.6 s`, `18%` mix).

### Scene B: Buddy Guy / Stevie Ray Pushed Edge (Chicago & Texas Blues)
- **Concept:** Expressive edge-of-breakup where soft fingerpicking shines cleanly while heavy Stratocaster digs erupt into gritty 5881 harmonic bark.
- **Voicing:** `CHANNEL_MODE = BRIGHT`, `BRIGHT_VOL = 65%`, `POWER_DRIVE = 62%`, `RECTIFIER_SAG = 65%`.
- **EQ & Presence:** `BASS = 44%`, `MIDDLE = 68%`, `TREBLE = 64%`, `PRESENCE = 60%`.
- **Space:** Vintage 6G15 Spring Tank (`2.0 s`, `22%` mix).

### Scene C: Cranked 4x10 Blues Crunch (Pre-JTM45 British/American Bridge)
- **Concept:** Massive, singing, classic-rock overdrive achieved by jumping both channels high and saturating the cathode follower and 5881 power section.
- **Voicing:** `CHANNEL_MODE = JUMPED`, `BRIGHT_VOL = 75%`, `NORMAL_VOL = 68%`, `POWER_DRIVE = 78%`, `RECTIFIER_SAG = 70%`.
- **EQ & Presence:** `BASS = 38%`, `MIDDLE = 74%`, `TREBLE = 58%`, `PRESENCE = 52%`.
- **Space:** Warm Studio Room (`1.4 s`, `16%` mix).

### Scene D: Billy Gibbons / Neil Young Tweed Meltdown (Fuzz-Like Sag)
- **Concept:** Pushing the 5F6-A past its limits into sputtering, molten, fuzz-drenched vintage overdrive with extreme rectifier droop.
- **Voicing:** `CHANNEL_MODE = JUMPED`, `BRIGHT_VOL = 90%`, `NORMAL_VOL = 85%`, `POWER_DRIVE = 92%`, `RECTIFIER_SAG = 88%`.
- **EQ & Presence:** `BASS = 32%` (tightens breakup), `MIDDLE = 80%`, `TREBLE = 66%`, `PRESENCE = 72%`.
- **Space:** Analog Tape Echo (`380 ms`, `30%` feedback) + Spring Tank.

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (Classic Tweed Clean) / Scene B (Buddy Guy Edge).
- **Footswitch B:** Scene C (Cranked 4x10 Crunch).
- **Footswitch C:** Scene D (Tweed Meltdown Fuzz) / Boost (+4 dB).
- **Knob 1 (GAIN):** Combined Bright/Normal Input Volume Drive.
- **Knob 2 (EQ / MID):** Cathode-Follower Midrange Presence.
- **Knob 3 (REVERB):** Slapback & Spring Reverb ambient mix.

### Tank-B Control Assignments
- **Returning to its Roots:** Built originally as a bass amp! Bassists using flatwound or roundwound P-Basses with `CHANNEL_MODE = NORMAL`, `NORMAL_VOL = 55%`, and `BASS = 68%` unlock legendary 1960s motown, blues, and classic-rock bass growl through 4x10 Jensen Alnico IRs.

### Black Box Desktop Configuration
- **Dual-Channel Channel Mixing:** Assign Bright Volume and Normal Volume independently to MIDI CCs so you can sweep from dark woody warmth to snappy tweed chime on the fly.
- **Expression Pedal 1:** Morph smoothly between `POWER_DRIVE` levels or control outboard 6G15 Spring Reverb Dwell!
