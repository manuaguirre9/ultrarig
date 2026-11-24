# Bass Guitar Rig Optimization & Tone Guide for Tank-B & UltraRig

With the release of **UltraRig Alpha 13+**, official firmware packages are available for the **M-VAVE Tank-B** (and Tank-G pedals running the bass package). This guide provides essential techniques for setting up professional electric bass tones, utilizing parallel routing for clean low-end blend, dialing in compression, and choosing bass-specific NAM captures and cabinet IRs.

---

## 1. The Core Philosophy of Digital Bass Tone

Unlike electric guitars, where the entire frequency spectrum is typically saturated through an amplifier and speaker cabinet, electric bass requires **two simultaneous priorities**:

1. **Sub-Low Foundation (35 Hz – 180 Hz):** Must remain tight, undistorted, phase-coherent, and dynamically consistent to lock in with the kick drum.
2. **Harmonic Midrange & Bite (500 Hz – 3.5 kHz):** Requires harmonic saturation, drive, or modulation to cut through dense band mixes and sound rich on small consumer speakers.

In UltraRig, this is achieved effortlessly using **Parallel Split/Merge Routing**.

---

## 2. Parallel Clean Blend Routing Architecture

When bass runs through a conventional serial distortion or chorus pedal, the low fundamental frequencies lose their punch and collapse into a muddy mess.

### Recommended Signal Chain Layout:
```text
[Input] -> [Noise Gate] -> [Compressor] -> [Parallel Split]
                                |
     +--------------------------+--------------------------+
     |                                                     |
  [Path A: Clean Low-End]                     [Path B: Grunt & Drive]
  - HPF: 35 Hz / LPF: 220 Hz                  - HPF: 200 Hz
  - Level: Unity (0.0 dB)                     - NAM Preamp: Darkglass / SVT
                                              - Chorus / Drive Block
     |                                                     |
     +--------------------------+--------------------------+
                                |
                        [Parallel Merge]
                                |
                    [1024-pt Bass Cabinet IR]
                                |
                          [Master Out]
```

### Path Breakdown:
* **Path A (Clean Sub-Path):**
  * Insert an EQ block with a **Low-Pass Filter (LPF) set to ~200–250 Hz**.
  * This passes only the pure, undistorted fundamental frequencies of the low E and B strings.
* **Path B (Grit / Mod Path):**
  * Insert an EQ block with a **High-Pass Filter (HPF) set to ~200 Hz** to remove the subs *before* hitting the overdrive or NAM amp capture.
  * Add your high-gain distortion, fuzz, or chorus here. Because the low-end is handled by Path A, you get all the aggressive metallic clank without losing sub-bass authority.
* **Merge:** Blend Path A and Path B at a 60/40 or 50/50 ratio.

---

## 3. Compression Techniques for Bass

Bass guitar produces tremendous dynamic spikes between fingerstyle, pick playing, and thumb slaps.

### Settings for Optical-Style Smooth Leveling:
* **Threshold:** Set so the meter shows **$3\text{ dB}$ to $6\text{ dB}$ of gain reduction** on typical notes, and up to $8\text{ dB}$ on heavy slaps.
* **Ratio:** `3:1` or `4:1` for natural dynamic control; `6:1` or `8:1` for modern metal or pop consistency.
* **Attack Time:** **$20\text{ ms}$ to $40\text{ ms}$ (Medium-Slow).**
  * *Critical:* If attack is too fast ($< 5\text{ ms}$), the compressor will squash the initial transient "thump" of the string attack, making the bass sound lifeless and pushed back in the mix.
* **Release Time:** **$100\text{ ms}$ to $200\text{ ms}$ (Medium-Fast).** Ensures the compressor recovers before the next note is struck.

---

## 4. Selecting NAM Preamp Captures for Bass

Look for embedded **A2-Lite** profiles on platforms like ToneHunt:

| Preamp / Amp Model | Sonic Character | Ideal Musical Genre |
|---|---|---|
| **Ampeg SVT / V4B** | Tube warmth, pillowy low-end, growly mid-range push. | Rock, Blues, Funk, Classic Metal |
| **Ampeg B-15 Portaflex** | Motown vintage roundness, warm mid focus. | Soul, R&B, Jazz, Indie |
| **Darkglass B7K / Vintage Ultra** | Aggressive upper-mid clank, scoop, modern saturation. | Progressive Metal, Modern Rock, Djent |
| **Noble Tube Preamp / DI** | Ultra-clean, three-dimensional high-headroom tube depth. | Gospel, Worship, Pop, Studio Session |
| **Gallien-Krueger 800RB** | Fast solid-state transient punch, "growl" in the 800 Hz range. | Punk, 90s Grunge, Alternative |

---

## 5. Choosing Bass Cabinet IRs (1024 Points)

* **8x10 Sealed Enclosure (Ampeg "Fridge"):**
  * Tight, fast bass response with natural acoustic rolloff below 50 Hz.
  * Best for cutting through dense drum kits without rumbling the stage.
* **4x10 Ported Enclosure (Hartke / Eden / Markbass):**
  * Extended sub-lows down to 35 Hz with a horn tweeter for high-end slap articulation.
* **1x15 Enclosure:**
  * Slow, warm, deep low-end bloom. Ideal for reggae, dub, and vintage rock.
* **Microphone Pairings:** Look for IRs captured with dynamic kick/bass mics: **AKG D112**, **Shure Beta 52A**, **Electro-Voice RE20**, or **Neumann U47 FET**.

---

## 6. Recommended 4-Scene Layout for Live Bassists

Within a single preset, configure the **4 Scenes** for hands-free live versatility:

1. **Scene 1: Fingerstyle Clean**
   - Clean NAM Preamp + Subtle Compression + 8x10 IR.
2. **Scene 2: Vintage Tube Drive**
   - Engages SVT drive path with parallel clean blend for verses and driving choruses.
3. **Scene 3: Modern Clank / Heavy Distortion**
   - Darkglass-style drive + Bright EQ boost at 2.5 kHz for metal breakdowns or solos.
4. **Scene 4: Synth / Ambient Wet**
   - Parallel Sub-Octave + Analog Chorus + Plate Reverb for intros or melodic bass interludes.
