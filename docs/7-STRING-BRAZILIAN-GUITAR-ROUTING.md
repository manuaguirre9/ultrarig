# Brazilian 7-String Classical Guitar (Violão de 7 Cordas) Routing Guide

This guide details the acoustic profile, frequency management, dynamic baixaria processing, and preset architecture for the **Brazilian 7-String Classical Guitar (Violão de 7 Cordas)** within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Acoustic Profile & Heritage of the 7-String Guitar

In Brazilian Choro and Samba, the 7-string nylon-string guitar (*violão de 7 cordas*) acts as both harmonic accompaniment and counterpoint bass foundation. Immortalized by masters such as **Dino 7 Cordas** (Horondino José da Silva), **Raphael Rabello**, **Rogério Caetano**, and **Yamandu Costa**, its hallmark technique revolves around **baixarias**—rapid, syncopated scalar bass runs played predominantly with the thumb (*polegar* or metal/plastic *dedeira*).

```
String 1 (1ª Corda - Cantadeira): E4 (Mi) - Plain Nylon / Carbon
String 2 (2ª Corda):             B3 (Si) - Plain Nylon / Carbon
String 3 (3ª Corda):             G3 (Sol)- Plain Nylon / Carbon
String 4 (4ª Corda):             D3 (Ré) - Silverplated Wound Nylon
String 5 (5ª Corda):             A2 (Lá) - Silverplated Wound Nylon
String 6 (6ª Corda):             E2 (Mi) - Silverplated Wound Nylon
String 7 (7ª Corda - Baixaria):  C2 (Dó) / B1 (Si) - Heavy Wound Core
```
*(Traditional Choro tuning tunes the 7th string down to $C_2 \approx 65.4\text{ Hz}$; modern samba and concert players frequently tune down to $B_1 \approx 61.7\text{ Hz}$).*

### 1.1 Electroacoustic Engineering Challenges

1. **Extreme Dynamic Disparity (Thumb Baixaria vs. Nylon Fingers):** When playing rapid baixarias with a thumbpick or firm thumb stroke, the acoustic output of the 7th string can be $+12\text{ dB}$ to $+18\text{ dB}$ hotter than delicate nylon fingerpicked chords. Uncontrolled, this overloads audio converters and creates mud.
2. **Body Resonance Boom (90 Hz – 135 Hz):** The large concert acoustic body resonates intensely in the low register. On live stages, the $C_2$ or $D_2$ fundamental excites the guitar soundboard into violent acoustic feedback.
3. **Piezo Transducer Hardness on Nylon:** Standard under-saddle piezo pickups accentuate the rigid pick attack while stripping the delicate, woody air of traditional French-polished spruce or cedar tops.
4. **Low-End Definition Without Thinness:** Over-filtering the bass to stop feedback robs the 7th string of its rich acoustic authority; under-filtering creates an indistinct, boomy wash.

---

## 2. DSP Signal Chain & Processing Topology

```
7-String Guitar In (Piezo / Under-Saddle Transducer)
   │
   ▼
[ Subsonic High-Pass Filter (45 Hz, 24 dB/oct Butterworth) ]
   │
   ▼
[ Dual-Band Dynamic Split (Crossover @ 220 Hz) ]
   ├── Low Band (< 220 Hz: Baixarias & Bass Strings 5-7) ──► [ Fast Optical Leveler & Low Notch @ 105 Hz ]
   │                                                                      │
   └── High Band (> 220 Hz: Nylon Treble Strings 1-4) ─────► [ Gentle Studio Comp & Piezo Tamer @ 3.2 kHz ]
   │                                                                      │
   └───────────────────────────────┬──────────────────────────────────────┘
                                   ▼
[ Acoustic Concert Classical Body IR Convolution ] (German Spruce & Brazilian Rosewood)
                                   │
                                   ▼
[ Surgical Notch Filter (Main Cavity Feedback Suppression) ]
                                   │
                                   ▼
[ Studio Ambience / Natural Acoustic Chamber Reverb ] ──► Stereo Output
```

---

## 3. Parameter Specifications

