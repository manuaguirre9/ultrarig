# NAM (Neural Amp Modeler) A2-Lite Guide for UltraRig

This guide explains how neural amp modeling works in **UltraRig**, how to choose or convert captures, and best practices for gain staging and DSP budget management on your M-VAVE pedal.

---

## 1. What is NAM A2-Lite?

[Neural Amp Modeler](https://github.com/sdatkinson/neural-amp-modeler) (NAM) is an open-source deep learning framework created by Steven Atkinson that models guitar and bass amplifiers and drive pedals with state-of-the-art accuracy.

On a desktop computer, NAM models typically use heavy **Standard (WaveNet)** or **LSTM** neural architectures with hundreds of thousands of parameters. The embedded DSP chips inside the M-VAVE Tank series (such as JieLi processors) have strict CPU and RAM limitations and cannot execute standard desktop models in real time without audio dropouts.

**A2-Lite** is an ultra-compact, highly optimized neural architecture specifically designed for low-power embedded processors:
- **Low latency:** Sub-millisecond inference time.
- **Minimal DSP footprint:** Leaves sufficient CPU cycles for parallel delays, reverbs, cabinet IRs, and the chromatic tuner.
- **High fidelity:** Preserves dynamic touch sensitivity, harmonic saturation, and pickup volume cleanup.

---

## 2. Choosing Captures: Preamp vs. Full Rig

When browsing or creating captures, understand the difference between capture types:

| Type | Signal Chain | Best Used In UltraRig As |
|---|---|---|
| **Preamp Capture** | Guitar $\to$ Preamp $\to$ Line Out | **Recommended.** Pair with UltraRig's Cabinet IR block. Gives flexibility to swap virtual speaker cabinets and microphones. |
| **Full Rig Capture** | Guitar $\to$ Amp $\to$ Cabinet $\to$ Mic | **Stand-alone.** Disable the Cabinet IR block in UltraRig to avoid double-filtering (the "blanket over the speaker" sound). |
| **Drive / Stomp Capture** | Guitar $\to$ Overdrive / Fuzz Pedal | Can be placed in front of a clean amp capture or used as a standalone boost. |

> [!TIP]
> **Preamp + IR** is almost always the best-sounding and most flexible approach on UltraRig. It allows you to tailor your high-end sizzle and low-end punch using your favorite 1024-point cabinet impulse responses.

---

## 3. Gain Staging & Input Trim

One of the most common user issues is unexpected distortion, digital clipping, or a capture sounding "muddy" or "thin." This is almost always caused by input gain mismatch.

NAM models are trained against a specific reference audio level (usually normalized to **0 dBu** or a standard dBFS peak during the re-amping capture process).

### Calibrating Your Guitar's Input:
1. **Low-output Single Coils (Strat / Tele):** May require a slight boost (`Input Trim: +1.5 dB` to `+3.0 dB`) to push edge-of-breakup and crunch models into natural saturation.
2. **High-output Humbuckers / Active Pickups (EMG / Fishman):** Often hit the pedal too hot. Set `Input Trim` between `-2.0 dB` and `-5.0 dB` to avoid harsh digital inter-sample clipping before the neural network.
3. **Listen for Natural Compression:** Roll your guitar's volume knob down to 6 or 7. If the tone cleans up smoothly without harsh artifacts, your input trim is correctly calibrated.

---

## 4. DSP Budget & Preset Management

UltraRig allows building complex signal chains with parallel routing branches, but the DSP chip has a finite budget per audio buffer cycle:

* **Heavy Blocks:**
  * NAM A2-Lite Amp Engine (~35-45% DSP budget)
  * Cabinet IR Engine (convolution filter)
  * Stereo Shimmer / Cloud Reverb
  * Pitch / Polyphonic Octave
* **Light Blocks:**
  * Noise Gate
  * Parametric / Graphic EQ
  * Compressor
  * Analog-style Delay / Chorus

> [!NOTE]
> If you notice micro-dropouts or stuttering (especially when engaging the chromatic tuner on complex presets):
> 1. Ensure you are running **UltraRig Alpha 13.1** or newer (which dynamic-allocates memory for the tuner).
> 2. Avoid placing two heavy modulation blocks simultaneously in parallel with a long reverb decay.
> 3. Use the **Scene** feature instead of duplicating entire heavy presets to switch between rhythm and lead tones.

---

## 5. Finding & Converting A2-Lite Captures

1. **ToneHunt:** Look for captures tagged with `A2-Lite`, `Nano`, or `Feather` on platforms like [ToneHunt.org](https://tonehunt.org).
2. **Converting Existing Models:**
   - Standard WaveNet models cannot simply be renamed to `.nam` and loaded into UltraRig. They must be re-trained or distilled using the A2-Lite architecture profile.
   - Use the official NAM training scripts (via Google Colab or local Python environments) specifying the `--model-type A2-Lite` flag against clean DI training audio.
3. **Loading Into UltraRig:**
   - Open the UltraRig Web Editor (`web\index.html`).
   - Navigate to the **Amp** block.
   - Click the folder icon to upload your `.nam` A2-Lite file directly to the pedal's flash memory.
