# Guia de Modelagem, Física de Saturação e Roteamento de Fuzz Vintage no UltraRig

Este documento estabelece a engenharia de emulação analógica, casamento de impedância de entrada, dinâmica de limpeza (*guitar volume clean-up*) e compensação harmônica de circuitos clássicos de **Fuzz Vintage** (*Fuzz Face Germânio e Silício, Big Muff Pi e Octave Fuzz Octavia*) no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

O efeito de fuzz foi o pioneiro histórico da distorção extrema na música moderna (*Jimi Hendrix, The Rolling Stones, The Who, Pink Floyd, The Black Keys, Nirvana*). Diferente de overdrives baseados em amplificadores operacionais ou distorções com diodos em hard-clipping suave, o fuzz original operava em circuitos primitivos de 2 a 4 transistores bipolares de junção que cortavam violentamente as cristas da forma de onda em ondas quadradas assimétricas, reagindo visceralmente ao sinal direto da guitarra.

---

## 1. Topologias Analógicas: Germânio vs. Silício vs. Diodo em Cascata

A resposta tímbrica e a dinâmica ao toque de um pedal de fuzz dependem fundamentalmente da física dos semicondutores utilizados:

```
+---------------------------------------------------------------------------------------+
|                 COMPARAÇÃO DE TOPOLOGIAS ANALÓGICAS DE FUZZ CLÁSSICO                 |
+----------------------+-----------------------------+----------------------------------+
| Topologia / Circuito | Transistores / Diodos       | Comportamento Tímbrico & Dinâmico|
+----------------------+-----------------------------+----------------------------------+
| Fuzz Face 1966       | 2x Germânio (AC128/NKT275)  | Soft clipping assimétrico, calor |
|                      | Vbe ~0.2V - 0.3V            | amadeirado, compressão esponjosa,|
|                      | Sensível à temperatura      | limpeza estelar no pot de volume |
+----------------------+-----------------------------+----------------------------------+
| Fuzz Face 1968-70    | 2x Silício (BC108/BC109)    | Hard clipping agressivo, agudos  |
|                      | Vbe ~0.6V - 0.7V            | cortantes, ganho elevado, ataque |
|                      | Estável com temperatura     | percussivo, timbre brilhante     |
+----------------------+-----------------------------+----------------------------------+
| Big Muff Pi 1971-77  | 4 estágios BJT em cascata   | Sustentação infinita tipo violino|
| (Ram's Head / Russo) | com 2 pares de diodos Si    | grave encorpado, scoop em 1 kHz  |
|                      | Filtro passivo tone tilt    | sonoridade densa de parede sonora|
+----------------------+-----------------------------+----------------------------------+
| Octave Fuzz (1967)   | Transformador de entrada    | Oitava superior gerada por       |
| (Tychobrahe Octavia) | + Retificador de 2 diodos Ge| retificação de onda (onda dobra  |
|                      | acoplado a estágio fuzz     | frequência acima do 12º traste)  |
+----------------------+-----------------------------+----------------------------------+
```

### A Física do Germânio vs. Silício no UltraRig
1. **Transistores de Germânio**:
   - Possuem tensão de condução baixa ($\approx 0.2\text{V} - 0.3\text{V}$), gerando uma transição arredondada para o ceifamento da onda. A curva de saturação introduz ricas harmônicas pares (2ª e 4ª ordem), soando orgânica e musical como uma válvula em pré-estresse.
   - Apresentam alta corrente de fuga reversa (*leakage current*), o que em circuitos físicos reais causa instabilidade de ponto de operação (*bias drift*) com mudanças de temperatura externa. No UltraRig, o modelo DSP emula o ponto ideal de bias a $25^\circ\text{C}$ sem a deterioração física.
2. **Transistores de Silício**:
   - Têm limiar de condução abrupto ($\approx 0.65\text{V}$), gerando harmônicas ímpares proeminentes (3ª, 5ª e 7ª ordem) e ceifamento praticamente plano em onda quadrada (*hard squaring*). Cortam com extrema autoridade em mixagens densas de banda.

