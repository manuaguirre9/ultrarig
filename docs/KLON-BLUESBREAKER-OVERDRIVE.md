# Transparent Overdrive Modeling Guide: Klon Centaur & Bluesbreaker

This guide details the internal dual-gang parallel clean blending, 18V charge-pump headroom dynamics, **1N34A Germanium diode clipping**, and gain-stacking architecture for **Transparent Overdrive** (inspired by the **Klon Centaur** and **Marshall Bluesbreaker Mk1**) within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Circuit Architecture of Transparent Overdrives

Unlike classic Tube Screamer (TS808) topologies—which aggressively cut low frequencies below $720\text{ Hz}$ and compress pick attacks—**Transparent Overdrives** preserve your guitar's natural acoustic timber, extended low-end weight, and sparkling string dynamics.

```
--- KLON CENTAUR TOPOLOGY (Dual-Gang Parallel Clean Blend) ---
Input ──► [ 1MΩ Buffer ] ──┬──► [ Clean High-Headroom Rail (+18V) ] ───────────────────────┐
                           │                                                               │
                           └──► [ Mid Boost (+1.1 kHz) ] ──► [ 1N34A Germanium Clipping ] ─┼──► [ Tone ] ──► Out

--- MARSHALL BLUESBREAKER TOPOLOGY (Low-Gain Op-Amp Series) ---
Input ──► [ Dual TL072 Op-Amp Gain Stage ] ──► [ 4x 1N4148 Soft Feedback Diodes ] ──► [ Passive Tone ] ──► Out
```

### 1.1 Klon Centaur: Parallel Clean-Blend & 18V Charge Pump

1. **Internal 18V / 27V Voltage Step-Up:** By using a charge pump IC (MAX1044), the Klon triples its internal voltage swing compared to standard 9V pedals. This provides immense clean headroom so hot humbuckers never clip harsh op-amp rails before hitting the overdrive stage.
2. **Dual-Gang Gain Potentiometer:** Rotating the **Gain** knob alters two separate circuit paths simultaneously:
   - Below 10 o'clock: Almost 100% unclipped clean boost dominates, adding punch and "magical" sheen to a tube amp.
   - Above 12 o'clock: The clipped Germanium diode signal fades up alongside a gentle $+4\text{ dB}$ push centered around $1.1\text{ kHz}$, keeping single-note solos soaring and focused while clean low-end anchors chords.
3. **1N34A Germanium Soft-to-Hard Clipping:** Vintage point-contact germanium diodes introduce smooth, asymmetric compression with rich 2nd-order even harmonics.

### 1.2 Marshall Bluesbreaker Mk1: Amp-Like Op-Amp Edge

Introduced in 1991 to replicate a cranked 1962 Marshall Bluesbreaker combo at bedroom volume (famously championed by **John Mayer** and **Eric Clapton**), it runs a flat-EQ dual op-amp stage feeding soft clipping diodes in series within the negative feedback loop. It maintains total chord clarity and responds instantaneously to pick dynamics.

### 1.3 Dual Gain Stacking Strategy

The hallmark of boutique pedalboards is **Gain Stacking**:
- Placing a **Bluesbreaker** (set to low edge-of-breakup) *after* a **Klon Centaur** (set as a clean mid-boost) pushes the Bluesbreaker's dynamic diodes harder for thick, vocal lead sustain while preserving transparent, uncompressed rhythm tones when the Klon is disengaged.

---

## 2. DSP Signal Chain & Processing Topology

```
Guitar / Bass In (Single-Coils / Humbuckers)
   │
   ▼
[ High-Z 1MΩ Input Buffer ]
   │
   ├───► [ Mode A: Klon Centaur Parallel Clean/Germanium Blend ]
   │           ├── Clean Rail (18V Headroom Boost)
   │           └── Clipping Rail (1.1 kHz Focus + 1N34A Germanium Soft-Clip)
   │
   ├───► [ Mode B: Bluesbreaker Series Soft-Diode Stage (4x 1N4148) ]
   │
   ├───► [ Mode C: Dual-Stack Cascade (Klon Boost -> Bluesbreaker Drive) ]
   │
   ▼
[ Active Treble Tilt Filter (Post-Drive High Shelf) ] ──► [ Tube Amp Preamp & IR ] ──► Output
```

---

## 3. Parameter Specifications

