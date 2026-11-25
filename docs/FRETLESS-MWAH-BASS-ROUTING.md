# 5 & 6-String Fretless Bass ("Mwah" Vocal Accentuation) Routing Guide

This guide details the fingerboard acoustics behind the signature fretless **"mwah"**, optical sustain shaping, mono-safe stereo chorus crossovers, and preset configuration for **5- and 6-String Fretless Bass Guitars** within UltraRig for M-VAVE hardware (Tank-B, Tank-G v1/v2, and Black Box).

---

## 1. Acoustic Physics of the Fretless "Mwah" Voice

Unlike fretted electric basses—where strings ring cleanly off rigid metal fret wires—a **Fretless Bass** terminates strings directly beneath the player's fingertip against a smooth, unfretted ebony, rosewood, or epoxy-coated fingerboard.

```
5-String Fretless:  B0 (30.87 Hz) | E1 (41.2 Hz) | A1 | D2 | G2
6-String Fretless:  B0 (30.87 Hz) | E1 | A1 | D2 | G2 | C3 (130.8 Hz High Chordal String)
```

### 1.1 What Creates the Iconic "Mwah"?

1. **Micro-Grazing Fingerboard Bounce:** As the bowed-like plucked string oscillates, its waveform grazes microscopically along the wooden fingerboard directly ahead of the fretting finger. This introduces subtle non-linear overtones centered between **$850\text{ Hz}$ and $1.6\text{ kHz}$** while softening the initial pick/finger transient—producing a singing, vocal envelope swell (*"mwah"*).
2. **Extended Sustain & Glissando Continuity:** Without metal frets providing crisp energy reflection, notes decay faster on bare wood fingerboards. Clean, transparent **Optical Compression** with a slow attack ($30\text{ ms} - 45\text{ ms}$) lets the natural envelope swell naturally while extending legato slide sustain effortlessly.
3. **Roundwound vs. Flatwound String Compensation:**
   - **Roundwound Strings (Jaco Pastorius / Gary Willis):** Maximize bright growl and intense *mwah* overtones, but generate string-slide hiss above $4.5\text{ kHz}$ that needs gentle high-shelf smoothing.
   - **Flatwound / Tapewound Strings (Pino Palladino / Upright Feel):** Deliver deep wooden thump ($160\text{ Hz} - 350\text{ Hz}$) and require a broader midrange boost around $1.1\text{ kHz}$ to bring the *mwah* out in dense mixes.

---

## 2. DSP Signal Chain & Processing Topology

```
5/6-String Fretless Bass In (Bridge J-Pickup Focus / Dual Humbucker)
   │
   ▼
[ Subsonic High-Pass Filter (30 Hz, 24 dB/oct Butterworth) ] (Protects speakers while keeping B0 = 30.87 Hz)
   │
   ▼
[ Optical Sustainer Compressor (LA-2A Style: Slow Attack 35 ms / Smooth Release) ]
   │
   ▼
[ Parametric "Mwah" Vocal Formant EQ ]
   ├── Low Mud Dip: -3.0 dB @ 280 Hz (Clears boxy boom on 5-string B0/E1)
   ├── "Mwah" Focus: +4.5 dB @ 1.15 kHz (Q = 1.4 - Singing vocal harmonic presence)
   └── Finger-Slide Sibilance Cut: Low-Pass / Soft Shelf @ 4.8 kHz (For Roundwounds)
   │
   ▼
[ Vintage Bass Preamp Model (Acoustic 360 OR Ampeg B-15N Portaflex) ]
   │
   ▼
[ Linkwitz-Riley 180 Hz Crossover ]
   ├── Low Band (< 180 Hz) ──► Strictly MONO & Unmodulated (Preserves chest punch) ──┐
   └── High Band (> 180 Hz) ─► [ Stereo BBD Chorus / Octave-Up / Plate Reverb ] ─────┴──► Hybrid 2x10 + 1x15 IR ──► Out
```

---

## 3. Parameter Specifications

