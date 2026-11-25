# Vox AC15 & Matchless Lightning 15W Class-A Routing Guide

This guide details the 15-watt dual-EL84 power tube architecture, **EZ81/5AR4 tube rectifier sag**, interactive Top Boost vs. Normal channels, and practical preset configuration for the **Vox AC15** and boutique **Matchless Lightning 15** within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Circuit Architecture of the 15W Class-A British Combo

Introduced in 1958 by Dick Denney at Jennings Musical Industries (and modernized in 1993 by Mark Sampson as the Matchless Lightning 15), the 15-watt British 1x12 combo is one of rock history's most expressive low-wattage tube circuits. While its bigger sibling (the AC30) stays clean much louder, the AC15's **dual EL84 power stage** saturates effortlessly into singing harmonic bloom.

```
Instrument In
   │
   ├───► [ Normal Channel: Fat Woody Midrange (Minimal Tonestack Loss) ] ──────────┐
   │                                                                               │
   └───► [ Top Boost / Lightning Channel: Interactive Passive Bass & Treble ] ─────┤
                                                                                   │
                                                                                   ▼
                                                                   [ 12AX7 Phase Inverter + Master Cut ]
                                                                                   │
                                                                                   ▼
[ 1x12 Celestion Alnico Blue IR ] ◄── [ 2x EL84 Power Stage (Zero NFB + EZ81 Rectifier Sag + Bias Tremolo) ]
```

### 1.1 Dual EL84 Power Saturation & EZ81 Tube Rectifier Sag

1. **Zero Negative Feedback (No NFB) Dual-EL84 Output:** Running two cathode-biased EL84 pentodes with zero global negative feedback allows the power tubes to breathe dynamically with every pick stroke, creating rich 2nd-order and 3rd-order harmonic overtones at modest gain levels.
2. **EZ81 / 5AR4 Tube Rectifier Voltage Sag:** Unlike solid-state diode rectifiers that supply instantaneous rigid DC voltage, vacuum tube rectifiers exhibit internal resistance. When hit by a loud chord or pick transient, plate voltage dips temporarily ("sags") for ~30 ms to 80 ms before recovering. This yields natural organic compression on attacks followed by blooming note sustain.

### 1.2 Normal Channel vs. Top Boost Channel

- **Normal Channel:** Features a remarkably direct signal path with almost zero passive tone-stack insertion loss. Warm, thick, and punchy in the lower midrange, making it an unmatched pedal platform for Fuzz, Treble Boosters, and Klon drives.
- **Top Boost / Matchless Lightning Channel:** Incorporates the legendary interactive Bass and Treble controls (where reducing Bass and Treble pushes midrange forward) plus an extra 12AX7 gain stage for shimmering high-end jangle.

---

## 2. DSP Signal Chain & Processing Topology

```
Guitar In (Single-Coils / P90s / Gretsch Filter'Trons)
   │
   ▼
[ Optional Pre-Amp Pedal Push: Dallas Rangemaster Treble Booster / Klon Clean Boost ]
   │
   ▼
[ Channel Selector: Normal (Warm/Fat) OR Top Boost (Jangly Chime) ]
   │
   ▼
[ Phase Inverter & Passive Master "Cut" Control ] (Rolls off high fizz gently)
   │
   ▼
[ 2x EL84 Power Amp Emulation + EZ81 Rectifier Sag Compression ]
   │
   ▼
[ Integrated Bias-Wiggle Tremolo Stage ] (Optional hypnotic vintage amplitude pulse)
   │
   ▼
[ 1x12 Celestion Alnico Blue (G12 Alnico) IR Convolution ] ──► Ambient Spring & Tape Delay ──► Out
```

---

## 3. Parameter Specifications

| Parameter | Range | Default | Unit | Description |
| :--- | :--- | :--- | :--- | :--- |
| `CHANNEL_MODE` | `NORMAL` / `TOP_BOOST` | `TOP_BOOST` | mode | Selects Normal woody channel or Top Boost chime channel. |
| `PREAMP_GAIN` | `0` - `100` | `58` | % | Input drive feeding 12AX7 preamp stages. |
| `BASS` | `0` - `100` | `46` | % | Interactive low-end shelf (Top Boost channel). |
| `TREBLE` | `0` - `100` | `64` | % | Interactive upper chime boost (Top Boost channel). |
| `MASTER_CUT` | `0` - `100` | `32` | % | Post-phase inverter treble smoothing filter (turn up to soften fizz). |
| `POWER_DRIVE` | `0` - `100` | `62` | % | Dual EL84 output saturation level driving 15W power compression. |
| `RECTIFIER_SAG` | `0` - `100` | `55` | % | EZ81 vacuum tube voltage droop compression under hard transients. |
| `TREMOLO_RATE` | `0.8` - `10.0` | `3.8` | Hz | Integrated power-tube bias tremolo speed. |
| `TREMOLO_DEPTH`| `0` - `100` | `0` | % | Bias-wiggle tremolo amplitude modulation depth. |
| `CAB_IR` | `ALNICO_BLUE` / `GREENBACK` | `ALNICO_BLUE`| file | 1x12 speaker cabinet impulse response profile. |

