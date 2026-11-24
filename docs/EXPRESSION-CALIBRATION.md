# Expression Pedal Calibration & Dynamic Control Guide

This guide explains how to connect, calibrate, and assign an external **Expression Pedal** in **UltraRig** (via TRS jack or external MIDI controllers like the M-VAVE Chocolate), allowing dynamic control over Wah, Volume swells, Pitch Whammy, Delay/Reverb mix, and Amp Gain.

---

## 1. Hardware Connections & TRS Wiring

Expression pedals typically use a **1/4" TRS (Tip-Ring-Sleeve) stereo cable**:

* **Standard Wiring Polarities:**
  * **Tip-Active (Standard / Roland / Boss / M-VAVE):**
    * `Tip`: Wiper (variable voltage signal)
    * `Ring`: $+3.3\text{V} / +5\text{V}$ reference voltage
    * `Sleeve`: Ground (GND)
  * **Ring-Active (Line 6 / Moog standard):**
    * `Ring`: Wiper
    * `Tip`: Reference voltage
    * `Sleeve`: Ground
* **Recommended Potentiometer Value:** **$10\text{k}\Omega$ to $25\text{k}\Omega$ Linear (Type B)** potentiometer taper offers the smoothest, most predictable sweep. Using a $100\text{k}\Omega$ or $250\text{k}\Omega$ volume pedal as an expression pedal can cause a steep "jump" near the toe position.

> [!TIP]
> If your expression sweep is backward (100% at heel and 0% at toe), toggle the **Invert Polarity** option in the UltraRig Web Editor or flip the polarity switch on your expression pedal.

---

## 2. Step-by-Step Calibration Procedure

To ensure a full $0$ to $127$ MIDI / DSP range without jitter or dead spots:

1. **Connect the Pedal:** Plug your expression pedal into the expression jack (or through an external MIDI foot controller mapped to `CC #11`).
2. **Open the Web Editor:** In Chrome/Edge, navigate to **Settings > Expression & Controllers**.
3. **Calibrate Heel Position (Minimum):**
   - Rock the pedal all the way back to the **Heel-Down** position.
   - Click **Set Heel**. The editor records the lowest raw ADC voltage.
4. **Calibrate Toe Position (Maximum):**
   - Push the pedal all the way forward to the **Toe-Down** position.
   - Click **Set Toe**. The editor records the highest raw ADC voltage.
5. **Adjust Deadzones:**
   - Add a $2\%$ to $4\%$ deadzone at both ends. This prevents physical wear or loose foot pressure from causing fluttering parameter values when your foot leaves the pedal.
6. **Save Calibration:** Click **Save Hardware Settings**. The calibration is stored in the pedal's persistent memory and applies globally across all presets.

---

## 3. Creative Assignment Targets

In the UltraRig Web Editor, an expression pedal can be assigned to modulate virtually any parameter:

### A. Classic Wah-Wah / Envelope Sweep
* **Target Block:** Filter / Wah
* **Target Parameter:** Center Frequency (`400 Hz` to `2.4 kHz`)
* **Toe Switch / Engage:** Set the pedal to auto-engage when moving above the 5% threshold, and auto-bypass after remaining in the heel-down position for 1.5 seconds.

### B. Pre-Amp vs. Post-Amp Volume Swell
* **Pre-Amp Volume (In front of NAM Amp):**
  * Acts just like your guitar's volume knob.
  * Rocking back cleans up amplifier gain and saturation while keeping output volume relatively consistent.
* **Post-Amp / Post-Cabinet Volume (Master Swell):**
  * Placed after the Cabinet IR block.
  * Controls overall output volume without changing amplifier distortion—ideal for violin-like volume swells with trailing reverb.

### C. Pitch Whammy / Octave Glide
* **Target Block:** Pitch Shifter
* **Target Parameter:** Pitch Shift (`0 semitones` at heel $\to$ `+12 semitones` / +1 Octave at toe).
* **Curve:** Linear sweep for smooth, glissando pitch bends.

### D. Ambient Morphing (Delay & Reverb Spill)
* Modulate multiple parameters simultaneously:
  * Delay Mix: $15\% \to 60\%$
  * Delay Feedback: $25\% \to 75\%$
  * Reverb Decay: $1.8\text{ s} \to 6.5\text{ s}$
* Rocking forward smoothly transitions your tone from a tight rhythm sound into a massive ambient wash without switching presets.

---

## 4. Troubleshooting Common Issues

| Symptom | Cause | Solution |
|---|---|---|
| **Value jumps suddenly near toe** | Logarithmic (audio taper) pot in pedal | Use an expression pedal with a linear ($10\text{k}\Omega$ 'B') pot. |
| **Values flutter when foot is off** | Physical potentiometer tolerance/noise | Increase the Heel/Toe deadzone to $3-5\%$ in the editor. |
| **Sweep is reversed** | Opposite TRS polarity (Tip vs Ring) | Enable "Invert" in the Web Editor or flip the pedal's polarity switch. |
| **No response from pedal** | Unconnected wiper or stereo cable fault | Verify you are using a stereo TRS cable, not a mono TS guitar cable. |
