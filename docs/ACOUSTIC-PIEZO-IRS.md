# UltraRig Acoustic Guitar Piezo IRs & Signal Chain Guide

Undersaddle piezoelectric (piezo) pickups are the industry standard for live acoustic guitars due to their high feedback resistance and stage reliability. However, piezo crystals measure direct mechanical string pressure under the bridge saddle rather than acoustic vibrations in the air. This produces the notorious **"piezo quack"** — an unnatural, brittle, plasticky transient spike between 2.5 kHz and 4.5 kHz that completely lacks the warm wooden resonance of an acoustic guitar body.

Using UltraRig's 1024-point convolution engine, you can load **Acoustic Body Impulse Responses (Acoustic IRs)** into your M-VAVE Tank-G, transforming raw piezo pickups into the rich, open tone of a high-end acoustic guitar recorded with studio condenser microphones.

---

## 1. How Acoustic IRs Eliminate "Piezo Quack"

```
 [ Acoustic Guitar Strings ]
             │
             ├───────────────────────────────────────────────────────┐
             ▼                                                       ▼
 [ Undersaddle Piezo Pickup ]                               [ Physical Guitar Body ]
             │ (Direct mechanical pressure)                  - Spruce/Cedar Soundboard
             │ - Harsh, sterile transients                   - Mahogany/Rosewood Cavity
             │ - No wood/air resonance                       - Air Helmhotz Resonance (~100 Hz)
             │ - Brittle 3 kHz "quack"                               │
             ▼                                                       ▼
 [ UltraRig 1024-Point Acoustic IR Convolver ] <─── [ Studio Condenser Microphone ]
             │                                       (Neumann KM184 / AKG C414)
             ▼
 [ Natural, Mic'd Studio Acoustic Tone at FOH ]
```

An **Acoustic IR** is the mathematical transfer function between the dry undersaddle piezo signal and a studio microphone positioned in front of the soundhole. When convolved in real-time by UltraRig's DSP:
1. It subtracts the harsh resonance peaks inherent to piezoelectric crystals.
2. It re-introduces the multi-dimensional body resonance of soundboard woods (Sitka Spruce, Engelmann, Cedar).
3. It simulates natural air cavity resonances and microphone distance characteristics.

---

## 2. Ideal Acoustic Signal Chain in UltraRig

Unlike electric guitar patches, an acoustic patch requires pristine linearity and headroom.

```
 [ Input Trim ] ──> [ High-Pass Filter (75 Hz) ] ──> [ Studio Compressor ]
       │
       ▼
 [ BYPASS NAM Block ] ──> [ 1024-pt Acoustic IR ] ──> [ Parametric Notch EQ ]
       │
       ▼
 [ Subtle Stereo Chorus / Doubler ] ──> [ Studio Plate Reverb ] ──> [ Output / PA ]
```

### 1. Bypass the NAM Amp Block
> [!IMPORTANT]
> The NAM (Neural Amp Modeler) block **must be bypassed** in acoustic patches. Guitar amp models introduce non-linear saturation, harmonic distortion, and midrange humps designed for electric guitars that will ruin acoustic clarity.

### 2. Input Gain Staging & High-Pass Filter
* **Input Trim:** Active piezo preamps (powered by 9V batteries inside the guitar) output significantly hotter signals than passive electric pickups. Reduce input trim if the clip indicator flashes on aggressive strumming.
* **Master High-Pass Filter (HPF):** Set to **70 Hz – 80 Hz** (12 dB/octave). Acoustic guitars produce no musical fundamentals below low E (82.4 Hz). Cutting below 75 Hz eliminates handling thumps, floor vibrations, and sub-bass boom.

### 3. Studio / Optical Compressor
* **Target:** Smooth out aggressive strumming spikes without killing delicate fingerpicking nuances.
* **Recommended Settings:**
  - **Ratio:** `2.5:1` to `3.5:1`
  - **Attack:** `25 ms – 40 ms` (allows the natural percussive pick attack to pass through before clamping down)
  - **Release:** `100 ms – 150 ms`
  - **Gain Reduction:** Aim for `-2 dB` to `-4 dB` of reduction during heavy strumming.

