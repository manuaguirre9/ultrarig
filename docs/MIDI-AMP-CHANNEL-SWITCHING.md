# Physical Amplifier Channel Switching via MIDI with UltraRig

This guide explains how to use **UltraRig** (on M-VAVE Tank-G, Tank-B, or Black Box) as a master rig controller to switch physical analog amplifier channels (Clean, Crunch, Lead, Solo Boost) via **MIDI Out** synchronized with your digital presets and scenes.

---

## 1. The Unified Hybrid Rig Concept

In a hybrid stage rig, guitarists often want the best of both worlds:
1. The organic sound, feel, and power section of their **physical tube amplifier** (Marshall, Mesa/Boogie, Peavey, EVH, ENGL, Revv, Hughes & Kettner).
2. The flexible digital modulation, delay, pitch, and reverb effects of **UltraRig** running in the amplifier's effects loop.

By configuring UltraRig to output **MIDI Program Change (PC)** or **Control Change (CC)** messages whenever you step on a footswitch, a single tap can simultaneously change your digital delay/reverb and switch your real tube amplifier from Clean to Lead.

---

## 2. Hardware Connections (Pedal to Physical Amp)

Because the M-VAVE Tank series utilizes USB and Bluetooth for MIDI, connecting to a physical amplifier's 5-pin DIN MIDI In port is achieved through one of the following methods:

### Option A: Wireless Bluetooth MIDI Adapter (CME WIDI Master / WIDI Jack)
* Plug a **CME WIDI Master** (or compatible BLE-to-DIN dongle) directly into the amplifier's rear 5-pin DIN **MIDI IN** port.
* Pair UltraRig's Bluetooth BLE output wirelessly to the WIDI adapter.
* *Advantage:* Zero cables between your pedalboard on the front of the stage and your amplifier head at the back.

### Option B: USB Host to 5-Pin DIN MIDI Converter Box
* Connect a USB cable from the pedal's USB port into a standalone USB MIDI Host box (e.g. Kenton MIDI USB Host, DoreMidi USB MIDI Host).
* Connect a standard 5-pin DIN cable from the Host box MIDI Out into the amplifier's MIDI In.

### Option C: External MIDI Relay Switcher (For Amps Without Native MIDI)
* If your tube amplifier uses traditional 1/4" analog footswitch jacks (e.g. standard Tip-to-Ground latching relays), insert an external MIDI relay switcher (such as a **Voodoo Lab Control Switcher**, **Suhr microMIDI**, or **Nobels MS-4**).
* The switcher receives MIDI commands from UltraRig and physically shorts the amplifier's channel footswitch relays.

---

## 3. Supported MIDI Amplifiers & Protocol Mapping

Many modern amplifier heads support direct MIDI channel switching out of the box:

| Amplifier Model | MIDI Protocol | Default Channel Functions |
|---|---|---|
| **Marshall JVM (410H / 205H)** | Program Change (PC) | PC 0–11: Channel selection, Reverb on/off, Master Volume 1/2. |
| **EVH 5150 III (50W / 100W)** | Program Change (PC) | PC 1 = Green (Clean), PC 2 = Blue (Crunch), PC 3 = Red (Lead). |
| **Mesa/Boogie Mark V** | External Relay / MIDI | Switch channels 1, 2, 3, Solo Boost, and Graphic EQ. |
| **Hughes & Kettner GrandMeister / Black Spirit** | PC & CC | Full channel recall + onboard power soak attenuation. |
| **ENGL (Powerball / Savage / Ironball)** | Program Change (PC) | Channel 1/2/3/4 + Master A/B switching. |
| **Revv Generator (120 / 100P / 100R)** | Program Change (PC) | Clean, Crunch, Purple (high-gain), Red (modern lead). |

---

## 4. Configuring Scene-Based MIDI Out in UltraRig

In the UltraRig Web Editor (`web\index.html`), configure each **Scene** to transmit a custom MIDI message when engaged:

### Real-World 4-Scene Hybrid Setup:

* **Scene 1: Sparkle Clean**
  * *Digital FX:* Compressor ON, Analog Chorus ON, Plate Reverb ON, NAM Amp bypassed.
  * *MIDI Out Command:* Transmit **PC 1** on Channel 1 $\to$ Sets amplifier to **Clean Channel**.
* **Scene 2: British Crunch**
  * *Digital FX:* Noise Gate ON, subtle Tape Delay, NAM Amp bypassed.
  * *MIDI Out Command:* Transmit **PC 2** on Channel 1 $\to$ Sets amplifier to **Crunch Channel**.
* **Scene 3: Searing Lead Solo**
  * *Digital FX:* Digital Delay (350 ms, 30% mix) ON, Hall Reverb ON, Volume Boost (+3 dB).
  * *MIDI Out Command:* Transmit **PC 3** on Channel 1 $\to$ Sets amplifier to **High-Gain Lead Channel** + engages amp Solo Master Volume.
* **Scene 4: Ambient Swells**
  * *Digital FX:* Shimmer Reverb (6.0s decay) ON, dotted-eighth Delay ON.
  * *MIDI Out Command:* Transmit **PC 1** on Channel 1 $\to$ Returns amplifier to **Clean Channel**.

---

## 5. Synchronization & Relay Pop Prevention

* **Timing & Zero Latency:** Because UltraRig processes scene parameter changes in RAM with **0 ms latency**, the digital effect change and the amplifier's relay click happen simultaneously without phase lag.
* **Muting Relay Clicks:** Some tube amplifiers produce an audible mechanical or electrical "click" when switching high-gain channels. Engaging UltraRig's **Noise Gate** at the front of the chain attenuates switching transients seamlessly.
* **Channel Matching:** Ensure UltraRig's MIDI transmit channel matches the physical amplifier's MIDI receive channel (typically set to Channel 1 or OMNI).