| Module | Parameter | Recommended Value | Purpose |
| :--- | :--- | :--- | :--- |
| **Input Filter**| High-Pass Filter | `30 Hz` (24 dB/oct) | Removes sub-audible rumble while preserving $B_0$ ($30.87\text{ Hz}$). |
| **Optical Comp**| Ratio / Attack / Rel| `3.0:1` / `35 ms` / `220 ms` | Extends smooth slide sustain without squashing vocal swell. |
| **Mud Clean** | Freq / Q / Gain | `280 Hz` / `Q=1.8` / `-3.0 dB`| Removes muddy cabinet congestion across low registers. |
| **Mwah Peak** | Freq / Q / Gain | `1.15 kHz` / `Q=1.4` / `+4.5 dB`| Accentuates singing woody fingerboard overtones. |
| **Slide Tamer**| High-Frequency Damping| `4.8 kHz` (`-3.5 dB`)| Tames roundwound finger-slide scratch without dulling tone. |
| **Amp Model** | Voicing | `Acoustic 360` / `Ampeg B-15` | Solid-state Jaco punch vs. warm tube upright bloom. |
| **Crossover** | Split Frequency | `180 Hz` | Keeps sub-bass anchored in mono beneath stereo chorus. |
| **Cabinet IR** | Speaker Profile | `Hybrid_2x10_1x15.wav` | Tight midrange focus (2x10) with deep 15" bottom weight. |
| **Reverb** | Type / Decay / Mix | `Studio Plate` / `2.1 s` / `22%`| Adds lush vocal space behind fretless melodies. |

---

## 4. Factory Scene Presets

### Scene A: Jaco Pastorius Bridge Punch & Chorus (Word of Mouth)
- **Concept:** The quintessential 1970s Weather Report fretless tone: biting rear Jazz pickup growl, tight 1.1 kHz vocal punch, and spacious chorus shimmer.
- **Amp & EQ:** Acoustic 360 Preamp emulation, `MWAH_BOOST = +5.0 dB @ 1.2 kHz`, mud dip at `290 Hz`.
- **Modulation:** Subtle Analog BBD Chorus (`0.65 Hz`, applied strictly above `180 Hz`).
- **Space:** Intimate Studio Room (`1.1 s`, `14%` mix).

### Scene B: Pino Palladino 80s Pop Fretless (Octaver + Chorus)
- **Concept:** Massive, singing, synth-like 1980s fretless tone (Paul Young / Don Henley) uniting an octave divider with lush stereo chorus and plate reverb.
- **Pitch & Mod:** Analog Sub-Octave (`-12 st` blended at `35%` for upper-neck solos) + Dimension D Stereo Chorus (`Mode 3`).
- **Space:** Glossy 80s Studio Plate Reverb (`2.6 s`, `28%` mix).

### Scene C: 6-String Chordal Ambient Solo (Steve Bailey / Michael Manring)
- **Concept:** Crystal-clear, orchestral hi-fi solo voicing allowing extended chords on the high $C_3$ string and singing low $B_0$ pedal drones.
- **Dynamics:** Transparent optical leveling (`2.5:1`), wide-range clean preamp (`Ampeg B-15` flat mode).
- **Space:** Modulated Stereo Ping-Pong Delay (`420 ms`, `30%` feedback) into Cathedral Hall Reverb (`4.2 s`).

### Scene D: Warm Motown Upright Flatwound Feel (Woody Acoustic Vibe)
- **Concept:** Deep, organic, acoustic double-bass-inspired fretless groove perfect for jazz ballads, soul, and neo-soul.
- **Amp & EQ:** Ampeg B-15N Flipped-Top tube preamp (`DRIVE = 28%`), smooth high-cut filter at `3.2 kHz`, low-mid bloom at `210 Hz (+2 dB)`.
- **Space:** Warm Wooden Studio Chamber (`1.4 s`, `16%` mix).

---

## 5. Hardware Setup & Mapping

### Tank-B Control Assignments
- **Built-in Fretless Machine:** Tank-B's dedicated $30\text{ Hz}$ subsonic HPF, optical compressor, and 180 Hz mono-safe chorus crossover make it an exceptional stage rig for 5- and 6-string fretless bassists.
- **Footswitch 1:** Scene A (Jaco Bridge Punch) / Scene B (Pino Octaver + Chorus).
- **Footswitch 2:** Scene C (6-String Ambient Solo) / Scene D (Woody Upright Feel).
- **Knob 1 (EQ / MWAH):** Sweeps the `Mwah Peak` center frequency ($850\text{ Hz}$ to $1.6\text{ kHz}$) to suit ebony vs. rosewood fingerboards.
- **Knob 2 (COMP):** Optical Sustainer compression depth.
- **Knob 3 (MOD / REVERB):** Stereo Chorus & Plate Ambience mix.

### Tank-G (v1 / v2) Control Assignments
- Keep amp preamp low-end moderate and load a hybrid `2x10 + 1x15` bass IR in the cabinet slot for clean solo bass performance.

### Black Box Desktop Configuration
- **Balanced XLR Direct Out:** Sends studio-polished fretless *mwah* directly to FOH without needing external tube DI preamps.
- **Expression Pedal 1:** Real-time continuous control over **Plate Reverb & Delay Mix** for dramatic solo bass swells.
