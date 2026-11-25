# Electroacoustic Harp (Concert, Celtic & Paraguayan) Routing Guide

This guide details the immense 6.5-octave frequency profile, trapezoidal cavity resonance suppression, dual-band glissando dynamics, and preset configuration for **Concert Pedal Harps**, **Celtic Lever Harps**, and the **Paraguayan Folk Harp (Arpa Paraguaya)** within UltraRig for M-VAVE hardware (Tank-B, Tank-G v1/v2, and Black Box).

---

## 1. Acoustic Range & Multi-Transducer Architecture of Harps

Few acoustic instruments span as broad a frequency spectrum as the harp. A full 47-string **Concert Pedal Harp** stretches from deep pipe-organ sub-bass ($C_1 = 32.7\text{ Hz}$) up to shimmering high trebles ($G_7 = 3136\text{ Hz}$)—requiring simultaneous sub-bass power, midrange warmth, and crystalline high-frequency transparency.

```
47-String Concert Pedal Harp: C1 (32.7 Hz)  ──►  G7 (3136 Hz)  [ Gut / Nylon / Steel Wire Basses ]
34-String Celtic Lever Harp:  C2 (65.4 Hz)  ──►  A6 (1760 Hz)  [ Warm Gut / Nylon Tension ]
36-String Arpa Paraguaya:     F1 (43.6 Hz)  ──►  F6 (1397 Hz)  [ Light Nylon, High Fingernail Snap ]
```

### 1.1 Electroacoustic Engineering Challenges

1. **Trapezoidal Soundbox Cavity Boom (110 Hz – 165 Hz):** Unlike small-bodied guitars, a harp's tapered spruce soundboard and deep soundbox act as a massive acoustic horn centered between $110\text{ Hz}$ and $165\text{ Hz}$. Multi-element bridge piezo strips (Dusty Strings, Camac, Schertler) capture booming stage resonance that quickly spirals into low-end feedback.
2. **Bass Pluck vs. Glissando Accumulation:** Plucking heavy wire-wound contrabass strings generates massive low-frequency transient waves, whereas rapid 30-string sweeping *glissandos* stack dense upper-mid energy ($2.8\text{ kHz} - 5.5\text{ kHz}$). A single broadband compressor squashes delicate trebles whenever a bass note is struck!
3. **Paraguayan Harp Nail Clicks:** Traditional *Arpa Paraguaya* playing uses brisk fingernail attacks and syncopated rhythmic *bordonas*, injecting sharp treble clicks through raw piezo elements.

---

## 2. DSP Signal Chain & Processing Topology

```
Harp In (Multi-Element Soundboard Piezo / Camac Electric System)
   │
   ▼
[ High-Z 1MΩ Buffer & High-Pass Filter (Concert: 30 Hz | Folk/Celtic: 50 Hz, 24 dB/oct) ]
   │
   ▼
[ Trapezoidal Cavity Surgical Notch Filter @ 132 Hz (Q = 6.5, -7 dB) ]
   │
   ▼
[ Dual-Band Dynamic Split (Crossover @ 250 Hz) ]
   ├── Low Band (< 250 Hz: Bass Wire Strings) ──► [ Tight Optical Compressor (3.0:1, Att: 22 ms) ]
   │                                                                   │
   └── High Band (> 250 Hz: Nylon/Gut Glissandos)► [ Dynamic Piezo Softener @ 3.6 kHz + Soft Limiter ]
                                                                       │
                                   ┌───────────────────────────────────┘
                                   ▼
[ Concert Spruce Soundboard IR Convolution ] (Lyon & Healy / Dusty Strings Body IR)
                                   │
                                   ▼
[ Micro-Stereo Spatializer & Concert Hall / Abbey Reverb ] ──► Balanced Stereo Output
```

---

## 3. Parameter Specifications

