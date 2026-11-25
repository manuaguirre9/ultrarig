# Electric Sitar & Jiwari Sympathetic Bridge Routing Guide

This guide details the non-linear grazing physics of the curved Indian ***Jiwari* (Jawari)** bridge, **Coral Electric Sitar** lipstick-pickup routing, tuned **13-string sympathetic *taraf* drone synthesis**, and preset configuration within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Acoustic Physics of the *Jiwari* Bridge & Sympathetic Strings

Designed in 1967 by Vincent Bell for Danelectro, the **Coral Electric Sitar** brought the exotic harmonic shimmer of classical Indian sitar onto iconic Western records (including Steely Dan's *Do It Again*, Metallica's *Wherever I May Roam*, and countless 1960s psychedelic pop hits). Whether amplifying a physical Coral/Jerry Jones sitar or synthesizing sitar textures from a standard electric guitar, the sound depends on two interconnected acoustic behaviors:

```
Guitar / Sitar String Vibration
   │
   ▼
[ Parabolic Curved "Jiwari" Bridge ] ──► Dynamic Grazing Point-Contact Modulation
   │ (Effective string length oscillates each cycle -> continuous harmonic energy cascade!)
   ├──► Bright Harmonic Buzz (1.8 kHz - 5.5 kHz) blooming 50-120 ms AFTER initial pluck
   │
   ▼
[ Sympathetic Drone Strings ("Taraf" Bank) ]
   └── 11 to 13 Resonant Comb Filters tuned to Raga Root / Fifth / Octave intervals
```

### 1.1 How the Curved *Jiwari* Bridge Works