---

## 2. A Interação de Baixa Impedância e o Efeito "Clean-Up"

Um dos segredos mais valorizados do Fuzz Face analógico original é a sua capacidade mágica de "limpar" (*clean-up*): ao baixar o potenciômetro de volume da guitarra de `10` para `7` ou `8`, o sinal não apenas perde ganho, mas transforma-se em um som cristalino, brilhante e estalado (*glassy clean* estilo *Little Wing* ou *Castles Made of Sand* de Hendrix).

```
[ Captador Passivo Guitarra ]
(Indutância L + Resistência R + Capacitância do Cabo C)
            │
            ▼ (Cabo P10 Passivo Direto)
[ Entrada do Fuzz Face: Impedância Ultra-Baixa (~10 kΩ a 50 kΩ) ]
            │
            ├─► Volume na Guitarra = 10: O circuito do fuzz carrega o captador;
            │   o pico de ressonância dos agudos é amortecido, gerando saturação rica e gorda.
            │
            └─► Volume na Guitarra = 7: A resistência do potenciômetro desacopla o captador;
                o corte de ganho no primeiro estágio BJT interrompe o ceifamento e
                restaura os harmônicos agudos cristalinos com dinâmica intocada.
```

### O Desafio do Buffer e Sistemas Sem Fio (Wireless)
- **A Armadilha do Buffer Ativo (Pre-Fuzz Buffering Trap)**:
  Se houver um pedal com bypass bufferizado de baixa impedância de saída (como pedais BOSS, tuners convencionais ou receptores de sistemas wireless sem fio) antes de um fuzz analógico, a impedância de entrada do fuzz deixa de interagir com o captador passivo. O resultado sonoro é desastroso: agudos estridentes, som estéril como "abelha em lata" e perda total da dinâmica de limpeza no botão de volume.
- **A Solução DSP no UltraRig**:
  No UltraRig, o bloco de drive implementa um algoritmo de impedância virtual adaptativa. Quando configurado em modo `VINTAGE FUZZ (IMPEDANCE COUPLED)`, o algoritmo rastreia o envelope de entrada em tempo real. Uma redução de amplitude na entrada modula simultaneamente o ganho interno e abre um filtro shelving passa-altas complementar, recriando o comportamento idêntico de um captador de bobina simples conectado por cabo passivo de alta qualidade mesmo quando o músico utiliza transmissores sem fio na entrada do pedal Tank-G/B!

---

## 3. Roteamento de Sinal e Modelagem no UltraRig

O roteamento ideal para fuzz vintage no UltraRig requer uma cadeia que compense a energia harmônica agressiva através de equalização pré e pós-saturação e casamento com resposta de impulsos (IR) de alto-falantes vintage:

```
[ Entrada Hi-Z ] ──► [ GATE DUAL ] ──► [ VINTAGE FUZZ ENGINE ] ──► [ PREAMP EQUALIZER ]
   (Direta ou          (Hiss & Buzz       (Ge / Si / Muff / Octave)    (High-Cut 4.5 kHz,
    Wireless)            Taming)                                        Mid-Hump / Scoop)
                                                                               │
                                                                               ▼
[ SAÍDAS BAL / FONE ] ◄── [ AMBIÊNCIA VINTAGE ] ◄── [ CABINET IR (Greenback) ] ◄─┘
 (XLR / P10 Estéreo)       (Plate / Analog Delay)    (Roll-off natural de agudos)
```

