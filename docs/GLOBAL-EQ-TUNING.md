# UltraRig Global EQ vs. Preset EQ Stage Tuning Guide

One of the most common challenges guitarists and bassists face is the **"bedroom-to-stage disconnect"**: presets carefully dialed at home using studio monitors or headphones sound drastically boomy, piercing, or buried in the mix when plugged into a live venue's PA system or stage monitors.

Adjusting 32 individual presets and 128 scenes during a rushed 10-minute soundcheck is impossible. **Global EQ** solves this problem by applying universal acoustic correction at the final output stage without altering your saved preset libraries.

This guide explains the distinct roles of Preset EQ versus Global EQ, optimal master high/low-pass filtering, and quick soundcheck recipes for various venue acoustics.

---

## 1. Architectural Distinction: Preset EQ vs. Global EQ

```
 [ Instrument ]
       │
       ▼
 ┌───────────────┐
 │   PRESET EQ   │ ──> Artistic Tone Sculpting (Per Preset & Scene)
 │ (Drive / Amp) │     - Mid boost on Lead scene (Tube Screamer style)
 └───────┬───────┘     - Bright acoustic guitar shimmer vs. dark rhythm chug
         │             - Saved inside individual `.json` preset files
         ▼
 ┌───────────────┐
 │ IR / FX Chain │
 └───────┬───────┘
         │
         ▼
 ┌───────────────┐
 │   GLOBAL EQ   │ ──> Environmental Acoustic Correction (Universal)
 │ (Output DAC)  │     - Master Low Cut (HPF) & High Cut (LPF)
 └───────┬───────┘     - Room resonance dips (muddy 350 Hz, harsh 4 kHz)
         │             - Stored in global pedal memory; NEVER alters presets
         ▼
 [ FOH PA / Stage Monitor / FRFR / In-Ear Monitors ]
```

| Dimension | Preset EQ (Parametric / Amp Stack) | Global Output EQ |
| :--- | :--- | :--- |
| **Purpose** | Artistic character of the instrument & amp | Acoustic compensation for speakers and rooms |
| **Scope** | Applies exclusively to the active preset/scene | Applies globally across all 32 banks and presets |
| **Storage** | Serialized into preset export files | Stored in pedal runtime flash memory |
| **Soundcheck Use** | Never adjust during soundcheck | The primary tool for venue adaptation |

---

## 2. Essential Master Filtering (HPF & LPF)

A full-range PA system reproduces frequencies from 20 Hz to 20,000 Hz. An electric guitar speaker cabinet, however, naturally rolls off frequencies below ~80 Hz and above ~6 kHz.

Applying a **High-Pass Filter (HPF)** and **Low-Pass Filter (LPF)** at the global master stage instantly tightens the sound:

```
  Response (dB)
    0 dB ──┐         ┌────────────────────────┐
           │        /                          \
           │       /                            \
           │      /                              \
  -6 dB ───┤     /                                \
           │    /                                  \
 -12 dB ───┴───/                                    \──────
              ▲                                      ▲
           HPF (Low Cut)                          LPF (High Cut)
           Guitar: 80 - 100 Hz                    Guitar: 5.5 - 6.5 kHz
           Bass:   30 - 40 Hz                     Bass:   4.5 - 5.5 kHz
```

### High-Pass Filter (Low Cut)
* **Electric Guitar:** Set to **80 Hz – 100 Hz**.
  - **Why:** Electric guitar low E is ~82.4 Hz (Drop D is ~73.4 Hz). Any energy below this range is stage rumble, handling noise, or sub-harmonic thumps that compete with the bass guitar fundamental and kick drum.
* **Bass Guitar (Tank-B):** Set to **30 Hz – 40 Hz**.
  - **Why:** Low B on a 5-string bass is ~30.9 Hz. Cutting below 30 Hz prevents power amp headroom starvation and eliminates speaker cone over-excursion without sacrificing punch.

### Low-Pass Filter (High Cut)
* **Electric Guitar:** Set to **5.5 kHz – 6.5 kHz**.
  - **Why:** Physical 12-inch guitar speakers (Celestion V30, Greenback, Creamback) produce virtually no usable musical frequencies above 6 kHz. Removing frequencies above 6.5 kHz eliminates harsh digital fizz and piercing PA compression horn sizzle.
* **Bass Guitar (Tank-B):** Set to **4.5 kHz – 5.5 kHz**.
  - **Why:** Tames finger clack and harsh tweeter hiss when playing through modern bass cabs with high-frequency horns.