| Parameter | Range | Default | Unit | Description |
| :--- | :--- | :--- | :--- | :--- |
| `DRIVE_MODEL` | `KLON` / `BLUESBREAKER` / `STACKED` | `KLON` | mode | Selects Klon Centaur, Marshall Bluesbreaker, or Series Dual Stack. |
| `GAIN_DRIVE` | `0` - `100` | `35` | % | Controls clipping drive (Klon blends parallel clean rail inversely). |
| `CLEAN_BLEND` | `0` - `100` | `55` | % | Explicit override of clean headroom parallel blend in Klon mode. |
| `HEADROOM_V` | `9V` / `18V` / `27V` | `18V` | volts| Internal rail voltage simulation (higher = cleaner, tighter bass punch). |
| `DIODE_TYPE` | `GERM_1N34A` / `SILICON_4148` | `GERM_1N34A`| mode | Germanium (warm/creamy) vs. Silicon (tight/snappy crunch). |
| `MID_PUSH` | `0` - `100` | `40` | % | Klon-style $1.1\text{ kHz}$ vocal presence push for cutting solo projection. |
| `TREBLE_TILT` | `0` - `100` | `55` | % | Active post-drive brightness control ($2.5\text{ kHz}$ shelving contour). |
| `OUTPUT_LEVEL` | `0` - `100` | `68` | % | Master output level driving downstream preamps into natural tube saturation. |

---

## 4. Factory Scene Presets

### Scene A: Klon Clean Boost & Buffer Magic (Always-On Sparkle)
- **Concept:** The iconic "magic clean enhancer"—adds 3D sheen, crisp transient snap, and harmonic bloom to clean amps without audible distortion.
- **Settings:** `DRIVE_MODEL = KLON`, `GAIN_DRIVE = 15%`, `CLEAN_BLEND = 85%`, `HEADROOM_V = 18V`, `OUTPUT_LEVEL = 75%`.
- **Tone:** `TREBLE_TILT = 58%`, `MID_PUSH = 25%`.

### Scene B: Bluesbreaker Transparent Edge (John Mayer / Continuum)
- **Concept:** Open, airy, flat-EQ edge-of-breakup that feels like a cranked blackface/vintage Marshall combo responding cleanly to fingerpicking.
- **Settings:** `DRIVE_MODEL = BLUESBREAKER`, `GAIN_DRIVE = 42%`, `DIODE_TYPE = SILICON_4148`, `HEADROOM_V = 18V`.
- **Tone:** `TREBLE_TILT = 54%`, `OUTPUT_LEVEL = 65%`.

### Scene C: Klon Mid-Boost Lead Stack (Pushing Tube Preamp)
- **Concept:** Uses a cranked Klon drive stage (`1.1 kHz` mid-push) directly ahead of a breaking-up Fender/Marshall amp for vocal, singing rock and blues solos.
- **Settings:** `DRIVE_MODEL = KLON`, `GAIN_DRIVE = 64%`, `DIODE_TYPE = GERM_1N34A`, `MID_PUSH = 70%`, `OUTPUT_LEVEL = 80%`.
- **Space:** Warm Analog Tape Slapback (`140 ms`) + Spring Reverb.

### Scene D: Dual Stack Boutique Saturation (Klon -> Bluesbreaker)
- **Concept:** Two transparent drives stacked in series creating smooth, singing, multi-stage sustain while keeping complex extended jazz/fusion chords completely distinct.
- **Settings:** `DRIVE_MODEL = STACKED`, `KLON_GAIN = 30%`, `BLUESBREAKER_GAIN = 48%`, `HEADROOM_V = 27V`.
- **Space:** Stereo Modulated Delay (`dotted 8th`, `410 ms`, `25%` feedback) + Studio Room Reverb.

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (Klon Clean Boost) / Scene B (Bluesbreaker Transparent Edge).
- **Footswitch B:** Scene C (Klon Mid-Boost Lead).
- **Footswitch C:** Scene D (Dual Stack Boutique) / Drive Bypass.
- **Knob 1 (GAIN):** Klon Parallel Gain / Bluesbreaker Clipping drive.
- **Knob 2 (TONE):** Active Treble Tilt ($2.5\text{ kHz}$ shelf).
- **Knob 3 (LEVEL):** Clean Boost Output driving downstream tube amp preamps.

### Tank-B Control Assignments
- Klon's parallel **Clean Blend** is extraordinary for electric bassists: because the low-end fundamentals remain untouched on the clean rail while the upper harmonics clip mildly through 1N34A Germanium diodes, bass chords stay thick and massive without losing sub-bass weight.

### Black Box Desktop Configuration
- **MIDI CC #89:** Instant footswitch stacking toggle allowing players to kick the Klon clean booster ahead of any amp/cab preset cleanly.
- **Dynamic Headroom:** Switch between `9V` (spongy sag) and `18V`/`27V` (hi-fi transparent punch) directly per preset scene.
