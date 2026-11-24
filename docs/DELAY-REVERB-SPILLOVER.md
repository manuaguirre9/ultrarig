# UltraRig Delay & Reverb Spillover (Trails) Guide

In live performance, transitioning from an expansive guitar solo drenched in ambient reverb and dotted-eighth delay back to a tight, dry rhythm riff often results in a jarring, unnatural **"audio chop"** if the spatial effects cut off abruptly.

**Spillover (also known as "Trails")** allows existing delay repeats and reverberation tails to ring out naturally across scene transitions, even after the effect has been turned off or switched to a dry sound.

Because UltraRig executes its **4 Scenes per Preset (A, B, C, D)** inside a unified, persistent DSP memory graph, it delivers true zero-latency scene switching with seamless delay and reverb spillover.

---

## 1. Presets vs. Scenes: Why Spillover Requires Scenes

```
  ┌────────────────────────────────────────────────────────────────────────┐
  │                           PRESET SWITCHING                             │
  │  Preset 01 (Lead)  ──────────────────────────────>  Preset 02 (Rhythm) │
  │  - Flushes DSP RAM                                                     │
  │  - Re-allocates audio buffers                                          │
  │  - Re-loads NAM neural network weights                                 │
  │  RESULT: Complete audio mute (~50-100 ms); spillover impossible        │
  └────────────────────────────────────────────────────────────────────────┘

  ┌────────────────────────────────────────────────────────────────────────┐
  │                            SCENE SWITCHING                             │
  │  Scene A (Solo Lead) ───────────────────────────>  Scene B (Dry Riff)  │
  │  - Runs inside the same active DSP graph                               │
  │  - Audio buffers remain intact                                         │
  │  - Seamless parameter interpolation                                    │
  │  RESULT: 0.0 ms audio dropout; perfect, natural delay & reverb trails  │
  └────────────────────────────────────────────────────────────────────────┘
```

> [!IMPORTANT]
> Switching between completely different presets (e.g., Bank 1 Preset 1 to Bank 1 Preset 2) flushes pedal DSP memory, abruptly clearing all delay lines. **Always configure your rhythm, crunch, lead, and ambient sounds as Scenes (A, B, C, D) within the same Preset** to achieve spillover.

---

## 2. Bypass Modes: Hard Cut vs. Trails (Mute Input)

Understanding how a digital delay or reverb block handles bypass is key to dialing in spillover:

```
                          ┌── [ Hard Bypass ] ──> Mutes Output Immediately (Sudden Cut)
 [ Wet Effect Engine ] ───┤
                          └── [ Trails Bypass ] ──> Mutes Input Only; Output Decays Naturally
```

### Hard Bypass (Mute Output)
* **How it works:** Instantly disconnects the effect's output from the signal chain.
* **Result:** Any repeats currently bouncing in the delay line or acoustic reflections in the reverb tank are immediately silenced.
* **When to use:** Sudden dramatic stops, staccato funk rhythms, or when you want complete, dead silence on a downbeat.

### Trails / Spillover Bypass (Mute Input)
* **How it works:** Disconnects the **input** feed into the effect while keeping the **output** connected to the mixer bus.
* **Result:** Newly played guitar notes pass straight through dry, but notes played *before* the switch continue repeating and reverberating until their energy dissipates naturally.
* **When to use:** Moving from a guitar solo back to rhythm verses, or transitioning from ambient clean intros into heavy riffs.

---

## 3. Two Methods to Configure Spillover in UltraRig

### Method 1: The Native "Trails" Toggle (Quick & Easy)
1. Open the UltraRig Web Editor and select your preset.
2. Click on the **Delay** or **Reverb** block to open its parameter inspector.
3. Locate the **Bypass Mode** dropdown.
4. Change the setting from `Hard Cut` to **`Trails`** (or toggle `Spillover: ON`).
5. In **Scene A (Lead)**, set the block to **Enabled** (`ON`).
6. In **Scene B (Rhythm)**, set the block to **Bypassed** (`OFF`).
7. When you step on Footswitch B, the block bypasses via Mute-Input, letting existing repeats fade out naturally while your rhythm notes stay bone dry.

