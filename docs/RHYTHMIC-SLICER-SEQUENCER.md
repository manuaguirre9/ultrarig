# Rhythmic Slicer & Tempo-Synced Step Sequencer Modeling Guide

This guide details the step-sequenced VCA gating mechanics, anti-click slew smoothing, stepped resonant filter modulation, and practical preset design for **Rhythmic Audio Slicing** (inspired by the **Boss SL-20 Slicer** and **Roger Linn AdrenaLinn**) within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Principles of Tempo-Synced Rhythmic Audio Slicing

A **Rhythmic Slicer** transforms sustained guitar chords, bass drones, or synth pads into intricate percussive rhythms by driving a real-time VCA (Voltage Controlled Amplifier), a resonant filter, and a stereo panner from a programmable 16-step sequencer.

```
Tap Tempo / MIDI Clock (24 PPQN) ──► [ 16-Step Pattern Sequencer ]
                                         ├── Step Amplitude Target (0% - 100%) ──► [ Anti-Click Slew ] ──► [ VCA Gate ]
                                         ├── Step Cutoff Target (80 Hz - 6 kHz) ───────────────────────► [ 24dB Resonant VCF ]
                                         └── Step Stereo Pan Target (L / C / R) ───────────────────────► [ Stereo Output ]
```

### 1.1 Anti-Click Envelope Slew & Duty Cycle Shaping

If a step sequencer toggles audio amplitude instantaneously from `0.0` to `1.0` in a single sample, it creates a step-function discontinuity that manifests as loud digital pops and clicks. UltraRig eliminates these artifacts while preserving sharp rhythmic punch:
- **Minimum Envelope Slew ($2.5\text{ ms} - 12\text{ ms}$):** Every gate edge transitions across a smooth raised-cosine curve. Short slews ($2.5\text{ ms}$) yield aggressive electronic trance gates; longer slews ($20\text{ ms} - 40\text{ ms}$) produce breathing acoustic tremolo pulses.
- **Step Duty Cycle:** Determines the open duration within each rhythmic subdivision (from $15\%$ ultra-short staccato stabs to $90\%$ legato pulses).

### 1.2 Stepped Resonant Filter Modulation & Stereo Panning

Each step inside the 16-step matrix stores three independent modulation vectors:
1. **Amplitude Gate ($A_i$):** Accents specific beats (e.g. Steps 1, 4, 7, 11) while muting or attenuating off-beats.
2. **Filter Cutoff ($f_i$):** Modulates a 4-pole resonant low-pass filter on each beat, producing squelchy synth-sequencer basslines and robotic rhythmic grooves.
3. **Stereo Pan ($P_i$):** Routes alternating slices across the stereo image (e.g. Left $\to$ Center $\to$ Right $\to$ Center) for kinetic spatial movement.

### 1.3 Transient Attack Reset (Human Sync Mode)

When playing live without an external MIDI clock, keeping a 16-step sequencer locked to your picking hand can be challenging. Enabling **Transient Attack Reset** uses an envelope flux detector to immediately reset the sequencer to **Step 1** whenever a new chord strum is struck, synchronizing the groove organically to human feel.

---

## 2. DSP Signal Chain & Processing Topology

```
Instrument Input (Guitar / Bass / Keys)
   │
   ├───► [ Pre-Slicer Optical Sustainer Compressor ] (Keeps chords ringing across all 16 steps)
   │
   ├───► [ Transient Attack Reset Detector ] ──► (Optional Step-1 Sync Trigger)
   │
   ▼
[ 4-Pole Resonant Ladder VCF ] ◄──── [ Step Filter Cutoff Sequencer ]
   │
   ▼
[ Dynamic VCA Gate Stage ] ◄──────── [ Step Amplitude Sequencer + Slew Limiter ]
   │
   ▼
[ Stereo Panorama Matrix ] ◄──────── [ Step Pan Sequencer (Left / Center / Right) ]
   │
   ▼
[ Parallel Dry Blend & Post-Slicer Ping-Pong Delay ] ──► Stereo Output
```

---

## 3. Parameter Specifications

