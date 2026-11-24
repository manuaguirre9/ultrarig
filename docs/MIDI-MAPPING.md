# MIDI Implementation & Mapping Specification for UltraRig

UltraRig features class-compliant **USB MIDI** and **Bluetooth BLE MIDI** capabilities. This enables external foot controllers (such as the M-VAVE Chocolate, Ampero Control, or Morningstar) and DAWs to switch presets, trigger scenes, toggle individual effects blocks, and synchronize tempo automatically.

---

## 1. MIDI Channels & Connection

* **Default Channel:** **Channel 1** (UltraRig listens on Channel 1 by default, or in Omni mode if configured).
* **Connection Types:**
  * **USB MIDI:** Connect a USB cable directly from your computer, USB MIDI host, or audio interface. No drivers are required on Windows 10/11, macOS, Linux, or Android.
  * **Bluetooth BLE MIDI:** Wirelessly pair the pedal with an external BLE controller or smartphone running a MIDI control app.

---

## 2. Program Change (PC) — Preset Recall

UltraRig organizes memory into **8 Banks** with **4 Presets each**, providing a total of **32 user presets**.

Sending a standard MIDI **Program Change (PC)** message recalls the corresponding preset instantly:

| Bank | Preset Slot | MIDI PC (0-indexed) | MIDI PC (1-indexed) |
|---|---|---|---|
| **Bank 1** | 1A / 1B / 1C / 1D | `0`, `1`, `2`, `3` | `1`, `2`, `3`, `4` |
| **Bank 2** | 2A / 2B / 2C / 2D | `4`, `5`, `6`, `7` | `5`, `6`, `7`, `8` |
| **Bank 3** | 3A / 3B / 3C / 3D | `8`, `9`, `10`, `11` | `9`, `10`, `11`, `12` |
| **Bank 4** | 4A / 4B / 4C / 4D | `12`, `13`, `14`, `15` | `13`, `14`, `15`, `16` |
| **Bank 5** | 5A / 5B / 5C / 5D | `16`, `17`, `18`, `19` | `17`, `18`, `19`, `20` |
| **Bank 6** | 6A / 6B / 6C / 6D | `20`, `21`, `22`, `23` | `21`, `22`, `23`, `24` |
| **Bank 7** | 7A / 7B / 7C / 7D | `24`, `25`, `26`, `27` | `25`, `26`, `27`, `28` |
| **Bank 8** | 8A / 8B / 8C / 8D | `28`, `29`, `30`, `31` | `29`, `30`, `31`, `32` |

---

## 3. Control Change (CC) — Scenes & Real-Time Parameters

Control Change (CC) commands trigger specific functions within the currently active preset without re-loading audio captures from flash.

### Scene Selection (Within Active Preset)
Each preset contains **4 Scenes** (instant parameter and bypass snapshots with zero-gap audio switching):

| Function | MIDI CC Number | Value Range | Behavior |
|---|---|---|---|
| **Scene Select** | `CC #20` | `0` = Scene 1<br>`1` = Scene 2<br>`2` = Scene 3<br>`3` = Scene 4 | Switches to designated scene |
| **Scene 1 Direct** | `CC #50` | `127` (momentary) | Recalls Scene 1 |
| **Scene 2 Direct** | `CC #51` | `127` (momentary) | Recalls Scene 2 |
| **Scene 3 Direct** | `CC #52` | `127` (momentary) | Recalls Scene 3 |
| **Scene 4 Direct** | `CC #53` | `127` (momentary) | Recalls Scene 4 |

### Individual Effect Block Bypass (Stompbox Mode)
Toggle individual blocks on/off in real time:

| Block | MIDI CC Number | Off (Bypass) | On (Active) |
|---|---|---|---|
| **Noise Gate** | `CC #21` | `0 - 63` | `64 - 127` |
| **Compressor** | `CC #22` | `0 - 63` | `64 - 127` |
| **NAM Amp / Drive** | `CC #23` | `0 - 63` | `64 - 127` |
| **Modulation (Chorus / Flanger / Phaser)** | `CC #24` | `0 - 63` | `64 - 127` |
| **Delay** | `CC #25` | `0 - 63` | `64 - 127` |
| **Reverb** | `CC #26` | `0 - 63` | `64 - 127` |
| **Cabinet IR** | `CC #27` | `0 - 63` | `64 - 127` |

### Utility Controls
| Function | MIDI CC Number | Value | Action |
|---|---|---|---|
| **Chromatic Tuner** | `CC #60` | `0 - 63` = Exit<br>`64 - 127` = Engage | Mutes audio output and activates tuner screen |
| **Tap Tempo** | `CC #64` | `127` (momentary) | Calculates delay time from consecutive taps |
| **Master Output Volume** | `CC #7` | `0 - 127` | Adjusts main output volume level |
| **Expression / Wah** | `CC #11` | `0 - 127` | Continuous parameter control (sweep) |

---

## 4. Integration Examples

### Example A: M-VAVE Chocolate Wireless Controller
The 4-button **M-VAVE Chocolate** is the ideal companion for the Tank-G / Tank-B:
1. Open the **CubeSuite** app on your phone to configure the Chocolate.
2. Select **Program Change Mode**:
   - Switch A: `PC 0` (Preset 1A)
   - Switch B: `PC 1` (Preset 1B)
   - Switch C: `PC 2` (Preset 1C)
   - Switch D: `PC 3` (Preset 1D)
3. Or select **Custom CC Mode (Scene Mode)**:
   - Switch A: `CC #50` (Scene 1)
   - Switch B: `CC #51` (Scene 2)
   - Switch C: `CC #52` (Scene 3)
   - Switch D: `CC #53` (Scene 4)

### Example B: DAW Live Automation (Reaper / Ableton Live)
For live stage performances with backing tracks:
1. Create a dedicated MIDI track in your DAW routed to the pedal's USB MIDI port.
2. Insert a **PC** message at song transitions to switch whole presets.
3. Insert **CC #20** or **CC #25** events synchronized to the track grid to automatically engage a lead boost and delay for guitar solos hands-free.

---

## 5. Web MIDI & SysEx Communication

The UltraRig Web Editor (`web/index.html`) communicates with the hardware via raw bidirectional **SysEx (System Exclusive)** packets over Web MIDI.
- **Diagnostics Dump:** SysEx command requests pedal status, RAM statistics, and battery voltage.
- **Preset Backup/Restore:** Sends preset binary structures in chunked 512-byte payloads.
