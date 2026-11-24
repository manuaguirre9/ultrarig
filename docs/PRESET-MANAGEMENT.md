# Preset & Scene Management Guide for UltraRig

This guide explains how to organize, level-match, and optimize presets and scenes in **UltraRig** for stage performances and home recording.

---

## 1. Presets vs. Scenes: Understanding the Architecture

To get the most out of your M-VAVE pedal (Tank-G, Tank-B, Black Box), it is essential to understand the difference between **Presets** and **Scenes**:

| Aspect | Preset (Banks 1–8, Slots A–D) | Scene (Scenes 1–4 per Preset) |
|---|---|---|
| **What it contains** | Full signal routing, NAM profile, Cabinet IR, all block parameters. | Bypass states, parameter levels, gain/volume boosts, mix ratios. |
| **Switching speed** | ~50–150 ms (reloads neural model weights from flash). | **0 ms (Instantaneous / Zero-gap audio switching).** |
| **Audio spillover** | May mute delay/reverb tails during reload. | Preserves seamless delay and reverb decay tails. |
| **Best used for** | Switching between completely different rigs or songs. | Switching between parts of the **same song** (Clean $\to$ Rhythm $\to$ Lead). |

---

## 2. Recommended 4-Scene Live Performance Strategy

Instead of creating separate presets for every section of a song, dial in one versatile amplifier capture (e.g. an edge-of-breakup British or American tube amp) and configure the **4 Scenes**:

* **Scene 1: Clean / Ambient**
  * Amp Gain: Low / Clean
  * Active Blocks: Compressor, Subtle Chorus, Plate Reverb
  * Usage: Verses, arpeggios, intro passages.
* **Scene 2: Rhythm Crunch**
  * Amp Gain: Medium / Punchy Overdrive
  * Active Blocks: Noise Gate, NAM Preamp, 1024-pt Cabinet IR
  * Usage: Heavy riffs, driving choruses.
* **Scene 3: Lead Solo Boost**
  * Amp Gain: High + Overdrive Boost (`+3.0 dB` level boost)
  * Active Blocks: Overdrive/Boost, NAM Preamp, Analog Delay (quarter-note), Reverb
  * Usage: Solos and prominent melodic lines.
* **Scene 4: Dynamic / Special FX**
  * Active Blocks: Parallel Pitch Octave, Flanger, Tremolo, or Shimmer Reverb
  * Usage: Bridges, ambient swells, or special song-specific moments.

> [!TIP]
> Because scenes do not reload models from flash memory, switching footswitches mid-song produces **no audio dropout or glitch**, ensuring tight transitions on stage.

---

## 3. Level Matching & Perceived Loudness

A common problem when playing live is that clean presets sound quiet, while high-gain presets overwhelm the mixer and clip the PA.

### Steps for Balanced Output Levels:
1. **Calibrate Against Unity Gain:**
   - Plug into your audio interface or PA mixer.
   - Adjust the **Master Output** knob on the pedal to approximately 12 o'clock (50%).
2. **Level Match Clean and Lead Scenes:**
   - High-gain distortion naturally compresses peaks, making it sound louder even if peak meters look similar.
   - Set your **Rhythm** sound as the baseline (aim for around -14 to -12 dBFS peak in your DAW).
   - Adjust the Clean scene volume up by `+1.5 dB` to compensate for lack of natural compression.
   - Set the Lead scene `+2.5 dB` to `+3.5 dB` above the Rhythm scene so solos cut through the band mix without harshness.
3. **Avoid Output Stage Clipping:**
   - Watch the output meter in the UltraRig Web Editor. If the signal bar turns red, reduce the output level of the final block (usually the Cabinet IR or Master EQ) rather than the pedal's physical output knob.

---

## 4. Footswitch Assignment & Live Mode

UltraRig allows customizing what each footswitch does:

* **Bank Mode (Default):**
  * Footswitches A, B, and C toggle presets; pressing two footswitches simultaneously switches banks up or down.
* **Scene Mode (Recommended for Gigs):**
  * Each footswitch directly activates Scene 1, 2, 3, or 4 of the currently loaded preset.
  * **Double-Tap / Long Press:** Assign footswitch double-tap or long-press to utility functions (e.g. engaging the Chromatic Tuner or Tap Tempo).

---

## 5. Saving Presets & Managing Flash Memory

* **Live Preset Persistence:**
  - When editing via the Web Editor (`web/index.html`), changes are sent in real time to the pedal's RAM.
  - Remember to click **Save Preset** to write the parameters to non-volatile flash memory.
* **USB Recording Note (Alpha 13.1+):**
  - In earlier versions, leaving a DAW recording session open over USB could delay automatic background saving.
  - Alpha 13.1 automatically flushes changes to flash within 10 minutes, protecting your tweaks during studio sessions.
