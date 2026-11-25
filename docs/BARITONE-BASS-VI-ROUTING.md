# Baritone Guitar & Fender Bass VI Electroacoustic Routing Guide

This guide details the scale-length string physics, **160 Hz Split-Band Crossover** architecture, strangle-switch low-end control, and preset configuration for **Baritone Guitars** ($B_1/A_1$) and the **Fender Bass VI** ($E_1$ octave below guitar) within UltraRig for M-VAVE hardware (Tank-B, Tank-G v1/v2, and Black Box).

---

## 1. Tuning, Scale Length & Acoustic Challenges

Spanning the sonic territory between standard electric guitar and 4-string bass guitar, **Baritone Guitars** and **Bass VIs** create immense low-frequency energy that overwhelms conventional guitar amplifiers and overdrive circuits.

```
Baritone B Standard (27" - 28.5" Scale): B1 (61.7 Hz) | E2 | A2 | D3 | F#3 | B3
Baritone A Drop / Standard:              A1 (55.0 Hz) | D2 | G2 | C3 | E3  | A3
Fender Bass VI (30" Scale - Octave Low): E1 (41.2 Hz) | A1 | D2 | G2 | B2  | E3  <=== True Sub-Bass Range
```

### 1.1 Why Standard Guitar Amp Chains Fail on Baritone & Bass VI

1. **Intermodulation Mud & Preamp "Farting Out":** Conventional guitar amps and distortion pedals are voiced for $E_2$ ($82.4\text{ Hz}$). Sending polyphonic chords rooted on $B_1$ ($61.7\text{ Hz}$) or $E_1$ ($41.2\text{ Hz}$) into standard overdrive clipping generates discordant intermodulation products, causing muddy, indistinct sub-bass mush.
2. **Cabinet Boom vs. Missing Twang:** Plugging a Bass VI into a dedicated bass cab preserves low end ($<100\text{ Hz}$) but sounds dull and lifeless above $2\text{ kHz}$, robbing it of its iconic metallic surf "twang". Conversely, a standard guitar cabinet rolls off frequencies below $80\text{ Hz}$, stripping foundational weight.
3. **The Classic Fender "Strangle Switch":** Originally built into the 1961 Fender Bass VI, this passive series capacitor acts as a subtle high-pass filter cutting low-end mud during bright solo lines or chorus-drenched Dream Pop chords.

---

## 2. DSP Signal Chain: The Split-Band Crossover Solution

To solve low-end distortion mud while keeping aggressive pick snap and stereo modulation crystal clear, UltraRig implements a **Linkwitz-Riley 160 Hz Split Crossover**:

```
Baritone / Bass VI In (Single-Coils / Lipstick / Humbuckers)
   │
   ▼
[ Subsonic High-Pass Filter (Baritone: 48 Hz | Bass VI: 35 Hz, 24 dB/oct) ]
   │
   ├──► Low Band (< 160 Hz) ──► [ Clean Optical Compressor (3.5:1) ] ───────────────────────┐
   │                            (Locks sub-fundamentals cleanly in MONO)                    │
   │                                                                                        │
   └──► High Band (> 160 Hz) ─► [ Optional Strangle Filter ] ──► [ Amp Drive / Overdrive ] ─┤
                                │                                                           │
                                └──► [ Stereo BBD Chorus / Tape Delay / Spring Reverb ] ────┤
                                                                                            ▼
[ Hybrid Cabinet IR: 1x15 Bass Bottom + 2x12 Guitar Top ] ◄──────────────────────── [ Summing Bus ]
```

---

## 3. Parameter Specifications

