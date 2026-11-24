# UltraRig Audio Latency & Buffer Diagnostics Guide

Audio latency is the time delay between plucking a guitar or bass string and hearing the processed sound from your speakers or headphones. While UltraRig provides near-instantaneous standalone processing on the pedal's onboard DSP, using the pedal as a USB audio interface with a Digital Audio Workstation (DAW) introduces additional operating system and buffer latencies.

This guide details latency benchmarks, buffer optimization across Windows, macOS, and mobile devices, and diagnostic procedures for eliminating audio dropouts, pops, and comb filtering.

---

## 1. Latency Types: Standalone Hardware vs. USB DAW Round-Trip

```
[ Guitar / Bass ]
       │
       ▼
 ┌───────────┐      [ Analog Path ]
 │ ADC (In)  │ ────> ~0.8 ms
 └─────┬─────┘
       ▼
 ┌───────────┐
 │ DSP Chain │ ────> ~1.5 - 2.0 ms (NAM A2-Lite + 1024-pt IR + FX)
 └─────┬─────┘
       ▼
 ┌───────────┐
 │ DAC (Out) │ ────> ~0.7 ms
 └─────┬─────┘
       │
       ├─────────────────────────────────> [ Standalone Output: ~3.0 - 3.5 ms ] (Headphone / Amp)
       │
       ▼ [ USB Audio Stream ]
 ┌───────────┐
 │ Host USB  │ ────> Input Buffer  (e.g., 128 samples = ~2.9 ms)
 │ Operating │
 │  System   │ ────> DAW Processing Engine
 │ & Drivers │ ────> Output Buffer (e.g., 128 samples = ~2.9 ms)
 └─────┬─────┘
       │
       └─────────────────────────────────> [ DAW Round-Trip (RTL): ~8.5 - 12.0 ms ]
```

### Standalone Pedal DSP Latency (~3.0 – 3.5 ms)
When playing through headphones, a guitar amplifier, or a PA system directly from the pedal's output jacks:
* **Analog-to-Digital Converter (ADC):** ~0.8 ms.
* **DSP Processing Engine:** ~1.5 to 2.0 ms (including full NAM A2-Lite inference, 1024-point FFT convolution cabinet IR, noise gate, and modulation).
* **Digital-to-Analog Converter (DAC):** ~0.7 ms.
* **Perceived Delay:** Equivalent to standing approximately **1 meter (3.3 feet)** from a physical speaker cabinet. This is completely imperceptible to human hearing and feels immediate.

### USB Audio Round-Trip Latency (RTL) (~6.0 – 15.0 ms)
When routing USB audio into a computer DAW, processing it through software plugins, and monitoring the DAW output, total latency includes the host USB driver transfer buffers and DAW engine processing buffers.

---

## 2. USB Buffer Size & Latency Reference Table

At the standard 44.1 kHz sample rate, buffer size determines the trade-off between latency and CPU stability:

| Buffer Size (Samples) | One-Way Buffer Delay | Estimated Round-Trip Latency (RTL) | Recommended Use Case | System Stability |
| :---: | :---: | :---: | :--- | :--- |
| **64** | ~1.45 ms | ~5.8 – 6.5 ms | Real-time software amp sims or live virtual instruments | Requires high-performance PC with low DPC latency |
| **128** | ~2.90 ms | ~8.5 – 10.0 ms | **Sweet Spot:** Tracking guitar in DAW with backing tracks | Excellent balance of feel and stability |
| **256** | ~5.80 ms | ~13.5 – 15.5 ms | Recording in medium-to-large projects with multiple plugins | Rock solid on almost all laptops |
| **512** | ~11.61 ms | ~25.0 – 28.0 ms | Mixing, mastering, and editing sessions (not for live playing) | Zero risk of audio dropouts |
| **1024** | ~23.22 ms | ~48.0 – 55.0 ms | Final rendering and resource-heavy multi-track playback | Noticeable lag if playing live |

---

## 3. Direct Hardware Monitoring vs. Software Monitoring

One of the most frequent audio issues reported by musicians is a "hollow, metallic, or flanging" sound during recording. This is caused by **phase cancellation (comb filtering)**.

```
                  ┌───────── Direct Pedal Output (3.2 ms) ─────────┐
Guitar ──> Pedal ─┤                                                ├──> Headphones (PHASE COMBING!)
                  └─> USB ──> DAW ──> Software Monitor (11.5 ms) ──┘
```

