# Power Amp Tube Saturation & Output Transformer Hysteresis Guide

This guide details the non-linear physics of **Power Tube Clipping**, **Output Transformer Magnetic Hysteresis**, **Rectifier Voltage Sag**, and **Reactive Speaker Impedance** for standalone power-amp modeling within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Anatomy of Tube Power Amplifier Dynamics

While overdrive pedals and guitar preamps shape distortion symmetrically in small voltage stages, the organic "glue," punch, and touch-sensitivity of a cranked tube amplifier originate in its **output power stage**:

```
External Preamp / Pedalboard In
   │
   ▼
[ Phase Inverter Stage (Cathodyne / Long-Tailed Pair) ]
   │
   ▼
[ Power Tube Stage: Class-A Single-Ended OR Class-AB Push-Pull ] ◄── [ Rectifier Sag (5AR4 / 5Y3 / Silicon) ]
   │ (6V6 | 6L6GC | EL34 | EL84 | 6550/KT88)
   ▼
[ Output Transformer Magnetic Core Hysteresis ] (Non-linear B-H Iron Saturation & Bass Glue)
   │
   ├──► [ Global Negative Feedback (NFB) Loop: Presence & Depth Controls ]
   ▼
[ Reactive Speaker Load Curve (4Ω/8Ω/16Ω Cabinet Resonance) ] ──► Speaker Cab IR Convolution ──► Output
```

### 1.1 Three Pillars of Power Stage Tone

1. **Class-A Single-Ended vs. Class-AB Push-Pull Harmonics:**
   - **Class-A Single-Ended:** A single power tube conducts across the entire $360^\circ$ audio cycle. Clipping occurs asymmetrically, producing abundant **2nd-order even harmonics**—warm, sweet, and singing (Fender Champ 5F1).
   - **Class-AB Push-Pull:** Two or four power tubes split positive and negative signal halves. Symmetric wave limiting produces assertive **3rd-order odd harmonics** alongside subtle crossover distortion notch warmth when biased cool (Marshall Plexi, Tweed Bassman).
2. **Output Transformer Magnetic Hysteresis ("Iron Weight"):** Audio passes magnetically through stacked silicon-steel laminations. Under heavy bass hits, the magnetic core enters soft saturation (B-H hysteresis curve), rounding sharp high-frequency fizz while compressing low-end transients with warm magnetic inertia.
3. **Power Supply Rectifier Sag:** Vacuum tube rectifiers (`5Y3`, `5AR4`/`GZ34`) exhibit internal series impedance. High-energy chord strikes momentarily droop DC supply voltage by $5\%$ to $15\%$, compressing initial pick snap before blooming into sustain.

### 1.2 Power Tube Comparative Voicing Matrix

| Tube Type | Headroom | Harmonic Profile | Signature Character & Classic Amps |
| :--- | :--- | :--- | :--- |
| **`6V6`** | Low-Med | Sweet 2nd & 3rd blend | Compact, spongy, sweet blues compression (Fender Deluxe 5E3 / Princeton). |
| **`6L6GC`** | High | Tight low-end, glassy highs | Wide American punch, shimmering bottom & chime (Twin Reverb, Bassman, 5150). |
| **`EL34`** | Medium | Aggressive upper-mid bite | Chewy British grind, focused crunch, howling sustain (Plexi, JCM800, Ecstasy). |
| **`EL84`** | Low-Med | Sparkling chime, early breakup | Immediate Class-A bloom, woody jangle (Vox AC15/AC30, Matchless DC-30). |
| **`6550 / KT88`**| Extreme | Massive iron sub-punch | Stiff, thunderous, authoritative sub-bass clarity (Ampeg SVT, Marshall Major). |

---

## 2. DSP Signal Chain & Processing Topology

```
Line Input (External Preamp / Amp-in-a-Box Pedal / Guitar Direct)
   │
   ▼
[ Phase Inverter Soft-Clip & Bias Shift Stage ]
   │
   ▼
[ Power Tube Model Selector: 6V6 / 6L6 / EL34 / EL84 / 6550 ]
   │
   ├──► [ Vacuum Rectifier Dynamic Voltage Sag Envelope ] (Modulates headroom threshold)
   │
   ▼
[ Output Transformer Magnetic Core Hysteresis Emulation ] (B-H Curve Saturation + HF Roll-off)
   │
   ▼
[ Negative Feedback Loop: Depth (Resonance @ 90 Hz) & Presence (> 2.5 kHz) ]
   │
   ▼
[ Reactive Speaker Load Model + Speaker Cabinet IR ] ──► Output
```

---

## 3. Parameter Specifications

