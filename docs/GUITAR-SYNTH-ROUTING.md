# UltraRig Guitar & Bass Monophonic Synthesizer Routing Guide

Transforming an electric guitar or bass into a vintage analog synthesizer traditionally required dedicated hexaphonic pickups (such as the Roland GK-3), 13-pin cables, or external MIDI converter hardware.

With UltraRig, you can generate **authentic analog monophonic synth tones** (Moog Minimoog leads, Daft Punk synth basses, Muse-style industrial fuzz hybrids, and 8-bit chiptune textures) directly using a standard 1/4" guitar cable through pitch-tracking wave shapers and resonant filter modulation.

This guide explains the synthesis architecture, signal routing topologies, dynamic envelope filtering, and playing techniques for glitch-free tracking.

---

## 1. Synthesis Engine Architecture

```
 [ Standard Guitar Input ]
            │
            ▼
 ┌─────────────────────┐
 │ FAST NOISE GATE     │ ──> Eliminates fret buzz, handling noise, and string bleed
 └──────────┬──────────┘
            ▼
 ┌─────────────────────┐
 │ WAVE SHAPER (VCO)   │ ──> Generates pure synthetic analog waveforms:
 │ (Pitch Tracker)     │     • Sawtooth (Rich, bright, brassy Moog lead)
 └──────────┬──────────┘     • Square / Pulse (Hollow, reedy, retro synth)
            │                • Sub-Oscillator (-1 Octave fat sine/square)
            ▼
 ┌─────────────────────┐
 │ RESONANT VCF        │ ──> 24 dB/oct 4-Pole Ladder Filter with Resonance
 │ (Filter + Envelope) │     • Modulated by pick velocity (Envelope Follower)
 └──────────┬──────────┘
            ▼
 ┌─────────────────────┐
 │ SPATIAL EFFECTS     │ ──> Stereo Analog Delay + Lush Hall Reverb
 └──────────┬──────────┘
            ▼
 [ Line Out / PA ]
```

---

## 2. Monophonic vs. Polyphonic Synth Tracking

* **Monophonic Precision (Recommended):** The wave shaper tracks the fundamental pitch of **one note at a time**. It delivers instantaneous transient response (<4 ms latency) and organic, analog-style pitch glides (*portamento*).
* **The "Chord Glitch" Effect:** Playing multi-note chords through a monophonic synth generator produces aggressive ring-modulation intermodulation artifacts. While chaotic for clean chords, this glitching is prized in industrial, noise rock, and lo-fi chiptune genres (Jack White / Nine Inch Nails style).

---

## 3. Signal Chain Topologies

### Topology A: Pure Vintage Monophonic Lead (Moog Minimoog Style)
```
[ In ] ──> [ Fast Gate ] ──> [ Synth Shaper (Sawtooth) ] ──> [ Resonant Filter ] ──> [ Delay ] ──> [ Reverb ] ──> [ Out ]
```
* **Best for:** Soaring 70s prog-rock synth solos, Daft Punk leads, and expressive synth melodies.
* **Configuration:** Bypass all guitar amp and IR blocks. The pure analog wave shaper feeding a 24 dB resonant low-pass filter provides authentic synthesizer timbre.

---

### Topology B: The Modern Hybrid Rig (Guitar + Synth Sub Anchor)
```
                              ┌──> [ High-Gain Guitar: Drive ──> NAM ──> Cabinet IR ] ──┐
[ In ] ──> [ Gate ] ──> [Split]─┤                                                         ├──> [Merge] ──> [Out]
                              └──> [ Sub-Synth Shaper (Square -1 Oct) ──> LPF 350 Hz ]  ──┘
```
* **Best for:** Massive alternative rock, industrial metal, and modern power-trio riffs (Muse, Royal Blood style).
* **Result:** Blends the organic pick attack and roar of a physical Marshall/5150 amp on Branch A with a devastating, earth-shaking sub-bass synth square wave on Branch B.

---

### Topology C: 80s Funk Bass Synth (Tank-B)
```
[ Bass In ] ──> [ Gate ] ──> [ Synth Shaper (Pulse Width) ] ──> [ Auto-Wah / Envelope ] ──> [ Chorus ] ──> [ Out ]
```
* **Best for:** Stevie Wonder / Parliament Funkadelic synth bass lines and modern neo-soul grooves.
* **Result:** Bouncy, rubbery low-end with dynamic vocal-like filter growl that reacts to every pluck.

---

## 4. Configuring the Resonant VCF (The "Synth Growl")

The soul of an analog synthesizer is its **Voltage-Controlled Filter (VCF)**:

```
 Low Pick Velocity (Soft Pluck)          High Pick Velocity (Hard Dig)
 ──────────────────────────────          ─────────────────────────────
 Filter Cutoff remains low (~450 Hz)     Filter Cutoff sweeps open (~3.8 kHz)
 Result: Warm, deep, rounded tone        Result: Bright, brassy, aggressive "quack"
```

### Essential Parameter Settings:
1. **Filter Type:** Low-Pass Filter (LPF 24 dB/octave 4-pole ladder).
2. **Resonance (Q):** Set between **3.5 and 5.5**. High resonance boosts the frequencies right at the cutoff edge, creating the classic whistling synth overtone.
3. **Envelope Modulation Source:** Assign `Envelope 1` to `Filter Cutoff`.
4. **Modulation Depth:** Set to `+70%` to `+85%`.
5. **Attack:** `8 ms` (fast transient snap).
6. **Release / Decay:** `140 ms – 220 ms` (smooth return as note sustains).

---

## 5. Pro Playing Techniques for Glitch-Free Synth Tracking

Because digital pitch tracking relies on clean sinusoidal fundamentals, subtle adjustments to your guitar setup and playing style dramatically enhance performance:

1. **Always Select the Neck Pickup:**
   - The neck pickup captures the maximum physical vibration of the string fundamental and suppresses harsh metallic pick transients, eliminating 95% of tracking misfires.
2. **Roll Down the Guitar Tone Knob (5 to 6):**
   - Dialing back the treble cuts high-frequency string squeak and fret noise, delivering an ideal sinusoidal wave to the pitch detection algorithm.
3. **Use Clean Legato (Hammer-ons & Pull-offs):**
   - Playing smoothly with hammer-ons and pull-offs creates a seamless, connected synth glide (*portamento*) between notes without re-triggering the envelope attack.
4. **Palm-Muting for Staccato Sequences:**
   - Rest your palm lightly on the bridge while playing staccato sixteenth notes to generate tight, punchy Roland TB-303 / sequencer basslines.
5. **Mute Unplayed Strings:**
   - Stray open strings vibrating sympathetically will confuse monophonic detection. Use proper left-hand muting discipline.

---

## 6. Recommended 4-Scene Synth Preset Layout

| Scene | Name | Oscillator Mode | Filter Configuration | Ideal Use Case |
| :---: | :--- | :--- | :--- | :--- |
| **A** | **Moog Bass** | Square Wave + Sub-Octave (-1) | Cutoff 400 Hz, Envelope Depth +60% | Synth basslines & funk grooves |
| **B** | **Screaming Lead** | Dual Sawtooth (+1 Octave) | High Resonance (Q=5.0), Open Cutoff | Soaring Jan Hammer / fusion solos |
| **C** | **Hybrid Wall** | Branch A: NAM Amp / Branch B: Sub | Balanced 50/50 mix | Muse / Nine Inch Nails heavy riffs |
| **D** | **8-Bit Chiptune** | Fast Pulse Wave (Square) | Resonant Band-Pass, Short Decay | Retro arcade / video game lo-fi leads |