### Cuidados Críticos na Cadeia:
1. **Gate Transparente Pré-Fuzz**: Circuitos de fuzz possuem ganho de ruído inerente enorme. Utilize o `Noise Gate` do UltraRig antes do drive com limiar sutil (`Threshold: -58 dB`, `Fast Release`) para eliminar o zumbido de indução de captadores single-coil sem cortar a cauda do sustain.
2. **Casamento com Impulse Responses (IRs)**:
   - **NUNCA** envie fuzz vintage em simulações lineares ou IRs de resposta estendida moderna (como monitores FRFR planos sem filtro).
   - Utilize IRs de caixas clássicas com falantes de 12 polegadas com ímã de alnico ou cerâmico vintage (*Celestion Greenback G12M, Alnico Blue ou Oxford 12T6*). Esses falantes possuem atenuação natural abrupta acima de 4.5 kHz a 5 kHz, eliminando a aspereza digital (*fizz*).
3. **Pós-Filtro Low-Pass e Mid-Sculpting**:
   - Para emular a famosa curva do Big Muff Pi, atenue 1 kHz em -4 dB a -6 dB com Q moderado (0.9) e reforce levemente 100 Hz (+2.5 dB) e 3.5 kHz (+1.5 dB).
   - Para Fuzz Face clássico, aplique um leve reforço em 800 Hz (+2.0 dB) para permitir que o solo salte à frente na mixagem de palco.

---

## 4. Presets de Performance em 4 Cenas (Scenes A/B/C/D)

A arquitetura de 4 cenas do UltraRig permite ao guitarrista transitar instantaneamente entre as quatro encarnações mais emblemáticas da história do fuzz em um único banco:

```
+---------------------------------------------------------------------------------------+
|                 BANCO DE PRESET ULTRA-FUZZ VINTAGE: 4 CENAS DE PALCO                 |
+---------------------+-------------------+---------------------+-----------------------+
| Cena A: 1966 Ge     | Cena B: 1968 Si   | Cena C: 1973 Muff   | Cena D: Octavia Fuzz  |
| Hendrix Clean-up    | Aggressive Bite   | Wall of Stone/Stoner| Riff Solo Psicodélico |
+---------------------+-------------------+---------------------+-----------------------+
```

### Cena A: 1966 Germanium Hendrix Clean-up
- **Objetivo**: Máxima resposta dinâmica; com o volume da guitarra em 7 soa cristalino e estalado; em 10 entrega saturação aveludada, espessa e com compressão orgânica.
- **Drive Module**:
  - `Model`: `FUZZ-FACE-GE` (Emulação AC128)
  - `Fuzz (Gain)`: 88%
  - `Output Volume`: 68%
  - `Input Loading (Virtual Impedance)`: Active (15 kΩ)
  - `Bias Control`: 4.5 V (Ponto central térmico)
- **EQ / Preamp**:
  - `Low-Cut`: 90 Hz (12 dB/oct para evitar embolamento de graves ao tocar acordes)
  - `Mid Band`: +2.0 dB em 750 Hz (Q: 1.2)
  - `High-Cut`: 4.8 kHz (Roll-off analógico doce)
- **Modulação / Ambiência**:
  - `Uni-Vibe / Phaser`: Off (ativável via footswitch auxiliar)
  - `Spring Reverb`: Mix 18%, Dwell 2.0s
- **IR Recomendado**: 4x12 Marshall 1968 com Celestion G12M Greenback 25W (Microfone Shure SM57 a 2 polegadas do cone).

### Cena B: 1968 Silicon Aggressive Bite
- **Objetivo**: Fuzz cortante de silício (BC108) estilo *Live at Pompeii* de David Gilmour e Hendrix no Woodstock. Ataque rápido, agudos brilhantes e sustain violento.
- **Drive Module**:
  - `Model`: `FUZZ-FACE-SI` (Emulação BC108)
  - `Fuzz (Gain)`: 92%
  - `Output Volume`: 72%
  - `Virtual Impedance`: 22 kΩ
  - `Bias Control`: 5.1 V (Ligeiramente mais quente para maior ataque e punch)
- **EQ / Preamp**:
  - `Low Band`: +1.0 dB em 120 Hz
  - `Mid Band`: 0.0 dB plano
  - `High-Cut`: 5.2 kHz
