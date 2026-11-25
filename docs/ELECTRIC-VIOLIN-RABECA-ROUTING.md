# Electric Violin & Brazilian Rabeca Electroacoustic Routing Guide

This guide details bowed-string transducer physics, piezo "tinny spike" suppression, Stradivarius/Guarneri acoustic body IR convolution, and preset architecture for **4/5-String Electric Violins** and the **Brazilian Rabeca Nordestina** within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Acoustic Profile & Transducer Mechanics of Bowed Strings

Unlike plucked guitars, bowed instruments sustain continuously through a complex **Helmholtz slip-stick friction** cycle between horsehair, rosin, and taut strings.

```
4-String Violin Standard:  G3 (196 Hz) | D4 (294 Hz) | A4 (440 Hz) | E5 (659 Hz)
5-String Electric Violin:  C3 (131 Hz) | G3 | D4 | A4 | E5
Rabeca Nordestina (Folk):  C3 | G3 | D4 | A4   OR   G3 | D4 | A4 | D5 (Open Modal)
```

### 1.1 Why Raw Piezo Electric Violins Sound "Tinny"

An acoustic violin's wooden soundbox acts as an extraordinarily complex resonant filter with over 20 distinct acoustic formants (most notably the Helmholtz air mode $A_0 \approx 275\text{ Hz}$, main body modes $B_1^-, B_1^+ \approx 450\text{ Hz} - 550\text{ Hz}$, and the Bridge Hill around $2.5\text{ kHz}$).

When an electric violin or amplified acoustic fiddle sends a direct bridge piezo signal into a mixer:
1. All wooden cavity resonances are absent, leaving only raw string/bridge vibration.
2. Piezo ceramic crystals exhibit high capacitive impedance and a severe resonant spike between **$2.4\text{ kHz}$ and $4.8\text{ kHz}$**, creating a harsh, nasal "mosquito" buzz.
3. **Bow Scratch & Rosin Friction:** Rapid bow direction changes (*martelé*, *spiccato*) create shrill high-frequency noise bursts above $5\text{ kHz}$.

### 1.2 The Brazilian Rabeca Nordestina

Handcrafted across Northeastern Brazil (Pernambuco, Paraíba, Ceará) for *Forró Pé-de-Serra*, *Cavalo-Marinho*, and *Maracatu* (championed by Mestre Salustiano, Antônio Nóbrega, and Siba), the **Rabeca** features flatter tops carved from *jaqueira* or *imbaúba* wood, lower tuning registers, and rustic string action. Its signature timbre relies on earthy, gravelly midrange rasp ($750\text{ Hz} - 1.8\text{ kHz}$) rather than polished classical brilliance.

---

## 2. DSP Signal Chain & Processing Topology

```
Violin / Rabeca In (Bridge Piezo / Under-Foot Transducer)
   │
   ▼
[ High-Z 1MΩ Buffer & High-Pass Filter (4-Str: 140 Hz | 5-Str/Rabeca: 95 Hz) ]
   │
   ▼
[ Surgical Piezo Tamer EQ ]
   ├── Band 1: Warmth Boost (+3.0 dB @ 280 Hz - Restores Helmholtz A0 body air)
   ├── Band 2: Nasal Cut (-5.5 dB @ 2.9 kHz - Eliminates piezo mosquito harshness)
   └── Band 3: Rosin De-Esser (Dynamic clamp @ 5.2 kHz - Smooths bow scrape)
   │
   ▼
[ Acoustic Body IR Convolution ] (Stradivarius Classical IR OR Rustic Rabeca Wood IR)
   │
   ▼
[ Smooth Optical Leveler Compressor ] (Gently evens string-to-string volume jumps)
   │
   ▼
[ Stereo Modulation / Octave Shifter / Hall Reverb ] ──► Stereo Output
```

---

## 3. Parameter Specifications