| Module | Parameter | Recommended Value | Purpose |
| :--- | :--- | :--- | :--- |
| **Input Filter** | High-Pass Filter | `45 Hz` (24 dB/oct) | Eliminates sub-audible stage rumble while preserving $B_1$ ($61.7\text{ Hz}$). |
| **Crossover** | Split Frequency | `220 Hz` | Separates heavy thumb baixarias from delicate nylon chord voicings. |
| **Low Band Comp**| Ratio / Attack / Rel | `4.0:1` / `15 ms` / `90 ms` | Controls explosive 7th-string thumb strikes without squashing sustain. |
| **High Band Comp**| Ratio / Attack / Rel | `2.0:1` / `30 ms` / `160 ms`| Preserves natural touch dynamics on treble nylon runs. |
| **Body Notch** | Freq / Q / Gain | `105 Hz` / `Q=7.0` / `-7.0 dB` | Suppresses main soundboard cavity boom and live stage feedback. |
| **Piezo Tamer** | Freq / Q / Gain | `3.2 kHz` / `Q=3.0` / `-3.5 dB` | Smooths harsh piezo clack on nylon strings. |
| **Body IR** | Impulse Response | `Concert_7String_Spruce.wav` | Restores authentic acoustic chamber bloom and microphonic warmth. |
| **Air Shelf** | Freq / Gain | `10.5 kHz` / `+2.0 dB` | Adds delicate acoustic air and string breath. |
| **Reverb** | Decay / Pre-delay | `1.5 s` / `25 ms` | Acoustic chamber simulating a concert hall stage. |

---

## 4. Factory Scene Presets

### Scene A: Choro Tradicional Dino 7 Cordas (Punchy Baixarias)
- **Concept:** Authoritative, clear, and punchy bass articulation inspired by Dino 7 Cordas' legendary accompaniment style.
- **Low-End Dynamics:** Fast low-band optical compression (`4.2:1`, `80 ms` release), notch at 108 Hz (-8 dB).
- **EQ:** Focused low-mids (+1.5 dB @ 280 Hz for wood warmth), high shelf rolling off above 8 kHz.
- **Space:** Dry, intimate Studio Room Reverb (`1.0 s`, `12%` mix) ensuring rhythm precision.

### Scene B: Samba de Raiz Encorpado (Rich Rhythmic Foundation)
- **Concept:** Warm, deep pulse for backing cavaquinho, pandeiro, and vocalists in traditional samba rodas.
- **Low-End Dynamics:** Smooth leveling (`3.0:1`, `120 ms` release) allowing notes to bloom naturally.
- **EQ:** Low-cut set at 50 Hz, warmth boost at 180 Hz (+2.0 dB), notch at 98 Hz (-6 dB).
- **Space:** Wooden Chamber Reverb (`1.6 s`, `20%` mix).

### Scene C: Violão Concerto Clássico 7C (Solo & Arpeggios)
- **Concept:** Pristine, high-headroom fidelity for classical concert pieces (Villa-Lobos, Radamés Gnattali, Raphael Rabello).
- **Dynamics:** Transparent dual-band leveling (`1.8:1`) preserving extreme pianissimo to fortissimo dynamics.
- **Acoustic IR:** German Spruce / Jacarandá concert body IR in 1024-sample slot.
- **Space:** Concert Hall Reverb (`2.6 s`, `24%` mix) with `30 ms` pre-delay.

### Scene D: Yamandu Style Modern Virtuoso Estéreo (Fast Transient Tracking)
- **Concept:** Ultra-fast transient response and modern spatial width for lightning-fast rasgueados, scale runs, and percussive tambor golpes.
- **Dynamics:** Peak limiter clamping instantaneous golpes (`0.5 ms` attack), fast recovery.
- **Modulation:** Subtle stereo micro-detuning (`+4 cents` left, `-4 cents` right) for panoramic breadth.
- **Space:** Plate Reverb (`2.0 s`, `22%` mix).

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (Dino Tradicional) / Scene B (Samba Encorpado).
- **Footswitch B:** Scene C (Concerto Clássico).
- **Footswitch C:** Scene D (Yamandu Virtuoso) / Tuner.
- **Knob 1 (EQ / TONE):** Sweepable low-notch frequency (`85 Hz` – `140 Hz`) to quickly cancel stage feedback.
- **Knob 2 (MOD FX):** Stereo spatial width and subtle detune.
- **Knob 3 (REVERB):** Acoustic room size and balance.

### Tank-B Control Assignments
- Tank-B is exceptionally well-suited for 7-string acoustic guitarists who need dedicated sub-bass control, dual-band compression, and notch filtering to handle the low $C_2$ or $B_1$ fundamental with studio fidelity.

### Black Box Desktop Configuration
- **High-Z Input:** Set input impedance to **1 MΩ** to prevent impedance loading and high-frequency roll-off from passive piezo transducers.
- **Direct XLR Output:** Sends balanced, low-noise studio sound directly to the front-of-house (FOH) PA console.
