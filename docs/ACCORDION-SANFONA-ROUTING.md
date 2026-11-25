# Accordion, Bandoneón & Brazilian Sanfona Electroacoustic Routing Guide

This guide details free-reed aerophone acoustics, dual-side treble/bass microphone balancing, bellows *sforzando* compression, and preset configuration for **Accordions**, **Bandoneóns**, and the **Brazilian Sanfona (8/120 Bass)** within UltraRig for M-VAVE hardware (Black Box, Tank-B, and Tank-G v1/v2).

---

## 1. Acoustic Profile & Dual-Capture Mechanics of the Accordion

Unlike plucked or bowed string instruments, free-reed aerophones produce continuous, dense harmonic waves pressurized by the player's **bellows (*fole*)**. Amplifying a traditional or MIDI-equipped acoustic accordion involves balancing two radically different acoustic chambers simultaneously:

```
Right Hand (Treble Keyboard / Botões): 3-5 Internal Grille Capsules (F3 = 175 Hz -> 8+ kHz)
   ├── Registers: Master, Clarinet, Piccolo, Bandoneón, Musette (Detuned Dual Reeds)
   │
Left Hand (Stradella Bass & Chords):   1-2 Internal Bass Capsules (E1 = 41.2 Hz -> 400 Hz)
   └── Deep resonant low fundamentals + percussive chord stabs & button key-clack
```

### 1.1 Critical Electroacoustic Obstacles

1. **Close-Miked Reed Harshness (2.6 kHz – 5.2 kHz):** Miniature electret microphones mounted mere centimeters from metal reeds capture aggressive reed buzz, sharp *Piccolo* sizzle, and abrasive mechanical pallet/key clicks—sounding harsh through modern horn-loaded PA tops.
2. **Bellows *Sforzando* Dynamic Spikes:** Aggressive bellows pushes (*fole rasgado* in Forró or Tango accents) instantaneously flood the preamps with $+14\text{ dB}$ sustained jumps that clip mixers without fast transparent compression.
3. **Left-Hand Bass Chamber Resonance (80 Hz – 150 Hz):** The left wooden bass box acts as a reverberant sub-cabinet, howling in stage floor monitors if left un-notched.
4. **Protecting Physical *Musette / Tremolo* Tuning:** Accordions with wet *Musette* or *Vozes Oitavadas* rely on delicate physical micro-tuning offsets between reed banks. Applying LFO pitch chorus creates dissonant beating against the real reeds—use **pure distance-mic IR spatialization** instead!

---

## 2. DSP Signal Chain & Processing Topology

```
Accordion Input (Summed Dual Cable OR Stereo Split: L = Treble Keyboard, R = Stradella Bass)
   │
   ├──► [ Left Input (Treble): HPF @ 135 Hz ] ──► [ Dynamic Reed De-Harsher @ 3.5 kHz ] ──┐
   │                                                                                        │
   └──► [ Right Input (Bass): HPF @ 42 Hz ] ────► [ Bass Chamber Notch @ 118 Hz + Comp ] ──┤
                                                                                            ▼
[ Optical Bellows Leveller Compressor (3.0:1, Soft Knee) ] (Tames sudden bellows pushes)
   │
   ▼
[ Ribbon-Mic Distance Studio IR Convolution ] (Transforms harsh close mics into warm room miking)
   │
   ▼
[ Natural Acoustic Chamber / Studio Plate Reverb (Mono-Safe < 160 Hz) ] ──► Balanced Output
```

---

## 3. Parameter Specifications

| Module | Parameter | Treble Setting | Bass Setting | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **Input HPF** | High-Pass Filter | `135 Hz` (18 dB/oct) | `42 Hz` (24 dB/oct) | Removes bellows handling noise while keeping deep bass notes. |
| **Bass Notch** | Freq / Q / Gain | Bypassed | `118 Hz` / `Q=6.0` / `-7.5 dB`| Eliminates hollow wooden bass box resonance and feedback. |
| **Reed Tamer** | Dynamic EQ Dip | `3.5 kHz` (`-4.5 dB`)| `2.4 kHz` (`-3.0 dB`)| Softens close-mic metal reed buzz and button key-click. |
| **Bellows Comp**| Ratio / Attack / Rel | `2.8:1` / `18 ms` / `140 ms`| `3.5:1` / `12 ms` / `100 ms`| Controls sudden *sforzando* bellows jumps naturally. |
| **Warmth EQ** | Low-Mid Polish | `320 Hz` (`+2.0 dB`) | `180 Hz` (`+2.5 dB`) | Adds organic wooden chest body missing from tiny condenser capsules. |
| **Distance IR**| Impulse Response | `Coles_4038_Ribbon_Dist.wav`| `Neumann_U47_Room.wav`| Simulates classic 1-meter ribbon microphone studio placement. |
| **High Roll-Off**| Smooth LPF | `9.5 kHz` (12 dB/oct)| `4.5 kHz` (12 dB/oct)| Eliminates synthetic electret hiss and air rasp. |
| **Reverb** | Type / Decay / Mix | `Wood Hall` / `1.6 s` / `20%`| `Dry / Tight` (< 160 Hz Mono)| Places treble melodies warmly while keeping bass pulse punchy. |

