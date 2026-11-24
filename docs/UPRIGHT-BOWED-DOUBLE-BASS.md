# Upright Double Bass (Bowed Arco & Dual-Mic) Routing & Tone Guide

This guide details acoustic resonance mitigation, dual-transducer phase alignment, dynamic bow-scratch management, and preset configuration for the **Acoustic Upright Double Bass** (Contrabaixo Acústico) within UltraRig for M-VAVE hardware (Tank-B, Tank-G v1/v2, and Black Box).

---

## 1. Acoustic & Transducer Physics of the Upright Double Bass

The upright double bass produces deep fundamental frequencies extending down to 41.2 Hz ($E_1$) or 30.8 Hz ($B_0$ on 5-string/extension instruments). Its massive carved spruce top and maple body generate complex acoustic interactions that present unique live reinforcement challenges.

```
Bridge Piezo Pickup (Underwood / Realist) ──► [ High-Z 5MΩ Buffer ] ──┐
                                                                      │
                                                                      ▼
Acoustic Clip-on Mic (DPA 4099 / Ehrlund) ─► [ Phase & Delay Align ] ─┼──► [ Summing & Filter Matrix ]
                                                                      │
                                                                      ▲
[ Polarity Invert 180° & Delay Trim (0.0 - 5.0 ms) ] ─────────────────┘
```

### 1.1 Acoustic Obstacles in Live Performance

1. **Subsonic Stage Rumble & Helmholtz Resonance (55 Hz – 68 Hz):** The main internal air cavity resonance produces uncontrollable low-end feedback on hollow wooden stages.
2. **Body Resonance "Wolf Tones" (98 Hz – 115 Hz):** Usually centered around $G_2$ or $A_2$, the bass body vibrates in sympathetic runaway oscillation, causing warbling notes with choked sustain.
3. **Piezo Transducer Nasal Bite (1.8 kHz – 3.2 kHz):** Bridge-mounted piezo elements lack natural acoustic "wood air" and sound harsh, dry, and clacking.
4. **Bowing (*Arco*) Rosin Scratch (2.5 kHz – 4.5 kHz):** When drawn with a French or German bow, rosin friction on wound steel or gut strings generates harsh continuous high-mid scratch that can be ear-fatiguing without dedicated dynamic smoothing.

### 1.2 Dual-Source Blending & Phase Alignment

The ideal upright tone combines the punch and feedback rejection of a bridge piezo with the breath, body, and string detail of a miniature condenser microphone:
- **Phase Cancellation:** Sound travels through air to the microphone ~1 ms later than it travels through the solid wood bridge into the piezo.
- **Delay Alignment:** Delaying the piezo path by $0.8 \text{ ms}$ to $1.5 \text{ ms}$ and testing $180^\circ$ polarity inversion aligns low-frequency waveforms, eliminating thin, hollow phase-cancellation notches in the 80 Hz to 200 Hz range.

---

## 2. DSP Signal Chain & Topology

```
Upright Bass In (Piezo / Dual Input)
   │
   ▼
[ Phase Polarity (0°/180°) & Delay Alignment (1.2 ms) ]
   │
   ▼
[ Subsonic High-Pass Filter (35 Hz, 24 dB/oct Butterworth) ]
   │
   ▼
[ Dual Parametric Notch Filters ]
   ├── Notch 1: Helmholtz Cavity @ 62 Hz (Q = 8.0, -8 dB)
   └── Notch 2: Wolf Tone Suppressor @ 104 Hz (Q = 10.0, -9 dB)
   │
   ▼
[ Acoustic Upright Body IR Convolution ] (Carved European Spruce Body Resonance)
   │
   ▼
[ Dynamic Bow Tamer / De-Scratcher ] (Dynamic EQ clamping 2.8 kHz - 4.2 kHz during arco)
   │
   ▼
[ Optical Tube Leveler Compressor ] (Smooth 2.5:1 ratio, preserving wood decay)
   │
   ▼
[ Studio Ambience / Chamber Reverb ] ──► Balanced Stereo Output
```

---

## 3. Parameter Specifications

