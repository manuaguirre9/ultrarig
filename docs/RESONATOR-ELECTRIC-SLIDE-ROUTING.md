# Electric Resonator & Slide Guitar (Lipstick / P90 Hybrid) Routing Guide

This guide details hybrid magnetic-cone blending, **glass vs. brass bottleneck slide** frequency shaping, optical sustain leveling, and preset configuration for **Electric Resonator Guitars** and **Slide Guitars** within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Sonic Mechanics of Hybrid Resonator & Slide Guitars

When players unite spun-aluminum **National/Dobro resonator cones** with vintage **magnetic pickups** (such as Danelectro Lipstick tubes, Teisco Gold Foils, Telecaster neck single-coils, or Gibson P90s—immortalized by **Ry Cooder**, **Sonny Landreth**, and **Derek Trucks**), they gain a uniquely expressive hybrid voice capable of soaring violin-like slide melodies and gritty swamp-blues bark.

```
Open D (D-A-D-F#-A-D) / Open G (D-G-D-G-B-D) / Open E (E-B-E-G#-B-E)
   │
   ├──► [ Magnetic Pickup: Lipstick / P90 / Gold Foil ] ──► Thick Electric Sustain & Low-Mid Punch
   │
   └──► [ Optional Biscuit / Spider Cone Piezo ] ─────────► Metallic Acoustic Honk (750 Hz - 1.5 kHz)
```

### 1.1 Slide Material Acoustics & Tonal Challenges

1. **Glass / Pyrex Bottlenecks (Coricidin Bottle Style):** Deliver smooth, liquid, singing vocal warmth with rounded high-frequency transients, yet require **transparent optical sustain compression** to maintain singing decay across higher frets without finger-fret contact.
2. **Heavy Brass / Steel Slides:** Maximize physical string sustain and assertive midrange bite, but produce aggressive metallic ringing glare ($2.8\text{ kHz} - 4.2\text{ kHz}$) on bare strings and can rattle against pickups unless high-mids are smoothed cleanly.
3. **Cone Piezo "Honk" & Phase Mismatch:** When blending an internal cone piezo with a magnetic pickup, phase interference can thin out the $150\text{ Hz} - 300\text{ Hz}$ low-mids while stacking excessive nasal midrange honk around $1.1\text{ kHz}$.

---

## 2. DSP Signal Chain & Processing Topology

```
Slide / Resonator In (Magnetic Lipstick/P90 OR Hybrid Mag + Cone Piezo)
   │
   ▼
[ High-Z 1MΩ Buffer & High-Pass Filter (65 Hz) ]
   │
   ▼
[ Optical Sustainer Compressor (LA-2A Style: Slow Attack 30 ms, Long Release) ]
   │ (Boosts seamless glass/brass slide sustain without flattening fingerpicking attack)
   ▼
[ Surgical Slide & Cone EQ ]
   ├── Cone Nasal Honk Notch: -3.5 dB @ 1.15 kHz (Q = 2.5 - Keeps hybrid cone natural)
   └── Metal Slide Glare Dip: -3.0 dB @ 3.5 kHz (Q = 2.8 - Smooths harsh brass slide ring)
   │
   ▼
[ Boutique Preamp Emulation (Supro / Tweed Bassman / Super Reverb / Dumble ODS) ]
   │
   ▼
[ Hybrid Cabinet IR: 1x12 Jensen Alnico / Supro + Optional Resonator Cone IR Blend ]
   │
   ▼
[ Vintage Bias-Wiggle Tremolo + 6G15 Spring Reverb & Tape Slapback ] ──► Stereo Output
```

---

## 3. Parameter Specifications

| Module | Parameter | Recommended Value | Purpose |
| :--- | :--- | :--- | :--- |
| **Input Filter**| High-Pass Filter | `65 Hz` (12 dB/oct) | Tightens dropped $D_2$ / $E_2$ open-tuning bass strings. |
| **Optical Comp**| Ratio / Attack / Rel | `3.2:1` / `28 ms` / `240 ms` | Smooths fingerpicking and gives glass slides liquid sustain. |
| **Cone Notch** | Freq / Q / Gain | `1.15 kHz` / `Q=2.5` / `-3.5 dB`| Controls excessive nasal aluminum cone honk in hybrid setups. |
| **Glare Dip** | Freq / Q / Gain | `3.5 kHz` / `Q=2.8` / `-3.0 dB`| Removes fatiguing metallic string-slide ringing on upper frets. |
| **Preamp** | Model / Gain | `Supro / Super Reverb` / `52%` | Touch-sensitive edge-of-breakup reacting dynamically to thumb strokes. |
| **Cabinet IR** | Profile | `1x12_Jensen_P12Q.wav` | Classic American roots-blues midrange bark and open air. |
| **Tremolo** | Rate / Depth | `3.1 Hz` / `45%` | Hypnotic swamp-blues tube bias pulse (Paris, Texas style). |
| **Reverb** | Type / Decay / Mix | `6G15 Spring` / `2.4 s` / `28%`| Deep atmospheric swamp depth and surfy shimmer. |

