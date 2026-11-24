# USB Audio Interface & DAW Recording Guide for UltraRig

This guide explains how to use your M-VAVE pedal (Tank-G, Tank-B, Black Box) running **UltraRig** as a direct **USB Audio Interface** for recording guitars and bass in digital audio workstations (DAWs) like Reaper, Ableton Live, FL Studio, Cubase, Studio One, and Logic Pro.

---

## 1. Hardware USB Audio Specifications

UltraRig acts as a standard **Class-Compliant USB Audio Interface**:

* **Plug-and-Play Compatibility:**
  * **Windows 10 & 11:** Uses standard Microsoft USB-Audio drivers (no proprietary drivers required).
  * **macOS:** Class-compliant CoreAudio support with zero configuration.
  * **Linux:** Supported natively via ALSA / PipeWire / PulseAudio.
  * **Android & iOS:** Supported via OTG adapters for mobile recording apps (GarageBand, BandLab, n-Track).
* **Sample Rate:** **44.1 kHz** and **48 kHz** PCM.
* **Bit Depth:** **24-bit** (dynamic range $> 100\text{ dB}$).
* **Channels:** 2-channel Stereo Output (processed audio from the pedal's master bus).

---

## 2. Low-Latency Driver Setup on Windows (ASIO)

While macOS handles low-latency audio natively through CoreAudio, Windows users should configure an **ASIO driver** to prevent buffer latency and crackles when playing along with software backing tracks:

### Recommended ASIO Solutions:
1. **ASIO4ALL (Most Popular):**
   - Download and install [ASIO4ALL](https://www.asio4all.org).
   - In your DAW audio device preferences, select **ASIO** as the driver type and **ASIO4ALL v2** as the device.
   - Open the ASIO4ALL control panel, enable the pedal's `USB-Audio` device, and set the buffer size to **128 samples** (approx. $3.5\text{ ms}$ latency) or **256 samples** ($5.8\text{ ms}$).
2. **FlexASIO / WASAPI Exclusive:**
   - If you prefer an open-source driver that works without taking exclusive control of other desktop applications (like Spotify or YouTube), install [FlexASIO](https://github.com/dechamps/FlexASIO) configured with the `WASAPI` backend.

---

## 3. Input Gain Staging & Headroom in Your DAW

When recording digital guitar and bass tracks, digital inter-sample clipping produces harsh, unpleasant distortion.

### Dialing in Proper Levels:
* **The Sweet Spot (-18 to -12 dBFS):**
  - In digital audio, $0\text{ dBFS}$ is the absolute ceiling where clipping occurs.
  - Strum your guitar with maximum aggression. The peak meter on your DAW input track should hit between **-18 dBFS and -12 dBFS**.
  - This leaves approximately $12\text{ dB}$ to $18\text{ dB}$ of headroom for dynamic peaks, post-processing plugins, and mastering.
* **Adjusting Output Level from the Pedal:**
  - If your track is clipping, adjust the **Master Level** slider in the UltraRig Web Editor or lower the output knob of your active Cabinet IR block.

---

## 4. Hardware Direct Monitoring vs. Software Monitoring

To achieve zero-latency performance while recording:

* **Hardware Direct Monitoring (Recommended):**
  - Plug your headphones directly into the pedal's $3.5\text{ mm}$ headphone jack.
  - You will hear your guitar tone directly from the DSP processor with **sub-millisecond latency**.
  - **Important:** Disable **Software Monitoring (Track Input Monitoring)** inside your DAW for that track. Leaving both hardware direct monitoring and DAW software monitoring active will produce a phased, comb-filtered "chorused" sound due to tiny computer buffer delays.
* **Computer Playback:**
  - Set your computer's audio output device to the pedal (`Speakers (USB-Audio)`).
  - DAW backing tracks and metronome clicks will stream over the USB cable directly into your headphones, perfectly blended with your live guitar.

---

## 5. Alpha 13.1 Long-Session USB Preset Protection

> [!NOTE]
> **Studio Session Protection:**
> In earlier alpha builds, having a DAW or recording software actively streaming USB audio for hours could delay the pedal's automatic flash-saving routine.
> 
> Starting in **UltraRig Alpha 13.1**, the pedal incorporates an intelligent timer: even during uninterrupted recording sessions spanning multiple hours, the pedal automatically commits your last edited preset to non-volatile flash memory after **10 minutes at most**. You will never lose your dialed-in studio tones if you shut down your PC after a long session.
