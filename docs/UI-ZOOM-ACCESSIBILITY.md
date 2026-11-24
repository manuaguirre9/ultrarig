# UltraRig Editor — Interface Scaling, Accessibility & Tablet Landscape Guide

Introduced in **UltraRig Alpha 13.1**, the UI zoom scaling engine and tablet landscape mode allow musicians, sound engineers, and live performers to customize the graphical interface for any screen size, viewing distance, and performance context.

Whether you are configuring deep parallel routing on an 11-inch netbook, editing tone on an iPad/Android tablet, or monitoring your preset and tuner from 2 meters away on a dark live stage, this guide covers optimal setup and configuration.

---

## 1. Quick Reference: Zoom Controls

| Action | Mouse / Touch Method | Windows / Linux Shortcut | macOS Shortcut |
| :--- | :--- | :--- | :--- |
| **Cycle Zoom Levels** | Click percentage badge in top bar (`75%` → `100%` → `125%` → `150%`) | — | — |
| **Zoom In** | Click `+` button in Zoom menu | `Ctrl` + `+` (or `Ctrl` + `=`) | `Cmd` + `+` |
| **Zoom Out** | Click `-` button in Zoom menu | `Ctrl` + `-` | `Cmd` + `-` |
| **Reset to Default** | Double-click percentage badge | `Ctrl` + `0` | `Cmd` + `0` |

> [!NOTE]
> Zoom preferences are saved locally across sessions in your browser storage or desktop application config file.

---

## 2. Choosing the Right Scaling Level

```
   ┌──────────────────────────────────────────────────────────────┐
   │                  UI Scaling Use Cases                        │
   ├───────────┬──────────────────────────────────────────────────┤
   │    75%    │ Compact laptops (11"–13"), 1366x768, full graph  │
   │   100%    │ Standard FHD (1080p) monitors, default desktop   │
   │   125%    │ 14"–15" QHD / 4K high-DPI, tablet touch targets  │
   │   150%    │ Live stage visibility from 2+ meters, live tuner │
   └───────────┴──────────────────────────────────────────────────┘
```