---

## 3. Parametric EQ Frequency Bands for Live Environments

When the venue has pronounced acoustic flaws, use the Global EQ's parametric mid bands to address specific frequency problem areas:

| Frequency Range | Acoustic Description | Live Problem & Global EQ Solution |
| :--- | :--- | :--- |
| **200 Hz – 400 Hz** | *Low-Mids / Mud / Boxiness* | Small clubs, concrete walls, and hollow stages resonate heavily here. Cut **-2 dB to -4 dB** (Q=1.5) to restore clarity. |
| **500 Hz – 800 Hz** | *Body / Cardboard* | Too much makes guitar sound like a tin can; too little makes tone thin and detached. Usually kept neutral unless compensating for a hollow cab. |
| **1.5 kHz – 3.0 kHz** | *Presence / Cut-Through* | This band determines whether your solos cut through cymbals and vocals. Boost **+1.5 dB to +3.0 dB** if you are buried in the live band mix. |
| **3.5 kHz – 5.0 kHz** | *Bite / Ear Fatigue* | Cheap PA horns and reflective tile walls often peak here, causing listener fatigue. Cut **-2 dB to -3 dB** to smooth out harsh high-gain leads. |

---

## 4. Quick Soundcheck Recipes for Different Venues

```
 ┌────────────────────────────────────────────────────────────────────────┐
 │                     Venue Compensation Presets                         │
 ├───────────────────┬────────────────────────────────────────────────────┤
 │ 1. Boomy Hall     │ HPF: 100 Hz  | 320 Hz: -3 dB | LPF: 6.0 kHz        │
 │ 2. Piercing PA    │ HPF: 80 Hz   | 4.0 kHz: -3 dB| LPF: 5.5 kHz        │
 │ 3. Outdoor Stage  │ HPF: 70 Hz   | 120 Hz: +2 dB | LPF: 6.5 kHz        │
 │ 4. Flat IEMs / PA │ HPF: 80 Hz   | All flat (0 dB)| LPF: 6.5 kHz       │
 └───────────────────┴────────────────────────────────────────────────────┘
```

### Scenario A: Boomy Club (Concrete Walls, High Ceiling)
* **Symptom:** Rhythms sound muddy; low palm mutes overwhelm the front rows.
* **Global EQ Settings:**
  - **HPF:** `100 Hz`
  - **Band 1 (Low-Mid):** `320 Hz`, Gain: `-3.5 dB`, Q: `1.4`
  - **LPF:** `6.0 kHz`

### Scenario B: Piercing / Harsh Stage Monitors or PA Horns
* **Symptom:** Overdrive and lead presets hurt the ears; cymbals and guitar highs bleed together aggressively.
* **Global EQ Settings:**
  - **HPF:** `85 Hz`
  - **Band 2 (High-Mid):** `4.0 kHz`, Gain: `-3.0 dB`, Q: `2.0`
  - **LPF:** `5.5 kHz`

### Scenario C: Open Outdoor Stage / Festival Tent
* **Symptom:** Sound disperses rapidly into open air; guitar sounds thin, dry, and lacking low-end punch.
* **Global EQ Settings:**
  - **HPF:** `70 Hz`
  - **Band 1 (Low Shelf):** `120 Hz`, Gain: `+2.0 dB`
  - **Band 2 (Mid Boost):** `2.2 kHz`, Gain: `+1.5 dB`
  - **LPF:** `6.5 kHz`

### Scenario D: High-End In-Ear Monitoring (IEMs) & Studio FRFR
* **Symptom:** High-fidelity IEMs already have balanced drivers.
* **Global EQ Settings:**
  - **HPF:** `80 Hz`
  - **Bands:** Neutral (`0.0 dB`)
  - **LPF:** `6.5 kHz`

---

## 5. Collaboration with Front-of-House (FOH) Sound Engineers

1. **Keep Global EQ Conservative:**
   - Global EQ is intended for gentle broad strokes (1 to 4 dB max). Never use extreme cuts (-12 dB) to fix a bad preset; fix the preset's drive or IR instead.
2. **Communicate Master Cuts to the Engineer:**
   - Let the sound engineer know you already have an 80 Hz high-pass filter running internally on the pedal. This saves them channel setup time and ensures they don't double-filter your low end aggressively.
3. **Soundcheck with Your Heaviest & Cleanest Presets:**
   - Check your loudest high-gain rhythm tone first to verify low-mid clarity.
   - Check your pristine clean tone second to ensure top-end sparkle is not choked by the master LPF.
