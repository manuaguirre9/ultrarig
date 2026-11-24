# Guia de Roteamento de Sinal Estéreo Wet-Dry-Wet (W/D/W) para Palco e Estúdio no UltraRig

Este documento estabelece a arquitetura acústica, matriz de roteamento físico e digital, eliminação de cancelamentos de fase e configuração de performance da consagrada topologia **Wet-Dry-Wet (W/D/W)** no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

A topologia Wet-Dry-Wet é considerada por engenheiros de áudio e guitarristas profissionais (*Bob Bradshaw, Steve Lukather, Michael Landau, Eddie Van Halen, The Edge*) o "Santo Graal" da amplificação de guitarra em palcos de arena e estúdios de gravação. Ao separar o núcleo dinâmico do timbre seco (*Dry*) dos efeitos espaciais tridimensionais (*Wet*), o sistema elimina para sempre o eterno dilema entre peso rítmico percussivo e grandiosidade espacial.

---

## 1. O Conceito Wet-Dry-Wet vs. Sistemas Estéreo Convencionais

Em configurações estéreo comuns (onde pedais de delay e reverb são inseridos após a distorção ou no loop de efeitos estéreo), o sinal saturado principal é totalmente misturado com os efeitos nos canais esquerdo e direito:

```
+---------------------------------------------------------------------------------------+
|                 SISTEMA ESTÉREO CONVENCIONAL vs. SISTEMA WET-DRY-WET                  |
+---------------------+-----------------------------+-----------------------------------+
| Topologia           | Roteamento Físico           | Comportamento Acústico no Palco   |
+---------------------+-----------------------------+-----------------------------------+
| Estéreo Padrão      | 2 Caixas (Left e Right)     | O ataque da palheta divide-se     |
| (Wet/Wet ou Dry/Dry)| Efeitos e sinal principal   | entre L e R. Repetições de delay e|
|                     | misturados em ambas as      | caudas de reverb mascaram o ponto |
|                     | saídas físicas.             | de impacto percussivo da nota.    |
+---------------------+-----------------------------+-----------------------------------+
| Wet-Dry-Wet (W/D/W) | 3 Caixas / 3 Canais:        | O canal central garante 100% da   |
| Topologia Suprema   | - Centro (DRY): 100% Puro   | pegada, foco e punch do amp.      |
|                     | - Esquerda (WET L): Efeitos | As laterais criam uma muralha de  |
|                     | - Direita (WET R): Efeitos  | ambiência envolvente sem nunca    |
|                     |                             | enfraquecer o ataque central!     |
+---------------------+-----------------------------+-----------------------------------+
```

```
                              [ PALCO WET-DRY-WET ]

            ┌───────────────┐   ┌───────────────┐   ┌───────────────┐
            │  CAIXA WET L  │   │  CAIXA DRY C  │   │  CAIXA WET R  │
            │ (100% Efeitos)│   │ (100% Amp/IR) │   │ (100% Efeitos)│
            │ Delay / Pitch │   │  Sem Delays!  │   │ Reverb / Pitch│
            └───────┬───────┘   └───────┬───────┘   └───────┬───────┘
                    │                   │                   │
                    └──────────────┐    │    ┌──────────────┘
                                   ▼    ▼    ▼
                              [ PÚBLICO / AUDIÊNCIA ]
                     (Localização estéreo ultra-ampla com
                      núcleo percussivo inabalável no centro)
```

---

## 2. As Vantagens Acústicas e Psicoacústicas do W/D/W

1. **Clareza de Ataque e Articulação Imbatíveis**:
   - O falante central nunca é sobrecarregado com repetições emboladas de delay ou caudas de reverb denso. Ele reproduz apenas o transiente puro e a saturação harmônica do amplificador valvulado e do IR de gabinete.
2. **Imunidade a Cancelamentos de Fase na Soma Mono**:
   - Em muitos festivais e casas de shows, os sistemas de PA somam os canais L e R em mono para alimentar caixas de preenchimento (*front-fills, delays laterais e banheiros*). Em sistemas estéreo comuns com modulações de fase ou delay ping-pong, a soma mono causa filtragem em pente severa (*comb filtering*), fazendo a guitarra "desaparecer" da mix. No sistema W/D/W, como o canal DRY é independente, a guitarra mantém 100% de volume e timbre mesmo se os efeitos laterais sofrerem atenuação de fase.
