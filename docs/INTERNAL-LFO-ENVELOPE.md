# UltraRig Internal LFO & Envelope Follower Modulation Guide

While physical footswitches and expression pedals provide manual control, **Internal Modulators** allow UltraRig presets to evolve dynamically in real time without touching a single control.

By utilizing **Envelope Followers** (which track your picking strength) and **Low-Frequency Oscillators (LFOs)** (which generate cyclic waveforms), you can create touch-sensitive auto-wahs, dynamic drive stages that clean up on soft picking, rhythmic slicers, and drifting ambient reverbs.

This guide explains modulator mechanics, the routing matrix, waveform selection, and practical sound design recipes.

---

## 1. Modulator Architecture: Envelope Follower vs. LFO

```
  ┌────────────────────────────────────────────────────────────────────────┐
  │                    ENVELOPE FOLLOWER (Dynamic / Touch)                 │
  │   Guitar Pick Strike ──> Amplitude Peak ──> Instant Control Rise       │
  │   Note Ring-Out      ──> Signal Decays  ──> Smooth Return to Zero      │
  │   BEST FOR: Auto-Wah, Touch Overdrive, Dynamic Delay Ducking           │
  └────────────────────────────────────────────────────────────────────────┘

  ┌────────────────────────────────────────────────────────────────────────┐
  │                        INTERNAL LFO (Cyclic / Rhythmic)                │
  │   Continuous Waveform (Sine, Triangle, Square, Saw, Random S&H)        │
  │   Locked to Free Hz (0.05–20 Hz) or Master Tap-Tempo BPM               │
  │   BEST FOR: Tremolo, Rotary Speaker, Filter Sweeps, Auto-Pan           │
  └────────────────────────────────────────────────────────────────────────┘
```

---

## 2. The Envelope Follower: Touch-Sensitive Control

The **Envelope Follower** rectifies and smooths the incoming audio amplitude of your guitar, converting physical pick dynamics into a normalized modulation value (0% to 100%).

```
 Input String Transient:        [ Pluck! ]──────.
                                                \
                                                 \─────. (Note Sustain & Decay)
                                                        \───────
 Envelope Control Signal:       [ 100% ]──┐
                                          \
                                           \─────┐
                                                  \───── [ 0% Resting ]
```

### Core Parameters:
* **Sensitivity (Threshold):** Calibrates the detector to your guitar's output. Higher sensitivity responds to delicate fingerstyle; lower sensitivity requires aggressive plectrum digging.
* **Attack Time (5 ms – 50 ms):** How fast the control value jumps to maximum upon string contact. A fast attack (5 ms) gives immediate auto-wah "snap"; a slower attack (30 ms) produces a bowed, swelling swell effect.
* **Release / Decay Time (50 ms – 600 ms):** How gradually the parameter returns to resting level as the note rings out.
* **Polarity (Normal vs. Inverted):**
  - **Positive (+):** Harder plucking increases parameter value (e.g., opens filter cutoff).
  - **Inverted (-):** Harder plucking decreases parameter value (e.g., ducks delay mix during fast leads).

---

## 3. The Internal LFO: Waveforms & Rhythmic Sync

The **Internal LFO** generates continuous periodic oscillations to modulate parameters automatically.

```
 Sine:       /\    /\         Smooth vibrato, subtle chorus, rotary speaker
            /  \  /  \
 ─────────────────────
 Triangle:   /\    /\         Linear optical tremolo, auto-pan sweeps
            /  \  /  \
 ─────────────────────
 Square:    ┌──┐  ┌──┐        Hard chopper / killswitch, staccato synth gating
            │  └──┘  │
 ─────────────────────
 Sawtooth:  /| /| /|          Pumping synth bass filter, reverse tape illusion
 ─────────────────────
 Random:    ─┬_┌─┬_┌─         Stepped sample & hold (Z.Vex Seek-Wah style)
```

### Rate Modes:
1. **Free Rate (Hz):** Adjustable from **0.05 Hz** (one complete sweep every 20 seconds, perfect for slow ambient pads) to **15.0 Hz** (fast, fluttering rotary horn).
2. **BPM Sync (Musical Subdivisions):** Locks the LFO cycle to your pedal's Master Tap-Tempo:
   - `1/1` (Whole note), `1/2` (Half note), `1/4` (Quarter note), `1/8` (Eighth note), `1/8D` (Dotted eighth), `1/16` (Sixteenth note).