| Module | Parameter | Concert Pedal Harp | Celtic / Paraguayan Harp | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **Input Filter**| High-Pass Filter | `30 Hz` (24 dB/oct) | `50 Hz` (24 dB/oct) | Preserves $C_1$ ($32.7\text{ Hz}$) contrabass while cutting stage thump. |
| **Cavity Notch**| Freq / Q / Gain | `132 Hz` / `Q=6.5` / `-7 dB`| `148 Hz` / `Q=6.0` / `-6 dB`| Eliminates trapezoidal soundbox feedback boom. |
| **Crossover** | Split Frequency | `250 Hz` | `280 Hz` | Keeps booming bass strings from pumping high delicate glissandos. |
| **Low Comp** | Ratio / Attack | `3.0:1` / `22 ms` | `3.4:1` / `15 ms` | Tightens wire-wound basses and Paraguayan rhythmic *bordonas*. |
| **Piezo Tamer**| Dynamic Dip | `3.4 kHz` (`-3.5 dB`)| `3.8 kHz` (`-4.5 dB`) | Smooths harsh under-board piezo nasal clicks and nail scrape. |
| **Body IR** | Impulse Response | `Concert_Harp_Spruce.wav`| `Celtic_Cherry_Harp.wav` | Restores natural acoustic air and wood bloom. |
| **Air Shelf** | Freq / Gain | `11.5 kHz` / `+2.0 dB` | `10.5 kHz` / `+1.5 dB` | Adds silky string breath without upper-mid harshness. |
| **Reverb** | Type / Decay / Mix| `Concert Hall` / `2.8 s` / `26%`| `Wood Chamber` / `1.9 s` / `22%`| Evokes classical scoring halls or intimate acoustic venues. |

---

## 4. Factory Scene Presets

### Scene A: Classical Concert Harp Clarity (47-String Pedal Harp)
- **Concept:** High-headroom, transparent orchestral fidelity capturing deep contrabass warmth ($C_1$) alongside crystalline upper glissandos.
- **EQ & IR:** `HPF = 30 Hz`, cavity notch @ 132 Hz, `Concert_Harp_Spruce.wav` IR, gentle dynamic leveling (`2.0:1`).
- **Space:** Golden Symphony Hall Reverb (`2.8 s`, `25%` mix) with `34 ms` pre-delay.

### Scene B: Paraguayan Folk Harp (Arpa Paraguaya Bright Pulse)
- **Concept:** Crisp, rhythmic, dance-ready articulation tailored for *Pájaro Campana* runs, rapid tremolos, and energetic fingernail attacks.
- **Dynamics:** Tight low-band compressor (`3.5:1`), fast high-band nail-click limiter (`1.0 ms` attack), dynamic piezo dip at `3.8 kHz`.
- **Space:** Warm Studio Wood Room (`1.4 s`, `18%` mix).

### Scene C: Celtic Folk Stereo Ambience (Loreena McKennitt Style)
- **Concept:** Rich, warm, mystical folk tone with gentle low-mid wooliness and expansive stereo depth.
- **Modulation:** Subtle stereo micro-widening (`+4 cents` left, `-4 cents` right) strictly above `280 Hz`.
- **Space:** Ancient Stone Abbey Reverb (`3.6 s`, `30%` mix).

### Scene D: Ethereal Ambient Harp Cloud (Andreas Vollenweider / Electronic Crossover)
- **Concept:** Cinematic electric-harp landscape transforming delicate fingerpicked arpeggios into shimmering spatial pads.
- **Delay & Space:** Stereo Modulated Ping-Pong Delay (`dotted 8th`, `440 ms`, `32%` feedback) feeding Cathedral Shimmer Reverb (`6.0 s`, `40%` mix).

---

## 5. Hardware Setup & Mapping

### Tank-B Control Assignments
- **Sub-Bass Concert Advantage:** Because a 47-string concert harp reaches down to $C_1 = 32.7\text{ Hz}$ (even lower than a standard 4-string bass guitar's $41.2\text{ Hz}$!), **Tank-B** is the premier platform for concert pedal harpists—offering clean sub-bass headroom, a $30\text{ Hz}$ HPF, and dual-band compression without bottom-end distortion.
- **Footswitch 1:** Scene A (Classical Concert) / Scene C (Celtic Folk Ambience).
- **Footswitch 2:** Scene D (Ambient Shimmer Cloud).

### Tank-G (v1 / v2) Control Assignments
- Ideal for 34–38 string Celtic and Paraguayan folk harpists needing portable soundboard IR convolution, feedback notch sweeps, and stereo shimmer reverbs on stage.
- **Knob 1 (EQ):** Sweepable Cavity Notch (`105 Hz` to `185 Hz`) for quick stage feedback dialing.
- **Knob 3 (REVERB):** Concert Hall / Abbey wet balance.

### Black Box Desktop Configuration
- **High-Z 1 MΩ Buffer:** Vital for passive piezo harp pickup strips (without battery preamps) to retain crystalline high-frequency sparkles.
- **Balanced Dual XLR Outputs:** Sends stereo acoustic harp imagery cleanly directly to FOH consoles.