---

## 4. Factory Scene Presets

### Scene A: Beatles 60s Jangle Clean (Rickenbacker & Strat Chime)
- **Concept:** Sparkling, glassy 1964 British Invasion chime with open acoustic-like harmonics and crisp note separation.
- **Voicing:** `CHANNEL_MODE = TOP_BOOST`, `PREAMP_GAIN = 36%`, `POWER_DRIVE = 42%`, `RECTIFIER_SAG = 35%`.
- **EQ & Cut:** `BASS = 44%`, `TREBLE = 68%`, `MASTER_CUT = 25%`.
- **Cabinet IR:** `1x12_Celestion_Alnico_Blue.wav`.
- **Space:** Vintage Studio Chamber Reverb (`1.6 s`, `20%` mix).

### Scene B: British Invasion Edge-of-Breakup (Hank Marvin / Early Clapton)
- **Concept:** Touch-sensitive semi-clean responding expressively to picking force—glassy when strummed softly, warm tube bark when dug into.
- **Voicing:** `CHANNEL_MODE = NORMAL`, `PREAMP_GAIN = 60%`, `POWER_DRIVE = 65%`, `RECTIFIER_SAG = 60%`.
- **EQ & Cut:** `MASTER_CUT = 38%`.
- **Space:** Vintage Binson Echorec / Tape Slapback (`280 ms`, `24%` feedback) + Spring Reverb.

### Scene C: Creamy EL84 Tube Sag Lead (Matchless Lightning Roar)
- **Concept:** Cranking the 15W dual-EL84 power section all the way up for singing, compressed, harmonically rich solo sustain.
- **Voicing:** `CHANNEL_MODE = TOP_BOOST`, `PREAMP_GAIN = 78%`, `POWER_DRIVE = 85%`, `RECTIFIER_SAG = 75%`.
- **Boost:** Upstream Treble Booster pushing `1.4 kHz` bite into the glowing EL84 power stage.
- **EQ & Cut:** `BASS = 40%`, `TREBLE = 60%`, `MASTER_CUT = 46%` (smooth non-fatiguing edge).
- **Space:** Warm Tape Delay (`400 ms`, `26%` feedback).

### Scene D: Indie Pop Tremolo Room (Atmospheric British Pulse)
- **Concept:** Hypnotic bias-modulated tube tremolo over shimmering chord cleans, steeped in spring tank ambiance.
- **Voicing:** `CHANNEL_MODE = TOP_BOOST`, `PREAMP_GAIN = 40%`, `POWER_DRIVE = 48%`.
- **Modulation:** Integrated Bias Tremolo (`TREMOLO_RATE = 4.2 Hz`, `TREMOLO_DEPTH = 65%`).
- **Space:** 3-Spring Tank Reverb (`2.4 s`, `30%` mix).

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (60s Jangle Clean) / Scene B (British Edge-of-Breakup).
- **Footswitch B:** Scene C (Creamy EL84 Tube Sag Lead).
- **Footswitch C:** Scene D (Indie Tremolo Room) / Bias Tremolo Toggle.
- **Knob 1 (GAIN):** Preamp + EL84 Power Drive.
- **Knob 2 (TONE):** Master Cut control (turn clockwise to warm up bright pickups).
- **Knob 3 (MOD / REVERB):** Tremolo Speed / Spring Reverb balance.

### Tank-B Control Assignments
- Vintage-voiced bassists (emulating 1960s British recording sessions with flatwound strings) can use the `NORMAL` channel with `RECTIFIER_SAG = 50%` and `POWER_DRIVE = 45%` for warm, thumpy, gently compressed tube bass warmth.

### Black Box Desktop Configuration
- **Expression Pedal 1:** Map continuously to `TREMOLO_RATE` (morphing speed live like a vintage rotary horn) or `POWER_DRIVE`.
- **Stereo Dual-1x12 IR:** Blend `Celestion Alnico Blue` (Left) with `Celestion G12M-25 Greenback` (Right) for wide British combo studio depth.
