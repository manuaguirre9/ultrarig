# Guitarra Baiana (5-String) Electric Routing & Tone Guide

This guide details the historical origin, acoustic-electric properties, pickup voicing, and preset architecture for the **5-String Guitarra Baiana** (Brazilian solid-body electric 5-string mandolin/guitar) within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. History & Sonic Profile of the 5-String Guitarra Baiana

Invented in the early 1940s by Antônio Adolfo Nascimento (**Dodô**) and Osmar Álvares Macêdo (**Osmar**) in Salvador, Bahia, the *Pau Elétrico* was one of the world's first solid-body electric instruments (predating the commercial production of the Fender Broadcaster/Telecaster). In the 1970s, virtuoso **Armandinho Macêdo** revolutionized the instrument by adding a fifth low string ($C_3$), expanding its range into a tenor voice and establishing the modern **Guitarra Baiana**.

```
String 1 (1ª Corda): E5 (Mi) - High Plain Steel (Cutting Solo Treble)
String 2 (2ª Corda): A4 (Lá) - Plain Steel
String 3 (3ª Corda): D4 (Ré) - Plain Steel / Thin Wound
String 4 (4ª Corda): G3 (Sol)- Wound Steel
String 5 (5ª Corda): C3 (Dó) - Low Wound Steel (Tenor / Baixaria Fundamental)
```
*(Standard tuning in fifths: $C_3, G_3, D_4, A_4, E_5$; scale length ~340 mm to 380 mm).*

### 1.1 Critical Tonal Challenges

1. **Short Scale Tension & Harsh Treble Bite (3.8 kHz – 6.5 kHz):** Because the scale length is very short (~35 cm), the plain steel $E_5$ and $A_4$ strings produce aggressive, percussive pick attack transients. Through full-range PA systems, this easily turns brittle and ear-piercing without dedicated high-frequency damping.
2. **Cutting Through Massive Percussion:** In the context of a *Trio Elétrico* (Bahian carnival truck) or a frevo orchestra, the guitarra baiana must cut through a wall of acoustic percussion (*surdos, repiniques, timbaus*). This requires a focused, vocal midrange contour between 800 Hz and 1.8 kHz.
3. **Low C String Flabbiness:** The low $C_3$ string requires dedicated low-mid tightness; too much sub-bass ($<100$ Hz) causes mud, while too little makes bass riffs (*baixarias*) sound hollow.
4. **The Signature "Swirl":** Armandinho's signature voice relies on the interplay between singing tube overdrive, dynamic pick response, and a slow, deep 4-stage optical phaser or chorus.

---

## 2. DSP Signal Chain & Processing Topology

```
Guitarra Baiana In (High-Output Mini-Humbucker / Single-Coil)
   │
   ▼
[ High-Pass Filter (95 Hz, 12 dB/oct Butterworth) ]
   │
   ▼
[ Fast Optical Compressor ] (Levels rapid frevo picking and tremolos)
   │
   ▼
[ Vocal Mid-Hump Overdrive (Tube Screamer / Klon Topology) ] (Pushes 850 Hz - 1.4 kHz)
   │
   ▼
[ Boutique Tube Preamp Emulation (Clean-Crunch Voicing) ]
   │
   ▼
[ 2x12 Open-Back Celestion Alnico Blue IR Convolution ]
   │
   ▼
[ High-Frequency Tamer Shelf (-3 dB @ 5.5 kHz) ]
   │
   ▼
[ Vintage 4-Stage Optical Phaser / Modulation Matrix ] (The Armandinho Swirl)
   │
   ▼
[ Stereo Ambient Tape Delay & Studio Plate Reverb ] ──► Stereo Output
```

---

## 3. Parameter Specifications

