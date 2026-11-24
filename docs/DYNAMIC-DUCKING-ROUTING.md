# UltraRig Dynamic Ducking Delay & Reverb Routing Guide

Guitarists frequently face a classic mixing dilemma: **spacious ambiance versus solo articulation**:
* Large, immersive time-based effects (such as 500 ms quarter-note delays and cathedral reverbs) make sustained notes and melodic bends sound massive, smooth, and professional.
* However, during fast sixteenth-note shred runs, arpeggios, or staccato rhythm passages, those same repeats collide with your newly plucked notes, creating a cluttered, muddy wash of sound.

**Dynamic Ducking** (popularized by legendary studio processors like the TC Electronic 2290 and Lexicon 480L) solves this problem automatically. While you are actively playing notes, the volume of the wet delay and reverb is automatically attenuated ("ducked"). The moment you hold a sustained note, execute a vibrato bend, or pause, the repeats and reverb tails smoothly "bloom" back up to full volume.

This guide details the mechanics of dynamic ducking, parameter calibration, parallel sidechain routing, and sound design recipes for live performance.

---

## 1. How Dynamic Ducking Works

```
 Guitar Pick Attack:   [ Fast Shred Notes: * * * * * * * * ] ────> [ Sustained Bend ~~~ ]
                               │                                           │
                               ▼                                           ▼
 Envelope Level:       [ HIGH INPUT AMPLITUDE ]             [ LOW RESTING AMPLITUDE ]
                               │                                           │
                               ▼                                           ▼
 Delay / Reverb Level: [ DUCKED / ATTENUATED (-10 dB) ]     [ FULL BLOOM (0 dB UNITY) ]
                       Notes stay razor-sharp and punchy    Echoes fill the musical space
```

### The Benefits:
* **Zero Footwork:** You never need to tap-dance on footswitches to bypass delays during fast passages and re-engage them on slow solos.
* **Intelligible Pick Attack:** Every transient cuts through dense drums and bass without losing stereo depth.
* **Natural Musical Phrasing:** The wet effects fill the pauses between your musical phrases like an attentive studio mix engineer riding the faders.

---

## 2. Parameter Calibration & The "Goldilocks Zone"

```
 ┌────────────────────────────────────────────────────────────────────────┐
 │                      DUCKING PARAMETERS GUIDE                          │
 ├───────────────────┬────────────────────────────────────────────────────┤
 │ Sensitivity       │ Threshold where picking triggers the volume drop   │
 │ Ducking Depth     │ Amount of attenuation (Recommended: -6 to -12 dB)  │
 │ Release / Bloom   │ Recovery time for repeats to swell back up (ms)    │
 └───────────────────┴────────────────────────────────────────────────────┘
```

### 1. Ducking Depth (Attenuation Amount)
* **Too Extreme (-24 dB to -INF):** The repeats disappear completely while playing and suddenly leap out during pauses. This creates an unnatural, jarring on/off pumping effect.
* **Too Weak (-2 dB to -3 dB):** Not enough attenuation; fast note runs remain cluttered and muddy.
* **The Sweet Spot (-6 dB to -12 dB):** Reduces the wet level just enough to leave an ambient "halo" behind your lead lines while keeping your pick attacks crystal clear. When you stop, the tails blossom naturally.

### 2. Release Time (Bloom Speed)
* **Fast Shred Passages:** Set Release between **120 ms and 180 ms**. The repeats swell in almost instantly the moment your pick stops moving, catching short sixteenth-note pauses.
* **Slow Ballads & Melodic Solos:** Set Release between **250 ms and 400 ms**. Provides a smooth, cinematic swelling transition that blooms behind wide vibrato bends.

---

## 3. Two Implementation Methods in UltraRig

### Method 1: Integrated Block Ducking (Simple & Direct)
UltraRig's digital delay and studio reverb blocks feature built-in dynamic ducking:
1. Open the **Delay** or **Reverb** block parameter inspector in the Web Editor.
2. Locate the **Ducking** section.
3. Set **Ducking Depth:** `-8.0 dB`.
4. Set **Sensitivity:** Pluck a medium-strength lead note. Adjust sensitivity until the ducking indicator illuminates reliably during playing.
5. Set **Release Time:** `200 ms`.

