# UltraRig for M-VAVE Tank-G v2

UltraRig is an alternative firmware for the **M-VAVE Tank-G v2** guitar multi-effects pedal: NAM (Neural Amp Modeler) A2-Lite captures,
an editable effects chain, cabinet IRs, presets with snapshots, a tuner, and a control page that runs in your browser.

> **Status: closed alpha.** We are checking, pedal by pedal, that the installation works before anyone installs it.
> UltraRig is **not affiliated with or endorsed by M-VAVE / Cuvave / Sinco or JieLi**. "M-VAVE" and "Tank-G" are trademarks of their owners
> and are used here only to name the compatible hardware.

## Step 1 (now): the pre-install check

Before installing anything, run the **UltraRig Check** on your pedal. It is **read-only**: it goes through every step of the installer
except erasing or writing the pedal's memory, so it cannot change, damage or "brick" the pedal. It takes about 30 seconds.

**Any Tank-G can run it.** UltraRig supports the Tank-G **v2** with factory firmware 96 or 97 for now. On any other pedal (a Tank-G v1,
an older firmware...) the check does not enter the bootloader and does not read the memory: it only records what Windows knows about the
pedal (verdict NOT_SUPPORTED). Please send that report too: it helps us add support for more pedals.

**You need:** a Tank-G, Windows 10 or 11, and a USB **data** cable.
Connect the pedal directly to the computer (no hub), close M-EFCS, and unplug any other USB MIDI or USB audio device.

1. Download `UltraRig-check1.2-win.zip` from the [check release](../../releases/tag/check1) and unzip it. Keep the unzipped folder together:
   `UltraRig-Check.exe` needs the `_internal` folder next to it.
2. Read `README-CHECK.txt` inside (2 minutes), then double-click `UltraRig-Check.exe`.
3. At the end a window opens with the report selected: `UltraRig-check-<date>-<id>.json`.
4. Send that **one file**: open a [Check report issue](../../issues/new?template=check-report.yml) and drag the file into it.

**If the pedal does not restart by itself** after the check (it stays dark or silent, or Windows still shows a "WL82 UBOOT" drive):
its memory was never written, so nothing is lost.
1. Switch the pedal **off with its power switch**, wait 10 seconds, and switch it on again.
2. If it still does not turn on: unplug the computer's cable, plug a **USB-C charger** into the pedal's USB port and switch it on again.
   This resets the pedal and it starts normally. Then reconnect it to the computer.

**Never send the `backup_<date>` folder** that the check also creates in `Documents\tankg_installer`: it is a full copy of your pedal's
memory with data unique to your unit. Keep it safe; it is your way back to the factory state after installing UltraRig.

## Step 2 (later): installation

When your report says the pedal is ready, you will get the installer. It makes a full backup first, writes only the application area of the
pedal's memory, and can restore the factory firmware from that backup.

## What the check looks at

The pedal's identity and firmware version, the USB connection (direct port vs. hub), entering the chip's built-in bootloader, reading the
whole memory twice (the two reads must match), the boot loader and factory firmware against known fingerprints, a simulation of the install
on your own pedal's memory (which areas would be written), and the return to the factory firmware. The report contains the results and
timings, your Windows version and a short ID derived from the pedal's serial number. It contains no memory dump and no personal files or paths.

## License

UltraRig is free for **personal, non-commercial use** under the [PolyForm Noncommercial License 1.0.0](LICENSE.md): you may not sell the
firmware or pedals with it installed. It comes **with no warranty of any kind**; installing a non-official firmware may void your warranty.
Third-party components keep their own licenses: see [NOTICE.md](NOTICE.md). The source code is not published at this time.
