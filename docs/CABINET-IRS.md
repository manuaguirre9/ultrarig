# Cabinet Impulse Response (IR) Technical Specifications & Guide

This document details the audio specifications, format requirements, and best practices for loading **Cabinet Impulse Responses (IRs)** into **UltraRig** on M-VAVE hardware (Tank-G, Tank-B, Black Box).

---

## 1. Technical Format Specifications

UltraRig's embedded convolution DSP engine is optimized for high-fidelity speaker cabinet emulation with minimal processing latency:

| Specification | Supported / Native Standard | Behavior with Other Formats |
|---|---|---|
| **File Format** | Uncompressed PCM Audio (`.wav`) | Non-wav containers (`.aiff`, `.mp3`) are rejected. |
| **Convolution Length** | **1024 Samples** (~21.3 ms @ 48 kHz / ~23.2 ms @ 44.1 kHz) | Longer IRs (2048 pts / 500 ms) are automatically truncated. |
| **Sample Rate** | **44.1 kHz** and **48 kHz** | Converted automatically during flash upload. |
| **Bit Depth** | **24-bit** (Native) | 16-bit and 32-bit float files are converted to 24-bit. |
| **Channels** | **Mono** | Stereo WAV files are converted to mono (left channel extracted). |

---

## 2. Why 1024 Points? (DSP & Latency Balance)

Commercial impulse response packs (from vendors like York Audio, OwnHammer, or Celestion) often ship files in multiple lengths: 200 ms, 500 ms, 2048 samples, and 1024 samples.

* **What 1024 Samples (~22 ms) Captures:**
  * Initial transient impact of the guitar pick striking the strings.
  * Speaker cone voice coil inertia and frequency response.
  * Microphone proximity effect and frequency curve (e.g. Shure SM57, Royer R-121, Sennheiser MD421).
  * Internal cabinet body reflections and port resonances.
* **What Longer IRs (2048+ pts / Room IRs) Add:**
  * Extended room decay, wall reflections, and ambient reverb.
* **Why 1024 Samples is Ideal on Embedded Pedals:**
  * A 1024-point convolution filter guarantees **sub-millisecond DSP calculation time**, leaving ample CPU cycles for the Neural Amp Modeler (NAM A2-Lite), stereo delay, and reverb algorithms.

> [!NOTE]
> If you import a 2048-sample or 500 ms IR, the UltraRig Web Editor automatically applies a smooth mathematical Hann/Blackman window taper at sample 1024. This prevents abrupt truncation clicks or pops.

---

## 3. Phase Alignment & Minimum Phase

When selecting IRs from commercial packs, you may see filenames labeled `MPT` (Minimum Phase Transformed) or `RAW`:

* **Standard (RAW) IRs:** Include the microscopic physical time-of-flight delay between the speaker cone and the microphone capsule (typically 0.5 ms to 2 ms).
* **Minimum Phase (MPT) IRs:** The pre-delay is mathematically stripped, aligning the transient spike at sample zero.
* **Recommendation:**
  * If using a single cabinet IR, either format sounds excellent.
  * If running parallel signal paths (e.g. Path A clean blend, Path B distorted cab), use **Minimum Phase (MPT)** IRs to prevent phase cancellation and comb-filtering when the signals merge.

---

## 4. Supported IR Applications

UltraRig's convolution block is not limited to electric guitar speaker cabs:

1. **Electric Guitar Cabinets:**
   - 4x12 Closed-back (Celestion Vintage 30, Greenback, Creamback) for rock and metal.
   - 2x12 Open-back (Alnico Blue, Jensen) for blues, indie, and chimey cleans.
2. **Bass Guitar Cabinets (Tank-B / Tank-G):**
   - 8x10 Sealed Ampeg-style cabinets (punchy, tight low-end, smooth top).
   - 4x10 Ported cabinets with horn tweeters (modern slap and hi-fi tones).
   - 1x15 Sub-heavy cabs for vintage dub and soul.
3. **Acoustic Guitar Resonance IRs:**
   - Transform thin, harsh piezo undersaddle pickups into the warm, resonant sound of a mic'd Dreadnought or Jumbo acoustic guitar.

---

## 5. How to Import IRs into UltraRig

1. Connect the pedal to your computer and open the **UltraRig Web Editor** (`web\index.html`) in Google Chrome or Microsoft Edge.
2. Click **Connect** and wait for preset synchronization.
3. Navigate to the **Cab / IR** block in your signal chain.
4. Click on the slot selector or the **Upload (Folder)** icon.
5. Select your `.wav` file. The editor validates the header, resamples/truncates if necessary, and writes the impulse data into the pedal's flash memory.
6. Click **Save Preset** to make the assignment permanent.
