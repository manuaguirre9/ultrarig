# Electric & Acoustic Cello (Arco & Wolf-Tone Management) Routing Guide

This guide details bowed-string low-frequency mechanics, surgical **"Wolf Tone"** (*nota lobo*) suppression, Stradivarius cello body IR convolution, and preset configuration for **Electric and Acoustic Cellos** within UltraRig for M-VAVE hardware (Tank-B, Tank-G v1/v2, and Black Box).

---

## 1. Acoustic Profile & Resonance Physics of the Cello

The cello bridges the sonic gap between double bass profundity and human vocal lyricism. Spanning a massive low-to-midrange spectrum from its lowest open string ($C_2 = 65.4\text{ Hz}$) through the singing tenor $A_3$ ($220.0\text{ Hz}$) and soaring treble registers ($> 880\text{ Hz}$), it presents demanding transducer challenges.

```
4-String Cello Standard (Fifths): C2 (65.4 Hz) | G2 (98.0 Hz) | D3 (146.8 Hz) | A3 (220.0 Hz)
5-String Electric Cello:          C2 | G2 | D3 | A3 | E4 (329.6 Hz)  [or low F1 = 43.6 Hz]
```

### 1.1 The "Wolf Tone" Phenomenon & Piezo Challenges

1. **The Cello "Wolf Tone" (*Nota Lobo*):** Nearly every wooden cello—and even resonant hollow-chamber electric cellos—possesses a strong structural top-plate mode typically near $F\#_2 / G_2$ ($92\text{ Hz} - 98\text{ Hz}$) or its octave $F\#_3 / G_3$ ($185\text{ Hz} - 196\text{ Hz}$). When bowed at that pitch, string energy couples violently into the soundboard, resulting in a stuttering, beating warble that kills sustain and triggers brutal PA feedback.
2. **Bridge Piezo Nasal Bite (2.4 kHz – 4.2 kHz):** Under-foot bridge transducers (such as Yamaha SVC, NS Design, Fishman C-100, and David Gage Realist) bypass the carved spruce top and maple ribs completely, yielding dry, edgy upper-mids and emphasizing bow rosin scrape.
3. **High-Gain Bow Fuzz Trap:** Applying conventional electric guitar distortion directly to a bowed cello amplifies continuous rosin friction noise into unbearable white-noise fizz unless paired with steep post-drive cabinet low-pass filtering ($< 4.2\text{ kHz}$).

---

## 2. DSP Signal Chain & Processing Topology

```
Cello In (Bridge Piezo / NS Polar Pickup / Condenser Mic)
   │
   ▼
[ High-Z 1MΩ Input Buffer & Subsonic HPF (50 Hz, 24 dB/oct) ]
   │
   ▼
[ Dual Surgical Notch Filters ]
   ├── Notch 1: Helmholtz Air Cavity @ 64 Hz (Q=6.0, -5 dB)
   └── Notch 2: Wolf Tone Suppressor @ 185 Hz (Q=12.0, -8 dB) <=== Precision Anti-Wolf Target
   │
   ▼
[ Cello Acoustic Body IR Convolution ] (1711 Stradivarius Duport Concert IR)
   │
   ▼
[ Dynamic Bow Rosin De-Harsher ] (Clamps abrasive friction spikes @ 3.6 kHz)
   │
   ▼
[ Smooth Optical Sustainer Compressor ] (Evens delicate C-string low rumble vs. singing A-string)
   │
   ▼
[ Optional Tube Overdrive & 4x12 Low-Pass Cab IR (Rock Cello) OR Concert Hall Reverb ] ──► Out
```

---

## 3. Parameter Specifications

