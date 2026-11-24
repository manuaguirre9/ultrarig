# Dynamic Ducking Delay & Gated Reverb Modeling Guide

This guide details the algorithmic principles, sidechain envelope detection, attenuation ballistics, and preset design for **Dynamic Ducking Delay** and **Non-Linear Gated Reverb** within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Principles of Dynamic Ducking and Non-Linear Gating

In dense musical arrangements and high-speed soloing, heavy delay repeats and long ambient reverb tails often compete with the dry instrument signal, causing frequency masking, rhythmic clutter, and loss of note intelligibility.

```
Dry Instrument In ─────────────────────────────────────────────────────────────► [ Summing Node ] ──► Output
       │                                                                                ▲
       ├───► [ Sidechain Envelope Follower ] ──► [ Inverted Dynamic VCA Gain Mod ]      │
       │                                                │                               │
       ▼                                                ▼                               │
[ Delay Buffer / Reverb Generator ] ────────────► [ VCA Attenuator / Non-Linear Gate ] ─┘
```

### 1.1 Dynamic Ducking Architecture

Instead of a static mix level, a dynamic ducking system monitors the incoming dry guitar signal via a dedicated sidechain detector:
1. **Active Playing (Attack Phase):** While the guitarist is playing fast notes or rhythm patterns, the detector activates and attenuates (ducks) the wet delay repeats and reverb tail by a user-specified depth (typically $-6\text{ dB}$ to $-24\text{ dB}$).
2. **Phrase Pauses (Release / Bloom Phase):** As soon as the player stops or holds a sustained note, the envelope follower drops below the threshold and the VCA smoothly restores the wet signal to $0\text{ dB}$, allowing the ambient delay trails and rich reverb tails to "bloom" forward majestically into the empty space.

### 1.2 Non-Linear Gated Reverb Architecture

Pioneered in the early 1980s (most famously by Peter Gabriel, Phil Collins, and producer Hugh Padgham on the SSL 4000 Talkback channel), **Gated Reverb** creates an unnatural, explosive sense of size without acoustic mud:
1. A dense, high-energy room or plate reverb is generated.
2. A fast-acting non-linear noise gate monitors the reverb output.
3. The gate remains fully open during a precise **Hold Time** ($50\text{ ms}$ to $350\text{ ms}$), preserving a flat, explosive acoustic burst.
4. Once the hold timer elapses, an ultra-fast **Release Clamp** ($5\text{ ms}$ to $20\text{ ms}$) cuts off the tail instantly, creating total silence between rhythmic hits.

---

## 2. DSP Signal Chain & Topology

```
Input Audio (Guitar / Bass / Keys)
   │
   ├───► [ Dry Direct Signal Bus ] ────────────────────────────────────────────┐
   │                                                                           │
   ├───► [ Sidechain Envelope Detector ]                                       │
   │           │ (Threshold, Attack, Release, Ducking Ratio)                  │
   │           ▼                                                               │
   │     [ Gain Computer: Ducking Control Signal ]                             │
   │           │                                                               │
   ▼           ▼                                                               │
[ Delay Line & Reverb Matrix ] ──► [ Dynamic VCA Attenuator ]                  │
   │                                     │                                     │
   │                                     ├──► (Gated Mode: Hold & Hard Clamp)  │
   │                                     ▼                                     │
   └─────────────────────────────► [ Wet Stereo Bus ] ─────────────────────────┴──► Master Output
```

---

## 3. Parameter Specifications

| Parameter | Range | Default | Unit | Description |
| :--- | :--- | :--- | :--- | :--- |
| `EFFECT_MODE` | `DUCKED_DELAY` / `DUCKED_REVERB` / `GATED_REVERB` | `DUCKED_DELAY` | mode | Processing topology. |
| `DUCK_THRESHOLD`| `-40.0` to `0.0` | `-22.0` | dBFS | Dry signal level required to trigger ducking attenuation. |
| `DUCK_DEPTH` | `-36.0` to `0.0` | `-14.0` | dB | Amount of wet signal reduction applied while playing. |
| `DUCK_ATTACK` | `1.0` - `50.0` | `4.0` | ms | Speed at which ducking attenuation engages upon pick attack. |
| `DUCK_RELEASE`| `40` - `800` | `180` | ms | Speed at which delay/reverb bloom swells forward after playing stops. |
| `DELAY_TIME` | `10` - `2000` | `420` | ms | Base delay time (supports tempo sync: 1/4, dotted-8th, triplets). |
| `DELAY_FEEDBACK`| `0` - `100` | `48` | % | Number of delay repeat recirculations. |
| `GATE_HOLD` | `20` - `500` | `180` | ms | Duration the gated reverb tail remains wide open before cutoff. |
| `GATE_RELEASE`| `2.0` - `40.0` | `8.0` | ms | Hard cutoff speed of the non-linear gate clamp. |
| `MIX_WET_DRY` | `0` - `100` | `45` | % | Balance between dry signal and fully un-ducked wet space. |