---

### Method 2: Parallel Wet/Dry Routing with Send Muting (Studio Pro Method)

For complete control over spatial decay without any phase interaction with the direct guitar signal, route your time-based effects into a dedicated parallel branch:

```
                            ┌──> [ Direct Dry Guitar Path ] ───────────────────────────┐
 [ Guitar / Drive / NAM ] ──┤                                                           ├──> [ Merge ] ──> [ Out ]
                            └──> [ Branch B Mute Node ] ──> [ Delay ] ──> [ Reverb ] ──┘
                                 (100% Wet Effects on Parallel Branch)
```

1. Insert a **Split** block after your NAM Amp and Cabinet IR blocks.
2. Route your direct signal through **Branch A**.
3. Place your **Delay** and **Reverb** blocks on **Branch B**, and set their internal `Mix` controls to **100% Wet**.
4. Configure Scene parameters:
   - **Scene A (Lead):** Branch B Input Level = `0.0 dB`.
   - **Scene B (Rhythm):** Branch B Input Level = `-INF` (Muted).
   - In both scenes, leave the Branch B **Output Return** open at `0.0 dB`.
5. When switching from Scene A to Scene B, new guitar notes stop entering Branch B, but the reverb tail and delay repeats already inside Branch B continue flowing through the Merge block into the main output.

---

## 4. Avoiding the "Delay Time Pitch Warble" Trap

A common pitfall occurs when guitarists set different delay times across scenes (e.g., Scene A has a 500 ms quarter-note delay, while Scene B has a 250 ms eighth-note delay).

```
 Scene A (500 ms Delay) ──[ Scene Switch ]──> Scene B (250 ms Delay)
                                │
                                ▼
         [ Virtual Tape Speed Halves / Buffer Repositioned ]
                                │
                                ▼
         UNINTENDED PITCH WARBLE (Tape Slew / Pitch Dive Artifact)
```

### Why it Happens:
Analog-modeled and tape-style digital delays simulate physical tape head distance or bucket-brigade clocking. Changing the `Time` parameter while audio is decaying in the buffer forces the algorithm to stretch or compress the waveform, producing an audible pitch shift (like turning the time knob on a Boss DM-2 or tape echo).

### How to Prevent It:
1. **Lock Delay Time Across Scenes:** Keep the `Time` parameter identical between scenes (e.g., exactly 375 ms or synchronized to the same Tap Tempo BPM subdivision).
2. **Modulate Mix and Feedback Instead:**
   - In **Scene A (Solo):** Set `Delay Mix = 35%`, `Feedback = 45%`.
   - In **Scene B (Rhythm):** Set `Delay Mix = 0%` (or bypass with Trails).
3. Because the time parameter never moves, the buffer decays at constant tape speed with **zero pitch warbling**.

---

## 5. Preventing Reverb & Delay Feedback Runaway

* **Check Max Feedback:** Ensure delay feedback does not exceed 85–90%. Setting feedback to 100% or higher creates an infinite loop that will never decay, eventually overloading the DSP buffer into digital clipping.
* **Reverb Decay Time:** On long ambient reverbs with decay times over 4.0 seconds, high-frequency damping (Damp parameter around 4.5 kHz) prevents high-end build-up from muddying your rhythm tone across scene transitions.

---

## 6. Pre-Flight Spillover Verification Checklist

- [ ] Rhythm and lead tones configured as **Scenes (A/B/C/D)** within a single preset, not across separate presets.
- [ ] Delay / Reverb **Bypass Mode** set to `Trails` (Mute Input).
- [ ] Delay `Time` parameter locked or Tap-Tempo synchronized between scenes to avoid pitch warbling.
- [ ] Delay feedback configured under 85% to ensure natural decay.
- [ ] Reverb high-frequency damping enabled to prevent ambient build-up in dense band mixes.