| Module | Parameter | Classical / Acoustic | Rock / Distortion | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **Input Filter**| High-Pass Filter | `50 Hz` (24 dB/oct) | `60 Hz` (24 dB/oct) | Clears floor rumble while keeping $C_2$ ($65.4\text{ Hz}$) solid. |
| **Notch 1** | Air Boom Control | `64 Hz` / `Q=6.0` / `-5 dB`| `64 Hz` / `Q=7.0` / `-7 dB` | Controls Helmholtz air resonance on hollow bodies. |
| **Wolf Notch** | Wolf Tone Filter | `185 Hz` / `Q=12.0` / `-8 dB`| `185 Hz` / `Q=10.0` / `-6 dB`| Eliminates sympathetic beating/warble on $F\#_3 / G_3$. |
| **Body IR** | Impulse Response | `Stradivarius_Cello.wav`| Bypassed (Use 4x12 V30 IR)| Restores natural maple/spruce concert bloom. |
| **Rosin Tamer**| Dynamic De-Harsh | `3.6 kHz` (`-4.0 dB`) | `4.2 kHz` (Steep LPF Cut) | Removes harsh bow friction and post-distortion fizz. |
| **Warmth EQ** | Body / Chest | `240 Hz` / `+2.5 dB` | `140 Hz` / `+3.5 dB` | Adds woody projection and cinematic low-mid power. |
| **Compressor** | Ratio / Attack / Rel| `2.2:1` / `35 ms` / `200 ms`| `3.5:1` / `20 ms` / `140 ms`| Preserves expressive bow swell dynamics cleanly. |
| **Reverb** | Type / Decay / Mix| `Concert Hall` / `2.8 s` / `28%`| `Tight Room` / `1.2 s` / `15%`| Immersive orchestral space vs. punchy metal stage tight cut. |

---

## 4. Factory Scene Presets

### Scene A: Baroque Solo Cello IR (Bach Suites Intimacy)
- **Concept:** Authentic, woody, warm solo concert cello tone—transforming solid-body electric cellos into classic acoustic Stradivarius instruments.
- **EQ & IR:** `Stradivarius_Cello.wav` IR, Wolf Tone Notch at `185 Hz`, mild rosin de-harsher at `3.6 kHz`.
- **Space:** Wooden Concert Hall Reverb (`2.6 s`, `28%` mix) with `32 ms` pre-delay.

### Scene B: Modern Cinematic Hans Zimmer Punch (Trailer Ostinato)
- **Concept:** Massive, percussive, low-end-heavy bowed ostinato tone designed for film scoring and modern ensemble energy.
- **Dynamics:** Fast optical leveling (`3.2:1`), assertive chest boost at `135 Hz (+3.5 dB)`, crisp *spiccato* bow attack clarity at `1.8 kHz (+2 dB)`.
- **Space:** Vast Stone Scoring Stage Reverb (`3.4 s`, `24%` mix).

### Scene C: Rock Cello Distortion (Apocalyptica / Metal Arco)
- **Concept:** Singing, aggressive high-gain guitar-style distortion calibrated specifically for bowed strings without abrasive rosin static.
- **Drive & Cab:** Friedman/Marshall high-gain preamp emulation (`GAIN = 68%`) feeding a custom **4x12 Celestion Vintage 30 Cabinet IR** with steep high-frequency cut above `4.2 kHz` to eliminate bow-hair white noise.
- **Noise Gate:** Fast downward expander at `-36 dBFS` silencing bow idle friction between staccato riffs.

### Scene D: Ambient Bowed Cello Cloud (Zoe Keating Looping Pad)
- **Concept:** Lush, atmospheric looping foundation layering stereo modulation, dotted-8th delay trails, and expansive shimmer reverbs.
- **Modulation:** Dimension D Stereo Chorus (`Mode 3`).
- **Space:** Modulated Stereo Tape Delay (`440 ms`, `38%` feedback) into Shimmer Cathedral Reverb (`6.0 s`, `40%` mix).

---

## 5. Hardware Setup & Mapping

### Tank-B Control Assignments
- **Ideal Cello Platform:** Because the cello's lowest string ($C_2 = 65.4\text{ Hz}$) sits squarely in the bass register, Tank-B's dedicated low-frequency headroom, sub-bass EQ, and 1024-point IR loader handle arco and pizzicato cello dynamics superbly.
- **Footswitch 1:** Scene A (Baroque Solo Cello IR) / Scene B (Cinematic Ostinato).
- **Footswitch 2:** Scene C (Rock Cello Distortion) / Scene D (Ambient Looping Cloud).

### Tank-G (v1 / v2) Control Assignments
- Cellists can utilize Tank-G's high-gain amp cascades and 3-knob reverb/modulation layouts seamlessly—especially for Scene C (Rock Cello) and Scene D (Ambient Loops).

### Black Box Desktop Configuration
- **High-Z 1 MΩ Input:** Mandatory for passive piezo cello bridges (Realist / Fishman C-100) to avoid capacitive high-end thinning.
- **Expression Pedal 1:** Map to **Wolf Notch Frequency** sweep during soundcheck OR **Drive Gain** morphing from clean acoustic cello into soaring rock lead distortion mid-song!
