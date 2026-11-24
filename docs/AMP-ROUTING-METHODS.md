# Live Stage Connections & Real Amplifier Routing Guide for UltraRig

This guide explains how to connect your M-VAVE pedal (Tank-G, Tank-B, Black Box) running **UltraRig** to real guitar and bass amplifiers, FRFR monitors, PA systems, and in-ear monitors (IEMs), detailing when to enable or disable the Cabinet IR block to prevent tone degradation.

---

## 1. Quick Decision Matrix: Should the Cabinet IR Block Be ON or OFF?

The most common mistake guitarists make when playing through real amplifiers is leaving the digital Cabinet IR block engaged.

| Destination Device | Speaker Type | Cabinet IR Block Setting | Why? |
|---|---|---|---|
| **Real Guitar/Bass Amplifier (FX Return / Power Amp In)** | Physical Guitar Speaker (e.g. Celestion V30, Greenback) | ❌ **OFF (Disabled)** | The physical speaker already filters high frequencies. Two cabinet filters result in a dark, muffled "blanket over the speaker" tone. |
| **Front Input of Clean Guitar Amp** | Physical Guitar Speaker | ❌ **OFF (Disabled)** | Physical cabinet already provides acoustic filtering; disable both NAM amp and IR, or use transparent preamps. |
| **PA System / Audio Mixer / Front of House (FOH)** | Full-Range PA Speakers | ✅ **ON (Enabled)** | PA speakers are full-range flat-response; without an IR, digital distortion sounds like a harsh, buzzy "bee in a can". |
| **FRFR (Full-Range Flat-Response) Stage Wedge** | Flat-Response Powered Speaker (e.g. Headrush, Line 6) | ✅ **ON (Enabled)** | FRFR monitors are designed to faithfully reproduce virtual mic'd cabinet IRs. |
| **In-Ear Monitors (IEMs) / Headphones** | Full-Range In-Ear Drivers | ✅ **ON (Enabled)** | Requires an IR block to sound like a natural mic'd cabinet in a room. |

---

## 2. Method 1: Direct to Effects Loop Return (Power Amp In)

This is the **highest-fidelity method** for playing through a real physical guitar or bass amplifier on stage.

```text
[Guitar] ---> [UltraRig In]
                 |
                 +- [Noise Gate]
                 +- [Drive / Boost]
                 +- [NAM Preamp Model] (Plexi, Recto, SVT)
                 +- [Modulation / Delay / Reverb]
                 +- [Cabinet IR: BYPASSED / OFF]
                 |
[UltraRig 1/4" Out] ---> [Amplifier FX LOOP RETURN / POWER AMP IN]
                                |
                   [Amplifier Tube/Solid-State Power Section]
                                |
                   [Physical Guitar/Bass Speaker Cabinet]
```

### Why this works so well:
* Bypasses the physical amplifier's preamp stage and tonestack coloring.
* Uses the physical amp's power section (EL34, 6L6, or Class-D) purely to amplify the sound of UltraRig's **NAM Preamp Capture**.
* **Cabinet IR MUST be bypassed in this setup.**

---

## 3. Method 2: Front of Amp (Stompbox Mode)

If your amplifier does not have an effects loop (common on vintage Fender combos or compact practice amps):

```text
[Guitar] ---> [UltraRig In] ---> [UltraRig 1/4" Out] ---> [Amp Front Guitar Input]
```

### Configuration Tips:
* Set your physical amplifier's clean channel to a neutral EQ (Bass, Middle, Treble around 12 o'clock).
* **Bypass both the NAM Amp Capture and Cabinet IR blocks** in UltraRig, or use an ultra-clean, transparent preamp model with low gain.
* Use UltraRig as a high-powered digital pedalboard: engage its Compressor, Overdrive, Chorus, Phaser, Delay, and Reverb blocks in front of your clean amp.

---

## 4. Method 3: Direct to PA / FRFR Active Monitor / In-Ear Monitors (IEMs)

The modern standard for silent stages, portable touring rigs, and consistent sound at every venue.

```text
[Guitar] ---> [UltraRig In]
                 |
                 +- [Full Signal Chain: Drives, NAM Amp, Time FX]
                 +- [1024-point Cabinet IR: ACTIVE / ON]
                 |
[UltraRig XLR Out] ---> [Snake / Stage Box / PA Mixer (FOH)]
```

### Advantages:
* **Total Consistency:** Your tone sounds identical at home, at band rehearsal, and through the front-of-house sound system.
* **Stereo Ambiance:** If the sound engineer provides two channels, you can run stereo delays and lush reverbs panning wide across the venue PA.
* **No Stage Bleed:** Eliminates high volume levels on stage, allowing the vocal microphones to remain clean and feedback-free.

---

## 5. Method 4: Hybrid Stage Setup (FOH with IR + Stage Monitor without IR)

If you need to feed the front-of-house PA with a full mic'd sound while simultaneously driving a physical stage guitar cabinet:

* Use UltraRig's **Parallel Routing**:
  * **Path A (FOH Feed):** Route through your NAM Preamp $\to$ **Cabinet IR (ON)** $\to$ Output Left (or XLR) to PA.
  * **Path B (Stage Monitor Feed):** Route through NAM Preamp $\to$ **Cabinet IR (Bypassed)** $\to$ Output Right (1/4" Out) to the stage amp's Effects Return.

---

## 6. Ground Loops & 60-Cycle Hum Prevention

When connecting multi-effects units simultaneously to an AC-powered stage amplifier and a PA mixer:

* **What Causes Ground Loops:** Potential differences between the amplifier's electrical wall outlet ground and the soundboard's ground create a circulating current through the cable shield, resulting in a loud $50\text{ Hz} / 60\text{ Hz}$ low hum.
* **Solutions:**
  * Connect the pedal's balanced XLR output to a passive DI box equipped with a **Ground Lift switch** before feeding the PA snake.
  * Power your pedal and amplifier from the **same electrical power strip/outlet** on stage whenever possible.
  * Avoid running audio cables parallel to high-current AC power cables or stage lighting cables.
