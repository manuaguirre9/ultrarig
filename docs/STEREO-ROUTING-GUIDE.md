# UltraRig Stereo Routing & Ping-Pong Spatial Effects Guide

Modern guitar and bass rigs increasingly leverage spatial stereo imaging for immersive in-ear monitoring, dual-amplifier live stages, and studio recording. While the instrument input of the M-VAVE Tank-G is monophonic, UltraRig features a **Mono-In / Stereo-Out** architecture capable of routing independent left and right audio channels with dedicated spatial processing.

This guide details physical stereo output cabling, dual cabinet IR panning, ping-pong and dual-tempo delay configurations, in-ear monitoring (IEM) setups, and essential techniques to avoid the catastrophic **"mono summing phase cancellation"** trap on live stages.

---

## 1. UltraRig Stereo Signal Architecture

```
 [ Mono Guitar Input ]
          │
          ▼
 [ Noise Gate ──> Compressor ──> Overdrive ──> NAM A2-Lite Amp ] (Pure Monophonic Core)
          │
          ▼
   ┌───────────────┐
   │ STEREO SPLIT  │
   └──┬─────────┬──┘
      ▼         ▼
  [Branch A] [Branch B]  ──> Dual IRs / Dual Modulation / Ping-Pong Delays
      │         │
      ▼         ▼
  [  Left  ] [ Right  ]  ──> True Stereo Algorithmic Reverb
      │         │
      └────┬────┘
           ▼
  ┌─────────────────────────────────────────────────────────────┐
  │ Physical Outputs:                                           │
  │ 1. 3.5 mm TRS Headphone Jack (True Stereo Left + Right)      │
  │ 2. 6.35 mm Main Jack (Mono Mixdown or Left Channel)         │
  └─────────────────────────────────────────────────────────────┘
```

### Physical Output Cabling
To output true stereo from the pedal into a mixing desk, audio interface, or dual stage amplifiers:
* **The 3.5 mm TRS Stereo Breakout Cable:** Use a **3.5 mm TRS to dual 6.35 mm TS (or dual XLR male)** breakout Y-cable plugged into the headphone output jack.
  - **Tip:** Audio Left Channel
  - **Ring:** Audio Right Channel
  - **Sleeve:** Shared Ground / Shield
* The main 6.35 mm output jack serves as a balanced/unbalanced mono output summing the stereo bus or feeding a single front-of-house channel.

---

## 2. The Live Stage Reality: The Mono Summing Trap

> [!WARNING]
> Over 85% of club and festival Front-of-House (FOH) PA systems run in **Mono** to ensure audience members standing on the far left or far right hear a balanced musical mix.

```
 [ Stereo Rig ] ──> Left Channel:  Sinusoidal Wave  (+)
                ──> Right Channel: Phase Inverted   (-)
                          │
                          ▼ [ Club Mono Mixer Summing ]
                Left (+) + Right (-) = ZERO (COMPLETE CANCELLATION)
```

### The Problem:
Effects that create stereo width by inverting the phase of one channel (180° phase flip chorus or pseudo-stereo widening) sound massive in headphones. However, when a sound engineer presses the "Mono" button on the mixing desk, the positive and negative waves collide, causing **destructive phase cancellation**. Your guitar tone becomes thin, tinny, hollow, or completely vanishes from the live mix.

### Designing 100% Mono-Compatible Stereo Presets:
1. **Never use 180° phase inversion to create width.**
2. **Use Timbral Stereo Differentiation:** Instead of phase tricks, load two distinct cabinet IRs or set slightly different EQ curves on Branch A and Branch B.
3. **Always Test in Mono:** In the UltraRig editor or your DAW, toggle the master output to Mono. If your guitar volume drops noticeably or sounds like it's inside a metal pipe, reduce stereo width until the mono sum sounds punchy and full.

---

## 3. Dual Cabinet IR Stereo Panning (Massive Wall of Sound)

One of the most effective, phase-safe stereo techniques is panning two complementary cabinet impulse responses:

```
                            ┌──> [ Cabinet IR 1: Celestion V30 4x12 ] ──> [ Pan 100% Left ]  ──┐
 [ NAM Amp (Clean/Lead) ] ──┤                                                                   ├──> [ Stereo Bus ]
                            └──> [ Cabinet IR 2: Greenback 4x12 ]    ──> [ Pan 100% Right ] ──┘
```

* **Branch A (Hard Left):** Modern high-gain cab (e.g., Celestion Vintage 30 with dynamic SM57 microphone) — provides tight low-end punch and aggressive upper-mid cut.
* **Branch B (Hard Right):** Vintage warm cab (e.g., Greenback 4x12 or 2x12 Open Back with ribbon microphone) — provides smooth, woody midrange and silky highs.
* **Result:** A gigantic, wide three-dimensional guitar wall without any chorusing modulation or artificial comb filtering.

---

## 4. Ping-Pong Delay & Asymmetric Dual Subdivisions

### Ping-Pong Delay Mode
In Ping-Pong mode, the initial echo repeats in the Left channel, the second echo bounces to the Right channel, and subsequent repeats alternate back and forth across the stereo panorama.
* **Recommended Settings:**
  - **Time:** `350 ms – 450 ms` (or Tap-Tempo 1/4 note)
  - **Feedback:** `40% – 55%`
  - **Stereo Width:** `100%`
  - **Mix:** `25% – 35%`

### Dual-Tempo Polyrhythmic Delay
Rather than alternating ping-pong bounces, set independent delay time subdivisions on Left and Right:

```
 Left Channel Delay (1/8 Note: 250 ms)   ──> [ Repeats:  *     *     *     *     * ]
 Right Channel Delay (Dotted 1/8: 375 ms) ──> [ Repeats:    *        *        *   ]
```

* **Result:** A classic rhythmic pattern (The Edge / U2, Pink Floyd style) that fills the stereo field with rhythmic momentum without cluttering the center vocal space.

---

## 5. Live Stage Connection Topologies

```
 ┌────────────────────────────────────────────────────────────────────────┐
 │                      Stereo Stage Topologies                           │
 ├───────────────────┬────────────────────────────────────────────────────┤
 │ 1. In-Ear (IEM)   │ 3.5mm TRS ──> Stereo Wireless IEM Transmitter     │
 │ 2. FOH Stereo PA  │ 3.5mm TRS Breakout ──> Dual Passive DI Boxes ──> PA│
 │ 3. Dual Amps/FRFR │ Left ──> FRFR Cab 1 | Right ──> FRFR Cab 2 (Stage) │
 └───────────────────┴────────────────────────────────────────────────────┘
```

### Setup A: Wireless In-Ear Monitors (IEMs)
* Connect a 3.5 mm TRS-to-TRS (or 3.5 mm to dual XLR) cable directly from UltraRig's headphone output into your wireless stereo transmitter (Sennheiser, Shure, XVive).
* Enjoy a high-definition 3D stereo listening experience that isolates your guitar in space without stage bleed.

### Setup B: Front-of-House (FOH) via Dual DI Boxes
* When connecting into balanced stage snakes:
  - Plug the 3.5 mm TRS breakout into **two passive Direct Boxes (DI Boxes)**.
  - Run balanced XLR cables from DI 1 (Left) and DI 2 (Right) into the stage snake.
  - **Crucial Stage Tip:** If you hear a low 50/60 Hz hum, engage the **Ground Lift** switch on one of the DI boxes to break the ground loop between the two mixer channels.

### Setup C: Wet / Dry / Wet (WDW) Rig
* Route your dry NAM amp tone to the center stage amplifier/cabinet, while routing stereo ping-pong delays and reverbs to two side FRFR powered monitors.

---

## 6. Stereo Setup Checklist

- [ ] 3.5 mm TRS stereo breakout Y-cable tested and packed in gig bag.
- [ ] Presets verified for **Mono Summing Compatibility** (no phase cancellation).
- [ ] Dual cabinet IRs level-matched between Left and Right branches.
- [ ] Delay stereo width and pan positions verified in editor.
- [ ] Ground lift switch verified on stage DI boxes to eliminate ground loops.