| Parameter | Range | Default | Unit | Description |
| :--- | :--- | :--- | :--- | :--- |
| `TUBE_TYPE` | `6V6` / `6L6` / `EL34` / `EL84` / `6550` | `EL34` | tube | Selects power tube transfer curve and harmonic profile. |
| `AMP_CLASS` | `CLASS_AB` / `CLASS_A_SE` | `CLASS_AB`| class| Push-pull symmetric (`AB`) vs. Single-ended asymmetric (`A_SE`). |
| `POWER_DRIVE` | `0` - `100` | `55` | % | Master volume level pushing power tubes into non-linear compression. |
| `IRON_HYST` | `0` - `100` | `45` | % | Output transformer magnetic core saturation and iron low-end thickness. |
| `RECTIFIER_SAG`| `SILICON` / `5AR4` / `5Y3` | `5AR4` | rect | Power supply stiffness (`SILICON` = instant attack; `5Y3` = deep spongy sag). |
| `BIAS_HOTNESS` | `COLD` / `BALANCED` / `HOT` | `BALANCED`| bias | Cold bias increases crisp crossover bite; Hot bias yields creamy sustain. |
| `DEPTH_NFB` | `0` - `100` | `50` | % | Low-frequency speaker resonance thump in the negative feedback loop. |
| `PRESENCE_NFB` | `0` - `100` | `55` | % | Upper-frequency shimmer and cut in the negative feedback loop. |

---

## 4. Factory Scene Presets

### Scene A: 6V6 Tweed Power Tube Compression (Deluxe 5E3 Sweet Spot)
- **Concept:** Spongy, singing, organic small-amp power tube compression perfect for pairing ahead of clean or fuzz preamps.
- **Settings:** `TUBE_TYPE = 6V6`, `AMP_CLASS = CLASS_AB`, `POWER_DRIVE = 72%`, `RECTIFIER_SAG = 5Y3`, `IRON_HYST = 60%`.
- **Feedback:** Zero global NFB (`DEPTH_NFB = 15%`, `PRESENCE_NFB = 35%`).

### Scene B: EL34 Plexi Master-Volume Cranked (British Arena Roar)
- **Concept:** Massive 100W Marshall-style output stage saturation ideal for turning solid-state or pedalboard preamps into thunderous stacks.
- **Settings:** `TUBE_TYPE = EL34`, `AMP_CLASS = CLASS_AB`, `POWER_DRIVE = 68%`, `RECTIFIER_SAG = SILICON`, `IRON_HYST = 55%`.
- **Feedback:** `DEPTH_NFB = 60%`, `PRESENCE_NFB = 64%`, `BIAS_HOTNESS = BALANCED`.

### Scene C: Single-Ended Class-A Champ Heat (Asymmetric 2nd Harmonics)
- **Concept:** Ultra-warm, sweet studio recording texture bursting with rich 2nd-order even harmonics and effortless pick dynamics.
- **Settings:** `TUBE_TYPE = 6V6` (or `EL84`), `AMP_CLASS = CLASS_A_SE`, `POWER_DRIVE = 78%`, `RECTIFIER_SAG = 5Y3`.
- **Cabinet IR:** Small 1x8 or 1x10 Jensen Alnico combo impulse response.

### Scene D: SVT 6550 Bass Power Transformer Warmth (Ampeg Iron Glue)
- **Concept:** Heavy-iron tube power stage engineered specifically to give electric basses huge chest weight, warm transformer compression, and studio polish.
- **Settings:** `TUBE_TYPE = 6550`, `AMP_CLASS = CLASS_AB`, `POWER_DRIVE = 48%`, `IRON_HYST = 75%`, `RECTIFIER_SAG = SILICON`.
- **Feedback:** `DEPTH_NFB = 72%`, `PRESENCE_NFB = 45%`, feeding an `8x10 Ampeg SVT` cabinet IR.

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **External Analog Preamp Mode:** Guitarists running external tube pedals (e.g. Kingsley, Friedman IR-X, Tone King) into Tank-G can bypass Tank-G's internal preamp block and engage **Power Amp + Cab IR Mode** directly!
- **Footswitch A:** Scene A (6V6 Tweed) / Scene B (EL34 Plexi Power Stage).
- **Footswitch B:** Scene C (Class-A Single-Ended Heat).
- **Knob 1 (GAIN / MASTER):** Power Tube Saturation Drive (`POWER_DRIVE`).
- **Knob 2 (IRON / DEPTH):** Output Transformer Hysteresis & Bass Thump.
- **Knob 3 (PRESENCE):** Negative Feedback High-Frequency Edge.

### Tank-B Control Assignments
- Bassists using external clean preamps (Darkglass, SansAmp, Aguilar) can use Scene D (`6550 Tube + Iron Hysteresis + 8x10 IR`) strictly as a studio-grade tube power amp & speaker simulator!

### Black Box Desktop Configuration
- **Effects Loop / 4-Cable Method:** Run an external physical preamp send directly into Black Box Input with Preamp bypassed so UltraRig handles purely **6550/EL34/6L6 Power Tube Modeling + Cab IR** with near-zero latency.