| Module | Parameter | Classical Violin | Rabeca Nordestina | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **Input Filter** | High-Pass Filter | `140 Hz` (18 dB/oct) | `95 Hz` (18 dB/oct) | Removes bow arm thump while keeping low $C_3$ ($131\text{ Hz}$). |
| **Body Warmth** | Freq / Q / Gain | `280 Hz` / `Q=1.6` / `+3.0 dB`| `240 Hz` / `Q=1.4` / `+4.0 dB`| Reintroduces missing wooden $A_0$ cavity warmth. |
| **Piezo Dip** | Freq / Q / Gain | `3.1 kHz` / `Q=2.8` / `-5.5 dB`| `3.6 kHz` / `Q=2.5` / `-4.0 dB`| Removes harsh, tinny bridge piezo buzz. |
| **Bow De-Esser** | Dynamic Clamp | `5.2 kHz` (`-4.0 dB`) | `4.8 kHz` (`-3.0 dB`) | Smooths scratchy rosin attack during aggressive *spiccato*. |
| **Body IR** | Impulse Response | `Stradivarius_1715_Mic.wav`| `Rabeca_Jaqueira_Wood.wav`| Converts dry solid-body piezo into authentic acoustic resonance. |
| **Compressor** | Ratio / Attack / Rel | `2.2:1` / `35 ms` / `180 ms`| `2.8:1` / `20 ms` / `140 ms`| Balances piercing E-string against softer G-string without killing bow swell. |
| **Reverb** | Type / Decay / Mix | `Concert Hall` / `2.4 s` / `25%`| `Warm Wood Room` / `1.2 s` / `16%`| Natural hall bloom (Classical) vs. punchy rhythmic groove (Rabeca). |

---

## 4. Factory Scene Presets

### Scene A: Classical Concert Violin IR (Stradivarius Acoustic Bloom)
- **Concept:** Transforms any solid-body 4/5-string electric violin into a warm, resonant acoustic concert violin suitable for chamber music and ballads.
- **EQ & IR:** `Stradivarius_1715_Mic.wav` IR, +3 dB @ 280 Hz, -5.5 dB @ 3.1 kHz, dynamic rosin de-esser engaged.
- **Space:** Golden Concert Hall Reverb (`2.6 s` decay, `28 ms` pre-delay, `26%` wet mix).

### Scene B: Rabeca Nordestina Rústica (Forró & Cavalo-Marinho)
- **Concept:** Earthy, punchy folk tone engineered to sit powerfully alongside accordion (*sanfona*), zabumba, and triangle in Northeastern Brazilian music.
- **EQ & IR:** `Rabeca_Jaqueira_Wood.wav` IR, `HPF = 95 Hz`, gritty midrange warmth (+3 dB @ 950 Hz), rolled-off highs above 7.5 kHz.
- **Dynamics:** Fast optical leveling (`2.8:1`) locking double-stop drones cleanly.
- **Space:** Tight Dry Wooden Room (`1.0 s`, `14%` mix).

### Scene C: Electric Fusion Violin Overdrive (Jean-Luc Ponty / Mahavishnu)
- **Concept:** Singing, horn-like violin lead tone with smooth tube saturation, high-cut filtering, and soaring stereo delay.
- **Drive & Voicing:** Dumble/Tube Screamer mid-drive (`DRIVE = 48%`), steep low-pass speaker simulation (`3.8 kHz` cutoff) eliminating fizzy bow distortion!
- **Space:** Stereo Dotted-8th Modulated Delay (`380 ms`, `30%` feedback) + Studio Plate Reverb.

### Scene D: Ethereal String Quartet Pad (Octave Down -12 st + Hall)
- **Concept:** Layers a tracking $-12\text{ st}$ cello voice and subtle chorus behind the live violin, creating an instant one-person orchestral string section.
- **Pitch & Mod:** Polyphonic Pitch Shifter (`-12 st` blended at `45%`) + Dimension D Stereo Chorus (`Mode 3`).
- **Space:** Deep Cathedral Reverb (`4.8 s` decay, `38%` mix).

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (Classical Concert Violin IR) / Scene B (Rabeca Rústica).
- **Footswitch B:** Scene C (Electric Fusion Overdrive).
- **Footswitch C:** Scene D (String Quartet Pad) / Tuner.
- **Knob 1 (EQ):** Nasal Piezo Tamer sweep (`2.2 kHz` – `4.5 kHz`).
- **Knob 2 (MOD FX):** Stereo Dimension Chorus / Octave blend.
- **Knob 3 (REVERB):** Concert Hall decay and wet/dry balance.

### Tank-B Control Assignments
- Cellists and 5-string electric violinists/violists with low $C_3$ ($131\text{ Hz}$) or $C_2$ ($65.4\text{ Hz}$) strings benefit enormously from Tank-B's transparent low-end optical compression and high-headroom cabinet/body IR loaders.

### Black Box Desktop Configuration
- **High-Z 1 MΩ Input:** Mandatory for raw passive piezo violin transducers (e.g., Fishman V-100 / Realist) to prevent capacitive impedance loading that turns strings thin and nasal.
- **Expression Pedal 1:** Continuous volume/swell control or seamless morph between dry acoustic violin IR and saturated Fusion Lead overdrive.
