# Analog Octaver & Sub-Harmonic Divider Modeling Guide

This guide details CMOS **Flip-Flop Frequency Division** (Boss OC-2 style), hysteresis zero-crossing glitch mitigation, polyphonic octave synthesis, and **"Lowest-Note Priority"** bass splitting within UltraRig for M-VAVE hardware (Tank-B, Tank-G v1/v2, and Black Box).

---

## 1. Analog Sub-Harmonic Division vs. Polyphonic Pitch Shifting

Not all octave pedals generate sub-bass the same way. Understanding the architectural distinction between **Analog Flip-Flop Dividers** and **Polyphonic DSP Octavers** allows musicians to choose between organic synth fatness and clean chordal tracking.

```
--- CLASSIC ANALOG SUB-OCTAVE DIVIDER (Boss OC-2 Architecture) ---
Input ──┬──► [ 4th-Order Tracking LPF (Isolates Fundamental) ] ──► [ Schmitt Trigger Comparator ]
        │                                                                   │
        │                                       ┌───────────────────────────┴───────────────────────────┐
        │                                       ▼                                                       ▼
        │                           [ ÷2 Flip-Flop (-1 Oct) ]                               [ ÷4 Flip-Flop (-2 Oct) ]
        │                                       │                                                       │
        │                                       ▼                                                       ▼
        │                           [ Analog Warm LPF + VCA ] ◄── [ Envelope Follower ] ──► [ Analog Warm LPF + VCA ]
        │                                       │                                                       │
        └──► [ Dry Direct Signal ] ─────────────┴───────────────────────────┬───────────────────────────┘
                                                                            ▼
                                                                     Master Summing Out
```

### 1.1 Anatomy of Analog Flip-Flop Division (OC-2 Character)

1. **Zero-Latency Hardware Logic:** Unlike FFT-based polyphonic shifters that buffer audio frames ($5\text{ ms} - 15\text{ ms}$ latency), analog dividers operate instantaneously in the time domain using a **Schmitt Trigger** driving digital **D-Type Flip-Flops** ($\div 2$ for $-12\text{ st}$, $\div 4$ for $-24\text{ st}$).
2. **Envelope Follower & VCA Shaping:** Because a CMOS flip-flop outputs constant rail-to-rail square waves, UltraRig multiplies the divided pulse wave by the original instrument's dynamic amplitude envelope and rounds sharp corners through a resonant analog low-pass filter, yielding that iconic warm, syrupy, tuba-like synth bass tone.
3. **Hysteresis Tracking Calibration:** To prevent erratic harmonic octave jumps on decaying low strings ($E_1 - A_1$), a steep tracking low-pass filter ($150\text{ Hz}$) paired with adjustable comparator hysteresis locks steadily onto the fundamental wave cycle.

### 1.2 Lowest-Note Priority (Guitar + Bass Split Mode)

Inspired by modern polyphonic tracking architectures, **Lowest-Note Mode** dynamically identifies the lowest sounding fundamental frequency in a strummed guitar chord (typically $< 200\text{ Hz}$) and applies $-1\text{ octave}$ transposition strictly to that bass note—allowing solo acoustic, jazz, or fingerstyle guitarists to simulate an accompanying electric bassist underneath crisp upper voicings!

---

## 2. DSP Signal Chain & Processing Topology

```
Instrument Input (Electric Guitar / 4 or 5-String Bass)
   │
   ├───► [ Dry Direct Level ] ────────────────────────────────────────────────────────────────┐
   │                                                                                          │
   ├───► [ Mode A: Analog Flip-Flop Sub-Divider (-1 Oct / -2 Oct) ]                           │
   │           ├── Tracking Pre-LPF & Hysteresis Gate                                         │
   │           └── Post-Divider Sub-Tone Low-Pass Shaper (180 Hz - 1.5 kHz)                   │
   │                                                                                          │
   ├───► [ Mode B: Polyphonic Chordal Octaver (-1 Oct / +1 Oct) ]                             │
   │                                                                                          │
   └───► [ Mode C: Lowest-Note Priority Split (-1 Oct Locked to Bass Line Only) ]             │
               │                                                                              │
               ▼                                                                              │
[ Optional Parallel Amp Split (Royal Blood Style: Sub -> Bass Cab | Oct-Up -> Guitar Fuzz) ] ─┴──► Out
```

---

## 3. Parameter Specifications