3. **Dimensão Tridimensional sem Perda de Peso**:
   - Os canais laterais utilizam processamento de *Stereo Pitch Detune* ($\pm 9\text{ cents}$) e delays desfasados, gerando a famosa ilusão auditiva de que o som preenche uma sala infinitamente maior do que as dimensões do palco.

---

## 3. Topologia de Roteamento DSP no UltraRig

No processador do UltraRig (Tank-G v1/v2, Tank-B), a topologia W/D/W divide a cadeia após a simulação de amplificador e resposta de impulso (IR):

```
                                [ ENTRADA DA GUITARRA ]
                                           │
                                           ▼
                                 [ COMPRESSOR / DRIVE ]
                                           │
                                           ▼
                                [ AMPLIFICADOR + CAB IR ]
                                           │
                       ┌───────────────────┴───────────────────┐
                       │ (Divisão de Sinal)                    │
                       ▼                                       ▼
             [ RAMO CENTRAL (DRY) ]                  [ RAMO LATERAL (WET) ]
             (100% Sinal Limpo/Amp)                  (Isolação 100% Wet FX)
                       │                                       │
                       │                        ┌──────────────┴──────────────┐
                       │                        ▼                             ▼
                       │               [ STEREO DETUNE ]             [ STEREO DELAYS ]
                       │               (-9 cents L / +9 cents R)     (Ping-Pong / 480ms)
                       │                        │                             │
                       │                        └──────────────┬──────────────┘
                       │                                       ▼
                       │                             [ STEREO LUSH REVERB ]
                       │                             (100% Wet, Predelay 30ms)
                       │                                       │
                       │                                ┌──────┴──────┐
                       │                                ▼             ▼
                       ▼                             [ WET L ]     [ WET R ]
                 [ NÚCLEO DRY ]                         │             │
                       │                                │             │
       ┌───────────────┴───────────────┐                │             │
       ▼                               ▼                ▼             ▼
[ SAÍDA FONE P2 (Aux DRY) ]    [ MATRIZ L/R MIXADA COM IMAGEM W/D/W CENTRAL ]
 (Alimenta Amp de Centro)       (XLR L: Dry + Wet L | XLR R: Dry + Wet R)
```

### Configurações de Conexão Física no UltraRig:
1. **Modo 3-Cabos (Trifônico Completo)**:
   - `Saída XLR Left`: Envia canal **Wet Left** para caixa ativa L ou mesa de som.
   - `Saída XLR Right`: Envia canal **Wet Right** para caixa ativa R ou mesa de som.
   - `Saída de Fone / P2`: Configurada como **Center Dry Out** com sinal mono dedicado do amp/IR para alimentar a caixa central no palco.
2. **Modo 2-Canais Estéreo Pan-Separated (Para gravação e PA Estéreo)**:
   - Quando não houver 3 caixas físicas no palco, o UltraRig projeta o sinal DRY 100% no centro fantasma da imagem estéreo, enquanto expande os efeitos espaciais com abertura de 100% para os extremos L e R, recriando a experiência W/D/W em fones in-ear ou no PA estéreo da casa.

---

## 4. Equalização e Filtragem Dedicada dos Canais Wet

Para que os canais de efeito não concorram com os graves e agudos do canal central:

```
+---------------------------------------------------------------------------------------+
|                    FILTRAGEM DE BANDA DEDICADA NOS CANAIS WET                         |
+---------------------+-------------------+---------------------------------------------+
| Filtro              | Ponto de Ajuste   | Finalidade Acústica                         |
+---------------------+-------------------+---------------------------------------------+
| High-Pass (Low-Cut) | 160 Hz - 200 Hz   | Corta sub-graves dos canais Wet. Todo o     |
| nos Canais Wet      | (12 dB/octave)    | impacto e definição do grave vem do centro. |
+---------------------+-------------------+---------------------------------------------+
| Low-Pass (High-Cut) | 5.5 kHz - 6.5 kHz | Amortece agudos pontiagudos nos efeitos. O  |
| nos Canais Wet      | (12 dB/octave)    | estalo brilhante da palheta fica no centro. |
+---------------------+-------------------+---------------------------------------------+
| Stereo Pitch Detune | L: -9 cents       | Cria separação microtonal estéreo sem       |
|                     | R: +9 cents       | desafinar perceptivelmente a afinação real. |
+---------------------+-------------------+---------------------------------------------+
```

---

## 5. Presets de Performance em 4 Cenas (Scenes A/B/C/D)