---

## 4. Factory Scene Presets

### Scene A: Derek Trucks Open-E Singing Slide (Glass Bottleneck)
- **Concept:** Pure, fluid, vocal slide lyricism with endless singing sustain and zero harsh pick clicks (designed for fingerpicking without a pick).
- **Dynamics & EQ:** `OPTICAL_COMP = 3.2:1`, `GLARE_DIP = -3.5 dB @ 3.5 kHz`, Dumble/Super Reverb edge-of-breakup preamp (`GAIN = 58%`).
- **Cabinet IR:** 4x10 Jensen P10R / 2x12 Electro-Voice EVM-12L.
- **Space:** Warm Studio Hall Reverb (`2.1 s`, `22%` mix).

### Scene B: Sonny Landreth Hybrid Cone & Amp (Zydeco Bayou Swell)
- **Concept:** Massive, singing, compressed hybrid tone merging spun-aluminum resonator overtones with howling Lipstick/Stratocaster harmonic overdrive.
- **Cone & Drive:** Resonator Cone IR blended at `30%` parallel alongside cranked Klon/Tube Screamer pushing a Tweed Bassman preamp (`GAIN = 68%`).
- **Space:** Vintage Tape Slapback (`135 ms`, `22%` feedback) + Spring Tank.

### Scene C: Delta Blues Swamp Overdrive (Supro / Tweed Greasy Slide)
- **Concept:** Raw, menacing, dirty Mississippi Delta electric slide tone with heavy brass bottleneck bite and hypnotic optical bias tremolo.
- **Preamp:** Vintage Supro / Valco 1x12 circuit pushed hard (`GAIN = 76%`), tight bass cut below `90 Hz` for raw gritty rasp.
- **Modulation:** Slow Bias Tremolo (`2.9 Hz`, `55%` depth).
- **Space:** Trashy Short Spring Tank (`1.8 s`, `26%` mix).

### Scene D: Ambient Glass Slide Sustain (Ry Cooder / Paris, Texas)
- **Concept:** Haunting, desolate cinematic desert soundscape crafted for weeping minor/open-G glass slide melodies.
- **Preamp:** Pristine high-headroom Blackface Twin Clean (`GAIN = 28%`).
- **Space:** Echoplex Stereo Tape Delay (`440 ms`, `35%` feedback) feeding Deep 6G15 3-Spring Tank Reverb (`3.2 s`, `38%` mix).

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (Derek Trucks Singing Slide) / Scene B (Sonny Landreth Hybrid).
- **Footswitch B:** Scene C (Delta Swamp Overdrive).
- **Footswitch C:** Scene D (Paris, Texas Ambient Slide) / Open-Tuning Quick Tuner.
- **Knob 1 (COMP):** Optical Sustainer compression depth (dial clockwise for endless singing glass slide notes).
- **Knob 2 (GAIN / DRIVE):** Preamp Breakup & Swamp Grit.
- **Knob 3 (REVERB):** 6G15 Spring Tank & Tremolo mix.

### Tank-B Control Assignments
- Resonator bassists and baritone-tuned lap steel / slide players (Open A or Low C tunings) can use Tank-B's dedicated low-end optical sustain and `Supro / Bassman` models to retain massive bottom-end authority beneath singing slide licks.

### Black Box Desktop Configuration
- **Dual Input Hybrid Blending:** Connect your guitar's magnetic pickup (Lipstick/P90) to Input L and your internal resonator cone piezo to Input R (1 MΩ High-Z), letting UltraRig blend, phase-align, and process both voices simultaneously!
- **Expression Pedal 1:** Control `OPTICAL_SUSTAIN` or Preamp Gain continuously during expressive slide crescendos.
