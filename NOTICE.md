# NOTICE: UltraRig para el Tank-G v2 de M-VAVE

UltraRig es un firmware alternativo para el pedal multiefectos **Tank-G v2 de M-VAVE** (SoC JieLi AC791N), escrito desde cero sobre el SDK público del fabricante del chip.
**No está afiliado a, ni avalado por, M-VAVE / Cuvave / Sinco ni por JieLi.** "M-VAVE" y "Tank-G" son marcas de sus dueños y se mencionan solo para identificar el hardware
compatible. Instalar este firmware reemplaza el firmware de fábrica y puede anular la garantía; el usuario lo hace bajo su propia responsabilidad. El instalador hace antes un
respaldo completo de la memoria del pedal: consérvelo y **no lo comparta** (contiene datos únicos de su unidad, incluida la zona de configuración Bluetooth).

## Qué se distribuye

UltraRig se distribuye **solo como un paquete de binarios**; el código fuente no se publica. El paquete contiene:

| Archivo | Qué es |
|---|---|
| `UltraRig-Installer.exe` | el instalador para Windows (un programa en Python empaquetado con PyInstaller como carpeta: el .exe y su carpeta `_internal`, que lleva el intérprete de Python, jl-uboot-tool, `wl82loader.bin` y un pequeño programa propio de reinicio para el pedal) |
| `UltraRig-Check.exe` | el chequeo previo de solo lectura (mismo programa que el instalador, limitado a leer: nunca borra ni escribe la memoria del pedal); se distribuye en un paquete aparte con `README-CHECK.txt` |
| `<nombre>_app.bin` y `<nombre>_app.json` | la imagen del área de aplicación del firmware (487.424 B) y su descripción (versión, huella SHA-256) |
| `web/` | la web de control (`tankg.html`, `nam2chip.js` e `index.html`), para abrir localmente en Chrome o Edge |
| `docs/` | los documentos de usuario |
| `LICENSE.md`, `NOTICE.md`, `THIRD_PARTY_LICENSES.md`, `README.txt` | la licencia de UltraRig, este aviso, los textos completos de las licencias de terceros y las instrucciones básicas |

El paquete **no contiene** firmware, software, capturas ni respuestas al impulso de M-VAVE / Sinco, ni volcados de la memoria de ningún equipo.

## Licencia de UltraRig

Copyright (c) 2026 Manuel Aguirre. El instalador, el firmware y la web de UltraRig se distribuyen bajo la **PolyForm Noncommercial License 1.0.0** (texto completo en
`LICENSE.md`): uso no comercial; está prohibido vender el firmware o pedales con el firmware instalado. Se entregan **sin garantía de ningún tipo**. Los componentes de terceros
que van dentro de los binarios conservan sus propias licencias (abajo): la PolyForm no las reemplaza ni las restringe.

## Componentes de terceros incluidos

Textos completos de las licencias en `THIRD_PARTY_LICENSES.md`.

| Componente | Autor / titular | Licencia | Dónde va |
|---|---|---|---|
| **fw-AC79_AIoT_SDK** (SDK AC79 / WL82 de JieLi) | Zhuhai Jieli Technology Co., Ltd. (珠海杰理科技股份有限公司), 2024-2026 | Apache License 2.0 | **En el firmware** (`<nombre>_app.bin`): el firmware se compila como una aplicación del SDK y enlaza sus cabeceras, drivers, sistema operativo, USB y sus librerías precompiladas. Para el firmware se modificaron cuatro archivos del SDK: `setup.c`, `debug.c` e `init.c` (ganchos para la aplicación) y `usb_config.c` (tamaño de los buffers del puerto serie USB). El SDK no trae archivo NOTICE propio. |
| **FreeRTOS V9.0.0** (dentro de las librerías del SDK) | Real Time Engineers Ltd., 2016 | GNU GPL v2 con la excepción de FreeRTOS (según las cabeceras del SDK; ver http://www.freertos.org/a00114.html) | En el firmware, como parte de las librerías precompiladas del SDK. |
| **jl-uboot-tool** (`jltech/`, `scsiio/`) | Andrey Grigoryev (kagaimiq), 2023 | MIT | En el instalador: el protocolo con el modo de carga del chip (cifrado, CRC y comandos SCSI). |
| **wl82loader.bin** | JieLi (cargador de segunda etapa, distribuido con jl-uboot-tool) | **Sin licencia explícita.** No es obra de kagaimiq y la MIT de jl-uboot-tool no lo cubre | En el instalador, sin cambios (SHA-256 `d41da6126760c9d66660bcc0cac8d27d221806c5e369a8036921efe68dca5376`, comprobado antes de usarlo). Se carga en la RAM del pedal durante la instalación; no queda en el pedal. |
| **NeuralAmpModelerCore** (`example_models/A2.nam`) | Steven Atkinson, 2023 | MIT | En el firmware: **la captura que trae por omisión deriva de `A2.nam`** (submodelo A2-Lite de 3 canales, cuantizado). |
| **Python** (intérprete y biblioteca estándar) | Python Software Foundation | PSF License Agreement (y las licencias de los componentes que Python incluye) | En el instalador (PyInstaller lo empaqueta). |
| **python-rtmidi** (con **RtMidi**) | Christopher Arndt, 2012-2023 (RtMidi: Gary P. Scavone, 2003-2019) | MIT (RtMidi: MIT modificada) | En el instalador: detección del pedal de fábrica por MIDI. |
| **pyserial** | Chris Liechti, 2001-2020 | BSD 3-Clause | En el instalador: el puerto serie del pedal con UltraRig. |
| **crcmod** | Raymond L. Buvel, Craig McQueen | MIT | En el instalador (lo usa jl-uboot-tool). |
| **PyInstaller** (cargador del `.exe`) | PyInstaller Development Team | GPL v2 o posterior con una excepción que permite distribuir el cargador con cualquier programa | En el instalador. La excepción no impone condiciones al programa empaquetado. |

La web de control (`tankg.html`, `nam2chip.js`) no usa librerías ni fuentes de terceros: todo el JS, el CSS y los íconos son propios.

## Algoritmos y referencias (sin código de terceros)

- `fx.c` y el afinador implementan en punto fijo algoritmos publicados: Freeverb (Jezar at Dreampoint, dominio público), pasatodos de Schroeder, redes de retardo con
  realimentación (Stautner / Puckette) y YIN (A. de Cheveigné y H. Kawahara). No se copió código.
- El mapa de pines de pedaleras y LEDs, el mapa de la memoria y el protocolo SysEx del firmware de fábrica se obtuvieron por ingeniería inversa del equipo propio del autor, con
  fines de interoperabilidad. No se incluye código ni datos del firmware original.
- Las marcas citadas en la documentación y en los nombres de los efectos para describir su carácter (Marshall, Fender, Mesa, Ibanez Tube Screamer, Klon, Boss, ProCo RAT,
  Electro-Harmonix Big Muff, Dunlop Fuzz Face, TONE3000, NAM, entre otras) son de sus dueños y no implican relación con ellos.