| Module | Parameter | Recommended Value | Purpose |
| :--- | :--- | :--- | :--- |
| **Input Filter** | High-Pass Filter | `35 Hz` (24 dB/oct) | Eliminates sub-audible stage vibration and handling thumps. |
| **Phase Align** | Polarity / Delay | `180°` / `1.1 ms` | Resolves low-frequency phase cancellation between mic and piezo. |
| **Notch 1 (Air)**| Freq / Q / Gain | `62 Hz` / `Q=8.0` / `-8.0 dB` | Tames runaway Helmholtz body cavity boom. |
| **Notch 2 (Wolf)**| Freq / Q / Gain | `104 Hz` / `Q=10.0` / `-9.0 dB`| Suppresses resonant wolf tone on $G_2$ notes. |
| **Body IR** | Impulse Response | `Upright_Spruce_Concert.wav`| Restores microphonic warmth and spatial depth to dry piezos. |
| **Bow De-Scratch**| Threshold / Freq | `-18 dBFS` / `3.2 kHz` | Dynamically clamps harsh rosin friction during arco passages. |
| **Compressor** | Ratio / Attack / Rel | `2.5:1` / `25 ms` / `180 ms` | Smooth optical levelling that maintains percussive pizzicato attack. |
| **Mid Shaper** | Freq / Q / Gain | `750 Hz` / `Q=1.5` / `-3.0 dB`| Cleans up muddy "cardboard" boxiness in the midrange. |
| **Reverb** | Type / Decay / Mix | `Acoustic Chamber` / `1.8 s` / `18%` | Places the bass into an intimate natural hall space. |

---

## 4. Factory Scene Presets

### Scene A: Natural Jazz Pizzicato (Ray Brown / Ron Carter)
- **Concept:** Warm, punchy, woody definition with rich low-mid growl and percussive fingerboard response.
- **Transducer Balance:** 70% Bridge Piezo + 30% Condenser Mic / Body IR.
- **Filtering & EQ:** Notch @ 62 Hz, -3 dB cut at 750 Hz, gentle high shelf above 8 kHz.
- **Dynamics:** Optical compression (`2.2:1`, slow attack `30 ms` to preserve finger pluck).
- **Space:** Intimate Wood Room Reverb (`1.2 s`, `15%` mix).

### Scene B: Orchestral Bowed Legato (Arco)
- **Concept:** Silky, singing string sustain for classical, soundtrack, and melodic bowing without abrasive rosin screech.
- **Transducer Balance:** 50% Piezo + 50% Acoustic Body IR.
- **De-Scratch:** Dynamic EQ engaged at 3.4 kHz with fast-acting high-frequency attenuation.
- **Dynamics:** Gentle levelling (`3:1`, `45 ms` attack, `250 ms` release).
- **Space:** Concert Hall Reverb (`2.8 s`, `25%` mix).

### Scene C: Rockabilly & Bluegrass Slap Bass
- **Concept:** High-energy slap tone combining thumping low-end gut string punch with percussive fingerboard slap click.
- **Dual Processing:**
  - Low Channel: Tight low-pass filter at 800 Hz with fast optical peak limiting.
  - Slap Channel: High-pass filter at 1.5 kHz boosting fingerboard click transients.
- **Space:** Vintage Slapback Tape Echo (`95 ms`, single repeat) + Dry Studio Room.
- **Mix:** 85% Dry / 15% Space.

### Scene D: Modern Ambient Upright (Eberhard Weber Style)
- **Concept:** Atmospheric singing fretless-like sustain with subtle stereo chorusing and vast cavernous reverbs.
- **Modulation:** Subtle stereo chorus (`0.4 Hz`, `15%` depth, +8 cents detune).
- **Delay & Reverb:** Modulated Stereo Tape Delay (`480 ms`, `30%` feedback) into Shimmer Hall (`4.5 s` decay).
- **Mix:** 60% Wet / 40% Dry.

---

## 5. Hardware Setup & Mapping

### Tank-B Control Assignments
- **Footswitch 1:** Scene A (Jazz Pizzicato) / Scene B (Orchestral Bowed Arco).
- **Footswitch 2:** Scene C (Rockabilly Slap) / Scene D (Ambient Upright).
- **Compressor Knob:** Adjusts optical threshold to smooth out uneven pizzicato dynamics.
- **Low-Cut / Notch Filter:** Quick sweepable knob to isolate and eliminate stage feedback frequencies on venue soundchecks.

### Tank-G (v1 / v2) Control Assignments
- Configure input for acoustic instrument mode with flat preamp profile and load the `Upright_Spruce_Concert.wav` IR in slot 1.
- **Footswitch A / B:** Toggle between Pizzicato and Arco scene modes.
- **Knob 3 (REVERB):** Controls acoustic chamber size and dry/wet ratio.

### Black Box Desktop Configuration
- **Balanced XLR Direct Out:** Sends noise-free balanced microphone-level signals directly to front-of-house (FOH) PA mixers.
- **Dual Input Processing:** Route Piezo to Input L (High-Z) and Clip-on Mic to Input R, enabling independent pre-filtering and internal phase-delay compensation.
