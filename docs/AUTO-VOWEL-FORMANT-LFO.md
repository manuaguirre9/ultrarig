# Dynamic Formant Filter & Auto-Vowel LFO Modeling Guide

This guide details human vocal tract formant physics ($F_1, F_2, F_3$), continuous multi-band bandpass interpolation across vowel shapes (`/a/`, `/e/`, `/i/`, `/o/`, `/u/`), and practical preset configuration for **Dynamic Auto-Vowel LFO Filtering** within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Acoustic Principles of Vocal Formants & Continuous Vowel Morphing

Human speech distinguishes vowels not by fundamental pitch, but by shaping the throat and oral cavity to create three distinct resonant peaks—known as **formants** ($F_1, F_2, F_3$). UltraRig models the vocal tract using a parallel bank of three state-variable Band-Pass Filters (BPFs) whose center frequencies and Q-factors interpolate smoothly in real time.

```
Instrument In ──► [ Pre-Formant Harmonic Overdrive ] (Enriches spectrum across 250 Hz - 3.5 kHz)
                        │
                        ├──► [ Band-Pass Filter F1 (Low Vowel Throat: 270 - 730 Hz) ] ──┐
                        ├──► [ Band-Pass Filter F2 (Tongue Shape: 840 - 2290 Hz) ] ───────┼──► Stereo Vowel Sum
                        └──► [ Band-Pass Filter F3 (Lip / Nasal Resonance: 2.2 - 3.0 kHz)]┘
                                      ▲
                                      │
      [ LFO (Sine / Triangle / S&H) OR Tempo-Synced Step Sequencer ]
      (Continuously morphs F1, F2, F3 targets: e.g. /u/ -> /o/ -> /a/ -> /e/ -> /i/)
```

### 1.1 Standard Vocal Formant Matrix

| Vowel Target | Phonetic Feel | $F_1$ (Hz) | $F_2$ (Hz) | $F_3$ (Hz) | Sonic Character |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`/a/`** | "Ah" (*Father*) | `730` | `1090` | `2440` | Wide open, assertive, expressive talkbox punch. |
| **`/e/`** | "Eh" (*Bet*) | `530` | `1840` | `2480` | Bright, singing nasal upper-mid cut. |
| **`/i/`** | "Ee" (*Beet*) | `270` | `2290` | `3010` | Glassy, vocal whistle contrast between deep bass and sharp highs. |
| **`/o/`** | "Oh" (*Boat*) | `570` | `840` | `2410` | Warm, hollow, rounded lower-midrange vocal tone. |
| **`/u/`** | "Oo" (*Boot*) | `300` | `870` | `2240` | Dark, sub-heavy resonant synth-like bass drop. |

### 1.2 Pre-Formant Saturation & Stereo Formant Shift

1. **Why Pre-Formant Drive Matters:** Pure clean guitars lack dense overtones in the $1.5\text{ kHz} - 3.0\text{ kHz}$ region required to excite Formants $F_2$ and $F_3$. Placing mild tube or diode saturation *ahead* of the formant bank fills the frequency spectrum, making the guitar "speak" clearly across all five vowels.
2. **Stereo Formant Offset:** Shifting the Left and Right formant banks slightly apart (e.g., $+8\%$ frequency offset on Right channel) or alternating LFO phase by $90^\circ$ creates an immersive, bouncing 3D talking synth soundstage.

---

## 2. DSP Signal Chain & Processing Topology

```
Guitar / Bass In ────────────────────► [ Parallel Dry Clean Level ] ───────────────────────────┐
      │                                                                                        │
      ▼                                                                                        │
[ Pre-Formant Tube / Germanium Drive ] (Injects rich upper harmonics for F2 & F3 excitation)   │
      │                                                                                        │
      ├──► [ Formant F1 Parallel BPF ] ◄──┐                                                    │
      ├──► [ Formant F2 Parallel BPF ] ◄──┼── [ Vowel Interpolator Matrix ]                    │
      └──► [ Formant F3 Parallel BPF ] ◄──┘       ▲                                            │
            │                                     │                                            │
            ▼                             [ LFO / Step Sequencer / Envelope Blend ]            │
[ Stereo Formant Offset & Resonance Limiter ]                                                  │
      │                                                                                        │
      ▼                                                                                        │
[ Post-Formant Tape Delay & Studio Hall Reverb ] ──► [ Wet Level ] ────────────────────────────┴──► Output
```

---

## 3. Parameter Specifications

