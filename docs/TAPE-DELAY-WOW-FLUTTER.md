# Guia de Modelagem, Acústica de Fita e Roteamento de Tape Delay com Wow & Flutter no UltraRig

Este documento estabelece os fundamentos eletromecânicos, modulações psicoacústicas de velocidade de motor (*Wow & Flutter*), saturação não-linear magnética e degradação espectral acumulativa em circuitos de **Eco de Fita Analógico (*Tape Delay / Space Echo*)** no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

Antes do advento dos chips analógicos BBD de estado sólido e da memória digital moderna, o delay de estúdio e palco era gerado por maquinários eletromecânicos complexos utilizando laços contínuos de fita magnética de 1/4 de polegada (*Maestro Echoplex EP-2 e EP-3, Roland Space Echo RE-201, Watkins Copicat, Binson Echorec*). O charme orgânico e insubstituível do eco de fita reside justamente em suas "imperfeições" físicas: variações mecânicas de velocidade do motor, histerese magnética, saturação harmônica suave e filtragem passa-baixas cumulativa em cada repetição.

---

## 1. A Física Mecânica e Eletromagnética do Eco de Fita

```
+---------------------------------------------------------------------------------------+
|                    DIAGRAMA MECÂNICO DE UM ECO DE FITA ANALÓGICO                      |
|                                                                                       |
|   [ CABEÇA DE APAGAMENTO ] ──► [ CABEÇA DE GRAVAÇÃO ] ──► [ CABEÇAS DE REPRODUÇÃO ]  |
|     (Erase Head 100 kHz)         (Record Head + Bias)         (Playback Heads 1, 2, 3)|
|              ▲                            ▲                               ▲           |
|              └────────────────────────────┴───────────────────────────────┘           |
|                                     │                                                 |
|                        [ LAÇO DE FITA MAGNÉTICA EM LOOP ]                             |
|                                     │                                                 |
|                                     ▼                                                 |
|                          [ CAPSTAN + PINCH ROLLER ]                                   |
|                        (Motor de Tração Eletromecânico)                               |
+---------------------------------------------------------------------------------------+
```

### O Fenômeno de Degradação Cumulativa no Loop de Feedback:
Em um delay digital puro, a repetição nº 10 possui a exata mesma resposta de frequência e dinâmica da repetição nº 1. No eco de fita analógico, a cada ciclo no loop de realimentação (*feedback*):
1. **Perda de Agudos (High-Frequency Damping)**: O sinal sofre atenuação de $-2.5\text{ dB}$ a $-3.5\text{ dB}$ acima de 5 kHz por repetição, decorrente de perdas de gap da cabeça de leitura e dispersão magnética das partículas de óxido de ferro.
2. **Saturação Não-Linear de Fita (Tape Saturation)**: As cristas de sinal que ultrapassam o fluxo magnético de saturação do óxido sofrem ceifamento suave arredondado (*soft compression*), gerando harmônicas pares e ímpares ricas que aquecem o timbre.
3. **Corte Sub-Grave Preventivo (Head Bump & Low-Cut)**: Filtro passa-altas natural em 75 Hz a 90 Hz que impede a sobrecarga do núcleo do transformador de áudio.

---

## 2. A Física das Imperfeições Mecânicas: Wow & Flutter

As flutuações temporais do eco de fita são divididas fisicamente em duas faixas de frequência bem delimitadas:

```
+---------------------------------------------------------------------------------------+
|                       WOW vs. FLUTTER: DINÂMICA DE VELOCIDADE                        |
+---------------------+-------------------+---------------------------------------------+
| Parâmetro           | Faixa de Frequência| Origem Mecânica & Efeito Psicoacústico     |
+---------------------+-------------------+---------------------------------------------+
| WOW                 | 0.5 Hz a 2.0 Hz   | Causado por variações cíclicas lentas na    |
| (Flutuação Lenta)   | (Modulação lenta) | rotação do motor elétrico, desvio no eixo do|
|                     |                   | capstan ou carretel deformado. O efeito     |
|                     |                   | auditivo é uma desafinação suave, ondulante |
|                     |                   | e sonhadora de pitch (*pitch drift/chorus*).|
+---------------------+-------------------+---------------------------------------------+
| FLUTTER             | 15 Hz a 35 Hz     | Causado pelo atrito microscópico da fita    |
| (Tremulação Rápida) | (Micro-oscilação) | raspando contra as guias metálicas e bordas |
|                     |                   | das cabeças magnéticas (*scrape flutter*).  |
|                     |                   | O efeito auditivo é uma leve granulação e   |
|                     |                   | espalhamento aveludado nos agudos.          |
+---------------------+-------------------+---------------------------------------------+
```

No UltraRig, o bloco de tape delay modela **dois geradores de modulação assíncronos**: um LFO de forma de onda quase-aleatória (*randomized sine/drift*) para o Wow e um oscilador de ruído filtrado de alta taxa para o Flutter, garantindo que o movimento nunca soe como um chorus digital repetitivo ou estático.

---

## 3. O Famoso Pré-Amplificador JFET do Echoplex EP-3

