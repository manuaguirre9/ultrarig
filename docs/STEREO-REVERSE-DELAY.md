# Stereo Reverse Delay & Transient-Synced Buffer Modeling Guide

This guide details the circular buffer architecture, windowing crossfades, transient-aligned buffer swapping, and practical preset configuration for **Real-Time Stereo Reverse Delay** within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Principles & Buffer Architecture of Reverse Delay

Originally crafted in 1966 recording studios by physically flipping quarter-inch analog tape reels upside down (heard on The Beatles' *I'm Only Sleeping* and Jimi Hendrix's *Are You Experienced?*), **Reverse Delay** captures fixed segments of incoming audio and plays them backwards in real time.

```
Audio In ──► [ Write Pointer (+1 step) ] ──► [ Dual-Segment Ring Buffer (A / B) ]
                                                        │
                      ┌─────────────────────────────────┴─────────────────────────────────┐
                      ▼                                                                   ▼
         [ Read Pointer Left (-1 step) ]                                   [ Read Pointer Right (-1 step) ]
         (Hann Crossfade Window: 20 ms)                                    (Offset / Ping-Pong / 2x Crystal)
                      │                                                                   │
                      ▼                                                                   ▼
             [ High-Cut & Tape Damping ] ──► [ Feedback Regeneration Matrix ] ──► Stereo Wet Out
```

### 1.1 Dual-Buffer Windowing & Anti-Click Crossfading

Reading a circular buffer backwards creates a fundamental signal-processing challenge: when the read pointer reaches the start of a slice and jumps backward to the end of the newest recorded segment, an abrupt waveform discontinuity occurs, causing loud digital clicks and pops.

UltraRig avoids this via **Overlapping Windowed Crossfading**:
1. Two alternating read windows (Window A and Window B) read backwards through consecutive buffer frames.
2. During the final $15\text{ ms} - 30\text{ ms}$ of Frame A, a raised-cosine (Hann) crossfade transitions smoothly into Frame B.
3. Because the crossfade tapers amplitude smoothly to zero at slice boundaries, mechanical tape splice clicks are eliminated cleanly.

### 1.2 Transient-Synced Phrase Alignment

A common frustration with fixed-timer reverse delays is unpredictable chopping—notes frequently cut off mid-decay. UltraRig includes **Transient-Triggered Boundary Alignment**:
- An envelope flux detector monitors pick attacks.
- When **Transient Sync** is enabled, the buffer slice dynamically aligns its inversion boundary to the player's phrasing or locks tightly to Tap Tempo subdivisions (Quarter, Dotted-Eighth, or Triplets), ensuring every reversed swell lands musically in time.

### 1.3 Reverse Crystal Pitch Shifting (+12 st)

By advancing the reverse read pointer at $2.0\times$ speed (via cubic Hermite interpolation) while recording at $1.0\times$ speed, UltraRig produces ascending **Reverse Octave Crystal** reflections (inspired by Eventide and Strymon ambient algorithms) that shimmer upward behind chords.

---

## 2. DSP Signal Chain & Topology

```
Guitar / Bass In ───────────────────► [ Direct Dry Signal Level ] ─────────────────────────────┐
      │                                                                                        │
      ▼                                                                                        │
[ Transient Attack Detector ] ──► (Triggers Frame Swap / Tempo Sync Quantize)                  │
      │                                                                                        │
      ▼                                                                                        │
[ Ring Buffer (100 ms - 2000 ms) + Dual Inverted Read Pointers ]                               │
      │ (Optional 2x Speed / +12 st Crystal Pitch Shift)                                       │
      ▼                                                                                        │
[ Hann Anti-Click Crossfade Engine (20 ms Overlap) ]                                           │
      │                                                                                        │
      ▼                                                                                        │
[ Tape Saturation & Low-Pass Damping (1.5 - 12 kHz) ]                                          │
      │                                                                                        │
      ▼                                                                                        │
[ Stereo Ping-Pong Feedback Matrix ] ──► [ Wet Level ] ────────────────────────────────────────┴──► Stereo Output
```

---

## 3. Parameter Specifications

| Parameter | Range | Default | Unit | Description |
| :--- | :--- | :--- | :--- | :--- |
| `REVERSE_MODE` | `PURE_REV` / `PING_PONG` / `CRYSTAL_OCT` | `PURE_REV` | mode | Read direction and stereo feedback architecture. |
| `DELAY_TIME` | `100` - `2000` | `650` | ms | Length of each reversed audio phrase window. |
| `TEMPO_DIV` | `FREE` / `1/4` / `DOT_8` / `1/8_T` | `DOT_8` | sync | Rhythmic subdivision synced to Tap Tempo or MIDI Clock. |
| `TRANSIENT_SYNC`| `OFF` / `ON` | `ON` | bool | Aligns buffer reversal boundaries smoothly with picked note attacks. |
| `CROSSFADE_MS` | `5` - `50` | `20` | ms | Window fade overlap eliminating slice-boundary clicks. |
| `FEEDBACK` | `0` - `95` | `42` | % | Number of recirculating reversed phrase echoes. |
| `CRYSTAL_PITCH` | `OFF` / `+12 st` / `+7 st`| `OFF` | st | Optional pitch-shifted reverse read rate (+12 st = octave up crystal). |
| `HF_DAMPING` | `1.5` - `14.0` | `5.5` | kHz | Analog tape high-frequency rolloff softening reverse transient spikes. |
| `MIX_WET_DRY` | `0` - `100` | `55` | % | Parallel blend (Set to 100% for authentic backward-tape soloing). |

---

## 4. Factory Scene Presets

### Scene A: Psychedelic Backward Solo (Hendrix / Beatles Voice)
- **Concept:** Authentic 1960s backwards-tape lead tone where played notes swell backward into explosive pick attacks.
- **Delay Settings:** `REVERSE_MODE = PURE_REV`, `DELAY_TIME = 680 ms`, `TRANSIENT_SYNC = ON`, `FEEDBACK = 25%`.
- **Tone & Crossfade:** `CROSSFADE_MS = 25 ms`, `HF_DAMPING = 4.8 kHz` (warm analog tape).
- **Mix:** `MIX_WET_DRY = 100%` (Pure backwards wet signal; dry muted).

### Scene B: Dotted-Eighth Reverse Ping-Pong (Modern Post-Rock)
- **Concept:** Rhythmic stereo cascade alternating backwards echoes left and right in tight musical sync.
- **Delay Settings:** `REVERSE_MODE = PING_PONG`, `TEMPO_DIV = DOT_8` (Left = Dotted-8th, Right = Quarter note), `FEEDBACK = 48%`.
- **Mix:** `MIX_WET_DRY = 45%` (Retains direct rhythm attack with lush stereo reversed trail).

### Scene C: Reverse Crystal Shimmer (+12 st Octave Clouds)
- **Concept:** Ethereal upward-rising octave shimmer crystals blooming gently behind clean arpeggios and swells.
- **Delay Settings:** `REVERSE_MODE = CRYSTAL_OCT`, `CRYSTAL_PITCH = +12 st`, `DELAY_TIME = 520 ms`, `FEEDBACK = 55%`.
- **Space:** Modulated Hall Reverb (`4.0 s` decay) post-delay.
- **Mix:** `MIX_WET_DRY = 50%`.

### Scene D: Ambient Pad Reverse Texture (Slow Ethereal Wash)
- **Concept:** Long 1.4-second reversed swells blended smoothly into lush ambient reverb, dissolving note boundaries into continuous atmospheric pads.
- **Delay Settings:** `REVERSE_MODE = PURE_REV`, `DELAY_TIME = 1400 ms`, `CROSSFADE_MS = 45 ms`, `FEEDBACK = 60%`.
- **Mix:** `MIX_WET_DRY = 65%`.

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (Psychedelic Backward Solo) / Scene B (Dotted-Eighth Ping-Pong).
- **Footswitch B:** Scene C (Reverse Crystal Shimmer).
- **Footswitch C:** Tap Tempo / Scene D (Ambient Wash).
- **Knob 1 (DELAY):** Delay Window Time (`150 ms` to `1500 ms`).
- **Knob 2 (FEEDBACK):** Regeneration Repeats & Tape Damping.
- **Knob 3 (BLEND):** Wet / Dry Parallel Balance (turn all the way clockwise for 100% backward tape mode).

### Tank-B Control Assignments
- Bassists can utilize Scene B with `HF_DAMPING = 3.2 kHz` and parallel dry retention (`MIX_WET_DRY = 35%`) for haunting, reversed ambient bass intros without losing low-end anchor.

### Black Box Desktop Configuration
- **Expression Pedal 1:** Continuous control over `MIX_WET_DRY`, letting players morph seamlessly from subtle reversed background echoes (20%) to full backwards-tape solos (100%).
- **MIDI Clock Sync:** Automatically locks `DELAY_TIME` subdivisions to external DAW or drummer click tracks.
