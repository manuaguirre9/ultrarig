# Training & Converting NAM A2-Lite Models via Google Colab

**UltraRig** uses **NAM (Neural Amp Modeler)** machine learning inference to reproduce the complex non-linear saturation, compression, and harmonic dynamics of tube amplifiers and analog drive pedals.

Because the M-VAVE Tank-G runs on an embedded micro-DSP, standard desktop NAM models (which require heavy GPU or desktop multi-core CPU compute) cannot execute within the pedal's real-time audio cycle budget. UltraRig requires **A2-Lite** models — an optimized, lightweight neural network architecture designed for ultra-low latency real-time DSP.

This guide provides a complete walkthrough for capturing your own physical amplifiers or pedals, training an A2-Lite model using a free **Google Colab** GPU, and importing the resulting `.nam` file into UltraRig.

---

## 1. Architecture Overview: Standard vs. A2-Lite

```
  ┌─────────────────────────────────┬─────────────────────────────────┐
  │     Standard Desktop NAM        │     UltraRig A2-Lite Model      │
  ├─────────────────────────────────┼─────────────────────────────────┤
  │ WaveNet: 16+ Layers / High Chan │ WaveNet: Pruned Lite Topology   │
  │ High CPU/GPU Memory Overhead    │ <2 ms DSP Execution Budget      │
  │ Intended for DAW Plugins        │ Optimized for Tank-G Micro-DSP  │
  │ Rejected by UltraRig Validator  │ 100% Hardware Compatible        │
  └─────────────────────────────────┴─────────────────────────────────┘
```

> [!IMPORTANT]
> The UltraRig editor validates model architecture before sending it to the pedal. Files trained under "Standard" or "Feather" profiles will be rejected with an architecture mismatch error. You must select the **Lite** / **A2-Lite** profile during training.

---

## 2. Equipment & Prerequisites

```
                     ┌─────────────────── DAW / Audio Interface ───────────────────┐
                     │                                                             │
                     │  Track 1: NAM Calibration Signal (v1_1_1.wav)               │
                     │  Track 2: Recorded Amp Output (Clean DI)                    │
                     └───────────────┬─────────────────────────────▲───────────────┘
                                     │ (Line Out)                  │ (Line In)
                                     ▼                             │
                              ┌─────────────┐                      │
                              │  Reamp Box  │                      │
                              └──────┬──────┘                      │
                                     │ (Instrument Level)          │
                                     ▼                             │
                              ┌─────────────┐                      │
                              │ Guitar Amp  │                      │
                              │ or Stompbox │                      │
                              └──────┬──────┘                      │
                                     │ (Speaker Out)               │
                                     ▼                             │
                              ┌─────────────┐                      │
                              │Reactive Load│──────────────────────┘
                              │ Box (DI Out)│
                              └─────────────┘
```

1. **Audio Interface:** Must support 48 kHz / 24-bit recording with at least 1 line output and 1 instrument/line input.
2. **Reamp Box:** Converts low-impedance line-level DAC output from your interface into high-impedance instrument-level signal suitable for an amplifier's front input.
3. **The Target Gear:**
   - **Stompbox / Drive Pedal:** Connect directly from Reamp Box out → Pedal in → Interface line in.
   - **Tube / Solid-State Amp Head:** **DO NOT connect an amp speaker output directly to an audio interface.** You **must** connect the speaker output to a **Reactive Load Box** (e.g., Two Notes Torpedo Captor, Suhr Reactive Load) and take the balanced DI line out to the interface.
