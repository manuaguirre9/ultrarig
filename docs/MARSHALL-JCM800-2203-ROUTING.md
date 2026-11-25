# Marshall JCM800 2203 & Hot-Rod Mod High-Gain Routing Guide

This guide details the classic **3-stage 12AX7 preamp cascade**, **1000 pF Bright Cap** interaction, **High vs. Low input** architecture, **Boss SD-1 / Hot-Rod #34/#39** boosting strategies, and preset configuration for the **Marshall JCM800 2203** within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Circuit Architecture of the Marshall JCM800 2203

Released in 1981 (evolving directly from the 1975 JMP Master Volume 2203), the single-channel 100-watt **Marshall JCM800 2203** defined the sonic punch of 1980s hard rock, NWOBHM, and thrash metal—anchored in the rigs of **Zakk Wylde**, **Slash**, **Kerry King**, **Randy Rhoads**, and **John Sykes**.

```
Guitar In
   │
   ├── (HIGH SENSITIVITY JACK) ──► [ V1B Stage + 470k/1000pF Bright Cap ] ──┐
   │                                                                        │
   └── (LOW SENSITIVITY JACK: Bypasses V1B for Pure Clean Headroom!) ───────┼──► [ V1A 10k Cold Clipper ]
                                                                                           │
                                                                                           ▼
                                                                           [ V2A Gain Stage & V2B Cathode Follower ]
                                                                                           │
                                                                                           ▼
                                                                           [ Passive Tonestack (Bass / Mid / Treble) ]
                                                                                           │
                                                                                           ▼
[ 4x12 Marshall 1960A IR (G12T-75 / V30 / Greenback) ] ◄── [ 4x EL34 Power Amp + Presence NFB ]
```

### 1.1 High Input vs. Low Input & the 1000 pF Bright Cap

- **High Input:** Cascades through all three 12AX7 triode stages (`V1B` $\to$ `V1A` $\to$ `V2A`). The $10\text{ k}\Omega$ cathode resistor on V1A clips asymmetrically, yielding focused, cutting British midrange crunch.
- **Low Input:** Mechanically bypasses V1B entirely, feeding the guitar straight into V1A. Because one full voltage-amplification stage is omitted, the Low Input stays remarkably clean, crisp, and punchy—an ideal clean pedal platform!
- **1000 pF Bright Cap Behavior:** A bright capacitor sits across the Preamp Gain pot. At lower gain settings (`1 - 4`), high frequencies bypass the pot completely, creating sharp, bright, sometimes biting trebles. Above Gain `7`, the Bright Cap's effect vanishes naturally as the pot approaches full conduction.

### 1.2 Why Giants Boosted the 2203: SD-1 Pushing & Hot-Rod Mods