| Parameter | Range | Default | Unit | Description |
| :--- | :--- | :--- | :--- | :--- |
| `VOWEL_START` | `A` / `E` / `I` / `O` / `U` | `U` | vowel | Starting vocal shape at the trough of the LFO/modulation sweep. |
| `VOWEL_MID` | `A` / `E` / `I` / `O` / `U` | `O` | vowel | Intermediate vocal target crossed mid-sweep. |
| `VOWEL_END` | `A` / `E` / `I` / `O` / `U` | `A` | vowel | Peak vocal shape at the crest of the LFO/modulation sweep. |
| `MOD_SOURCE` | `LFO_SINE` / `STEP_SEQ` / `S_AND_H` | `LFO_SINE`| mode | Smooth sinusoidal wave, tempo-locked steps, or random Sample & Hold. |
| `RATE_SYNC` | `0.1 - 12 Hz` / `SYNC`| `1/8 Note`| Hz/div| Sweep speed (free Hz or locked to Tap Tempo / MIDI Clock). |
| `RESONANCE_Q` | `2.0` - `18.0` | `8.5` | - | Narrow selectivity of $F_1, F_2, F_3$ peaks (higher = stronger vocal character). |
| `PRE_DRIVE` | `0` - `100` | `45` | % | Amount of pre-formant harmonic distortion exciting upper formants. |
| `FORMANT_SHIFT` | `-35` to `+35` | `0` | % | Shifts overall vocal tract pitch scale (male baritone vs. bright soprano). |
| `STEREO_OFFSET` | `0` - `100` | `45` | % | Phase and formant separation between Left and Right channels. |
| `MIX_WET_DRY` | `0` - `100` | `85` | % | Parallel dry/wet mix (set to 100% for pure talking synth). |

---

## 4. Factory Scene Presets

### Scene A: Talking Groove Vowel Sweep (`A -> E -> O`)
- **Concept:** Expressive, melodic vocal singing effect smoothly cycling through `Ah-Eh-Oh` shapes behind guitar riffs and leads.
- **Vowels & Mod:** `VOWEL_START = O`, `VOWEL_MID = A`, `VOWEL_END = E`, `MOD_SOURCE = LFO_SINE`, `RATE_SYNC = 1/4 Note`.
- **Resonance & Drive:** `RESONANCE_Q = 9.0`, `PRE_DRIVE = 55%` (creamy tube saturation).
- **Mix:** `MIX_WET_DRY = 90%`.

### Scene B: Tempo-Synced Robot Vowel Sequencer (16th-Note Talk)
- **Concept:** Futuristic electronic step-sequenced chatter jumping rhythmically between `/i/`, `/o/`, `/a/`, and `/u/` locked tightly to BPM.
- **Vowels & Mod:** `MOD_SOURCE = STEP_SEQ`, `RATE_SYNC = 1/16 Note`, `RESONANCE_Q = 11.5`, `STEREO_OFFSET = 75%`.
- **Space:** Tight Stereo Ping-Pong Delay (`dotted 8th`, `28%` feedback) + Clean Hall.
- **Mix:** `MIX_WET_DRY = 100%`.

### Scene C: Psychedelic Phase-Vowel Swell (Slow `O -> U -> I`)
- **Concept:** Dreamy, slow-moving space-rock texture reminiscent of swirling vintage phasers combined with organic vocal breath.
- **Vowels & Mod:** `VOWEL_START = U`, `VOWEL_MID = O`, `VOWEL_END = I`, `MOD_SOURCE = LFO_SINE`, `RATE_SYNC = 0.25 Hz`.
- **Resonance & Drive:** `RESONANCE_Q = 6.5`, `PRE_DRIVE = 25%`, `STEREO_OFFSET = 85%`.
- **Space:** Modulated Analog Delay (`460 ms`, `35%` feedback) + Studio Plate Reverb (`3.2 s`).

### Scene D: Synth Bass Talking Wah (`U -> A` Funk Drop)
- **Concept:** Deep sub-heavy bass growl morphing smoothly from dark `/u/` bass into punchy open `/a/` bite on groove accents.
- **Vowels & Mod:** `VOWEL_START = U`, `VOWEL_END = A`, `RESONANCE_Q = 8.0`, `FORMANT_SHIFT = -15%` (deep vocal tract), `PRE_DRIVE = 60%`.
- **Mix:** `MIX_WET_DRY = 70%` (Retains 30% clean low-end bass fundamental).

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (Talking Groove Sweep) / Scene B (Robot Vowel Sequencer).
- **Footswitch B:** Scene C (Psychedelic Phase-Vowel Swell).
- **Footswitch C:** Tap Tempo / Scene D (Synth Bass Talking Wah).
- **Knob 1 (MOD FX):** LFO Rate / Tempo Subdivision.
- **Knob 2 (GAIN):** Pre-Formant Saturation Drive.
- **Knob 3 (TONE / RES):** Formant Shift (vocal tract size) and Resonance Q.

### Tank-B Control Assignments
- Bassists looking for Daft Punk / Justice / Chromeo style talking electro-bass grooves can deploy Scene D with a parallel low-pass clean blend below $140\text{ Hz}$ so the bottom end stays thunderous while the upper mids articulate clear `/u/` to `/a/` syllables.

### Black Box Desktop Configuration
- **Expression Pedal 1:** Bypass LFO temporarily to manually sweep directly between `VOWEL_START` and `VOWEL_END`—functioning as a super-expressive foot-controlled Talkbox without needing a plastic mouth tube!
- **MIDI Clock Sync:** Locks `STEP_SEQ` vowel transitions tightly to external DAW or drummer click tracks.
