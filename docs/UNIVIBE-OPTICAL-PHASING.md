# Guia de Modelagem Ótica, Não-Linearidade de Lâmpada e Roteamento de Uni-Vibe no UltraRig

Este documento estabelece os princípios da eletro-óptica analógica, não-linearidade térmica de filamentos incandescentes, comportamento assimétrico de varredura (*lumpy sweep throb*) e técnicas de roteamento de performance para emulações do clássico **Shin-ei Uni-Vibe (1968)** no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

Desenvolvido originalmente no Japão pelo engenheiro Fumio Mieda para simular os volumosos alto-falantes rotativos Leslie em órgãos eletrônicos, o Uni-Vibe transcendeu seu propósito inicial ao cair nas mãos de gênios da guitarra elétrica como Jimi Hendrix (*Woodstock "The Star-Spangled Banner", Band of Gypsys "Machine Gun"*), David Gilmour (*Pink Floyd "Breathe", "Time"*), Robin Trower (*"Bridge of Sighs"*) e Stevie Ray Vaughan (*"Cold Shot"*). Não se trata de um simples phaser nem de um chorus convencional, mas sim de uma experiência psicoacústica aquática e hipnótica única.

---

## 1. A Física Eletro-Óptica do Uni-Vibe vs. Phasers Convencionais

Ao contrário de phasers analógicos clássicos baseados em chips integrados ou transistores JFET casados (como o MXR Phase 90 ou Electro-Harmonix Small Stone), o circuito do Uni-Vibe original é estritamente discreto e óptico:

```
+---------------------------------------------------------------------------------------+
|                    DIAGRAMA DA CÂMARA ÓPTICA DO SHIN-EI UNI-VIBE                      |
|                                                                                       |
|                    ┌─────────────────────────────────────────────┐                    |
|                    │   TAMPA PROTETORA ESPELHADA (LIGHT SHIELD)  │                    |
|                    │                                             │                    |
|                    │         [ LDR 1 ]         [ LDR 2 ]         │                    |
|                    │             \                 /             │                    |
|                    │              \               /              │                    |
|                    │               ▼             ▼               │                    |
|                    │            [ LÂMPADA INCANDESCENTE ]        │                    |
|                    │            (Filamento de Tungstênio)        │                    |
|                    │               ▲             ▲               │                    |
|                    │              /               \              │                    |
|                    │             /                 \             │                    |
|                    │         [ LDR 3 ]         [ LDR 4 ]         │                    |
|                    │                                             │                    |
|                    └─────────────────────────────────────────────┘                    |
+---------------------------------------------------------------------------------------+
```

### Os Componentes Críticos da Textura Sonora:
1. **Quatro Células LDR de Sulfeto de Cádmio (CdS)**:
   - Quatro fotoresistores dispostos ao redor da lâmpada comandam os 4 estágios de filtro passa-tudo (*all-pass phase stages*). Os fotoresistores de CdS não reagem instantaneamente à luz; possuem uma curva logarítmica lenta de resposta de resistência.
2. **Inércia Térmica do Filamento de Tungstênio (A Origem do "Throb")**:
   - Um LFO comum produz ondas simétricas (senoidais ou triangulares). No Uni-Vibe real, a corrente elétrica aquece a lâmpada incandescente rapidamente, mas o filamento demora muito mais tempo para esfriar e apagar.
   - Esse comportamento físico gera uma **onda de varredura altamente assimétrica**: a subida é rápida e enérgica, enquanto a descida é lenta e elástica. O resultado é o famoso "balanço mancante" (*lumpy throb*), que soa como uma respiração orgânica ou o bater de um coração submerso.

---

## 2. Modos Operacionais: Chorus vs. Vibrato

O Uni-Vibe clássico possui uma chave de modo que altera fundamentalmente a relação de fase do sinal de saída:

```
+---------------------------------------------------------------------------------------+
|                           MODO CHORUS vs. MODO VIBRATO                                |
+---------------------+-------------------+---------------------------------------------+
| Modo Selecionado    | Relação de Sinal  | Comportamento Psicoacústico                 |
+---------------------+-------------------+---------------------------------------------+
| CHORUS              | 50% Sinal Seco    | A interação de fase entre o sinal direto e  |
| (Modo Clássico)     | + 50% Sinal Wet   | o sinal defasado pelos 4 estágios óticos    |
|                     |                   | cria entalhes ressonantes móveis (notches). |
|                     |                   | O som parece girar e ondular em 3 dimensões |
|                     |                   | (*som líquido estilo Hendrix e Gilmour*).   |
+---------------------+-------------------+---------------------------------------------+
| VIBRATO             | 0% Sinal Seco     | Ao eliminar o sinal seco, desaparece o      |
| (Modo Pitch Puro)   | + 100% Sinal Wet  | cancelamento de fase por filtragem em pente.|
|                     |                   | O sinal sofre modulação contínua e pura de  |
|                     |                   | afinação/frequência, gerando uma desafinação|
|                     |                   | ondulante sonhadora e nostálgica.           |
+---------------------+-------------------+---------------------------------------------+
```

---

## 3. Roteamento de Sinal e Posicionamento na Cadeia no UltraRig

