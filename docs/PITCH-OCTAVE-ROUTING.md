# UltraRig Pitch Shifter, Octaver & Virtual Whammy Routing Guide

Pitch shifting effects — ranging from sub-octave dividers (Boss OC-2 style) to continuous pedal pitch benders (DigiTech Whammy style), polyphonic harmonizers, and micro-pitch stereo detuners — allow guitarists and bassists to radically transform their instrument's range without changing guitars or alternate tunings.

However, pitch shifting algorithms analyze incoming fundamental audio frequencies in real-time. Improper placement within the DSP chain causes severe tracking latency, warbling artifacts ("bubbling"), and harmonic dissonance.

This guide details optimal graph placement (pre-amp vs. post-amp), expression pedal calibration for virtual Whammy divebombs, stereo micro-pitch widening, and tracking optimization.

---

## 1. Effect Types & DSP Mechanics

| Effect Type | Algorithm Target | Typical Range | Primary Musical Use |
| :--- | :--- | :--- | :--- |
| **Virtual Whammy** | Continuous monophonic/polyphonic pitch glide | -24 to +24 semitones (-2 to +2 octaves) | Tom Morello pitch squeals, Dimebag Darrell squeals, Jeff Beck divebombs |
| **Sub-Octaver** | Sub-harmonic frequency division | -1 Octave (-12 semitones), -2 Octaves | Royal Blood bass lines, synth-guitar leads, funk octave riffs |
| **Harmonizer** | Fixed or scale-based parallel interval | +3rd, +5th, -4th, +7th, +Octave | Thin Lizzy, Iron Maiden, Queen dual-lead harmonies |
| **Virtual Drop-Tune** | Polyphonic downward transposition | -1 to -5 semitones | Drop D, Eb Standard, D Standard without swapping guitars |
| **Micro-Pitch Detune** | Subtle cents detuning (no LFO cycle) | -15 to +15 cents | EVH 5150 / 80s studio widening without cyclic flanging |

---

## 2. The Golden Rule: Pre-Amp vs. Post-Amp Placement

```
 [ GUITAR ]
     │
     ▼
 ┌───────────────┐
 │ PITCH BLOCK   │ ──> PRE-AMP PLACEMENT (Recommended for Whammy, Octave & Drop-Tune)
 │ (Clean Fund.) │     - Analyzes pure, uncompressed string fundamentals
 └───────┬───────┘     - Zero intermodulation distortion
         │             - Natural tracking and organic pick attack response
         ▼
 ┌───────────────┐
 │ OVERDRIVE /   │ ──> Drives and saturates the already-shifted notes
 │ NAM CAPTURE   │     - Behaves just like playing an actual low-tuned or high-register guitar
 └───────┬───────┘
         │
         ▼
 ┌───────────────┐
 │ PITCH BLOCK   │ ──> POST-AMP PLACEMENT (Recommended ONLY for Studio Harmonizers)
 │ (Harmonizer)  │     - Generates parallel harmonies (+3rd / +5th) from the distorted signal
 └───────┬───────┘     - Avoids the muddy intermodulation of driving multiple intervals together
         │
         ▼
 [ CABINET IR / REVERB ]
```

### Why Pre-Amp Placement is Essential for Whammy & Octaves:
* Overdrive pedals and NAM neural amp models create non-linear saturation, compressing dynamics and generating complex harmonic overtones (intermodulation products).
* If you place a pitch shifter **after** high-gain distortion, the pitch tracking engine receives a noisy, saturated wave containing multiple conflicting harmonics, resulting in glitching, note dropout, and digital warble.
* Placing the Pitch block **at the beginning of the chain** (immediately after the Noise Gate) gives the DSP a pristine, sinusoidal pickup signal, ensuring lightning-fast, glitch-free tracking.

### When to Use Post-Amp Placement (Studio Harmonizers):
* If you want to create twin-lead harmonies (e.g., dual guitar solo in 3rds), running two notes into a high-gain amp causes the two pitches to distort against each other, creating unpleasant harmonic clash.
* Placing the pitch shifter in a parallel branch **after the NAM amp and Cabinet IR** allows the distorted tone of your single lead to be cleanly duplicated and transposed without extra intermodulation fuzz.

---

## 3. Signal Chain Topologies