### The Solution:
1. **Disable Software Input Monitoring in your DAW:** In Reaper, Ableton Live, Studio One, Logic, or Cubase, turn off the speaker icon / input monitoring on the active recording track.
2. **Listen Exclusively to UltraRig's Analog Output:** Plug your headphones or studio monitors into the pedal's 3.5 mm headphone out or 6.35 mm output jacks.
3. You will hear zero-latency, full-fidelity tone directly from the pedal while your DAW records the pristine USB audio stream in the background.

---

## 4. Operating System Configuration

### Windows Optimization (ASIO vs. WDM/WASAPI)
> [!IMPORTANT]
> Never use generic Windows audio drivers (MME, DirectSound, or WASAPI Shared) for live tracking. They route through the Windows Audio Engine mixer, adding **30 to 60 ms** of unalterable latency.

1. **Use Dedicated ASIO Drivers:**
   - Install the official OEM M-VAVE USB Audio driver or **ASIO4ALL v2** / **FL Studio ASIO**.
   - In your DAW audio preferences, set **Audio Device Type** to **ASIO**.
2. **DPC Latency Diagnostics (LatencyMon):**
   - If you experience clicks, pops, or audio dropouts even at 256 or 512 samples, background Windows drivers may be stalling the CPU.
   - Download and run **Resplendence LatencyMon**.
   - Common culprits:
     - **Wi-Fi / Network Drivers (`ndis.sys`):** Temporarily disable Wi-Fi while recording live takes.
     - **ACPI Battery Management (`acpi.sys`):** In Windows Power Plan, select **High Performance** or **Ultimate Performance** to prevent CPU core parking and clock throttling.

### macOS Optimization (CoreAudio)
* macOS handles USB audio natively through **CoreAudio** with low-overhead class compliance. No drivers are required.
* Open your DAW preferences, select UltraRig as both **Input Device** and **Output Device**, and set the I/O Buffer Size to **128 samples**.
* Ensure **Drift Correction** is enabled if creating an Aggregate Device combining UltraRig inputs with a separate monitor output.

### Android & Mobile Devices
* UltraRig communicates over USB OTG as a standard USB Audio Class 1.0 device.
* **DAW Apps:** In apps like **Cubasis**, **BandLab**, or **n-Track Studio**, select the **AAudio** driver engine (Android 8.0+) instead of legacy OpenSL ES for the lowest latency.
* **Crucial Bluetooth Rule:** Bluetooth connectivity on UltraRig is exclusively for MIDI and parameters in the Web/Android Editor. **Never attempt to stream wireless audio monitoring over Bluetooth headphones (A2DP).** Bluetooth audio introduces **150 to 300 ms** of latency due to wireless encoding, making real-time instrument playing physically impossible.

---

## 5. DSP Overload & Dropout Diagnostics

If you hear stuttering or audio interruptions while the pedal is operating standalone (disconnected from USB):

1. **Serial NAM Model Stacking:**
   - UltraRig's DSP processor is tailored for **one active NAM A2-Lite model** at a time. Placing two separate NAM blocks simultaneously across parallel branches can exceed the DSP execution budget per audio frame.
   - Use an analog-modeled drive block (Overdrive, Boost, Distortion) in Branch A and a NAM amp capture in the main path.
2. **Convolution IR Truncation:**
   - Ensure custom cabinet IRs do not exceed 1024 points (approximately 21.3 ms at 48 kHz). Longer IRs (2048 or 4096 points) are truncated by the engine or may drop processing cycles.
3. **USB Bus Power Stability:**
   - Always connect the pedal directly to a rear motherboard USB port or a powered USB hub. Unpowered front-panel USB splitters can cause instantaneous voltage drops that trigger audio chip resets.

---

## 6. Pre-Session Latency Checklist

- [ ] USB data cable connected directly to PC/Mac (no passive hubs).
- [ ] DAW audio engine set to **ASIO** (Windows) or **CoreAudio** (macOS).
- [ ] Buffer size configured to **128 samples** for tracking, **512 samples** for mixing.
- [ ] DAW Software Track Monitoring turned **OFF** to eliminate phase comb filtering.
- [ ] Headphones connected directly to UltraRig 3.5 mm output jack for zero-latency monitoring.
- [ ] Windows power scheme set to **High Performance**.
