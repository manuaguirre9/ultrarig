# UltraRig Bass Multiband Dynamic Crossover & Parallel Compression Guide

For bassists performing live or recording in studio, the biggest tonal challenge is balancing **low-end stability** with **midrange aggression and high-frequency articulation**:
1. **The Single-Band Compression Problem:** Low frequencies (especially the low E and low B strings on 5-string basses) carry massive acoustic energy. Standard single-band compressors clamp down aggressively on the lowest notes, squashing the entire frequency spectrum and making slap pops, pick attack, and high-register fills inaudible.
2. **The Full-Spectrum Distortion Mud Problem:** Distorting the entire bass signal turns the sub-bass fundamentals (30 Hz – 150 Hz) into flubby, muddy noise that destroys the kick drum definition and empties the room of low-end weight.

Using UltraRig's parallel routing engine on the **M-VAVE Tank-B** (or Tank-G), you can build a studio-grade **Multiband Crossover Rig** that splits low sub-frequencies from mid/high grit, compresses them independently, and sums them into a punchy, professional bass tone.

---

## 1. Multiband Crossover Routing Topology

```
 [ Bass Input ] 
       │
       ▼
 ┌─────────────┐
 │    SPLIT    │
 └──┬───────┬──┘
    │       │
    │       ▼ [ BRANCH A: The Sub Anchor (Clean & Brickwall Compressed) ]
    │       ┌─────────────────────────────────────────────────────────────┐
    │       │ • Master Low-Pass Filter (LPF): 250 Hz                      │
    │       │ • Heavy Compressor: Ratio 4:1, Attack 15ms, -6 to -8 dB GR  │
    │       │ • Clean Unity Level: Solid, unmoving low-end foundation     │
    │       └─────────────────────────────┬───────────────────────────────┘
    │                                     │
    ▼ [ BRANCH B: The Mid/High Attack (Overdrive & Slap Definition) ]      │
    ┌─────────────────────────────────────────────────────────────┐       │
    │ • Master High-Pass Filter (HPF): 250 Hz                      │       │
    │ • Bass Overdrive / Distortion (SVT / B7K / SansAmp style)   │       │
    │ • Presence EQ Boost: +3.0 dB at 2.8 kHz (Metallic clack)    │       │
    └─────────────────────────────┬───────────────────────────────┘       │
                                  │                                       │
                                  ▼                                       ▼
                           ┌─────────────┐
                           │    MERGE    │ ──> Blends Anchor (70%) + Grit (45%)
                           └──────┬──────┘
                                  ▼
                           ┌─────────────┐
                           │ CABINET IR  │ ──> 8x10 or 4x10 Sealed Bass Cab Convolver
                           └──────┬──────┘
                                  ▼
                           [ XLR / PA Output ]
```

---

## 2. Choosing the Crossover Point (LPF & HPF)

The crossover point determines where the low-end anchor ends and the mid/high grit begins:

| Crossover Frequency | Sonic Character | Ideal Musical Genre |
| :---: | :--- | :--- |
| **180 Hz** | Deep, focused sub-bass; allows warm, woody natural midrange to pass through Branch B | Motown, Jazz, Neo-Soul, Classic R&B |
| **250 Hz** | **The Modern Sweet Spot:** Tight sub fundamental with clear separation from drive harmonics | Modern Rock, Pop, Hard Rock, Funk Slap |
| **350 Hz** | High crossover point; low-mids remain clean and heavy, distortion focuses strictly on top treble | Modern Metal, Djent, Industrial, Drop-Tuned Bass |

> [!IMPORTANT]
> Keep the filter frequencies complementary: set Branch A's Low-Pass Filter (LPF) to the **exact same frequency** as Branch B's High-Pass Filter (HPF) (e.g., both set to 250 Hz) to avoid an unnatural frequency gap or acoustic bump at the crossover junction.

---

## 3. Configuring Branch A: The Low-End Anchor

Branch A's sole responsibility is providing an unmoving, foundational low-end anchor that keeps the band grooving regardless of how aggressively you play.

