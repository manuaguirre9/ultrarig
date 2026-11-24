# Connection & Web MIDI / Bluetooth Troubleshooting Guide

This guide provides step-by-step solutions for resolving connectivity issues between your M-VAVE pedal (Tank-G, Tank-B, Black Box) and the **UltraRig Web Editor**, **Desktop App**, or **Android Companion App**.

---

## 1. Web MIDI & Browser Requirements (Computer)

The UltraRig Web Editor (`web/index.html`) relies on the **Web MIDI API** with full System Exclusive (SysEx) permission to communicate bidirectionally with the hardware.

### Compatible Browsers
* ✅ **Google Chrome** (Windows, macOS, Linux, ChromeOS)
* ✅ **Microsoft Edge** (Windows, macOS)
* ✅ **Brave / Opera / Vivaldi** (Chromium-based)
* ❌ **Firefox** (Web MIDI SysEx is not supported)
* ❌ **Safari** (Web MIDI is not supported without third-party extensions)

### Step 1: Check Browser Permissions
When opening `web/index.html`, Chrome or Edge will prompt:
> **"Allow site to control and reprogram MIDI devices?"**

If you accidentally clicked "Block" or didn't see the prompt:
1. In Chrome/Edge, click the **tune/lock icon** next to the URL bar (or go to `chrome://settings/content/midiDevices`).
2. Ensure **MIDI devices** is set to **"Allow"** and **"Turn on SysEx"** is enabled.
3. Refresh the page (`Ctrl + F5` or `Cmd + Shift + R`).

### Step 2: Resolve Exclusive MIDI Port Locking (Windows)
On Windows, the standard USB MIDI driver is **exclusive-access by default**. If another software opens the pedal's MIDI port, the web browser will be completely blocked from seeing it.

* **Close conflicting software before connecting:**
  * Official tools: `M-EFCS`, `M-UPGRADE`
  * DAWs: Reaper, Ableton Live, FL Studio, Cubase, Studio One
  * Virtual MIDI bridges: `teVirtualMIDI`, `loopMIDI`, `MIDI-OX`
* If unsure, unplug the USB cable, plug it back in, and click **"Connect"** in the browser before opening any other audio program.

---

## 2. USB Cable & Port Issues

* **Charge-Only Cables:** Many micro-USB and USB-C cables bundled with phone chargers or headphones only contain power lines (VBUS & GND) and lack data lines (D+ & D-).
  * *Test:* Check Windows Device Manager (`Win + X` $\to$ `Device Manager`). Under **"Sound, video and game controllers"**, you must see `USB-Audio` and `USB-Midi`. If nothing appears when plugging in, swap the cable.
* **USB Hubs:** Unpowered or passive USB splitters can cause voltage drops and SysEx packet corruption during preset transfers.
  * Connect directly to a motherboard rear USB port or laptop port. Avoid front-panel hubs and monitors with built-in pass-throughs.

---

## 3. Bluetooth BLE Troubleshooting (Android App)

The UltraRig companion app (`UltraRig-<version>-android.apk`) connects to the pedal over **Bluetooth Low Energy (BLE)**.

### Crucial Android Settings:
1. **Never Pair Through Android System Settings:**
   * Do **NOT** go to `Android Settings > Bluetooth` and try to pair the pedal there. M-VAVE pedals broadcast two Bluetooth IDs:
     * `Tank-G Audio` (or similar): Classic Bluetooth for streaming music/backing tracks from your phone to the pedal's headphone jack.
     * `UltraRig BLE`: Low Energy MIDI communication for the editor.
   * Only pair **inside the UltraRig app** by tapping the connect icon.
2. **Enable Location Services (GPS):**
   * Android OS security requires the **Location permission** and GPS turned on to scan for nearby BLE beacons. If Location is disabled, the app will scan indefinitely and find no devices.
3. **Grant Nearby Devices Permission:**
   * On Android 12 and newer, ensure `Nearby Devices (Bluetooth)` permission is set to **"Allow"** under `Settings > Apps > UltraRig > Permissions`.

---

## 4. Diagnostic Checklist

| Symptom | Likely Cause | Solution |
|---|---|---|
| Browser says *"No MIDI devices found"* | Exclusive lock by DAW or official software | Close Reaper, M-EFCS, and M-UPGRADE; replug USB cable. |
| Browser finds pedal, but clicking *Connect* times out | SysEx permission disabled in browser settings | Enable SysEx under `chrome://settings/content/midiDevices`. |
| Android app shows blank device list | Location (GPS) turned off | Turn on Location toggle and grant Nearby Devices permission. |
| Pedal disconnects during preset transfer | Bad USB cable or passive USB hub | Connect directly with a shielded high-speed data cable. |
| Windows asks to format drive upon connection | Normal flash-mode behavior | **Click CANCEL.** Never format the drive! |

---

## 5. Exporting Diagnostics for Support

If connection fails repeatedly:
1. In the Web Editor, navigate to **Settings > Pedal > Copy diagnostics**.
2. If the pedal is connected via USB, check Windows PowerShell:
   ```powershell
   Get-PnpDevice -PresentOnly | Where-Object { $_.FriendlyName -match 'MIDI|Audio' }
   ```
3. Attach this output when opening a [Bug report](../../issues/new?template=bug-report.yml).