---

### Method 2: Parallel Wet/Dry Sidechain Ducking (Studio Pro Routing)

For complete control over multiple parallel spatial effects, use UltraRig's parallel branches with an **Inverted Envelope Follower**:

```
                              ┌──> [ Branch A: 100% Dry Guitar + NAM + IR ] ────────────┐
 [ Guitar / Drive / NAM ] ────┤                                                          ├──> [ Merge ] ──> [ Out ]
                              └──> [ Branch B: Delay (100% Wet) ──> Reverb (100% Wet) ] ──┤
                                                        ▲                                │
                                                        │                                │
                                   [ Inverted Envelope Follower (-75% Depth) ] ──────────┘
```

1. Insert a **Split** block after your NAM Amp and Cabinet IR blocks.
2. Route the direct tone through **Branch A**.
3. Place your **Delay** and **Reverb** blocks on **Branch B**, and configure their internal mixes to **100% Wet**.
4. Insert a **Gain / Volume** block on Branch B immediately following the reverb.
5. Open the **Modulation Matrix**:
   - **Source:** `Envelope 1` (tracking input guitar dynamics).
   - **Destination:** `Branch B Gain: Level`.
   - **Modulation Depth:** `-70%` (Inverted polarity).
   - **Attack:** `10 ms`, **Release:** `220 ms`.
6. When you pick aggressively, `Envelope 1` pulls Branch B's volume down automatically. When you pause or sustain, Branch B opens up to unity gain, creating a lush, professional studio ducking swell.

---

## 4. Practical Sound Design Recipes

### Recipe 1: The Arena Lead (Pink Floyd / David Gilmour Style)
* **Goal:** Huge 450 ms analog delay and lush hall reverb that never masks expressive blues phrasing.
* **Delay Mix:** `40%`, **Feedback:** `50%`.
* **Ducking Depth:** `-9.0 dB`, **Release:** `280 ms`.
* **Result:** Fast pentatonic runs remain clear and punchy; held bends at the end of each phrase are enveloped in massive, singing repeats.

---

### Recipe 2: The Shredder's Safety Net (John Petrucci / Steve Vai Style)
* **Goal:** High-gain liquid lead tone with stereo delay that stays articulate at 160+ BPM sixteenth notes.
* **Delay Mix:** `35%`, **Feedback:** `45%`.
* **Ducking Depth:** `-12.0 dB`, **Release:** `130 ms`.
* **Result:** Zero mud during lightning-fast sweep picking and arpeggio runs.

---

### Recipe 3: The "Cloud Reverb" Ambient Swell
* **Goal:** Massive 8-second ambient hall reverb that clears out during rhythm chord strums.
* **Reverb Mix:** `50%`, **Decay:** `7.5s`.
* **Ducking Depth:** `-14.0 dB`, **Release:** `400 ms`.
* **Result:** Rhythm chord changes remain clear and punchy, but the second you stop playing, an immense ambient cloud washes over the room.

---

## 5. Recommended 4-Scene Layout with Dynamic Ducking

| Scene | Name | Delay Configuration | Ducking Settings | Ideal Musical Style |
| :---: | :--- | :--- | :--- | :--- |
| **A** | **Rhythm Crunch** | Delay Bypassed (Trails On) | Ducking OFF | Heavy verses & tight chugs |
| **B** | **Fast Solo** | Quarter-Note Delay (400 ms) | Ducking `-12 dB`, Release `130 ms` | Shred runs & fast arpeggios |
| **C** | **Melodic Lead** | Dotted Eighth Delay (350 ms) | Ducking `-8 dB`, Release `300 ms` | Expressive ballad solos & bends |
| **D** | **Ambient Swell** | Delay + Cathedral Reverb | Inverted Envelope Ducking `-16 dB` | Film score pads & slow volume swells |