---

## 4. Factory Scene Presets

### Scene A: High-Speed Solo Ducked Delay (80s Shredder Clarity)
- **Concept:** Crystal-clear fast solo articulation where delay repeats duck out of the way during blistering runs, then bloom immediately on sustained notes.
- **Ducking:** `EFFECT_MODE = DUCKED_DELAY`, `DUCK_THRESHOLD = -20 dBFS`, `DUCK_DEPTH = -16 dB`, `DUCK_RELEASE = 140 ms`.
- **Delay:** `DELAY_TIME = dotted 8th (375 ms at 120 BPM)`, `DELAY_FEEDBACK = 50%`.
- **Mix:** `MIX_WET_DRY = 50%` (Zero clutter during fast runs; rich repeats when holding vibrato).

### Scene B: Ambient Blooming Reverb (Post-Rock & Worship Swell)
- **Concept:** Massive, cavernous hall reverb that ducks during chord strums to avoid mud, then billows into an immense ambient cloud in between chords.
- **Ducking:** `EFFECT_MODE = DUCKED_REVERB`, `DUCK_THRESHOLD = -24 dBFS`, `DUCK_DEPTH = -18 dB`, `DUCK_RELEASE = 350 ms`.
- **Reverb:** Cathedral Hall (`8.5 s` decay time, `45 ms` pre-delay, low-damping at 5 kHz).
- **Mix:** `MIX_WET_DRY = 60%`.

### Scene C: 80s Studio Gated Reverb (Percussive Power Stabs)
- **Concept:** Iconic non-linear gated space that delivers explosive room ambience on guitar chugs or snare hits, cut off dead with surgical precision.
- **Gating:** `EFFECT_MODE = GATED_REVERB`, `GATE_HOLD = 220 ms`, `GATE_RELEASE = 6.0 ms`.
- **Reverb:** Dense Acoustic Stone Room (`2.8 s` base decay before cutoff).
- **Mix:** `MIX_WET_DRY = 45%`.

### Scene D: Rhythmic Clean Ping-Pong Ducking (Funk & Pop Comping)
- **Concept:** Stereo alternating ping-pong delay ducked during tight rhythm comping, splashing outward into wide stereo panorama on phrase breaks.
- **Ducking:** `EFFECT_MODE = DUCKED_DELAY`, `DUCK_THRESHOLD = -18 dBFS`, `DUCK_DEPTH = -12 dB`, `DUCK_RELEASE = 160 ms`.
- **Delay:** Stereo Ping-Pong (`Left = 1/8 note`, `Right = dotted 1/8 note`, `FEEDBACK = 42%`).
- **Mix:** `MIX_WET_DRY = 40%`.

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (High-Speed Solo Ducked Delay) / Scene B (Ambient Blooming Reverb).
- **Footswitch B:** Scene C (80s Gated Reverb).
- **Footswitch C:** Scene D (Rhythmic Ping-Pong) / Tap Tempo.
- **Knob 1 (DELAY):** Delay Feedback and Ducking Depth.
- **Knob 2 (REVERB):** Decay Time / Gated Hold Duration.
- **Knob 3 (BLEND):** Wet/Dry parallel mix.

### Tank-B Control Assignments
- Ducked delay is invaluable for bass soloists and modern slap bassists: repeats duck by -18 dB while slapping, keeping the low-end groove tight and articulate, while blooming into ambient space on melodic fills.

### Black Box Desktop Configuration
- **MIDI CC #68:** Real-time Ducking Depth adjustment via expression pedal (from 0 dB static mix to -24 dB deep ducking).
- **Stereo TRS Output:** Provides full stereo separation for ping-pong ducked repeats and wide gated room reflections.