A bone-stock JCM800 2203 delivers roaring classic-rock crunch rather than saturated modern metal sustain. Players unlocked modern aggression in two legendary ways:
1. **Front-End Overdrive Push (Boss SD-1 / Ibanez TS808):** Running an asymmetric **Boss SD-1** ahead of the High Input (`LEVEL = 100%`, `DRIVE = 15%`) strips away flubby sub-100 Hz bass *before* V1B while pushing mid-focused ($800\text{ Hz}$) signal hard into the tubes—yielding tight palm mutes and howling pinch harmonics (Zakk Wylde / Kerry King).
2. **Hot-Rod Preamp Mods (SIR #34 / #39 & Jose Mod):** Inserting an additional 12AX7 tube stage or switchable clipping diodes directly inside the chassis produces thick, singing *Appetite for Destruction* compression without needing an external floor pedal.

---

## 2. DSP Signal Chain & Processing Topology

```
Guitar In (Humbuckers / High-Output Pickups)
   │
   ▼
[ Fast Noise Gate / Downward Expander ] (Tames boosted high-gain idle hiss)
   │
   ├──► [ Optional Front-End Pedal Push: Boss SD-1 Asymmetric Overdrive ] (Level 90%, Drive 18%)
   │
   ▼
[ Input Selector: Stock High / Stock Low (Clean) / Hot-Rod #39 Extra 12AX7 Stage ]
   │
   ▼
[ 1000 pF Bright Cap + 10k Cold Clipper + Cathode Follower ]
   │
   ▼
[ 3-Band British Tonestack (Bass / Middle / Treble) ]
   │
   ▼
[ 100W 4x EL34 Power Amp Model + Negative Feedback Presence ]
   │
   ▼
[ Speaker Cabinet IR: Marshall 1960A (G12T-75) OR 1960BV (V30 / Greenback) ] ──► FX Loop ──► Out
```

---

## 3. Parameter Specifications

| Parameter | Range | Default | Unit | Description |
| :--- | :--- | :--- | :--- | :--- |
| `INPUT_JACK` | `HIGH` / `LOW` / `HOT_ROD` | `HIGH` | mode | Stock 3-stage High, 2-stage Clean Low, or 4-stage Hot-Rod Mod. |
| `SD1_BOOST` | `OFF` / `ON` | `OFF` | bool | Engages Boss SD-1 asymmetric mid-boost ahead of preamp input. |
| `PREAMP_GAIN` | `0` - `100` | `68` | % | Gain pot controlling V1B/V1A saturation (and Bright Cap bypass ratio). |
| `BRIGHT_CAP` | `STOCK_1000PF` / `MOD_OFF` | `STOCK_1000PF`| mode | Retains aggressive 1000 pF treble snap or softens top-end fizz. |
| `BASS` | `0` - `100` | `54` | % | Tone stack bottom end. |
| `MIDDLE` | `0` - `100` | `68` | % | Classic British bark and solo projection midrange. |
| `TREBLE` | `0` - `100` | `58` | % | High-frequency bite and pick cut. |
| `MASTER_VOL` | `0` - `100` | `60` | % | Drives 4x EL34 power tubes into warm output transformer punch. |
| `PRESENCE` | `0` - `100` | `56` | % | Negative feedback high-frequency presence in power stage. |
| `CAB_IR` | `G12T75` / `V30` / `GREENBACK` | `G12T75` | file | 4x12 Marshall cabinet speaker profile. |

---

## 4. Factory Scene Presets

### Scene A: Classic 80s JCM800 Crunch (Stock High Input)
- **Concept:** Raw, dynamic, punchy 1980s hard-rock crunch (AC/DC, The Cult, early Iron Maiden) cleaning up cleanly with guitar volume knob rollback.
- **Voicing:** `INPUT_JACK = HIGH`, `SD1_BOOST = OFF`, `PREAMP_GAIN = 65%`, `MASTER_VOL = 65%`.
- **EQ & IR:** `BASS = 52%`, `MIDDLE = 68%`, `TREBLE = 56%`, `CAB_IR = GREENBACK` (or `G12-65`).
- **Space:** Subtle Studio Wood Room (`1.1 s`, `14%` mix).

### Scene B: Zakk Wylde / Kerry King SD-1 Metal Lead (Tight Thrash & Pinch Harmonics)
- **Concept:** Blistering, ultra-tight heavy metal rhythm and screaming pinch-harmonic leads driven by a front-end SD-1 boost.
- **Voicing:** `INPUT_JACK = HIGH`, `SD1_BOOST = ON` (`DRIVE = 18%`, `LEVEL = 95%`), `PREAMP_GAIN = 78%`.
- **EQ & IR:** `BASS = 48%`, `MIDDLE = 62%`, `TREBLE = 64%`, `PRESENCE = 66%`, `CAB_IR = V30` (or `G12T75`).
- **Space:** Noise Gate at `-32 dBFS` + Subtle Chorus / Micro-Pitch Detuner for lead chorus depth.

### Scene C: Slash Appetite Hot-Rod Mod (`#39` Extra Gain Stage)
- **Concept:** Thick, singing, harmonic-rich late-80s Los Angeles rock tone with vocal midrange creaminess and smooth high-end compression.
- **Voicing:** `INPUT_JACK = HOT_ROD`, `SD1_BOOST = OFF`, `PREAMP_GAIN = 72%`, `BRIGHT_CAP = MOD_OFF` (smooth warm lead edge).
- **EQ & IR:** `BASS = 56%`, `MIDDLE = 74%`, `TREBLE = 52%`, `CAB_IR = V30 / GREENBACK`.
- **Space:** Analog Slapback Delay (`125 ms`) + Studio Plate Reverb (`1.8 s`, `20%` mix).

### Scene D: Low-Input Volume-Rollback Clean & Blues
- **Concept:** Punchy, authoritative British clean using the V1B-bypassed Low Input Jack—crystal clear for chorus, arpeggios, and classic blues pedals.
- **Voicing:** `INPUT_JACK = LOW`, `PREAMP_GAIN = 45%`, `MASTER_VOL = 55%`.
- **Space:** Vintage 3-Spring Reverb (`1.9 s`, `22%` mix) + Stereo Tape Delay (`380 ms`).

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (Classic 80s Crunch) / Scene B (Zakk SD-1 Metal Boost).
- **Footswitch B:** Scene C (Slash Hot-Rod `#39` Lead).
- **Footswitch C:** Scene D (Low Input Clean) / Noise Gate Toggle.
- **Knob 1 (GAIN):** Preamp Saturation Gain (`PREAMP_GAIN`).
- **Knob 2 (EQ / MID):** British Midrange Bark (`MIDDLE`).
- **Knob 3 (REVERB / DELAY):** Studio Room & Solo Delay blend.

### Tank-B Control Assignments
- Rock and punk bassists (inspired by Lemmy Kilmister's cranked Marshall Super Bass / JCM800 roar) can select `INPUT_JACK = LOW`, push `MASTER_VOL = 75%`, and blend parallel clean low-end below `160 Hz` for monstrous grinding overdrive!

### Black Box Desktop Configuration
- **Stereo 4x12 Mixing:** Load `Celestion G12T-75` on Left Output and `Celestion Vintage 30` on Right Output for classic 1980s studio wall-of-guitars spread.
- **MIDI CC #91:** Instant footswitch engagement of the front-end **Boss SD-1 Overdrive** without changing preamp settings!