Um dos maiores segredos dos timbres de guitarra dos anos 70 (*Jimmy Page, Eddie Van Halen, Brian May*) foi o uso contínuo do **Echoplex EP-3** mesmo com as repetições desligadas. O circuito de pré-amplificação com transistor de efeito de campo (JFET TIS58) adiciona:
- Leve ganho de volume limpo ($+2\text{ dB}$ a $+3.5\text{ dB}$).
- Compressão sutil e musical no ataque da palheta.
- Casamento de impedância que aveluda os médios e amortece a estridência de captadores agudos.

No UltraRig, a emulação `EP-PREAMP (JFET COLOR)` pode ser ativada na entrada do bloco de delay, reproduzindo essa assinatura analógica lendária.

---

## 4. Presets de Performance em 4 Cenas (Scenes A/B/C/D)

```
+---------------------------------------------------------------------------------------+
|                  BANCO DE PRESET ULTRA-TAPE DELAY: 4 CENAS DE PALCO                   |
+---------------------+-------------------+---------------------+-----------------------+
| Cena A: Space Echo  | Cena B: EP-3 Tube | Cena C: Multi-Head  | Cena D: Lo-Fi Dark    |
| RE-201 Atmosphere   | Rockabilly Slap   | Rhythmic Dual Tape  | Degrading Cloud       |
+---------------------+-------------------+---------------------+-----------------------+
```

### Cena A: 1974 Roland Space Echo RE-201 Atmosphere
- **Objetivo**: A lendária ambiência tridimensional do Space Echo com múltiplas cabeças virtuais e reverb de mola analógico embutido.
- **Parâmetros Tape Delay**:
  - `Model`: `SPACE-ECHO RE-201`
  - `Tape Speed / Time`: 420 ms
  - `Wow Depth`: 28% (Oscilação lenta de 0.8 Hz)
  - `Flutter Depth`: 18% (Vibração sutil em 22 Hz)
  - `Tape Saturation / Drive`: 35% (Calor harmônico de fita)
  - `High-Frequency Roll-off`: 4.2 kHz (Cada repetição escurece progressivamente)
  - `Low-Cut`: 100 Hz
  - `Feedback`: 48% (5 a 6 repetições envolventes)
  - `Mix`: 32% Wet
- **Ambiência Embutida**: Spring Reverb Vintage (Mix 18%, Dwell 2.0s).

### Cena B: EP-3 Vintage Rockabilly Slapback
- **Objetivo**: O slapback clássico, seco, percussivo e cheio de atitude para Rockabilly, Country, Classic Rock e solos estilo anos 50/70.
- **Parâmetros Tape Delay**:
  - `Model`: `ECHOPLEX EP-3 SOLID STATE`
  - `Delay Time`: 115 ms (Slapback curto e percussivo)
  - `Wow Depth`: 12%
  - `Flutter Depth`: 10%
  - `EP-Preamp JFET Color`: Ativo (+2.5 dB boost quente)
  - `Tape Saturation`: 45% (Comprime o ataque percussivo)
  - `Feedback`: 12% (Exatamente 1 a 2 repetições limpas)
  - `Mix`: 40% Wet
- **Amp**: Fender Tweed Deluxe ou Bassman levemente estalado.

### Cena C: Multi-Head Rhythmic Dual Tape (Pink Floyd / The Edge)
- **Objetivo**: Uso de 2 cabeças de leitura físicas simultâneas para gerar polirritmia espacial galopante sem embolar o andamento musical (*estilo Run Like Hell / Echoes*).
- **Parâmetros Tape Delay**:
  - `Head 1 Time`: 350 ms (Colcheia normal)
  - `Head 2 Time`: 525 ms (Semínima pontuada, razão 3:2)
  - `Stereo Panning`: Head 1 em 70% L / Head 2 em 70% R
  - `Wow Depth`: 22%
  - `Flutter Depth`: 15%
  - `Feedback`: 55%
  - `Mix`: 40% Wet

### Cena D: Lo-Fi Dark Degrading Tape Cloud
- **Objetivo**: Textura desgastada de fita magnética velha e esticada (*worn tape*), com forte oscilação de afinação, saturação densa e cauda que se funde em uma cama sonora analógica escura.
- **Parâmetros Tape Delay**:
  - `Model`: `WORN TAPE MACHINE`
  - `Delay Time`: 560 ms
  - `Wow Depth`: 65% (Desafinação ondulante e psicodélica)
  - `Flutter Depth`: 50%
  - `Tape Age / Friction`: High
  - `High-Cut Filter`: 2.8 kHz (Repetições extremamente aveludadas e escuras)
  - `Tape Drive / Saturation`: 70% (Distorção harmônica analógica densa)
  - `Feedback`: 72% (Entra em auto-oscilação musical suave sem estourar o sinal)
  - `Mix`: 45% Wet

---

## 5. Dicas Práticas de Ajuste no UltraRig

1. **Auto-Oscilação Segura (*Self-Oscillation*)**:
   - Em delays de fita mecânicos, girar o feedback para 100% gera auto-oscilação infinita. No UltraRig, o limitador analógico interno comprime a cauda oscilante, permitindo criar efeitos de "decolagem de nave espacial" mudando o tempo de delay ao vivo sem clipar os alto-falantes do PA.
2. **Posição em Relação à Distorção**:
   - Posicione o bloco de Tape Delay **após a simulação de amplificador e pré-amp** para obter repetições límpidas e espaciais. Se desejar o som sujo e cru dos primórdios do rock (anos 60), posicione o delay **antes do amplificador** para que as repetições sejam comprimidas e saturadas pelas válvulas virtuais.
