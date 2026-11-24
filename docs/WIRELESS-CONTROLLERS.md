# Wireless Bluetooth MIDI Controllers Integration Guide for UltraRig

This guide explains how to pair, configure, and map external **Wireless Bluetooth MIDI Foot Controllers** (such as the **M-VAVE Chocolate**, **Hotone Ampero Control**, and **Xsonic Airstep**) with **UltraRig** running on M-VAVE pedals (Tank-G, Tank-B, Black Box).

---

## 1. Why Add an External Wireless Controller?

While the M-VAVE Tank series offers integrated footswitches, pairing an external wireless Bluetooth controller unlocks a new tier of live stage flexibility:

* **Button Expansion (From 3 to 7/8 Switches):** Use the physical pedal footswitches exclusively for Bank selection or Stompbox mode, while the wireless controller handles instantaneous Scene changes and Tuner/Tap-Tempo utility functions.
* **Stage Separation (Clean Stage Setup):** Keep your main pedal, audio cables, and power cables tucked neatly near the amplifier or stage snake, placing only a tiny, battery-powered wireless controller at the front of the stage.
* **Expression Expansion:** Many controllers (like the M-VAVE Chocolate) include an expression pedal TRS jack, sending wireless expression data (`CC #11`) to UltraRig without running long audio cables across the stage.

---

## 2. Pairing & Bluetooth BLE Setup

UltraRig implements the standard **Bluetooth Low Energy (BLE) MIDI** profile:

### Pairing with M-VAVE Chocolate:
1. Turn on the Chocolate controller and power on your UltraRig pedal.
2. Open the **CubeSuite** companion app on your smartphone.
3. Select **Chocolate** $\to$ **Wireless MIDI Connection**.
4. Scan for nearby BLE devices and select your **UltraRig pedal**.
5. Once paired, the Bluetooth indicator on the Chocolate lights solid blue. The units will now auto-reconnect automatically whenever powered on.

---

## 3. Configuration Modes & MIDI Mappings

Using your controller's configuration app (e.g. CubeSuite for Chocolate, Ampero App for Ampero Control), set the controller's footswitches to one of the following stage modes:

### Mode 1: Instantaneous Scene Selection (Recommended for Gigs)
Allows zero-latency, zero-gap switching between song sections without changing presets:

| Switch | MIDI Message Type | MIDI Channel | CC Number | Value | Action in UltraRig |
|---|---|---|---|---|---|
| **A** | Control Change (CC) | 1 | `50` | `127` (Momentary) | Recall Scene 1 (Clean) |
| **B** | Control Change (CC) | 1 | `51` | `127` (Momentary) | Recall Scene 2 (Crunch) |
| **C** | Control Change (CC) | 1 | `52` | `127` (Momentary) | Recall Scene 3 (Lead Solo) |
| **D** | Control Change (CC) | 1 | `53` | `127` (Momentary) | Recall Scene 4 (Ambient FX) |

---

### Mode 2: Stompbox Toggle Mode
Toggle individual effects blocks on and off like individual physical stompboxes:

| Switch | Effect Target | MIDI Message Type | CC Number | Off Value | On Value |
|---|---|---|---|---|---|
| **A** | **Drive / Boost** | CC (Toggle) | `23` | `0` | `127` |
| **B** | **Modulation (Chorus / Flange)** | CC (Toggle) | `24` | `0` | `127` |
| **C** | **Delay** | CC (Toggle) | `25` | `0` | `127` |
| **D** | **Reverb** | CC (Toggle) | `26` | `0` | `127` |

---

### Mode 3: Preset Bank Navigation (Program Change)
Step through full presets across all 8 banks:

* **Switch A:** `Program Change (PC)` $\to$ Preset 1A (`PC 0`)
* **Switch B:** `Program Change (PC)` $\to$ Preset 1B (`PC 1`)
* **Switch C:** `Program Change (PC)` $\to$ Preset 1C (`PC 2`)
* **Switch D:** `Program Change (PC)` $\to$ Preset 1D (`PC 3`)
* **Bank Up / Down:** Configure long-press on Switch A/B or C/D to increment/decrement bank numbers.

---

## 4. Wireless Expression Pedal Integration

If your wireless controller has an expression pedal TRS jack (such as the Chocolate's back-panel expression port):

1. Plug a standard linear ($10\text{k}\Omega$ to $25\text{k}\Omega$) expression pedal into the controller.
2. In the controller's configuration app, assign the expression jack to:
   * **MIDI Type:** `Control Change (CC)`
   * **MIDI Channel:** `1`
   * **CC Number:** `11` (Standard Expression) or `7` (Master Volume)
   * **Min/Max Range:** `0` to `127`
3. UltraRig receives the continuous expression sweep over Bluetooth in real time with sub-10 ms latency, modulating Wah, Whammy, or volume swells wirelessly.

---

## 5. Live Stage Reliability & 2.4 GHz Optimization

* **Line of Sight:** Bluetooth Low Energy operates on the $2.4\text{ GHz}$ ISM band. For best results on crowded festival stages with dozens of smartphones, keep a clear line of sight between the controller and the pedal (within $5\text{ to }10\text{ meters}$).
* **Battery Level:** Keep the controller charged; weak battery voltage in BLE transmitters can increase latency or cause dropped packets.
* **Avoid Metal Shielding:** Do not place the wireless controller directly under large metal amp chassis or behind dense stage monitors that block radio wave propagation.