### 4. Acoustic Body IR (1024 Points)
* Load an acoustic guitar body IR matched to your instrument's body shape (e.g., Dreadnought, Grand Auditorium, Jumbo, Parlor, or Classical Nylon).
* Set IR block mix to **100% Wet** (or blend 80% IR / 20% dry piezo if you need extra snappy attack in high-energy pop/rock bands).

### 5. Parametric Notch EQ (Anti-Feedback & De-Quacking)
* **Band 1 (Body Resonance / Boom):** Narrow notch (Q=3.5 to 5.0) at **105 Hz – 125 Hz**, attenuated by **-3 dB to -5 dB** to eliminate runaway low-end feedback.
* **Band 2 (Piezo Quack Remnant):** Broad dip (Q=1.4) centered at **3.2 kHz**, attenuated by **-2 dB to -3.5 dB** to smooth out lingering string bite.
* **Band 3 (Air & Shimmer):** Gentle high shelf boost at **10 kHz – 12 kHz** (+1.5 dB) for open studio air.

### 6. Spatial Effects (Reverb & Modulation)
* **Reverb:** Select a **Studio Plate** or **Small Concert Hall** algorithm. Set decay time between **1.2s and 1.8s** with a subtle mix of **10% to 15%**.
* **Chorus (Optional):** Keep rate slow (0.8 Hz) and depth shallow (15%) for subtle dimension without obvious pitch warble.

---

## 3. Recommended 4-Scene Layout for Acoustic Gigs

Take advantage of UltraRig's 4 scenes per preset for seamless switching during acoustic sets:

| Scene | Name | Description & Block Configuration |
| :---: | :--- | :--- |
| **A** | **Fingerstyle** | Maximum IR richness (100% IR), gentle compression, +2 dB volume lift, warm plate reverb. |
| **B** | **Strumming Rhythm** | Tight compression (-4 dB gain reduction), slight 3.2 kHz cut, scooped 800 Hz to sit under vocals. |
| **C** | **Acoustic Lead / Solo** | +3.5 dB clean boost, subtle analog delay (350 ms, 2 repeats), widened stereo image. |
| **D** | **12-String / Ambient** | Parallel pitch block with octave-up detuned by +7 cents, shimmer reverb for atmospheric intros. |

---

## 4. Live Stage Feedback Prevention

Acoustic instruments have hollow wooden bodies that act as acoustic microphones on stage, creating feedback loops when exposed to loud stage monitors or subwoofers.

### Step 1: Install a Soundhole Cover ("Feedback Buster")
A rubber soundhole plug stops external stage monitor vibrations from entering the guitar cavity while having zero negative impact on your undersaddle piezo pickup signal.

### Step 2: Sweep the Feedback Notch Filter
If a low howling pitch occurs during soundcheck:
1. Boost a narrow parametric band (+8 dB, Q=6.0).
2. Slowly sweep between **90 Hz and 220 Hz** until the feedback screams.
3. Once the offending frequency is pinpointed, invert the gain to **-6 dB to -9 dB**.

### Step 3: Phase Inversion
If stage monitor sound cancels out your guitar's low end or triggers runaway feedback, toggle the **Phase (180°)** switch in UltraRig's output block.

---

## 5. Acoustic IR File Specifications for UltraRig

When importing third-party or custom-generated acoustic IRs into the Tank-G:

| Specification | Supported / Recommended Value | Notes |
| :--- | :--- | :--- |
| **Format** | Linear PCM WAV (`.wav`) | Uncompressed audio |
| **Sample Rate** | 44.1 kHz or 48.0 kHz | Handled natively by UltraRig's engine |
| **Bit Depth** | 24-bit (or 16-bit) | 32-bit float should be converted to 24-bit PCM |
| **Channels** | Mono (1 channel) | Stereo files will use channel 1 (Left) |
| **Length** | **1024 samples (~21.3 ms)** | Longer files (2048/4096) are automatically truncated |

### Trusted Acoustic IR Sources
* **Open Source / Community Generator:** Cuki79's open-source Acoustic IR generator scripts.
* **Commercial Libraries:** 3 Sigma Audio Acoustic IRs, Worship Tutorials Acoustic IRs.
* **Custom ToneDexter Captures:** Wavemaps exported from ToneDexter pedals can be converted to standard 1024-point mono WAV files.