---

## 4. The UltraRig Modulation Matrix

To connect an internal modulator to any effect parameter:

```
 [ Source ]           [ Depth & Polarity ]           [ Destination ]
  ENV 1      ───>       +75% Depth           ───>     Filter: Cutoff
  LFO 1      ───>       -40% Depth           ───>     Delay: Mix
  LFO 2      ───>       100% (Square Wave)   ───>     Master Volume
```

1. Select the target effect block in the UltraRig Editor (e.g., Filter, Drive, Reverb, Delay).
2. Click the **Modulation Assignment** icon next to the parameter you want to control.
3. Choose **Source:** `Envelope 1`, `LFO 1`, or `LFO 2`.
4. Set **Depth (%):** Determines the maximum range of modulation.
5. Set **Floor / Ceiling:** Clamps minimum and maximum boundaries so the parameter never exceeds usable musical ranges.

---

## 5. Practical Sound Design Recipes

### Recipe 1: Classic 70s Funk Auto-Wah (Mutron Style)
* **Target Block:** Parametric / Resonant Filter (Slot 2, before Drive/Amp).
* **Filter Mode:** Low-Pass (LPF 24 dB/oct) with High Resonance (Q = 4.5).
* **Modulation Source:** `Envelope 1`
* **Destination:** `Filter: Cutoff`
* **Settings:**
  - Base Cutoff: `350 Hz` (warm and dark when resting)
  - Mod Depth: `+85%` (opens up to ~3.8 kHz on hard funk plucks)
  - Attack: `8 ms`, Release: `160 ms`

---

### Recipe 2: The "Living Ambient Reverb" (Drifting Pad)
* **Target Block:** Studio Reverb (Slot 6).
* **Modulation Source:** `LFO 1`
* **Destination 1:** `Reverb: Damping` (Depth: `+30%`)
* **Destination 2:** `Reverb: Mix` (Depth: `+15%`)
* **LFO Settings:**
  - Waveform: `Sine`
  - Rate: `0.12 Hz` (Free rate; one smooth, drifting wave every 8 seconds)
* **Result:** Reverb reflections subtly brighten and swell periodically, creating a breathing cinematic pad under guitar chords without becoming muddy.

---

### Recipe 3: Hard Chopper Killswitch (Tom Morello / Radiohead Slicer)
* **Target Block:** Volume Block (Slot 7, after Cabinet IR).
* **Modulation Source:** `LFO 1`
* **Destination:** `Volume: Level`
* **LFO Settings:**
  - Waveform: `Square`
  - Rate: `BPM Sync: 1/16` (or 1/8 triplet)
  - Mod Depth: `-100%`
* **Result:** Aggressive, instantaneous on/off rhythmic slicing locked perfectly to the drummer's click tempo.

---

### Recipe 4: Dynamic Lead Ducking (Automatic Solo Clarity)
* **Target Block:** Digital Delay (Slot 5).
* **Modulation Source:** `Envelope 1` (Inverted Polarity)
* **Destination:** `Delay: Mix`
* **Settings:**
  - Base Delay Mix: `45%`
  - Mod Depth: `-40%` (Inverted)
  - Attack: `10 ms`, Release: `250 ms`
* **Result:** While playing fast shred leads, the loud pick strikes duck the delay mix down to ~5%, keeping notes crisp and articulate. The moment you hold a sustained note or pause, the delay mix blooms back up to 45% to fill the space.

---

## 6. Scene Integration with Modulators

Take advantage of UltraRig's 4 scenes to alter modulator behavior instantly:
* **Scene A (Verse):** LFO Speed = `1/4 note`, Mod Depth = `15%` (Subtle movement).
* **Scene B (Chorus):** LFO Speed = `1/16 note`, Mod Depth = `60%` (Fast, swirling rotary).
* **Scene C (Solo):** Envelope Ducking active on delay line.
* **Scene D (Outro):** LFO Random S&H active for glitchy synth textures.
