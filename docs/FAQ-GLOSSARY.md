# Audio Engineering Glossary & FAQ for UltraRig

This guide explains key digital signal processing (DSP) concepts, audio routing terminology, and frequently asked questions for musicians using **UltraRig**.

---

## 1. Glossary of Technical Concepts

### Impulse Response (IR) vs. Neural Amp Modeler (NAM)
Understanding the difference between linear and non-linear audio processing is essential when dialing in tones:

| Concept | Type of Processing | What It Models | Can It Model Distortion? |
|---|---|---|---|
| **Cabinet IR** | Linear Time-Invariant (LTI) Convolution | Speaker cabinets, acoustic spaces, microphone placement, resonance curves. | **No.** An IR cannot simulate clipping, tube overdrive, or harmonic saturation. |
| **NAM Profile** | Non-Linear Deep Learning (Neural Network) | Guitar/bass preamps, power amps, overdrive/fuzz clipping diodes, tube sag. | **Yes.** NAM precisely captures dynamic distortion and harmonic overtones. |

> [!TIP]
> **Best Practice:** Always pair a **NAM Preamp capture** with a **Cabinet IR block**. If you use a "Full Rig" NAM capture (which already includes the speaker cabinet), turn the Cabinet IR block **off** to avoid double-filtering (which makes the tone muffled and muddy).

---

### Serial vs. Parallel Signal Routing

UltraRig allows building flexible signal paths using **Split** and **Merge** nodes:

* **Serial Routing:** Blocks are chained one after another ($Block_1 \to Block_2 \to Block_3$). The full output of one effect feeds into the next.
* **Parallel Routing:** The audio path divides into two independent branches (**Path A** and **Path B**) and blends back together at a Merge block:
  * **Bass Clean Blend:** Route low-end sub frequencies cleanly through Path A (with a compressor), while applying aggressive distortion/NAM on Path B. This preserves low-end punch and clarity.
  * **Parallel Time Effects:** Run delay and reverb in parallel branches so the reverb tail doesn't wash out repeated delay echoes.

---

### High-Pass (HPF) & Low-Pass (LPF) Filters

* **High-Pass Filter (HPF / Low Cut):** Cuts frequencies below a specified point.
  * *Guitar recommendation:* Set between **60 Hz and 80 Hz** to eliminate stage rumble and low-end flub.
  * *Bass recommendation:* Set around **30 Hz to 40 Hz** to remove inaudible sub-sonic speaker excursion.
* **Low-Pass Filter (LPF / High Cut):** Cuts harsh frequencies above a specified point.
  * *Guitar recommendation:* Set between **5.5 kHz and 7.0 kHz** to eliminate harsh digital "fizz" and recreate natural guitar speaker rolloff.

---

### Presets vs. Scenes (Zero-Gap Switching)

* **Preset Switching (Bank A–D):**
  * Loads an entirely new signal graph, NAM capture, and cabinet IR from the pedal's flash memory.
  * *Audio gap:* Takes a brief moment (a few milliseconds) to stream and instantiate new neural model weights.
* **Scene Switching (Scenes 1–4):**
  * Operates within the **currently active preset**.
  * Instantaneously changes block bypass states, delay feedback, gain levels, and EQ settings.
  * *Audio gap:* **0 ms (Zero-latency / seamless).** Perfect for switching between rhythm and lead tones mid-song without muting or audio clicks.

---

### Audio Buffer & Latency

* **Round-Trip Latency:** The total time taken for your guitar signal to enter the analog-to-digital converter (ADC), process through the DSP chain, and exit through the digital-to-analog converter (DAC).
* In UltraRig, internal buffer processing is tuned for **sub-3 millisecond** total latency—equivalent to standing approximately 1 meter (3 feet) from a physical guitar cabinet.

---

## 2. Frequently Asked Questions (FAQ)

### Q: Why does my tone sound buzzy, harsh, or like a "bee in a can"?
* **Cause:** Your Cabinet IR block is bypassed or disabled while playing directly into headphones, an audio interface, or a full-range PA system.
* **Solution:** Enable the **Cabinet IR** block in your preset and select a 1024-point speaker IR.

---

### Q: Why does my volume drop when engaging Chorus, Delay, or Reverb?
* **Cause:** Modulation and time-based effects have dedicated **Mix** and **Level** controls. If the dry/wet mix is set too high or the block output level is below unity gain (0 dB), the overall perceived volume may decrease.
* **Solution:** Set the effect **Level** knob to `0.0 dB` (unity) and adjust the blend using the **Mix** parameter (typically 20% to 35% for natural ambiance).

---

### Q: Can I load acoustic guitar or electric bass IRs?
* **Yes.** UltraRig accepts standard mono WAV impulse responses (44.1 kHz / 48 kHz, 24-bit). You can load acoustic guitar body resonance IRs, electric bass cabinet IRs (e.g. 8x10 or 4x10 cabs), or microphone captures.

---

### Q: Can I share presets between Tank-G and Tank-B?
* **Yes.** Both pedals share the same core firmware architecture and effects engine. A preset created for Tank-G can be imported into Tank-B (and vice-versa). However, bass-optimized presets typically emphasize parallel clean blends and lower center-frequency EQs.

---

### Q: Why did the tuner go silent on my heavy preset?
* **Cause:** Prior to Alpha 13.1, complex presets with high CPU utilization (NAM + long reverb + pitch octave) left insufficient memory for the chromatic tuner.
* **Solution:** Update to **UltraRig Alpha 13.1** or newer, which dynamically manages audio memory when engaging the tuner.
