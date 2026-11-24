# Battery Care & Thermal Management Guide for UltraRig

This guide explains battery specifications, charging recommendations, thermal characteristics, and lifespan preservation for the internal lithium-ion battery in the **M-VAVE Tank-G**, **Tank-B**, and related pedals running **UltraRig**.

---

## 1. Battery Specifications & Runtime Expectations

The M-VAVE Tank-G and Tank-B pedals are equipped with an internal **3.7V Lithium-ion (Li-ion)** rechargeable battery (typically $3000\text{ mAh}$ capacity):

| Operating Condition | Expected Runtime | Why? |
|---|---|---|
| **UltraRig (Heavy NAM + IR + Stereo FX)** | **~6 to 8 Hours** | Neural network matrix calculations (NAM A2-Lite) and convolution filtering keep the DSP processor under continuous computational load. |
| **Factory Firmware (Standard DSP)** | **~10 to 12 Hours** | Basic digital modeling uses fewer CPU cycles and less memory bus bandwidth. |
| **Bypass / Low-Complexity Presets** | **~8 to 10 Hours** | Clean signals without heavy modulation or long reverbs consume less current. |

---

## 2. The Alpha 13.1 Battery Calibration Fix

In earlier alpha releases, users frequently noticed that the battery indicator in the Web Editor appeared stuck at **85%**, even after leaving the pedal plugged in overnight.

### Technical Explanation:
* A fully charged Li-ion cell reaches **$4.20\text{V}$**, while its nominal resting voltage is **$3.70\text{V}$**, dropping to a cutoff safety threshold around **$3.40\text{V}$**.
* Earlier builds utilized a linear voltage-to-percentage formula that misjudged the high-voltage plateau of the charging circuit.
* **Starting in UltraRig Alpha 13.1**, an updated battery curve correctly maps the internal ADC voltage readings, allowing a fully charged pedal to display a true **100%** reading.

---

## 3. Safe Charging Practices & Power Sources

### Recommended Power Supplies:
* **Standard 5V USB Chargers:** Use a high-quality 5V USB-A or USB-C power adapter capable of delivering **1.0A to 2.4A** ($5\text{W}$ to $12\text{W}$).
* **USB Powerbanks (Stage Safe):** Powering your pedal via a standard 5V mobile phone powerbank is one of the cleanest, quietest methods for live stage gigs. It completely eliminates 60-cycle AC mains ground loop hum.

### What to Avoid:
* ⚠️ **High-Voltage Fast Chargers:** Avoid proprietary "Quick Charge" (QC 9V/12V) or poorly regulated USB Power Delivery (PD) bricks that fail to negotiate clean 5V output.
* ⚠️ **Noisy Switch-Mode Wall Warts:** Cheap, unshielded phone chargers can inject high-frequency switching whine directly into the guitar audio path.

---

## 4. Thermal Management & Chassis Heat Dissipation

You may notice that after an hour of playing, the bottom and sides of the pedal feel noticeably warm to the touch. **This is completely normal and by design.**

### How Thermal Dissipation Works:
* The Tank series features a heavy **solid aluminum alloy metal enclosure**.
* Rather than using internal cooling fans (which introduce acoustic noise and drain power), the pedal uses its entire metal body as a **passive heatsink** to draw thermal energy away from the JieLi DSP chip, the battery charging controller, and the Bluetooth radio.

### Thermal Best Practices:
1. **Never Leave the Pedal in Direct Sunlight:** During outdoor festival gigs, placing black aluminum pedals directly under blazing sunlight can heat the chassis past $50^\circ\text{C}$ ($122^\circ\text{F}$), triggering thermal safety shutdown. Shade your pedalboard.
2. **Do Not Power On Inside Gig Bags:** Never leave the pedal powered on while enclosed inside a padded gig bag, flight case, or backpack. Airflow around the metal chassis is necessary for passive convection.
3. **Never Store in Hot Vehicles:** Storing lithium-ion batteries inside a car trunk on hot summer days severely degrades battery capacity and accelerates chemical aging.

---

## 5. Long-Term Battery Health & Storage

If you plan to store your pedal for several weeks or months without playing:

* **Ideal Storage State (~50% Charge):** Store the pedal with its battery indicator showing approximately **50% to 60%** charge (around $3.8\text{V}$).
* **Avoid Deep Discharge (0%):** Never store a lithium battery completely depleted. Over months of self-discharge, a battery sitting at 0% can drop below the safety cutoff voltage ($< 2.5\text{V}$), permanently damaging the chemical cells and preventing it from taking a charge.
* **Top-Up Routine:** For pedals in long-term storage, plug them in for 30 minutes every 3 to 4 months to maintain cell health.