### Parameter Configuration:
1. **Low-Pass Filter (LPF):** Set to `250 Hz` (12 dB/octave slope).
2. **Compressor Block:**
   - **Type:** VCA or Optical Compressor.
   - **Ratio:** `4:1` to `6:1`.
   - **Attack Time:** `15 ms – 25 ms` (allows initial string snap to pass before clamping down).
   - **Release Time:** `80 ms – 120 ms` (recovers quickly between sixteenth-note grooves).
   - **Threshold:** Dial down until the gain reduction meter displays **-6 dB to -8 dB** of reduction on open low E or low B plucks.
3. **Gain / Level:** Set to unity (`0.0 dB`).
4. **Distortion:** **Zero**. Never apply overdrive to Branch A.

---

## 4. Configuring Branch B: Mid/High Grit & Articulation

Branch B provides the growl, personality, fret clack, and pick articulation that cuts through wall-of-sound rhythm guitars and heavy cymbals.

### Parameter Configuration:
1. **High-Pass Filter (HPF):** Set to `250 Hz` (matching Branch A).
2. **Drive / Preamp Block:**
   - Select an analog bass overdrive, tube screamer, or bass fuzz model.
   - **Drive:** `35% – 60%` (adds harmonic grind to upper notes without muddying lows).
   - **Tone / Treble:** Boost slightly to accentuate harmonics.
3. **Parametric EQ:**
   - **Dip at 500 Hz:** `-2.5 dB` (Q=1.5) to scoop out boxy cardboard frequencies.
   - **Boost at 2.8 kHz – 3.5 kHz:** `+3.0 dB` (Q=2.0) for metallic pick attack and slap pop definition.
4. **Compressor:** Optional. Keep it bypassed or use a gentle 2:1 ratio to preserve aggressive dynamic transient spikes.

---

## 5. Recommended 4-Scene Layout for Bassists

| Scene | Name | Branch A (Low Anchor) | Branch B (Mid/High Path) | Ideal Style |
| :---: | :--- | :--- | :--- | :--- |
| **A** | **Fingerstyle Clean** | Active (-6 dB GR) | Flat EQ, Drive OFF, Clean Presence | Jazz, Pop, R&B finger grooves |
| **B** | **Slap & Pop Funk** | Fast Peak Limiting (-8 dB GR) | Scooped 500 Hz, +4 dB boost at 3.5 kHz | Marcus Miller / Flea funk slap |
| **C** | **Aggressive Drive** | Active (-6 dB GR) | High-Gain Overdrive, +3 dB cut at 2.8 kHz | Metalcore, Modern Rock, Heavy Pick |
| **D** | **Sub-Synth & Fuzz** | Deep Sub Anchor (LPF 150 Hz) | Octave Down + Gated Bass Fuzz | Muse, Synth-Bass, Dub / EDM fills |

---

## 6. Input Trim Calibration: Active (18V) vs. Passive Basses

Bass pickups output drastically different signal levels:
* **Passive P-Bass / Jazz Bass:** Output is typically moderate (-18 to -12 dBFS). Set input trim to **0.0 dB** to ensure adequate signal reaches the compressor threshold.
* **Active 9V / 18V Basses (Music Man, Dingwall, Ibanez, Warwick):** Active onboard preamps output very hot line-like transients (+6 to +12 dB higher than passive pickups).
  - Check the input meter on the UltraRig editor toolbar while slapping the low string.
  - If the red clip indicator illuminates, lower the **Input Trim by -4.0 dB to -7.0 dB** to prevent harsh digital converter distortion before the signal enters the DSP chain.

---

## 7. Pre-Gig Bass Soundcheck Checklist

- [ ] Crossover frequencies matched on both branches (e.g., LPF 250 Hz on A, HPF 250 Hz on B).
- [ ] Branch A compressor achieving consistent -6 dB to -8 dB gain reduction on low notes.
- [ ] Branch B drive produces grit without sub-bass mud.
- [ ] Merge block balance dialed: Anchor clearly audible over stage subwoofers without overpowering vocal mics.
- [ ] Output routed through a dedicated 8x10 or 4x10 bass cabinet impulse response.
