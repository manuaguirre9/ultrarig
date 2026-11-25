# Pedal Steel & Lap Steel Electroacoustic Routing Guide

This guide details the electrical pickup characteristics, volume-pedal headroom architecture, steel tone-bar frequency management, and preset configuration for **Pedal Steel** (E9 / C6) and **Lap Steel** guitars within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Sonic Profile & Hardware Mechanics of Steel Guitars

Unlike standard guitars where strings terminate over wood fretboards, **Pedal Steel** and **Lap Steel** instruments use a solid cylindrical stainless-steel or chrome **tone bar** sliding smoothly over tensioned strings. Coupled with high-output single-coil or wide-aperture humbucking pickups (such as Emmons, George L's E-66, or Lawrence 705), they produce massive sustain, glassy harmonics, and extreme dynamic range.

```
Pedal Steel E9 (10-String Nashville Standard):
 1: F#4 | 2: D#4 | 3: G#4 | 4: E4 | 5: B3 | 6: G#3 | 7: F#3 | 8: E3 | 9: D3 | 10: B2

Lap Steel C6 (6-String Western Swing / Hawaiian):
 1: E4 | 2: C4 | 3: A3 | 4: G3 | 5: E3 | 6: C3
```

### 1.1 Critical Tonal & Routing Challenges

1. **Tone Bar "Ice-Pick" Resonance (2.8 kHz – 4.5 kHz):** Pressing a solid steel bar onto plain high strings creates ringing metallic upper-mid harmonics. Through full-range PA speakers or poorly matched guitar cabinets, this produces ear-fatiguing shrillness.
2. **Volume Pedal Impedance Loading:** Steel players constantly shape every note's attack and sustain using a foot volume pedal. Passive potentiometer volume pedals (250k or 500k) placed in front of long cable runs suffer severe treble roll-off ("tone suck") unless buffered cleanly at $1\text{ M}\Omega$+.
3. **Ultra-High Clean Headroom Requirement:** Because pedal steel chords frequently involve 4 to 6 simultaneous notes swelling rapidly via the volume pedal, low-headroom preamps compress unpleasantly or fart out in the low register ($B_2 = 123.5\text{ Hz}$ and $C_3 = 130.8\text{ Hz}$). Classic steel rigs therefore rely on high-headroom power stages feeding **15-inch speakers** (JBL D130F or Peavey Black Widow 15").
4. **Post-Volume Pedal Effects Placement:** Delay and reverb must *always* be placed **after** the volume swell stage so that pulling back the pedal mutes the dry instrument cleanly while letting lush reverb and delay tails ring smoothly into space.

---

## 2. DSP Signal Chain & Processing Topology

```
Pedal Steel / Lap Steel In (High-Output Pickup)
   │
   ▼
[ High-Z 1MΩ Input Buffer & Subsonic HPF (55 Hz) ]
   │
   ▼
[ Transparent Optical Sustainer Compressor ] (Extends bar sustain without squashing swells)
   │
   ▼
[ Ultra-Clean Tube / Solid-State Steel Preamp ] (Peavey Nashville 112 / Fender Twin Style)
   │
   ├──► [ Surgical Mid-Ice-Pick Dip @ 3.4 kHz (-3.5 dB) ]
   └──► [ Optional Tube Grit Overdrive (For Sacred Steel / Rock Leads) ]
   │
   ▼
[ Post-Preamp Volume Swell Pedal Stage ] ◄─── (Expression Pedal 1 / Hardware Volume Loop)
   │
   ▼
[ 15-Inch Steel Speaker Cabinet IR Convolution ] (JBL D130F / Peavey Black Widow 15")
   │
   ▼
[ Deep Accutronics Spring Reverb + Stereo Modulated Delay ] ──► Stereo Output
```

---

## 3. Parameter Specifications

| Module | Parameter | Recommended Value | Purpose |
| :--- | :--- | :--- | :--- |
| **Input Buffer** | Impedance / HPF | `1 MΩ` / `55 Hz` | Prevents treble loss from passive volume pedals; clears floor rumble. |
| **Compressor** | Ratio / Attack / Rel | `2.4:1` / `35 ms` / `220 ms` | Smooths note decay during delicate chords without choking swells. |
| **Preamp Model** | Voicing | `Clean Twin / Nashville 112` | High-headroom clean clarity with tight low-end control. |
| **Preamp EQ** | Bass / Mid / Treble | `52%` / `44%` / `60%` | Gentle mid-scoop for classic hi-fi Nashville clarity. |
| **Ice-Pick Dip** | Freq / Q / Gain | `3.4 kHz` / `Q=3.2` / `-3.5 dB` | Tames harsh steel bar harmonics on upper strings. |
| **Presence** | High Air Shelf | `9.5 kHz` / `+2.0 dB` | Adds silky crystalline sheen without metallic bite. |
| **Cabinet IR** | Speaker Profile | `1x15_JBL_D130F.wav` | Delivers huge 15-inch bottom-end depth and open acoustic punch. |
| **Volume Swell** | Placement | `Post-Preamp / Pre-FX` | Lets delay and reverb tails decay cleanly when pedal is pulled back. |
| **Reverb** | Type / Decay / Mix | `3-Spring Tank` / `2.4 s` / `28%`| Signature Nashville steel ambiance and lush harmonic tail. |

---

## 4. Factory Scene Presets

### Scene A: Classic Nashville E9 Swell (Buddy Emmons / Paul Franklin)
- **Concept:** Iconic studio country pedal steel tone—glassy, liquid clean with deep 15-inch warmth and spacious spring ambiance.
- **Preamp & IR:** Clean Twin / Nashville 112 model (`GAIN = 25%`), `1x15_BlackWidow.wav` IR, ice-pick dip at `3.4 kHz`.
- **Dynamics:** Transparent optical leveling (`2.2:1`, slow attack).
- **Space:** Deep 3-Spring Tank Reverb (`2.6 s`, `30%` mix) + subtle studio slapback delay (`115 ms`).

### Scene B: Western Swing C6 Clean (Warm Jazz & Big Band)
- **Concept:** Thick, round, mid-forward acoustic jazz tone suited for walking C6 chord melodies and swing solos.
- **Preamp & EQ:** Midrange push (`MIDDLE = 64%`, `TREBLE = 42%`), warm high-cut shelf above `6.5 kHz`.
- **Cabinet IR:** `1x15_JBL_D130F.wav` (classic warm aluminum-dome cone character).
- **Space:** Warm Wooden Studio Chamber (`1.6 s`, `20%` mix).

### Scene C: Hawaiian Lap Steel Vintage (Sol Hoʻopiʻi / Acoustic Warmth)
- **Concept:** Nostalgic 1940s–1950s island lap steel sound with tube preamp sag and hypnotic optical vibrato/tremolo.
- **Preamp:** Vintage Tweed Pro 15" emulation (`GAIN = 45%` for subtle edge-of-breakup warmth).
- **Modulation:** Slow Bias Optical Tremolo (`3.2 Hz`, `35%` depth).
- **Space:** Vintage Tube Spring Reverb (`2.0 s`, `26%` mix).

### Scene D: Ambient Sacred Steel & Cinematic Swell (Daniel Lanois / Robert Randolph)
- **Concept:** Expressive singing overdrive and vast ambient clouds turning single steel lines into orchestral textures.
- **Saturation:** Warm Tube Screamer / Dumble style mid-drive (`DRIVE = 48%`) pushed into singing sustain.
- **Space:** Stereo Modulated Tape Delay (`dotted 8th`, `440 ms`, `35%` feedback) feeding Shimmer Hall Reverb (`5.5 s` decay).

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (Nashville E9 Swell) / Scene B (Western Swing C6).
- **Footswitch B:** Scene C (Hawaiian Vintage Tremolo).
- **Footswitch C:** Scene D (Ambient Sacred Steel Overdrive) / Tuner.
- **Knob 1 (COMP):** Optical Sustainer compression depth.
- **Knob 2 (EQ / TONE):** Ice-Pick high-mid smoothing (`2.5 kHz` – `5.0 kHz`).
- **Knob 3 (REVERB):** Spring Reverb tank dwell and ambient mix.

### Tank-B Control Assignments
- Because pedal steel extends comfortably into the baritone register ($B_2$ / $C_2$ on C6 10-string necks), Tank-B's 15-inch cabinet IRs and high-headroom clean path yield extraordinary low-end weight and clarity.

### Black Box Desktop Configuration
- **Expression Pedal 1 (Post-Preamp Volume):** Map internal digital volume block directly *after* the Amp/IR stage and *before* Delay/Reverb for effortless single-cable swells without an external heavy analog volume pedal.
- **High-Z Input (1 MΩ):** Ensures passive pickups preserve crystal-clear top harmonics across long stage cables.