| Parameter | Range | Default | Unit | Description |
| :--- | :--- | :--- | :--- | :--- |
| `PATTERN_BANK` | `1` to `24` | `1` | preset | Built-in rhythmic templates (16th trance, triplets, dubstep wobble, funk). |
| `STEP_COUNT` | `4` to `16` | `16` | steps | Sequence length before looping (set to 12 for 3/4 or triplet feels). |
| `TEMPO_BPM` | `40` - `240` | `120` | BPM | Internal master tempo clock (overridden by Tap Tempo or MIDI Clock). |
| `MIDI_SYNC` | `INTERNAL` / `MIDI_CLK`| `INTERNAL` | mode | Locks sequencer phase precisely to external DAW or drummer click tracks. |
| `ATTACK_SLEW` | `2.0` - `50.0` | `4.5` | ms | Rise/fall transition time of each VCA slice (low = sharp; high = soft tremolo). |
| `DUTY_CYCLE` | `15` - `95` | `55` | % | Gate hold width within each rhythmic step before decaying to silence. |
| `FILTER_DEPTH` | `0` - `100` | `50` | % | Modulation excursion applied to the stepped 24 dB/oct resonant VCF. |
| `FILTER_RES` | `0` - `90` | `45` | % | Resonance Q peak accentuating filter movement on accented steps. |
| `STEREO_PAN` | `MONO` / `ALTERNATING` / `RANDOM` | `ALTERNATING` | mode | Spatial pan trajectory across Left and Right outputs. |
| `ATTACK_RESET` | `OFF` / `ON` | `ON` | bool | Automatically restarts pattern on Step 1 when strumming a new chord. |
| `MIX_WET_DRY` | `0` - `100` | `85` | % | Parallel blend between dry direct sustain and sliced rhythm output. |

---

## 4. Factory Scene Presets

### Scene A: 16th-Note Trance Gate (EDM / Synth-Rock Chord Chop)
- **Concept:** Razor-sharp, syncopated 16th-note Euro-trance gating turning any held guitar power chord into an electronic synthesizer riff.
- **Sequencer:** `PATTERN_BANK = 1` (Syncopated 16th pulse), `ATTACK_SLEW = 2.5 ms`, `DUTY_CYCLE = 48%`.
- **Spatial & Filter:** `STEREO_PAN = ALTERNATING`, `FILTER_DEPTH = 30%`, `MIX_WET_DRY = 95%`.
- **Space:** Subtle Studio Hall Reverb (`1.8 s`, `20%` mix) post-slicer to add size without blurring steps.

### Scene B: Stereo Ping-Pong Triplet Slice (Dreamy Poly-Rhythm)
- **Concept:** Hypnotic 12-step triplet cadence sweeping gracefully from left to right into dotted-8th echoes.
- **Sequencer:** `STEP_COUNT = 12`, `ATTACK_SLEW = 14.0 ms`, `DUTY_CYCLE = 65%`, `STEREO_PAN = ALTERNATING`.
- **Space:** Stereo Tape Delay (`dotted 8th`, `420 ms`, `35%` feedback) + Plate Reverb.
- **Mix:** `MIX_WET_DRY = 75%`.

### Scene C: Filter-Sweep Dubstep Groove (Resonant Step VCF)
- **Concept:** Aggressive rhythmic "wobble" bass/guitar groove created by modulating a resonant low-pass ladder filter across alternating steps.
- **Sequencer:** `PATTERN_BANK = 14` (Half-time wobble groove), `FILTER_DEPTH = 90%`, `FILTER_RES = 72%`, `DUTY_CYCLE = 85%`.
- **Pre-Drive:** Heavy fuzz or high-gain amp overdrive *ahead* of the slicer filter for massive synth harmonics.
- **Mix:** `MIX_WET_DRY = 100%`.

### Scene D: Percussive Funk Rhythmic Chop (Tight Auto-Mute)
- **Concept:** Tight, groovy 16th-note rhythmic chopping with clean envelope-follower punch for funk comping and electronic pop.
- **Sequencer:** `PATTERN_BANK = 6` (Accent funk chop), `ATTACK_SLEW = 3.5 ms`, `DUTY_CYCLE = 35%`.
- **Attack Sync:** `ATTACK_RESET = ON` so every single chord strum lands tight on beat 1.
- **Mix:** `MIX_WET_DRY = 65%` (Retains 35% clean pick attack).

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (16th Trance Gate) / Scene B (Triplet Slice).
- **Footswitch B:** Scene C (Dubstep Filter Groove).
- **Footswitch C:** Tap Tempo (3-tap tempo lock) / Scene D.
- **Knob 1 (MOD FX):** Duty Cycle width (turns staccato stabs into smooth pulses).
- **Knob 2 (FILTER / TONE):** Resonant Filter Modulation Depth.
- **Knob 3 (BLEND):** Wet / Dry balance.

### Tank-B Control Assignments
- A game-changing tool for modern electronic, pop, and industrial bassists! Use Scene C (`FILTER_RES = 70%`) with a distorted bass or octaver feeding the slicer to generate locked-in dubstep and synth-bass wobble grooves on stage.

### Black Box Desktop Configuration
- **MIDI Clock Sync:** Automatically locks the slicer tempo and phase directly to Ableton Live, Logic Pro, or hardware drum machines via USB-MIDI or TRS MIDI In.
- **Expression Pedal 1:** Morphs `DUTY_CYCLE` smoothly from $20\%$ (tight percussion) to $90\%$ (ambient wave) during builds and drops.