### 75% Scale: Compact Laptops & Complex Graph Views
* **Ideal for:** 11" to 13" displays (Surface Go, MacBook Air 11", netbooks, 720p/768p portable displays).
* **Benefits:**
  - Displays the entire parallel dual-path routing canvas (Split, Branch A, Branch B, Merge) on a single screen without horizontal scrolling.
  - Keeps all 6 effect parameter knobs visible at once inside the selected block inspector.
* **When to avoid:** High-resolution 4K displays where text becomes uncomfortably small to read.

### 100% Scale: Standard Desktop & Studio Editing
* **Ideal for:** 21" to 27" Full HD (1920×1080) monitors in home and studio recording setups.
* **Benefits:**
  - 1:1 pixel parity with standard UI design layout.
  - Balanced spacing between preset bank selector, scene switches, and parameter faders.

### 125% Scale: Touchscreen Devices & High-DPI Screens
* **Ideal for:** Surface Pro, touch-enabled laptops, and 14"–16" QHD (2560×1440) or 4K displays.
* **Benefits:**
  - **Larger Touch Targets:** Rotary knobs, bypass toggles, and preset selection tiles expand by 25%, drastically reducing accidental mis-taps when using fingers instead of a mouse.
  - Prevents eye strain on high pixel density (Retina/High-DPI) laptop panels.

### 150% Scale: Live Stage Readability (2+ Meters Away)
* **Ideal for:** Placing a laptop, iPad, or 2-in-1 convertible on top of your guitar cabinet, amp head, or on a mic-stand tablet holder during rehearsals and gigs.
* **Benefits:**
  - **Large Font Readability:** The current bank, preset name, and active scene letter (`A`, `B`, `C`, or `D`) can be identified at a glance from standing playing distance (1.5 to 2.5 meters).
  - **High-Visibility Tuner:** Chromatic tuner needle and note letter fill the top area, allowing quick, silent tuning between songs without crouching down to the pedal.
  - **Mute / Bypass Status:** Clear visual distinction between active processing and global mute under aggressive stage lighting.

---

## 3. Tablet Landscape Mode (Alpha 13.1+)

Prior to Alpha 13.1, mobile and tablet browsers defaulted to a stacked single-column layout designed primarily for smartphones. 

In **Alpha 13.1**, UltraRig introduces **Adaptive Tablet Landscape Detection**:

```
 ┌────────────────────────┐         ┌──────────────────────────────────────────────┐
 │                        │         │  UltraRig Editor — Full Desktop Experience   │
 │   Mobile Portrait      │  Rotate │  ┌───────────────┐ ┌──────────────────────┐  │
 │   ┌──────────────┐     │  ─────> │  │ Parallel Graph │ │ Parameter Matrix   │  │
 │   │ Single Block │     │  90 deg │  │ Path A / B    │ │ Gain, EQ, Mix, IR  │  │
 │   │ Inspector    │     │         │  └───────────────┘ └──────────────────────┘  │
 │   └──────────────┘     │         │  [Bank 01] [Scene A] [Scene B] [Scene C]     │
 └────────────────────────┘         └──────────────────────────────────────────────┘
    (Vertical Stacking)                    (Side-by-Side Dual Pane Layout)
```

### Supported Devices & Browsers
* **Apple iPad:** iPad Mini, iPad 10.2", iPad Air, iPad Pro (Safari, Chrome).
* **Android Tablets:** Samsung Galaxy Tab S/A series, Lenovo Tab, Xiaomi Pad (Chrome, Kiwi, Edge).
* **Windows Tablets:** Microsoft Surface Pro / Surface Go (Edge, Chrome).

### How to Trigger Tablet Landscape Mode
1. Ensure your tablet's **Auto-Rotate** lock is disabled in system quick settings.
2. Open UltraRig Web Editor in your browser (e.g., via Web MIDI / Chrome).
3. Rotate the tablet horizontally into **Landscape orientation**.
4. The editor automatically switches from vertical mobile view to the full desktop dual-pane UI.
5. If UI elements appear slightly oversized for your tablet's screen width, tap the zoom indicator in the top toolbar to set it to **75%** or **100%**.

---

## 4. Stage & Accessibility Best Practices

### Stage Lighting & Contrast
* Keep the editor in dark mode to preserve night vision on stage while ensuring bright highlight colors for active blocks (Green for Clean/Delay, Red for High-Gain Amp, Blue for Modulation).
* At 150% zoom, the active scene banner glows brightly, giving immediate confirmation that a foot controller command was received.

### Touchscreen Knob Dragging vs. Scrolling
* On touchscreen tablets, drag rotary knobs vertically (up/down) rather than circular gestures for predictable, fine-grained control.
* Double-tap any knob parameter to reset it to its default unity value.

### Preventing Browser Zoom Interference
* UltraRig's built-in zoom scales the internal application canvas independently from your browser's native zoom.
* If your browser accidentally zooms the entire HTML page (causing outer scrollbars to appear):
  - On Windows/Linux: Press `Ctrl` + `0` in Chrome/Edge to reset browser viewport zoom to 100%, then use UltraRig's internal zoom badge.
  - On iPadOS/Android: Perform a pinch-to-zoom out gesture on the screen edge to reset native viewport scaling.

---

## 5. Troubleshooting & FAQ

### Q1: The zoom badge is cut off or missing from the top bar.
* If your browser window is narrower than 768 pixels, the top toolbar collapses secondary items into a hamburger menu (`⋮` or `☰`). Tap the menu icon to access zoom controls, or rotate your device to landscape mode.

### Q2: Parameter knobs feel sluggish when scaling to 150% on older tablets.
* High zoom factors on low-power mobile GPUs (older tablets from 2018 or earlier) can increase canvas redraw time. Set zoom to **100%** or **125%** and close background browser tabs to maintain 60 FPS slider responsiveness.

### Q3: Does changing the zoom setting affect the pedal's DSP or audio in any way?
* No. Zoom scaling is strictly a graphical rendering property of the Editor application. It does not alter pedal memory, audio buffers, presets, or SysEx MIDI transmission.