O posicionamento do bloco Uni-Vibe no UltraRig define dramaticamente o caráter do timbre:

```
[ GUITARRA ] ──► [ WAH ] ──► [ VINTAGE FUZZ ] ──► [ UNI-VIBE ] ──► [ VALVULADO / IR ]
                             (Fuzz Face Ge/Si)    (Antes do Amp)     (Plexi Saturado)
```

### Pré-Distorção vs. Pós-Distorção:
1. **Antes do Ganho / Pré-Amplificador (Posição Tradicional Vintage)**:
   - É a posição utilizada por Hendrix e David Gilmour. O pulsar assimétrico do Uni-Vibe atinge os estágios de ganho do amplificador, modulando a saturação e a compressão das válvulas a cada ciclo. Quando a lâmpada acende, o ganho estala; quando esfria, o som amortece suavemente.
2. **Após o Ganho / No Loop de Efeitos**:
   - Produz um efeito de chorus/vibrato muito mais límpido, nítido e estéreo, preservando a distorção constante enquanto a imagem espacial viaja entre as caixas.

---

## 4. Presets de Performance em 4 Cenas (Scenes A/B/C/D)

```
+---------------------------------------------------------------------------------------+
|                  BANCO DE PRESET ULTRA-UNIVIBE: 4 CENAS DE PERFORMANCE                |
+---------------------+-------------------+---------------------+-----------------------+
| Cena A: 1969        | Cena B: Breathe   | Cena C: Bridge of   | Cena D: Pure Pitch    |
| Woodstock Throb     | Underwater Swirl  | Sighs Heavy Vibe    | Vibrato Wobble        |
+---------------------+-------------------+---------------------+-----------------------+
```

### Cena A: 1969 Woodstock Lumpy Throb (Jimi Hendrix)
- **Objetivo**: O pulsar visceral, rústico e assimétrico de Jimi Hendrix em *Woodstock* e *Band of Gypsys*.
- **Parâmetros Uni-Vibe**:
  - `Mode`: `CHORUS (Dry/Wet 50/50)`
  - `Rate / Speed`: 1.4 Hz (Velocidade média-rápida pulsante)
  - `Intensity / Depth`: 88%
  - `Lamp Bias (Tensão Central da Lâmpada)`: 52% (Balanço ideal de assimetria térmica)
  - `LDR Thermal Inertia`: High (Emulação da inércia de tungstênio e cádmio)
  - `Pre-Drive`: Fuzz Face Germânio ligado em série
- **Amp**: Marshall Super Lead 1959 Plexi cranked com IR de caixa 4x12 Greenback.

### Cena B: Breathe Underwater Swirl (David Gilmour / Pink Floyd)
- **Objetivo**: Modulação lenta, aveludada, cósmica e aquática de *The Dark Side of the Moon*.
- **Parâmetros Uni-Vibe**:
  - `Mode`: `CHORUS`
  - `Rate / Speed`: 0.65 Hz (Varredura ultra lenta de quase 1.5s por ciclo)
  - `Intensity`: 65%
  - `Lamp Bias`: 45% (Suave, sem picos abruptos)
  - `Mix`: 48% Wet / 52% Dry
- **Ambiência**: Warm Binson Drum Delay (Tempo 380 ms, Feedback 30%) + Plate Reverb suave.

### Cena C: Bridge of Sighs Heavy Vibe (Robin Trower)
- **Objetivo**: Textura espessa, mastigada e cheia de autoridade rítmica com overdrive gordo nos médios.
- **Parâmetros Uni-Vibe**:
  - `Mode`: `CHORUS`
  - `Rate / Speed`: 1.15 Hz
  - `Intensity`: 95% (Máxima excursão óptica)
  - `Lamp Bias`: 60%
  - `Overdrive Pré-Vibe`: Tube Screamer TS-808 moderado
  - `High-Cut Filter`: 5.2 kHz (Elimina ruídos de comutação)

### Cena D: Pure Pitch Vibrato Wobble (Desafinação Orgânica)
- **Objetivo**: Modo Vibrato analógico puro. Desconecta o sinal direto e entrega uma oscilação melancólica de pitch estilo fita magnética velha ou amplificadores Magnatone vintage.
- **Parâmetros Uni-Vibe**:
  - `Mode`: `VIBRATO (100% WET)`
  - `Rate / Speed`: 2.2 Hz
  - `Intensity`: 55%
  - `Mix`: 100% Wet
- **Ambiência**: Spring Reverb curto (Decay 1.4s).

---

## 5. Dicas de Otimização e Controle em Tempo Real

1. **Controle Dinâmico de Velocidade via Pedal de Expressão**:
   - Assim como no pedal de controle de velocidade mecânico original que acompanhava o Shin-ei Uni-Vibe, mapeie o pedal de expressão no UltraRig para o parâmetro `Uni-Vibe Speed`. Isso permite acelerar a pulsação para o refrão e desacelerar nas estrofes em tempo real durante a execução musical.
2. **Casamento com Wah-Wah**:
   - Quando usar Wah junto com Uni-Vibe, posicione o Wah **antes** do Uni-Vibe. O filtro ressonante do Wah alimentará o estágio ótico do Vibe criando sobretons harmônicos espetaculares.