| Parameter | Range | Default | Unit | Description |
| :--- | :--- | :--- | :--- | :--- |
| `OCTAVE_ENGINE` | `ANALOG_OC2` / `POLY` / `LOWEST_NOTE` | `ANALOG_OC2` | mode | CMOS flip-flop monophonic synth vs. polyphonic chordal vs. bass split. |
| `DIRECT_LEVEL` | `0` - `100` | `80` | % | Original dry instrument balance (turn to 0% for pure synth sub-bass). |
| `OCT1_LEVEL` | `0` - `100` | `75` | % | $-1\text{ octave}$ ($-12\text{ st}$) sub-harmonic level. |
| `OCT2_LEVEL` | `0` - `100` | `20` | % | $-2\text{ octave}$ ($-24\text{ st}$) deep sub-seismic synth level. |
| `OCT_UP_LEVEL` | `0` - `100` | `0` | % | $+1\text{ octave}$ ($+12\text{ st}$) polyphonic chime level (Poly mode only). |
| `TRACK_HYST` | `0` - `100` | `45` | % | Comparator stability threshold reducing false glitch triggers on bass decay. |
| `SUB_TONE_LPF` | `180` - `2400` | `520` | Hz | Post-divider smoothing filter controlling synth warmth vs. square buzz. |
| `SPLIT_CUTOFF` | `100` - `350` | `190` | Hz | Ceiling threshold isolating lowest chord root note in Lowest-Note mode. |

---

## 4. Factory Scene Presets

### Scene A: OC-2 Monophonic Funk Synth (`-1 / -2` Analog Fatness)
- **Concept:** The quintessential Pino Palladino / Tim Lefebvre analog synth bass sound: zero dry signal, pure fat divided sub-oscillator warmth.
- **Settings:** `OCTAVE_ENGINE = ANALOG_OC2`, `DIRECT_LEVEL = 0%`, `OCT1_LEVEL = 100%`, `OCT2_LEVEL = 30%`, `SUB_TONE_LPF = 480 Hz`.
- **Pro Tip:** On bass guitar, play above the 7th fret on D and G strings using the neck pickup with tone rolled back for rock-solid tracking!

### Scene B: Sub-Bass Guitar Reinforcement (Fingerstyle Bass Split)
- **Concept:** Adds an organic, tight electric bass player strictly beneath the lower strings of your guitar without muddying upper jazz or folk chords.
- **Settings:** `OCTAVE_ENGINE = LOWEST_NOTE`, `SPLIT_CUTOFF = 185 Hz`, `DIRECT_LEVEL = 100%`, `OCT1_LEVEL = 68%`, `SUB_TONE_LPF = 380 Hz`.
- **Dynamics:** Gentle optical compression (`2.5:1`) gluing dry guitar and sub-octave bass seamlessly together.

### Scene C: Royal Blood / White Stripes Riff Split (Dual Rig Power)
- **Concept:** Transforms a single electric bass or guitar into a full two-piece rock band using parallel split amplification!
- **Routing:**
  - **Path L (Bass Rig):** Clean instrument + `-1 Oct` sub-weight sent into Ampeg SVT 8x10 Bass IR.
  - **Path R (Guitar Rig):** `+1 Oct` (or clean unison) pushed hard through Big Muff Fuzz + Marshall 4x12 Guitar IR!
- **Settings:** `OCTAVE_ENGINE = POLY`, `DIRECT_LEVEL = 90%`, `OCT1_LEVEL = 70%`, `OCT_UP_LEVEL = 85%`.

### Scene D: 12-String & Organ Polyphonic Shimmer Octave (POG Swell)
- **Concept:** Rich, cathedral-like chordal organ pad pairing simultaneous $-12\text{ st}$ and $+12\text{ st}$ polyphonic harmonies.
- **Settings:** `OCTAVE_ENGINE = POLY`, `DIRECT_LEVEL = 75%`, `OCT1_LEVEL = 55%`, `OCT_UP_LEVEL = 65%`.
- **Space:** Modulated Stereo Tape Delay (`420 ms`) + Lush Plate Reverb (`3.5 s`).

---

## 5. Hardware Setup & Mapping

### Tank-B Control Assignments
- **Every Bassist's Secret Weapon:** Tank-B handles Scene A (`OC-2 Analog Synth`) effortlessly. Set `TRACK_HYST = 55%` to maximize low-frequency stability when holding sustained grooves above the 5th fret.
- **Footswitch 1:** Scene A (OC-2 Synth Bass) / Scene C (Royal Blood Fuzz Split).
- **Footswitch 2:** Direct Dry Kill Switch (toggles `DIRECT_LEVEL` instantly between `100%` and `0%` for synth drops).

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene B (Lowest-Note Fingerstyle Split) / Scene C (White Stripes Fuzz Riff).
- **Knob 1 (MOD / OCT1):** $-1\text{ Octave}$ Sub-Harmonic level.
- **Knob 2 (TONE):** `SUB_TONE_LPF` synth warmth sweep.
- **Knob 3 (BLEND):** Direct Instrument / Octave Mix balance.

### Black Box Desktop Configuration
- **True Bi-Amp Dual Outputs:** Route the clean sub-octave Path L out of Output Left to a dedicated PA bass sub channel, and the octave-up fuzz Path R out of Output Right to a guitar amp or stereo FOH channel!