```
+---------------------------------------------------------------------------------------+
|                   BANCO DE PRESET ULTRA-WDW: 4 CENAS DE PERFORMANCE                   |
+---------------------+-------------------+---------------------+-----------------------+
| Cena A: Bradshaw    | Cena B: Clean     | Cena C: High-Gain   | Cena D: Ambient       |
| Stadium Crunch      | Spatial Panorama  | Laser Center Lead   | Orbital Immersion     |
+---------------------+-------------------+---------------------+-----------------------+
```

### Cena A: Bradshaw 1980s Stadium Crunch (Lukather / Van Halen)
- **Objetivo**: O som definitivo de guitarras de arena dos anos 80: centro Marshall Plexi estalado com pitch detune estéreo e delay nos lados.
- **Canal Central (Dry)**:
  - `Amp Model`: British Plexi JTM/JCM800 saturado
  - `Cab IR`: 4x12 Greenback (SM57 close-mic)
  - `Wet Effects`: 0% (Dry puro e seco)
- **Canais Laterais (Wet L / Wet R)**:
  - `Stereo Pitch Detune`: L: -8 cents / R: +8 cents (Emulação Eventide H3000)
  - `Dual Delay`: L: 380 ms (Feedback 25%) / R: 510 ms (Feedback 28%)
  - `Plate Reverb`: Mix 100% Wet, Decay 2.2s, Pre-delay 20 ms
  - `High-Cut Wet`: 5.8 kHz

### Cena B: Clean Spatial Panorama (Fender Shimmer Center)
- **Objetivo**: Limpo cintilante com centro encorpado e exuberante panorama estéreo ao redor para dedilhados funk, pop e baladas.
- **Canal Central (Dry)**:
  - `Amp Model`: US Blackface Twin Reverb limpo com compressor ótico no input
  - `Cab IR`: 2x12 Jensen C12N
- **Canais Laterais (Wet L / Wet R)**:
  - `Stereo Dimension Chorus`: Modulação sutil sem oscilação cíclica
  - `Ping-Pong Delay`: Tempo sincronizado em colcheia pontuada (3/16)
  - `Hall Reverb`: Mix 100% Wet, Decay 3.5s

### Cena C: High-Gain Laser Center Lead (Solo Virtuoso Cortante)
- **Objetivo**: Solo de alto ganho com sustentação e corpo que cortam a mixagem como um laser no centro, enquanto delays estéreo se abrem nos lados sem embolar o shredding.
- **Canal Central (Dry)**:
  - `Amp Model`: Modern High-Gain Lead (Soldano / 5150)
  - `Noise Gate`: Ativo no centro (-52 dB)
  - `Cab IR`: 4x12 V30
- **Canais Laterais (Wet L / Wet R)**:
  - `Stereo Ducking Delay`: Tempo 460 ms, Feedback 40%, Ducking -8 dB durante palhetadas rápidas
  - `Stereo Reverb`: Cauda suave de 2.0s filtrada em 6.0 kHz

### Cena D: Ambient Orbital Immersion (Trilhas Sonoras e Post-Rock)
- **Objetivo**: Melodia principal perfeitamente inteligível no centro enquanto nuvens orbitais cósmicas e reversas preenchem a sala lateralmente.
- **Canal Central (Dry)**:
  - `Amp Model`: AC30 Top Boost no ponto de saturação leve
- **Canais Laterais (Wet L / Wet R)**:
  - `Reverse Delay Estéreo`: L: 500 ms / R: 750 ms
  - `Shimmer Reverb 100% Wet`: Decay 8.0s, Octave Pitch +12 semitons
  - `Low-Cut Wet`: 220 Hz (Elimina qualquer lama lateral)

---

## 6. Checklist de Passagem de Som com Técnico de PA

1. **Equilíbrio de Nível entre Dry e Wet**:
   - Ajuste o nível central (DRY) como a referência primária de volume no medidor da mesa de som. Os canais laterais (WET) devem ser configurados entre **$-6\text{ dB}$ e $-10\text{ dB}$** abaixo do canal central para envolver a guitarra sem sobrepô-la.
2. **Pan nos Canais da Mesa**:
   - Instrua o técnico a posicionar o canal Central rigorosamente em `PAN 0 (Centro)`, o canal Wet L em `PAN 100% L` e o canal Wet R em `PAN 100% R`.
3. **Monitoração In-Ear**:
   - Músicos utilizando in-ears desfrutam de um palco silencioso com profundidade espacial cinematográfica, reduzindo o volume necessário de monitoração e prevenindo fadiga auditiva em turnês.
