# B3 Organ Synthesizer & Independent Dual-Rotor (Leslie 122) Modeling Guide

This guide details polyphonic tonewheel drawbar synthesis, **Key Click & Harmonic Percussion**, **6550 vacuum-tube saturation**, and independent **Horn & Drum physical inertia** modeling for emulating a **Hammond B3 + Leslie 122** within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Acoustic & Electronic Architecture of the B3 + Leslie 122

Transforming a plucked electric guitar or bass into a convincing **Hammond B3 Tonewheel Organ** requires reshaping the instrument's attack envelope, reconstructing additive organ drawbar harmonics polyphonically, saturating a **6550 tube amplifier**, and passing the audio through an asymmetrically rotating dual-rotor cabinet.

```
Guitar / Bass In ──► [ Transient Softener (Removes Pick Attack) ]
                           │
                           ▼
      [ Polyphonic Tonewheel Additive Matrix ] (16' | 5 1/3' | 8' | 4' | 2 2/3')
                           │
                           ├──► [ 2nd / 3rd Harmonic Percussion & Key Click ]
                           ▼
      [ 6550 Tube Amplifier Saturation (Warm Overdrive) ]
                           │
                           ▼
      [ Leslie 122 Passive Crossover (800 Hz) ]
         ├── High (> 800 Hz) ──► [ Rotating Treble Horn ] (Fast Acceleration: ~0.9 s) ──┐
         └── Low (< 800 Hz)  ──► [ Rotating Wooden Drum ] (Heavy Inertia Lag: ~3.2 s) ──┴──► Stereo Mic Out
```

### 1.1 Polyphonic Drawbars & Harmonic Percussion

Unlike monophonic guitar synth pedals that fail on chords, UltraRig processes chords cleanly using polyphonic phase-locked harmonic stacking:
- **Drawbar 16' ($-12\text{ st}$):** Deep sub-octave foundation adding massive weight to chords.
- **Drawbar 5 1/3' ($+7\text{ st}$ below 8'):** Quint harmonic reinforcing rich jazz and gospel voicings.
- **Drawbar 8' ($0\text{ st}$):** Unison organ fundamental.
- **Drawbar 4' ($+12\text{ st}$) & 2 2/3' ($+19\text{ st}$):** Upper harmonics yielding sparkling church/rock brilliance.
- **Harmonic Percussion & Key Click:** Because organ keys trigger 9 parallel tonewheel busbars simultaneously with mechanical contact bounce, UltraRig injects a brief broadband key-click burst and fast-decaying 2nd/3rd harmonic ping *on top* of smoothed sustain envelopes.

### 1.2 Independent Horn & Drum Physical Inertia

Real Leslie 122 wooden cabinets house two separate motors and physical rotors separated at **$800\text{ Hz}$**:
1. **Treble Compression Horn (Top):** Lightweight phenolic/plastic horn that accelerates briskly ($0.8\text{ s} - 1.2\text{ s}$) when switched from **Chorale** (~$0.8\text{ Hz}$) to **Tremolo** (~$6.8\text{ Hz}$).
2. **15" Wooden Bass Drum Rotor (Bottom):** Heavy wooden baffle possessing considerable rotational momentum; it lags noticeably behind the horn ($2.8\text{ s} - 4.0\text{ s}$ ramp), creating hypnotic phase-shifted tension as the two rotors spin in and out of sync.
3. **3D Doppler & Shadow Attenuation:** As the virtual horn rotates past virtual stereo microphones (angled $90^\circ$ or $180^\circ$ apart), UltraRig models directional high-frequency rear-cabinet attenuation alongside physical Doppler pitch shifts.

---

## 2. DSP Signal Chain & Processing Topology

```
Instrument Input (Neck/Middle Pickup Preferred for Organ Smoothness)
   │
   ▼
[ Input Auto-Swell Softener ] (Smooths harsh pick percussiveness into flat organ sustain)
   │
   ▼
[ Polyphonic Drawbar Harmonic Engine (16' | 8' | 4' | Percussion 2nd/3rd | Key Click) ]
   │
   ▼
[ Leslie 122 40W 6550 Tube Amp Saturation ] (Asymmetric warm growl)
   │
   ▼
[ Linkwitz-Riley 800 Hz Crossover ]
   ├──► [ Upper Horn Simulator: Doppler + LPF Shadow + Fast Inertia Motor ] ──┐
   │                                                                           ├──► Stereo Cabinet Mics
   └──► [ Lower Drum Simulator: Warm Bass Spin + Heavy Inertia Motor ] ────────┘     (L/R Spread)
```

---

## 3. Parameter Specifications

