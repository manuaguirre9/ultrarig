# Noise Gate Calibration & Sustain Optimization Guide for UltraRig

This guide explains how to configure and fine-tune the internal **Noise Gate** in **UltraRig** (Tank-G, Tank-B, Black Box) to eliminate 60-cycle single-coil hum, preamp tube hiss, and high-gain feedback without cutting off natural note sustain or introducing artificial gate chattering.

---

## 1. The Fundamental Noise Gate Challenge

A poorly configured noise gate ruins musical expression:
* **Threshold Set Too High:** Sustained lead notes choke out abruptly, quiet fingerpicking passages get silenced, and chord decays stutter into silence ("gate chatter").
* **Threshold Set Too Low:** Amplifier feedback screeches during pauses, single-coil electromagnetic hum rings through, and high-gain background hiss remains audible.

UltraRig's DSP noise gate utilizes an adaptive envelope detector designed to respond dynamically to pick attack while providing smooth exponential decay.

---

## 2. Parameter Definitions & How They Work

| Parameter | Function | Recommended Starting Range |
|---|---|---|
| **Threshold (dB)** | The signal level below which the gate begins closing and attenuating audio. | **$-65\text{ dB}$ to $-45\text{ dB}$** |
| **Attack Time (ms)** | How quickly the gate opens to 100% volume once a pick strike crosses the threshold. | **$0.5\text{ ms}$ to $1.5\text{ ms}$ (Fast)** |
| **Hold Time (ms)** | How long the gate remains 100% open after the signal dips below the threshold. | **$10\text{ ms}$ to $35\text{ ms}$** |
| **Decay / Release (ms)** | How smoothly the gate attenuates volume down to silence. | **$150\text{ ms}$ to $400\text{ ms}$** |
| **Reduction (dB)** | Maximum amount of attenuation applied when fully closed. | **$-60\text{ dB}$ (Full Mute) or $-24\text{ dB}$ (Soft Tame)** |

---

## 3. Placement in the Signal Chain: The Golden Rules

Where you place the noise gate in UltraRig's signal graph dictates how it responds:

```text
[Guitar In] ---> [Noise Gate] ---> [NAM Preamp] ---> [Delay & Reverb] ---> [Cab IR]
                       ^                                   ^
                       |                                   |
           (Controls pick dynamics)            (Must NEVER be before the gate!)
```

> [!CAUTION]
> **Never Place Delay or Reverb Before the Noise Gate!**
> If delay echoes or reverb ambient decays are placed before the gate, the gate will abruptly chop off the trailing repeats as soon as their volume drops below the threshold. Always place time-based effects **after** the gate block.

---

## 4. Tuning Recipe A: High-Gain Modern Rock & Djent

For percussive, tight, palm-muted staccato riffs on 7-string or 8-string guitars with high-gain NAM captures (5150, Dual Rectifier, ENGL):

* **Goal:** Instantaneous silence between palm-muted chugs with zero background hiss.
* **Settings:**
  * **Threshold:** Set to around **$-48\text{ dB}$ to $-42\text{ dB}$**.
  * **Attack:** **$0.1\text{ ms}$ (Instantaneous).** Preserves aggressive pick attack.
  * **Hold:** **$5\text{ ms}$ to $15\text{ ms}$.**
  * **Decay / Release:** **$40\text{ ms}$ to $80\text{ ms}$ (Very Fast).** Snaps shut the instant the palm rests on the strings.
  * **Reduction:** **$-70\text{ dB}$ (Complete silence).**

---

## 5. Tuning Recipe B: Blues & Classic Rock (Preserving Long Sustain)

For singing guitar solos, blues bends, and vintage single-coil Strat/Tele playing:

* **Goal:** Tame electromagnetic 60 Hz idle hum while allowing gentle note decays and volume swells to ring out naturally for 5+ seconds.
* **Settings:**
  * **Threshold:** **$-60\text{ dB}$ to $-54\text{ dB}$ (Gentle).**
  * **Attack:** **$1.0\text{ ms}$.**
  * **Hold:** **$35\text{ ms}$ to $50\text{ ms}$.** Prevents gate chattering on low notes.
  * **Decay / Release:** **$300\text{ ms}$ to $500\text{ ms}$ (Smooth Exponential Rolloff).** Notes fade away seamlessly without a sudden cliff edge.
  * **Reduction:** **$-24\text{ dB}$ to $-30\text{ dB}$ (Soft Attenuation).** Rather than a hard digital clamp, soft reduction drops the noise floor below ambient room levels while keeping the audio path alive.

---

## 6. Single-Coil Pickups & 60-Cycle Hum Solutions

Single-coil pickups act like antennas, picking up electromagnetic interference (EMI) from stage lighting dimmers, neon signs, and computer monitors:

1. **Gate Calibration Routine for Strats/Teles:**
   - Switch your guitar to position 1 (Bridge) or position 5 (Neck).
   - Turn your guitar's volume knob to 10.
   - Rest your hands on the strings without playing.
   - In the UltraRig Web Editor, slowly raise the **Threshold** slider until the background hum completely disappears.
   - Now play a soft, gentle note. If the note sounds choked, back the threshold down by $2\text{ dB}$ and increase **Decay** to $350\text{ ms}$.
2. **Utilize Hum-Canceling Positions:**
   - In 3-pickup guitars with reverse-wound middle pickups, positions 2 and 4 (Bridge+Middle, Neck+Middle) naturally cancel 60-cycle hum. Calibrate your gate for position 1/5 so it remains completely quiet on all pickup selections.

---

## 7. Scene-Based Gating Strategy

Take advantage of UltraRig's **4 Scenes per Preset** to adapt the gate dynamically:
* **Scene 1 (Clean):** Gate **BYPASSED** (allows ultra-quiet fingerpicking dynamics).
* **Scene 2 (Rhythm Crunch):** Gate **ACTIVE** (Tight, fast decay for riffs).
* **Scene 3 (Lead Solo):** Gate **ACTIVE** with **Long Decay ($400\text{ ms}$)** for singing sustain.
* **Scene 4 (Ambient):** Gate **BYPASSED** with long trailing reverbs.