- **Ambiência**:
  - `Tape Delay`: Tempo 380 ms, Feedback 35%, Mix 22% (Warm Tape saturation)
  - `Plate Reverb`: Mix 15%, Decay 1.8s
- **IR Recomendado**: 2x12 Hiwatt Custom com Fane Crescendo Speakers.

### Cena C: 1973 Russian/Op-Amp Wall of Muff
- **Objetivo**: Parede sonora intransponível, graves estrondosos e sustain infinito tipo violoncelo para Stoner Rock, Grunge (*Smashing Pumpkins, Dinosaur Jr.*) e solos melódicos sustentados.
- **Drive Module**:
  - `Model`: `BIG-MUFF-PI` (4 estágios cascateados com diodos de silício)
  - `Sustain (Gain)`: 82%
  - `Tone`: 48% (Balanço entre graves maciços e topo cortante)
  - `Volume`: 65%
- **EQ Pós-Drive**:
  - `Mid Scoop / Mid Boost Option`: 1.0 kHz em -3.5 dB (clássico scooped) ou +2.0 dB (versão "Mid Boost" para cortar na banda ao vivo)
  - `Low-Cut`: 70 Hz (Para evitar oscilações infrassônicas de sub-grave)
  - `High-Cut`: 5.0 kHz
- **Ambiência**:
  - `Analog Reverb / Room`: Mix 14%, Room Size: Medium
- **IR Recomendado**: 4x12 Mesa Oversized ou Marshall 1960B com Celestion Vintage 30.

### Cena D: Octave Fuzz / Tychobrahe Octavia
- **Objetivo**: Oitava aguda por dobra de onda analógica. Perfeito para solos blues-rock sincopados (*Purple Haze solo, Band of Gypsys*). Funciona com máxima intensidade quando tocado acima da 10ª casa com o captador do braço da guitarra e o tom ligeiramente fechado.
- **Drive Module**:
  - `Model`: `OCTAVE-FUZZ` (Circuito retificador dobrador de frequência)
  - `Fuzz Drive`: 75%
  - `Octave Balance`: 80% (Intensidade do harmônico superior)
  - `Volume`: 70%
- **EQ / Shaping**:
  - `Low-Cut`: 100 Hz
  - `Presence / High-Cut`: 4.2 kHz (atenua zumbidos de intermodulação indesejados)
- **Ambiência**:
  - `Slight Slapback Delay`: Tempo 110 ms, Feedback 10%, Mix 18%
- **IR Recomendado**: 4x10 Fender Bassman Tweed ou 2x12 Blackface Twin Reverb.

---

## 5. Dicas de Ouro para Execução ao Vivo e em Estúdio

1. **Seleção de Captadores na Guitarra**:
   - Para timbres estilo Hendrix/SRV com Fuzz Face, utilize sempre o **captador do braço (neck)** com o tom da guitarra entre 6 e 8. Isso suaviza o ataque estridente do piezo ou do primeiro transistor e produz uma ressonância aveludada tipo saxofone tenor.
   - Para o efeito Octavia da Cena D, o captador do braço é obrigatório para enfatizar a onda senoidal fundamental que ativa o retificador de oitava superior.
2. **Posição do Pedal de Wah**:
   - Se utilizar pedal de expressão configurado como Wah no UltraRig, posicione o bloco de Wah **imediatamente antes** do Fuzz. Ajuste o ganho do Wah com moderação para evitar sobrecarregar a entrada do fuzz em frequências ressonantes agudas.
3. **Calibração de Nível LUFS entre Cenas**:
   - Como o fuzz comprime a faixa dinâmica drasticamente elevando a densidade RMS, verifique o volume de saída percebido (*Loudness Matching*) para que as Cenas A, B, C e D fiquem em patamares coerentes de -16 LUFS integrado, evitando sustos de volume durante a troca de cenas no show.