4. **NAM Calibration Audio File:** Download the official `v1_1_1.wav` test signal from the [Neural Amp Modeler GitHub repository](https://github.com/sdatkinson/neural-amp-modeler).

---

## 3. Step 1: Capturing the Audio Signal (Reamping)

1. **DAW Session Setup:**
   - Set project sample rate to **48.0 kHz** (or 44.1 kHz), **24-bit**.
   - Create **Track 1**: Import `v1_1_1.wav` (set track output to the physical line out connected to your reamp box). Ensure volume fader is set to unity (`0.0 dB`).
   - Create **Track 2**: Set input to the physical input receiving the signal from your load box or pedal DI.
2. **Gain Staging & Level Check:**
   - Play the test signal through the amp. Watch the recording meter on Track 2.
   - **Crucial Rule:** Ensure the loudest peaks reach between **-6 dBFS and -3 dBFS**. **Never allow the recording to hit 0 dBFS (clipping)**. Digital converter clipping will permanently corrupt neural network training.
3. **Record the Full Pass:**
   - Hit Record. Let the entire 3-minute test sequence run from start to finish without pausing.
   - The test track contains sine sweeps, noise bursts, silence, and guitar DI passages.
4. **Export Clean Output Audio:**
   - Export Track 2 as an uncompressed WAV file: `output.wav` (Mono, 48 kHz, 24-bit).
   - Ensure the exported `output.wav` has the exact same duration and starts at the exact same sample as the input test file.

---

## 4. Step 2: Training on Google Colab (Free GPU)

1. Open the official **Neural Amp Modeler Google Colab Notebook** in your browser.
2. Sign in with any free Google account.
3. Set runtime environment: Click **Runtime** → **Change runtime type** → select **T4 GPU** (Hardware Accelerator).
4. Run the first cell to install PyTorch, CUDA, and the NAM training dependencies.
5. **Upload Audio Files:**
   - Upload `v1_1_1.wav` (input test file) and your recorded `output.wav` to the Colab files sidebar.
6. **Configure Architecture Parameters:**
   - Set model configuration to:
     ```python
     # UltraRig A2-Lite Architecture Settings
     model_type = "WaveNet"
     wavenet_config = "Lite"   # Selects reduced channel & layer budget
     epochs = 200              # 150-250 epochs are sufficient for high accuracy
     batch_size = 16
     learning_rate = 0.004
     ```
7. **Start Training:**
   - Execute the training cell.
   - On a free Google Colab T4 GPU, training an A2-Lite model typically takes **10 to 18 minutes**.

---

## 5. Step 3: Evaluating ESR (Error-to-Signal Ratio)

During training, watch the **ESR (Error-to-Signal Ratio)** metric:

```
  ESR Value       Model Accuracy Assessment
  ──────────────────────────────────────────────────────────
  < 0.008         Exceptional (Indistinguishable from real amp)
  0.008 - 0.025   Great (Studio-grade capture for high-gain/crunch)
  0.025 - 0.050   Acceptable (Good for edge-of-breakup / clean)
  > 0.070         Poor (Phase misalignment, noise, or clipping)
```

If ESR remains high (> 0.07):
* Check if Track 2 clipped during recording.
* Check for ground loop 60 Hz hum on the input line.
* Verify there is no time-alignment latency offset between the input test file and the recorded output.

---

## 6. Step 4: Exporting & Verifying the `.nam` File

1. When training finishes, download the generated model file (e.g., `model.nam`).
2. Open the file in a text editor (e.g., VS Code or Notepad). Verify the JSON header:
   ```json
   {
     "version": "0.5.3",
     "architecture": "WaveNet",
     "config": {
       "layers": 8,
       "channels": 16
     },
     "metadata": {
       "name": "MyCustomAmp_A2Lite"
     }
   }
   ```
3. Ensure the metadata confirms the lightweight channel/layer count suitable for A2-Lite deployment.

---

## 7. Step 5: Importing into UltraRig

1. Connect your M-VAVE Tank-G via USB cable to your computer.
2. Open the UltraRig Web Editor (`web/index.html` in Chrome/Edge) and click **Connect**.
3. Navigate to the **NAM Captures** library tab.
4. Select an empty user slot (or replace an existing slot) and click **Import .nam**.
5. Select your trained `MyCustomAmp_A2Lite.nam` file.
6. UltraRig's file validator will inspect the model tensor dimensions. Once confirmed, it uploads the capture to the pedal flash memory.
7. Assign the capture to a preset block, pair it with a matching 1024-point cabinet IR, and adjust the input trim.

---

## 8. Training Troubleshooting FAQ

### Q1: The Web Editor displays "Unsupported NAM Architecture".
* **Cause:** The model was trained with the desktop `Standard` or `Nano` preset instead of the `Lite` / `WaveNet Lite` topology.
* **Fix:** Re-run the Colab training cell ensuring `wavenet_config = "Lite"` is specified.

### Q2: High-gain captures sound "fuzzy" or "fizzy".
* **Cause:** Amp captures recorded from a load box line out do not have speaker cabinet filtering applied.
* **Fix:** In UltraRig, always place a 1024-point cabinet IR block immediately after the NAM amp block, or enable the Master Low-Pass Filter (LPF) at 6.0 kHz.

### Q3: Google Colab disconnected before training finished.
* **Cause:** Free Google Colab sessions time out if the browser tab is closed or idle.
* **Fix:** Keep the browser tab visible, or reduce training epochs to 150 (which finishes faster and still yields excellent ESR).