| Module | Parameter | Baritone Setting | Bass VI Setting | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **Input Filter**| High-Pass Filter | `48 Hz` (24 dB/oct) | `35 Hz` (24 dB/oct) | Eliminates sub-audible rumble while anchoring $B_1$ / $E_1$. |
| **Crossover** | Split Frequency | `160 Hz` | `180 Hz` | Isolates clean sub-bass fundamentals from upper harmonic grit. |
| **Low Comp** | Ratio / Attack | `3.5:1` / `20 ms` | `4.0:1` / `15 ms` | Stabilizes thick wound bottom strings for studio consistency. |
| **Strangle Sw**| High-Pass Dip | `OFF` (or `120 Hz`) | `ON` (`130 Hz` Soft) | Cleans thick low-mids during Robert Smith Dream Pop chords. |
| **Twang Peak** | Freq / Q / Gain | `2.4 kHz` / `Q=1.6` / `+2.5 dB`| `2.8 kHz` / `Q=1.8` / `+3.0 dB`| Brings out signature metallic pick attack and Danelectro twang. |
| **Mud Cut** | Freq / Q / Gain | `320 Hz` / `Q=2.2` / `-3.5 dB`| `280 Hz` / `Q=2.5` / `-4.0 dB`| Removes boxy hollow low-mid congestion. |
| **Hybrid IR** | Speaker Profile | `Hybrid_1x15_2x12.wav` | `Ampeg_2x10_Twin_2x12.wav`| Combines solid sub-bass projection with guitar speaker chime. |
| **Mod / Space**| Stereo Effects | `> 160 Hz` Only | `> 180 Hz` Only | Prevents stereo chorus and reverb from muddying the sub-bass core. |

---

## 4. Factory Scene Presets

### Scene A: Spaghetti Western Twang Baritone (Ennio Morricone / Twin Peaks)
- **Concept:** Deep, cinematic, shimmering clean baritone tone steeped in vintage tape slapback and dripping spring reverb.
- **Amp & IR:** Clean Blackface Twin / Showman model (`GAIN = 30%`), `Hybrid_1x15_2x12.wav` IR, subtle twang boost at `2.4 kHz`.
- **Modulation & Space:** Vintage Bias Optical Tremolo (`3.2 Hz`) + Echoplex Slapback (`140 ms`) + 6G15 Spring Reverb (`2.8 s`, `32%` mix).

### Scene B: Shoegaze & Dream Pop Bass VI (The Cure / Robert Smith)
- **Concept:** Melancholic, lush 1980s post-punk and shoegaze Bass VI sound combining chimey single-coil clarity with sweeping stereo chorus.
- **Filtering:** **Strangle Switch ON** (gentle low-mid shelf reducing 130 Hz mud), `CROSSOVER = 180 Hz`.
- **Modulation:** Analog BBD Chorus / Dimension D (`Mode 3`, applied strictly above `180 Hz`).
- **Space:** Modulated Stereo Tape Delay (`440 ms`, `30%` feedback) + Studio Plate Reverb.

### Scene C: Modern Drop-A Djent Clarity (Split-Band Tight Metal)
- **Concept:** Razor-sharp modern progressive metal and heavy rock rhythm where low-tuned chugs hit with crushing precision and zero mud.
- **Crossover & Drive:** Low Band ($<180\text{ Hz}$) strictly compressed clean; High Band ($>180\text{ Hz}$) driven through Friedman/Soldano high-gain overdrive (`GAIN = 74%`).
- **Gate & IR:** Fast downward noise gate (`-32 dBFS`), Celestion Vintage 30 4x12 IR blended with 1x15 punch.

### Scene D: Vintage Tic-Tac Country Bass & Surf (Danelectro Longhorn)
- **Concept:** Authentic 1960s Nashville studio "tic-tac" doubling tone—crisp, palm-muted thump cutting cleanly beside upright bass.
- **Dynamics:** Fast optical compression (`4:1`, `8 ms` attack), subtle tube warmth (`18%` drive), tight studio room reverb (`0.8 s`, `12%` mix).

---

## 5. Hardware Setup & Mapping

### Tank-B Control Assignments
- **Built for Tank-B:** Tank-B is uniquely equipped for Baritone and Bass VI players! Its dedicated low-end dynamic compressor and bass/guitar hybrid IR capabilities handle $41.2\text{ Hz}$ ($E_1$) down to Drop-G# cleanly without input clipping.
- **Footswitch 1:** Scene A (Spaghetti Western) / Scene B (Dream Pop Chorus).
- **Footswitch 2:** Scene C (Split-Band Metal Drive) / Tuner.

### Tank-G (v1 / v2) Control Assignments
- Engage the built-in High-Pass Filter at `45 Hz` and keep amp channel Bass controls conservative (`30% - 40%`), relying on cabinet IR depth rather than preamp bass boost to avoid mush.

### Black Box Desktop Configuration
- **Dual Hybrid IR:** Load a `1x15` or `2x10` bass IR in Left Slot and a `2x12 Alnico/V30` guitar IR in Right Slot for massive studio separation.
- **MIDI CC #90:** Toggles the **Fender Strangle Switch** contour instantaneously between fat bass doubling and bright chordal soloing.