| Module | Parameter | Recommended Value | Purpose |
| :--- | :--- | :--- | :--- |
| **Input Filter** | High-Pass Filter | `95 Hz` (12 dB/oct) | Cleans up handling noise and tightens low C string ($C_3$). |
| **Compressor** | Ratio / Attack / Rel | `3.2:1` / `12 ms` / `140 ms` | Smooths high-speed alternate picking dynamics. |
| **Mid Overdrive** | Drive / Tone / Level | `45%` / `55%` / `65%` | Injects rich vocal harmonics and singing lead sustain. |
| **Mid Focus** | Freq / Q / Boost | `1.1 kHz` / `Q=1.8` / `+3.5 dB` | Ensures lead melodies cut through carnival percussion. |
| **High Cut** | Shelf Freq / Gain | `5.8 kHz` / `-4.0 dB` | Tames piezo/mini-humbucker pick click on short scale strings. |
| **Amp Model** | Model Type | `Clean-Crunch Tube (6L6)` | Provides punchy, high-headroom transient dynamics. |
| **Cabinet IR** | Speaker Model | `2x12_Alnico_OpenBack.wav` | Delivers warm acoustic chime and open midrange. |
| **Phaser** | Rate / Depth / Stages| `0.45 Hz` / `75%` / `4-Stage` | Emulates the iconic swirling Trio Elétrico lead sound. |
| **Delay** | Time / Feedback / Mix| `380 ms` (Dotted 8th) / `30%` / `25%`| Stereo delay adding spaciousness to rapid solos. |

---

## 4. Factory Scene Presets

### Scene A: Frevo Elétrico Armandinho (Signature Carnival Lead)
- **Concept:** The quintessential Bahian carnival lead: soaring, singing sustain with slow optical phaser swirl and warm tube saturation.
- **Drive & Voicing:** Tube Screamer style mid-boost (`DRIVE = 55%`, `MID_BOOST = +4 dB @ 1.2 kHz`).
- **Modulation:** 4-Stage Optical Phaser (`RATE = 0.4 Hz`, `DEPTH = 80%`).
- **Space:** Stereo Tape Delay (`375 ms`, `25%` feedback) into Warm Plate Reverb.
- **Mix:** 100% Wet Preamp / 25% Ambient Space.

### Scene B: Trio Elétrico Outdoor Cut (High-SPL Live Rig)
- **Concept:** Engineered to project through massive PA arrays and deafening outdoor acoustic percussion without shrillness.
- **Drive & Voicing:** Clean-crunch tube edge (`DRIVE = 35%`), tight bass rolloff below 110 Hz.
- **EQ:** Pronounced high-shelf cut at 5.2 kHz (-5 dB), heavy presence at 1.8 kHz (+3 dB).
- **Dynamics:** Fast optical limiter (`2.8:1`) clamping high $E_5$ transients.
- **Space:** Dry slapback echo (`110 ms`) for punchy rhythm articulation.

### Scene C: Choro Elétrico Limpo (Virtuoso Melodic Counterpoint)
- **Concept:** Pure, sparkling clean tone designed for intricate Brazilian choro solos, counterpoint, and baixarias.
- **Drive & Voicing:** 100% Clean Preamp with high headroom (`GAIN = 28%`).
- **Dynamics:** Transparent studio optical leveling preserving subtle finger dynamic nuances.
- **Modulation:** Subtle stereo chorus (`0.6 Hz`, `20%` depth) for spatial sheen.
- **Space:** Natural Wooden Chamber Reverb (`1.6 s`, `20%` mix).

### Scene D: Tropical Modern Fusion (Afoxé & Reggae-Frevo Groove)
- **Concept:** Hybrid fusion tone combining reggae-style envelope filter attack with warm modulation and delay.
- **Modulation:** Dynamic Envelope Filter (Up-sweep) + Mild Dimension Stereo Chorus.
- **Space:** Modulated Ping-Pong Delay (`dotted 8th`, `440 ms`, `35%` feedback) + Hall Reverb.
- **Mix:** 40% Wet / 60% Dry.

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (Frevo Elétrico Armandinho) / Scene B (Trio Elétrico Cut).
- **Footswitch B:** Scene C (Choro Elétrico Limpo).
- **Footswitch C:** Optical Phaser Toggle / Scene D.
- **Knob 1 (GAIN / DRIVE):** Overdrive saturation and singing sustain.
- **Knob 2 (MOD FX):** Phaser Rate & Depth.
- **Knob 3 (DELAY/REVERB):** Ambient Space mix.

### Tank-B Control Assignments
- Guitarra baiana players using Tank-B benefit from its dedicated low-cut filter and punchy compressor, which tighten the low $C_3$ string and prevent stage low-frequency feedback.

### Black Box Desktop Configuration
- **Stereo Routing:** Sends Left/Right modulated delay and phaser signals directly to the FOH mixing console.
- **MIDI CC #75:** Real-time speed switching for the optical phaser (Slow 0.4 Hz swirl to Fast 4.5 Hz rotary wobble).
