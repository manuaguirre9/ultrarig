# Vintage Tube Spring Reverb Tank (Fender 6G15) & Tape Echo Guide

This guide details the electromechanical spring coil physics, dispersive "drip" chirp behavior, 6K6/6V6 tube driver saturation (**Dwell**), and preset configuration for emulating the standalone **Fender 6G15 Tube Spring Reverb** paired with **Echoplex Tape Echo** within UltraRig for M-VAVE hardware (Tank-G v1/v2, Tank-B, and Black Box).

---

## 1. Electromechanical Architecture of the Fender 6G15 Spring Tank

Introduced in 1961, the standalone Fender 6G15 tube spring reverb was designed to sit *in front of* the guitar amplifier—meaning the drenched spring reflections pass straight into the amp's preamp overdrive stage.

```
Instrument In ──┬──► [ Dry Signal Path ] ──────────────────────────────────────────────────┐
                │                                                                          │
                ▼                                                                          │
      [ 12AX7 + 6K6GT Reverb Driver Tube & Dwell Control ]                                 │
                │ (High-Voltage Transformer Saturation)                                    │
                ▼                                                                          │
      [ Accutronics 3-Spring Tank Model (4AB3C1B) ]                                        │
        ├── Dispersive All-Pass Chain (Simulates "Drip" / Chirp Physics)                   │
        └── Multi-Tap Helical Coil Comb Delays (35 - 75 ms staggered coils)                │
                │                                                                          │
                ▼                                                                          │
      [ Post-Tank Tone Filter ] ──► [ Mixer Control ] ─────────────────────────────────────┴──► To Amp Input
```

### 1.1 The Physics of Spring "Drip" and Chirp

Unlike room or plate reverbs where all frequencies reflect at the speed of sound in air or steel plates, sound waves traveling down coiled steel springs experience **frequency dispersion**:
1. Low-mid frequencies travel down the helical spring coils relatively quickly, while high-frequency pick transients arrive slightly delayed, stretched into a downward sweeping chirp.
2. When struck by a sharp pick attack on heavy guitar strings, this dispersive all-pass phenomenon creates the unmistakable liquid **"drip"** or **"boing"** essential to Surf Rock (Dick Dale, The Ventures).

### 1.2 The "Dwell" Control vs. "Mix" Control

- **Dwell:** Controls the gain feeding the 6K6GT driver tube and reverb transformer *entering* the springs. Cranking Dwell causes the driver tube to compress and saturate hard, triggering dramatic spring splash and sustain even on soft notes.
- **Tone:** A passive low-pass filter on the wet spring recovery stage, rolling off metallic ringing above $3.5\text{ kHz}$ for smooth, dark vintage warmth or opening wide for bright surf splash.
- **Pre-Amp vs. Post-Amp Routing:** Putting the 6G15 **before** a slightly breaking-up tube amp makes the spring tail distort organically with the guitar notes, gluing the reverb and amp together into one swirling instrument.

---

## 2. DSP Signal Chain & Processing Topology

```
Guitar / Baritone In
   │
   ▼
[ Optional Pre-Spring Tape Echo (Echoplex EP-3 Emulation) ] (Saturates & feeds echo repeats into springs)
   │
   ├───► [ Direct Dry Signal ] ────────────────────────────────────────────────┐
   │                                                                           │
   ▼                                                                           │
[ Dwell Tube Driver (6K6GT Asymmetric Saturation + Transformer Compression) ]  │
   │                                                                           │
   ▼                                                                           │
[ 3-Spring Dispersive Delay Matrix (All-Pass Chirp Cascade + Coil Feedback) ] │
   │                                                                           │
   ▼                                                                           │
[ Spring Tank Recovery Tone Filter (1.8 kHz - 10 kHz Low-Pass) ]               │
   │                                                                           │
   ▼                                                                           │
[ Mixer Summing ] ◄────────────────────────────────────────────────────────────┘
   │
   ▼
[ Optional Amp Stage (Twin Reverb / Bassman Edge-of-Breakup) + 2x12 IR ] ──► Output
```

---

## 3. Parameter Specifications