1. **Dynamic Speaking-Length Modulation:** On a standard guitar, strings cross a sharp metal saddle, vibrating at fixed harmonics. On a sitar's sloped, parabolic *Jiwari* bridge (made of bone, Delrin, or horn), the oscillating string grazes smoothly up and down the curved surface on every wave cycle—continuously modulating its speaking length.
2. **Delayed Harmonic Bloom:** Instead of decaying duller over time like normal strings, energy cascades *upward* from the fundamental into shimmering upper harmonics ($1.8\text{ kHz} - 5.5\text{ kHz}$) ~50 ms after the pick strike, then decays back to pure fundamental tone.
3. **Sympathetic *Taraf* Halo:** Classical sitars (and the Coral Electric Sitar's side-mounted 13-string harp section) feature fine steel strings tuned to the mode/raga. When you play matching pitches on the fretboard, these drone strings resonate sympathetically without ever being plucked!

---

## 2. DSP Signal Chain & Processing Topology

```
Input (Physical Coral Electric Sitar OR Standard 6-String Guitar in Synth Mode)
   │
   ▼
[ High-Z 1MΩ Buffer & High-Pass Filter (110 Hz) ]
   │
   ├──► [ Optical Sustainer Compressor (Slow Attack 25 ms) ] (Enhances singing buzz decay)
   │
   ├──► [ Jiwari Grazing Synthesizer (Optional for Standard Guitars) ]
   │        └── Envelope-Shaped Asymmetric Wavefolder + Dynamic Mid-Buzz Peak (2.4 kHz - 4.8 kHz)
   │
   ├──► [ Parallel Sympathetic Comb Resonator Bank (Taraf Drone Matrix) ]
   │        └── Multi-Tap Tuned Feedback Comb Filters locked to Raga Root / 5th / Octave
   │
   ▼
[ Lipstick Tube / Clean Tweed Preamp Voicing + 2x12 Alnico Open-Back IR ]
   │
   ▼
[ Stereo Tape Slapback / Plate Reverb & Optional Reverse-Delay Psychedelia ] ──► Out
```

---

## 3. Parameter Specifications

| Parameter | Range | Default | Unit | Description |
| :--- | :--- | :--- | :--- | :--- |
| `SITAR_MODE` | `CORAL_REAL` / `JIWARI_SYNTH` | `JIWARI_SYNTH` | mode | Routing for physical electric sitar pickups vs. guitar-to-sitar DSP synthesis. |
| `JIWARI_BUZZ` | `0` - `100` | `65` | % | Intensity of dynamic grazing harmonic bloom ($2.4\text{ kHz} - 4.8\text{ kHz}$). |
| `SYMP_DRONE_LVL`| `0` - `100` | `45` | % | Volume of the tuned sympathetic *taraf* comb resonator halo. |
| `DRONE_ROOT` | `C` to `B` | `E` | note | Fundamental root key tuning the sympathetic drone matrix. |
| `RAGA_VOICING` | `YAMAN` / `BHAIRAV` / `DORIAN` / `5TH_OCT` | `5TH_OCT` | scale | Interval tuning across sympathetic string banks. |
| `DRONE_DECAY` | `0.5` - `6.0` | `2.6` | s | Resonance sustain time of sympathetic sympathetic ringing strings. |
| `LIPSTICK_SNAP` | `0` - `100` | `55` | % | Danelectro Lipstick single-coil upper-mid chime and sparkle. |
| `GLARE_TAMER` | `0` - `100` | `35` | % | Smooths excessive metallic ringing above $5.8\text{ kHz}$ on bright pickups. |
| `MIX_WET_DRY` | `0` - `100` | `75` | % | Blend between direct electric tone and synthesized sitar buzz + drones. |

---

## 4. Factory Scene Presets

### Scene A: Coral Electric Sitar 60s Pop (Steely Dan / Paint It Black)
- **Concept:** The unmistakable 1967 studio electric sitar sound—crisp Lipstick single-coil chime, signature Delrin bridge buzz, and warm vintage plate ambiance.
- **Settings:** `SITAR_MODE = CORAL_REAL` (or `JIWARI_SYNTH = 55%` on standard Strat bridge pickup), `DRONE_ROOT = E`, `SYMP_DRONE_LVL = 35%`, `LIPSTICK_SNAP = 68%`.
- **Space:** Vintage Studio Plate Reverb (`1.9 s`, `24%` mix) + subtle tape slapback (`110 ms`).

### Scene B: Ravish Drone Raga Meditation (13 Sympathetic Taraf Strings)
- **Concept:** Deep, hypnotic Indian classical atmosphere transforming standard electric guitar melodies into singing sitar phrases over rich sympathetic drones.
- **Settings:** `SITAR_MODE = JIWARI_SYNTH`, `JIWARI_BUZZ = 78%`, `DRONE_ROOT = D`, `RAGA_VOICING = BHAIRAV`, `SYMP_DRONE_LVL = 65%`, `DRONE_DECAY = 4.2 s`.
- **Space:** Intimate Wooden Chamber (`2.2 s`, `26%` mix).

### Scene C: Psychedelic Rock Sitar Lead (Beatles Revolver / Tomorrow Never Knows)
- **Concept:** Saturated, swirling late-60s sitar lead running through a slightly breaking-up Fender Tweed / Vox preamp with tape flanging!
- **Settings:** `JIWARI_BUZZ = 70%`, `SYMP_DRONE_LVL = 40%`, gentle Tweed preamp crunch (`GAIN = 45%`), slow Tape Through-Zero Flanging (`0.18 Hz`).
- **Space:** Analog Tape Echo (`360 ms`, `30%` feedback).

### Scene D: Modern Ambient Sympathetic Cloud (World Fusion)
- **Concept:** Ethereal ambient sitar textures weaving resonant drone harmonics into lush dotted-8th stereo delays and vast hall reverbs.
- **Settings:** `JIWARI_BUZZ = 45%`, `SYMP_DRONE_LVL = 55%`, `DRONE_DECAY = 5.0 s`.
- **Space:** Stereo Modulated Ping-Pong Delay (`440 ms`) + Shimmer Cathedral Hall (`5.2 s`).

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (Coral 60s Pop) / Scene B (Ravish Drone Raga).
- **Footswitch B:** Scene C (Psychedelic Rock Sitar).
- **Footswitch C:** Scene D (Ambient Sympathetic Cloud) / Tuner.
- **Knob 1 (MOD FX):** Sympathetic Drone Root Key (`C` through `B`) for instant song-key matching!
- **Knob 2 (GAIN / BUZZ):** *Jiwari* Grazing Buzz intensity.
- **Knob 3 (REVERB / DRONE):** Sympathetic *Taraf* Halo & Plate Reverb mix.

### Tank-B Control Assignments
- Experimental and world-fusion bassists can turn standard electric bass lines into haunting **Surbahar** (bass sitar!) performances using Scene B (`DRONE_ROOT = E` or `D`, `HPF = 45 Hz`) for massive low-register raga resonance!

### Black Box Desktop Configuration
- **Expression Pedal 1:** Morph smoothly between standard clean Lipstick electric guitar (`JIWARI_BUZZ = 0%`) and full sympathetic *Jiwari* sitar bloom (`JIWARI_BUZZ = 85%`) mid-solo!
- **Dual Input Mode (For Physical Coral Sitars):** Plug the Main Sitar Neck pickup into Input L and the dedicated Sympathetic Drone Harp pickup into Input R for independent EQ and stereo panning!