### Topology A: Virtual Whammy & Drop-Tuning (Front-of-Chain)
```
[ In ] ──> [ Gate ] ──> [ PITCH (Whammy / Drop) ] ──> [ Overdrive ] ──> [ NAM Amp ] ──> [ IR ] ──> [ Delay/Reverb ] ──> [ Out ]
```
* **Best for:** Drop tuning, 1-octave / 2-octave pitch pedal bends, sub-octave synth riffs.
* **Result:** Pristine tracking; amp distortion responds authentically to the transposed register.

### Topology B: Parallel Studio Harmonizer (Dual Lead in 3rds/5ths)
```
                                 ┌──> [ Direct Distorted Lead ] ─────────────┐
[ In ] ──> [ Drive ] ──> [ NAM ] ─┤                                           ├──> [ Merge ] ──> [ Delay/Rev ]
                                 └──> [ PITCH: +4 Semitones (Maj 3rd) ] ─────┘
```
* **Best for:** Thin Lizzy, Boston, and Iron Maiden style orchestrated harmony solos.
* **Result:** Two distinct, studio-clean distorted guitar lines playing in harmony without mud.

### Topology C: Stereo Micro-Pitch Detune (EVH 80s Widening)
```
                               ┌──> [ Branch A: Detune +8 Cents ] ──> [ Pan Left ]  ──┐
[ NAM Amp ] ──> [ Cabinet IR ] ─┤                                                     ├──> [ Stereo Output ]
                               └──> [ Branch B: Detune -8 Cents ] ──> [ Pan Right ] ──┘
```
* **Best for:** Massive stereo spread on high-gain rhythm guitars and clean arpeggios.
* **Why it beats chorus:** Unlike traditional chorus or flanger, micro-pitch detuning uses no low-frequency oscillator (LFO), meaning **zero cyclical whoosh or phase cancellation**.

---

## 4. Expression Pedal Setup for Virtual Whammy

To use an expression pedal (plugged into the Tank-G TRS jack or connected via Bluetooth MIDI controller like the M-VAVE Chocolate):

```
 Expression Pedal Position (TRS)          Pitch Transposition Output
 ───────────────────────────────────────────────────────────────────
 Heel Down (0% Value)               ───>  Unity / 0 Semitones (Original Pitch)
 Mid Travel (50% Value)             ───>  +7 Semitones (Perfect 5th)
 Toe Down (100% Value)              ───>  +12 Semitones (+1 Full Octave)
```

### Configuration Steps in UltraRig Editor:
1. Insert the **Pitch** block at Slot 1 or 2 (before the Drive and NAM blocks).
2. Open the **Expression Matrix** (or MIDI CC Mapping).
3. Assign **Source:** `EXP 1` (or `CC #11`).
4. Assign **Destination:** `Pitch: Shift Amount`.
5. Set **Min Value:** `0` (Heel down = dry unaltered guitar).
6. Set **Max Value:** `+12` (Toe down = 1 octave up) or `+24` (2 octaves up for extreme squeals).
7. Set **Curve:** `Linear` (for predictable slide guitar style pitch sweeps) or `Exponential` (for fast snap at the top).

### Divebomb Mode:
* Set **Min Value:** `-12` or `-24` (Heel down = deep divebomb slack-string pitch).
* Set **Max Value:** `0` (Toe down = regular playing pitch).

---

## 5. Tracking Optimization & Performance Tips

1. **Use the Neck Pickup:**
   - The neck pickup captures greater fundamental string excursion and significantly fewer high-frequency pick scraping harmonics than the bridge pickup, resulting in faster and more accurate pitch tracking.
2. **Roll Down the Guitar Tone Knob Slightly:**
   - Dialing your guitar's tone control back to **6 or 7** cuts high-frequency string squeak and fret noise, delivering an ideal sinusoidal signal to the pitch analysis engine.
3. **Palm Muting Discipline:**
   - In sub-octave modes (-1 Octave), heavy palm muting can cause momentary low-end pitch "glitching" if pick transients are inconsistent. Pluck cleanly and evenly.
4. **Buffer Latency Consideration:**
   - Polyphonic pitch shifting algorithms require a 10 ms to 15 ms analysis window. For hyper-fast shred passages, monophonic tracking mode offers the lowest latency and sharpest pick attack.