---

## 4. Factory Scene Presets

### Scene A: Forró Pé-de-Serra Luiz Gonzaga (Baixão & Clarinete)
- **Concept:** Authentic Northeastern Brazilian Sanfona voice—punchy, woody *Clarinete* / *Bandoneon* midrange cutting alongside zabumba and triangle, anchored by tight left-hand baixaria grooves.
- **Treble & Bass EQ:** `BASS_HPF = 45 Hz`, notch @ 118 Hz (-7 dB), warm mid focus `+2.5 dB @ 650 Hz`, dynamic reed de-harsher at `3.6 kHz`.
- **Dynamics:** Fast bellows optical compressor (`3.2:1`, `12 ms` attack).
- **Space:** Intimate Wooden Studio Room (`1.1 s`, `14%` mix).

### Scene B: Tango Bandoneón & Musette (Astor Piazzolla / Paris Café)
- **Concept:** Emotional, dark, breathy European and Argentine tone emphasizing woody reed resonance without piercing highs or artificial chorus.
- **IR & EQ:** Ribbon-mic distance IR (`Coles_4038_Ribbon_Dist.wav`), smooth high-cut above `7.5 kHz`, warm low-mid bloom at `280 Hz (+3 dB)`.
- **Space:** Vintage Stone Theatre Hall (`2.2 s`, `25%` mix) with `30 ms` pre-delay.

### Scene C: Gaúcho / Chamamé Estéreo Aberto (Gaita Ponto & Vanerão)
- **Concept:** Bright, energetic southern Brazilian *Gaita* / Chamamé brilliance with pristine treble clarity for fast 16th-note runs (*floreios*).
- **Treble & Dynamics:** Air polish `+2.0 dB @ 8.5 kHz`, aggressive key-clack attenuation at `2.8 kHz`, tight bass compression.
- **Space:** Crisp Studio Plate Reverb (`1.7 s`, `20%` mix).

### Scene D: Modern Fusion Accordion Ambient (Richard Galliano / Jazz)
- **Concept:** Polished jazz concert sound for harmonic solo improvisations with spacious stereo dimension and modulated tape delay.
- **Space:** Subtle Stereo Dotted-8th Delay (`390 ms`, `22%` feedback, strictly above 200 Hz) + Cathedral Hall (`3.4 s`, `30%` mix).

---

## 5. Hardware Setup & Mapping

### Black Box Desktop Configuration
- **True Dual Treble/Bass Routing:** The Black Box shines for accordions equipped with separate Treble and Bass output jacks! Route **Treble** into Input L (with `135 Hz` HPF and Ribbon Distance IR) and **Bass** into Input R (with `42 Hz` HPF, `118 Hz` Feedback Notch, and Tight Comp) for total live mix mastery!
- **Balanced XLR Outputs:** Eliminates noisy stage DI boxes and ground loops between active internal accordion mic preamps and FOH mixing boards.

### Tank-B Control Assignments
- Ideal for single-jack summed accordions or left-hand bass optimization: Tank-B's dedicated low-end compressor and notch filters tame booming bass registers cleanly without sacrificing treble crispness.

### Tank-G (v1 / v2) Control Assignments
- **Footswitch A:** Scene A (Forró Pé-de-Serra) / Scene B (Tango Bandoneón).
- **Footswitch B:** Scene C (Gaúcho Chamamé).
- **Knob 1 (COMP):** Bellows Dynamic Levelling depth.
- **Knob 2 (EQ / TONE):** Reed Harshness / Distance Mic warmth.
- **Knob 3 (REVERB):** Concert Hall ambience mix.