| Parameter | Range | Default | Unit | Description |
| :--- | :--- | :--- | :--- | :--- |
| `DRAWBAR_16` | `0` - `8` | `6` | level | Sub-octave ($-12\text{ st}$) organ registration weight. |
| `DRAWBAR_8` | `0` - `8` | `8` | level | Unison fundamental organ registration. |
| `DRAWBAR_4` | `0` - `8` | `5` | level | Upper-octave ($+12\text{ st}$) brightness harmonic. |
| `KEY_CLICK` | `0` - `100` | `35` | % | Mechanical 9-busbar contact click burst on note onset. |
| `PERC_MODE` | `OFF` / `2ND` / `3RD`| `3RD` | mode | Decaying organ harmonic percussion ping. |
| `TUBE_DRIVE` | `0` - `100` | `45` | % | 6550 vacuum tube amplifier overdrive and harmonic grit. |
| `ROTOR_STATE` | `CHORALE` / `TREMOLO` / `BRAKE`| `CHORALE`| mode | Slow lush swirl, fast spinning tremolo, or stopped stationary wood cabinet. |
| `HORN_INERTIA` | `0.4` - `2.5` | `1.0` | s | Acceleration/deceleration ramp time of the treble horn. |
| `DRUM_INERTIA` | `1.5` - `5.0` | `3.2` | s | Heavy momentum ramp time of the 15" bass drum baffle. |
| `MIC_SPREAD` | `0` - `100` | `85` | % | Stereo microphone angular placement around cabinet louvers. |
| `MIX_WET_DRY` | `0` - `100` | `100` | % | Set to 100% for pure organ simulation; lower to blend dry guitar. |

---

## 4. Factory Scene Presets

### Scene A: Jon Lord Rock Organ Overdrive (Deep Purple / Uriah Heep)
- **Concept:** Massive, roaring distorted Hammond B3 through a cranked tube stack—ideal for heavy rock chord riffs and unison guitar/organ jams.
- **Drawbars:** `16' = 8`, `8' = 8`, `4' = 7`, `KEY_CLICK = 45%`, `PERC_MODE = 3RD`.
- **Tube & Rotor:** `TUBE_DRIVE = 78%`, `ROTOR_STATE = TREMOLO` (toggleable to Chorale via footswitch).
- **Space:** Tight Studio Wood Room (`1.1 s`, `15%` mix).

### Scene B: Booker T. Soul Gospel B3 (Green Onions / Stax Warmth)
- **Concept:** Sweet, punchy, groovy soul organ tone with distinct 3rd harmonic percussion pings and rich Chorale warmth.
- **Drawbars:** `16' = 8`, `8' = 6`, `4' = 4`, `KEY_CLICK = 50%`, `PERC_MODE = 3RD`.
- **Tube & Rotor:** `TUBE_DRIVE = 35%`, `ROTOR_STATE = CHORALE`.
- **Space:** Vintage Spring Tank (`1.8 s`, `20%` mix).

### Scene C: Pink Floyd Echoes Swirl (Atmospheric Space Organ)
- **Concept:** Hypnotic, dreamy ambient B3 swells floating in endless stereo space (inspired by Rick Wright).
- **Drawbars:** `16' = 6`, `8' = 8`, `4' = 6`, `KEY_CLICK = 10%`, `PERC_MODE = OFF`.
- **Tube & Rotor:** `TUBE_DRIVE = 18%`, `ROTOR_STATE = CHORALE`.
- **Space:** Modulated Stereo Tape Delay (`440 ms`, `35%` feedback) into Vast Hall Reverb (`4.5 s`).

### Scene D: Jazz Lounge Trio Percussive Organ (Jimmy Smith)
- **Concept:** Authentic swinging jazz-organ registration with fast 2nd harmonic click and stationary/slow cabinet warmth.
- **Drawbars:** `16' = 8`, `8' = 8`, `4' = 0` (Classic `888000000` Jazz setting), `PERC_MODE = 2ND`.
- **Tube & Rotor:** `TUBE_DRIVE = 25%`, `ROTOR_STATE = BRAKE` (or slow Chorale).
- **Space:** Intimate Club Room Reverb (`1.2 s`, `16%` mix).

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (Jon Lord Overdrive) / Scene B (Soul Gospel B3).
- **Footswitch B:** **Rotary Speed Switch (Chorale <-> Tremolo)** with physical inertia ramp!
- **Footswitch C:** Scene C (Echoes Swirl) / Scene D (Jazz Trio).
- **Knob 1 (GAIN):** 6550 Tube Amplifier Overdrive growl.
- **Knob 2 (MOD FX):** Drawbar 4' Upper Harmonic balance.
- **Knob 3 (REVERB):** Studio Hall Ambience mix.

### Tank-B Control Assignments
- Bassists can craft colossal prog-rock keyboard bass pads (Geddy Lee / Chris Squire style) by selecting Scene A with `MIX_WET_DRY = 65%` so the clean bass string anchors sub-frequencies beneath spinning 6550 organ harmonics.

### Black Box Desktop Configuration
- **Expression Pedal 1:** Emulates the classic **B3 Swell Volume Pedal** (controls input volume feeding the 6550 distortion stage—so pushing down increases both volume and tube saturation!).
- **Stereo Outputs:** Required to capture the immersive 3D Doppler sweeps of the upper compression horn.