| Parameter | Range | Default | Unit | Description |
| :--- | :--- | :--- | :--- | :--- |
| `TANK_MODEL` | `6G15_SURF` / `BLACKFACE_INTERNAL` / `SHORT_TANK` | `6G15_SURF` | mode | Physical coil dimensions (Long 3-spring 6G15 vs. standard combo tank). |
| `DWELL_DRIVE` | `0` - `100` | `65` | % | Input drive hitting the 6K6GT driver tube and spring input transducer. |
| `DRIP_CHIRP` | `0` - `100` | `75` | % | Dispersion strength of the all-pass cascade creating classic surf "drip". |
| `TONE_DAMP` | `1.5` - `12.0` | `5.2` | kHz | Recovery tone filter smoothing bright metallic spring rattle. |
| `TANK_DECAY` | `0.8` - `6.0` | `2.8` | s | Overall decay tail length of the coupled coil tank. |
| `ROUTING_POS` | `PRE_AMP` / `POST_AMP` | `PRE_AMP` | mode | Places tank ahead of amp saturation (authentic 6G15) or in post FX loop. |
| `TAPE_PRE_ECHO`| `OFF` / `ON` | `OFF` | bool | Inserts Echoplex EP-3 pre-spring tape echo ahead of tank input. |
| `ECHO_TIME` | `60` - `600` | `145` | ms | Pre-spring echo time for slapback and western twang. |
| `MIX_WET_DRY` | `0` - `100` | `42` | % | Reverb Mixer ratio blending spring recovery into dry path. |

---

## 4. Factory Scene Presets

### Scene A: Dick Dale Surf Drip Tank (6G15 In Front of Amp)
- **Concept:** Massive, dripping, percussive surf-rock reverb with explosive coil saturation and organic amp interaction.
- **Tank Settings:** `TANK_MODEL = 6G15_SURF`, `DWELL_DRIVE = 82%`, `DRIP_CHIRP = 90%`, `TONE_DAMP = 6.8 kHz`, `TANK_DECAY = 3.2 s`.
- **Routing:** `ROUTING_POS = PRE_AMP` feeding a loud Fender Dual Showman / Twin Reverb clean-edge amp.
- **Mix:** `MIX_WET_DRY = 52%`.

### Scene B: Spaghetti Western Baritone Twang (Ennio Morricone Style)
- **Concept:** Haunting, desolate cinema tone pairing a warm Echoplex slapback with dark spring reverb and slow bias tremolo.
- **Tank & Echo:** `TAPE_PRE_ECHO = ON` (`ECHO_TIME = 165 ms`, `22%` feedback) into `6G15_SURF` (`DWELL_DRIVE = 60%`, `TONE_DAMP = 3.8 kHz`).
- **Modulation:** Vintage Tube Bias Tremolo (`2.8 Hz`, `45%` depth).
- **Mix:** `MIX_WET_DRY = 45%`.

### Scene C: Ambient Dub Spring Splash (King Tubby Style)
- **Concept:** Exploding, metallic dub-style spring percussion bursts driven by aggressive tape echo feedback.
- **Tank & Echo:** `TAPE_PRE_ECHO = ON` (`ECHO_TIME = 340 ms`, `58%` feedback), `DWELL_DRIVE = 95%`, `DRIP_CHIRP = 85%`.
- **Routing:** `ROUTING_POS = POST_AMP` with high-pass filter at `220 Hz` on the wet tank to keep sub-bass crystal clear.
- **Mix:** `MIX_WET_DRY = 55%`.

### Scene D: Vintage Blues Subtle Room (Chicago / Texas Studio Warmth)
- **Concept:** Sweet, understated internal combo amp spring reverb that adds depth and organic glue without getting in the way of blues phrasing.
- **Tank Settings:** `TANK_MODEL = BLACKFACE_INTERNAL`, `DWELL_DRIVE = 38%`, `DRIP_CHIRP = 25%`, `TONE_DAMP = 3.4 kHz`, `TANK_DECAY = 1.9 s`.
- **Routing:** `ROUTING_POS = POST_AMP`.
- **Mix:** `MIX_WET_DRY = 24%`.

---

## 5. Hardware Setup & Mapping

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (Surf Drip Tank) / Scene B (Spaghetti Western Twang).
- **Footswitch B:** Scene C (Ambient Dub Splash).
- **Footswitch C:** Scene D (Vintage Blues Room) / Bypass.
- **Knob 1 (REVERB / DWELL):** Driver Tube Dwell saturation (`0%` to `100%`).
- **Knob 2 (TONE):** Recovery Tone Filter (`2.0 kHz` dark to `9.0 kHz` splash).
- **Knob 3 (BLEND):** Spring Mixer dry/wet ratio.

### Tank-B Control Assignments
- Dub bassists and surf baritone players can engage Scene C with a built-in wet-only `220 Hz` HPF so that low $E_1$ and $A_1$ bass notes hit the tape echo cleanly without muddying the spring tank.

### Black Box Desktop Configuration
- **Expression Pedal 1:** Real-time continuous control over `DWELL_DRIVE` (allows kicking a tank into dramatic spring splash during staccato accents, then pulling back for clean rhythm).
- **Stereo Dual-Spring Mode:** Pans left and right springs slightly apart with complementary coil lengths for massive studio breadth.
