# Guia de Engenharia Eletroacústica, Dinâmica e Convolução de IR para Ukulele no UltraRig

Este documento estabelece as diretrizes de engenharia de áudio, filtragem de ruído mecânico de manuseio (*handling noise*), equalização corretiva anti-quack de captadores piezoelétricos e convolução de respostas de impulso (IR) de madeiras nobres (*Acacia Koa e Mogno*) para **Ukuleles Eletroacústicos (Soprano, Concert, Tenor e Barítono)** no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

O ukulele tornou-se um instrumento essencial na música acústica mundial, pop contemporâneo, indie folk e MPB (*Israel Kamakawiwo'ole, Jake Shimabukuro, Eddie Vedder, Billie Eilish, Tiago Iorc*). Por possuir uma escala física reduzida e cordas leves de nylon ou fluorocarbono, sua resposta acústica difere drasticamente da de um violão convencional. Quando amplificado no palco por captadores piezoelétricos sob o rastilho, o instrumento sofre cronicamente com estridência plástica aguda, falta de sustentação natural e suscetibilidade severa a ruídos percussivos de batida de unhas no tampo.

---

## 1. A Física Acústica das Quatro Famílias de Ukulele

```
+---------------------------------------------------------------------------------------+
|                    COMPARAÇÃO ACÚSTICA DAS FAMÍLIAS DE UKULELE                        |
+---------------------+-------------------+---------------------+-----------------------+
| Modelo              | Comprimento Escala| Afinação Padrão     | Frequência Fundamental|
+---------------------+-------------------+---------------------+-----------------------+
| Soprano             | ~13 polegadas     | G4 - C4 - E4 - A4   | Nota mais grave: C4   |
| (O original havaiano| (33 cm)           | (Reentrante: 4ª corda| (~261.6 Hz)!          |
|  caixa minúscula)   |                   |  é mais aguda que C)| Ausência total de sub |
+---------------------+-------------------+---------------------+-----------------------+
| Concert             | ~15 polegadas     | G4 - C4 - E4 - A4   | Nota mais grave: C4   |
| (Maior projeção)    | (38 cm)           | (Reentrante)        | (~261.6 Hz)           |
+---------------------+-------------------+---------------------+-----------------------+
| Tenor               | ~17 polegadas     | G4 - C4 - E4 - A4   | Com Low-G: G3         |
| (Padrão solo/palco) | (43 cm)           | ou Low-G (G3 grave) | (~196.0 Hz)           |
+---------------------+-------------------+---------------------+-----------------------+
| Barítono            | ~19 polegadas     | D3 - G3 - B3 - E4   | Nota mais grave: D3   |
| (Voz grave encorpada| (48 cm)           | (Igual às cordas 1-4| (~146.8 Hz)           |
|  estilo violão)     |                   |  da guitarra)       |                       |
+---------------------+-------------------+---------------------+-----------------------+
```

### O Desafio dos Graves Inexistentes e Ruído Mecânico:
Como a nota mais grave de um ukulele soprano ou concert é o **Dó central ($C_4 \approx 261.6\text{ Hz}$)**, qualquer frequência abaixo de $180\text{ Hz}$ presente no sinal não pertence à música! Toda a energia abaixo dessa faixa consiste exclusivamente em:
- Batidas de unha ou polegar no tampo durante o rasqueado (*strumming*).
- Ruído de atrito da caixa contra o peito ou camisa do músico.
- Zumbidos mecânicos e vibração de cabos.

---

## 2. Roteamento de Sinal e Filtragem Cirúrgica no UltraRig

Para transformar a saída seca e plástica do piezo em um timbre quente, amadeirado e equilibrado, o UltraRig implementa a seguinte arquitetura DSP:

```
[ UKULELE COM PIEZO ]
          │
          ▼
 [ FILTRO HPF CIRÚRGICO ] ──► [ EQUALIZADOR PARAMÉTRICO ] ──► [ COMPRESSOR ÓTICO ]
 (Corte em 180 Hz Soprano/     (De-quack -4.5 dB em 3.2 kHz,   (Nivela strumming
  120 Hz Tenor Low-G)           reforço de corpo em 400 Hz)      e dedilhados)
                                                                       │
                                                                       ▼
 [ SAÍDAS XLR / FONES ] ◄── [ AMBIÊNCIA PLATE / SALA ] ◄── [ WOODEN KOA BODY IR ] ◄─┘
  (Sinal doce e aveludado)   (Decay 1.5s, madeira quente)   (Convolução 2048 amostras)
```

### Blocos Críticos da Cadeia:
1. **Filtro Passa-Altas Cirúrgico (High-Pass Filter - HPF)**:
   - Para Soprano e Concert: Configurar entre **$170\text{ Hz}$ e $200\text{ Hz}$** ($18\text{ dB/octave}$). Limpa 100% dos ruídos mecânicos e batidas de unhas sem perder absolutamente nada do corpo musical das cordas.
   - Para Tenor Low-G e Barítono: Configurar entre **$110\text{ Hz}$ e $130\text{ Hz}$**.
2. **Equalização Corretiva Anti-Quack de Médios-Agudos**:
   - `Corte de Aspereza Piezo`: Atenuação estreita de $-4.0\text{ dB}$ a $-5.5\text{ dB}$ em **$3.0\text{ kHz}$ a $3.4\text{ kHz}$** ($Q: 2.0$). Essa é a região que causa a sensação de "plástico estalado".
   - `Reforço de Ressonância de Madeira`: Suave realce de $+2.5\text{ dB}$ em **$450\text{ Hz} - 650\text{ Hz}$** para dar a sensação de corpo oco de madeira.
   - `Brilho Sedoso de Ar`: Realce tipo high-shelf em **$10\text{ kHz}$** ($+2.0\text{ dB}$) para devolver o brilho cintilante das cordas de fluorocarbono.

---

## 3. Dinâmica: Controle Ótico para Rasqueado e Dedilhado

O ukulele apresenta uma disparidade dinâmica violenta entre o dedilhado com a polpa dos dedos (*fingerpicking*) e o rasqueado percussivo enérgico com a unha (*strumming*):

```
+---------------------------------------------------------------------------------------+
|                    PARÂMETROS DE COMPRESSÃO ÓTICA PARA UKULELE                        |
+---------------------+-------------------+---------------------------------------------+
| Parâmetro           | Ajuste Padrão     | Motivação Acústica                          |
+---------------------+-------------------+---------------------------------------------+
| Attack Time         | 25 ms a 35 ms     | Deixa passar o ataque estalado inicial de   |
|                     |                   | unha, mantendo a sensação rítmica viva.     |
+---------------------+-------------------+---------------------------------------------+
| Release Time        | 120 ms a 150 ms   | Garante recuperação rápida entre batidas    |
|                     |                   | rápidas de rasqueado sem "sufocar" o som.   |
+---------------------+-------------------+---------------------------------------------+
| Ratio               | 2.8:1 a 3.5:1     | Compressão musical transparente.            |
+---------------------+-------------------+---------------------------------------------+
| Threshold           | -20 dBFS          | 3 a 5 dB de redução de ganho no rasqueado.  |
+---------------------+-------------------+---------------------------------------------+
```

---

## 4. Convolução de Resposta de Impulso de Madeira Havaiana (Koa IR)

A madeira Acacia Koa, nativa das ilhas do Havaí, é o padrão-ouro tradicional de construção de ukuleles finos (como *Kamaka, Kanile'a e KoAloha*). Ela oferece médios aveludados, compressão orgânica natural e sobretons doces que nenhum captador sob rastilho consegue captar diretamente.

No UltraRig, o bloco de IR carrega uma resposta de impulso acústica de 2048 amostras a 48 kHz capturada em sala tratada com par casado de microfones condensadores de diafragma pequeno (*Small Diaphragm Condensers - KM184*). Aplicar esse IR restaura a reverberação interna da caixa de madeira, transformando instantaneamente até ukuleles de compensado econômico em instrumentos de boutique.

---

## 5. Presets de Performance em 4 Cenas (Scenes A/B/C/D)

```
+---------------------------------------------------------------------------------------+
|                 BANCO DE PRESET ULTRA-UKULELE: 4 CENAS DE PERFORMANCE                 |
+---------------------+-------------------+---------------------+-----------------------+
| Cena A: Hawaiian    | Cena B: Modern    | Cena C: Ambient     | Cena D: Baritone      |
| Traditional Koa     | Pop Strumming     | Fingerstyle Cloud   | & Low-G Depth         |
+---------------------+-------------------+---------------------+-----------------------+
```

### Cena A: Hawaiian Traditional Koa Warmth (Israel Kamakawiwo'ole)
- **Objetivo**: O som amadeirado, doce, orgânico e relaxante tradicional das ilhas havaianas (*Over the Rainbow*).
- **Módulos DSP**:
  - `HPF`: 180 Hz (18 dB/oct)
  - `Parametric EQ`: Low-Mid +2.0 dB @ 500 Hz, Mid Dip -4.0 dB @ 3.2 kHz, High Shelf +1.5 dB @ 9 kHz
  - `Optical Compressor`: Ratio 3:1, Attack 30 ms, Release 140 ms, Gain Reduction -3.5 dB
  - `Body IR`: Hawaiian Acacia Koa Tenor 2048 pts (Mix 55%)
  - `Warm Wood Room Reverb`: Mix 16%, Decay 1.3s, Pre-delay 20 ms
- **Saída**: XLR Balanceada direta para o sistema de som.

### Cena B: Modern Pop Percussive Strumming (Bases Rítmicas em Banda)
- **Objetivo**: Rasqueado brilhante, firme e perfeitamente nivelado para cortar em mixagens pop modernas com bateria, baixo e sintetizadores.
- **Módulos DSP**:
  - `HPF`: 210 Hz (corte agressivo de batidas mecânicas)
  - `Compressor`: Ratio 4:1, Attack 15 ms, Release 90 ms (segura picos percussivos)
  - `Parametric EQ`: Scoop em 800 Hz (-2 dB), presença aberta em 6 kHz (+2.5 dB)
  - `Body IR`: Modern Spruce/Mahogany Concert (Mix 40%)
  - `Plate Reverb`: Mix 12%, Decay 0.9s

### Cena C: Ambient Fingerstyle Cloud (Jake Shimabukuro / Solos)
- **Objetivo**: Sustentação estelar e expansiva para arranjos instrumentais dedilhados delicados e solos virtuosos.
- **Módulos DSP**:
  - `HPF`: 165 Hz
  - `Compressor`: Ratio 2.5:1, Attack 40 ms, Release 180 ms (máxima preservação de dinâmica)
  - `Stereo Dimension Chorus`: Modulação sutil tridimensional (Mix 18%)
  - `Analog Tape Delay`: Tempo 380 ms, Feedback 28%, Wow 15%, Mix 20%
  - `Lush Hall Reverb`: Decay 2.8s, Mix 28%
  - `Body IR`: Master Grade Koa Tenor (Mix 65%)

### Cena D: Baritone & Low-G Acoustic Depth (Afinações Graves)
- **Objetivo**: Adaptado especificamente para Ukuleles Tenor com corda Low-G (G3) ou Ukuleles Barítonos afinados em D-G-B-E, entregando calor de violão clássico de cordas de nylon.
- **Módulos DSP**:
  - `HPF`: 115 Hz (permite a passagem integral do Ré grave de 146.8 Hz e Sol grave de 196 Hz)
  - `EQ`: +2.5 dB em 220 Hz (ressonância encorpada), notch -4 dB em 2.8 kHz
  - `Optical Compressor`: Attack 35 ms, Release 150 ms
  - `Body IR`: Solid Mahogany Baritone IR (Mix 50%)
  - `Room Reverb`: Mix 15%, Decay 1.4s

---

## 6. Dicas Práticas de Palco para Músicos de Ukulele

1. **Escolha de Cordas (Nylon vs. Fluorocarbono)**:
   - **Cordas de Fluorocarbono**: Tensão ligeiramente maior, ataque brilhante, maior sustentação e afinação mais estável. Casam perfeitamente com a Cena A e C.
   - **Cordas de Nylon Tradicionais**: Som mais macio, doce e aveludado, ideal para MPB e folk acústico.
2. **Prevenção de Realimentação com Correias**:
   - Tocar ukulele sem correia força o músico a pressionar o instrumento contra a caixa torácica, transmitindo vibrações do corpo para o tampo. O uso de uma correia leve estabiliza o instrumento e reduz o ruído de manuseio no palco em até 10 dB.
