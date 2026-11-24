# Guia de Modelagem de Bitcrusher, Decimação e Degradação Digital Lo-Fi no UltraRig

Este documento estabelece as diretrizes de processamento digital de sinais (DSP), matemática de ruído de quantização (*bit depth reduction*), reflexão espectral de serrilhamento (*foldover aliasing por sample rate decimation*) e técnicas de roteamento paralelo para efeitos de **Bitcrusher e Degradação Digital Lo-Fi** no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

Enquanto a distorção analógica tradicional baseia-se na física suave e arredondada de válvulas e semicondutores, a distorção digital intencional (*bitcrushing*) explora a destruição geométrica da forma de onda através da redução matemática da resolução e da taxa de amostragem. Consagrada no rock alternativo, indie lo-fi, synth-rock e música industrial (*Nine Inch Nails, Muse - "Plug In Baby" fuzz lo-fi, Radiohead, Jack White, Gorillaz*), essa ferramenta permite transformar guitarras elétricas e baixos em sintetizadores arcade retrô de 8 bits, samplers de hip-hop clássicos de 12 bits e texturas industriais cortantes.

---

## 1. A Matemática da Degradação Digital: Bits vs. Taxa de Amostragem

O bloco de destruição digital do UltraRig atua em dois eixos matemáticos fundamentais:

```
+---------------------------------------------------------------------------------------+
|                    O PLANO DE DEGRADAÇÃO: RESOLUÇÃO vs. TEMPO                         |
|                                                                                       |
|  EIXO VERTICAL (AMPLITUDE): Redução de Resolução (Bit Depth Reduction)                |
|  - Reduz os níveis discretos de voltagem disponíveis para quantizar a onda sonora.    |
|  - A 24 bits: 16.777.216 níveis (pureza cristalina de estúdio).                       |
|  - A 8 bits:  256 níveis (ruído estático de fliperamas arcade e consoles clássicos).  |
|  - A 4 bits:  16 níveis (a onda torna-se uma escada abrupta com fuzz agressivo).     |
|                                                                                       |
|  EIXO HORIZONTAL (TEMPO): Decimação de Amostragem (Sample Rate Decimation)            |
|  - Reduz o número de capturas temporais por segundo de 48 kHz para 1 a 8 kHz.        |
|  - Sem o filtro reconstrutor de Nyquist, frequências agudas são refletidas para trás  |
|    no espectro (foldover aliasing), gerando sobretons inarmônicos e zumbidos robóticos|
+---------------------------------------------------------------------------------------+
```

```
                        [ FORMA DE ONDA DESTRUIDA EM DEGRAUS ]

       Onda Senoidal Pura ────────► [ REDUÇÃO PARA 4 BITS ] ────────► Onda em Degraus
              ~                                                            _┌─┐_
             / \                                                          │   │
            /   \                                                        ─┘   └──
```

### A Fórmula do Ruído de Quantização:
A relação sinal-ruído teórica máxima para áudio linear de $N$ bits é expressa por:
$$\text{SNR}_{\text{max}} \approx 6.02 \times N + 1.76\text{ dB}$$
- **A 12 bits**: $\text{SNR} \approx 74\text{ dB}$ (O timbre aveludado e com pegada percussiva dos clássicos samplers *E-mu SP-1200 e Akai S950*).
- **A 8 bits**: $\text{SNR} \approx 49.9\text{ dB}$ (A textura crua de consoles de videogame *NES e Game Boy*).
- **A 4 bits**: $\text{SNR} \approx 25.8\text{ dB}$ (O piso de ruído e as cristas do sinal fundem-se em um fuzz quadrado abrasivo e destruidor).

---

## 2. A Física do Serrilhamento Espectral (Foldover Aliasing)

O Teorema de Nyquist-Shannon estabelece que qualquer frequência acima da metade da taxa de amostragem ($f > f_s / 2$) não pode ser representada no domínio digital.

Quando o parâmetro `Sample Rate` do UltraRig é reduzido para $4\text{ kHz}$ (limite de Nyquist em $2\text{ kHz}$):
- Uma nota aguda tocada na guitarra a $2.5\text{ kHz}$ sofre reflexão especular no espelho de Nyquist:
  $$f_{\text{alias}} = |4\text{ kHz} - 2.5\text{ kHz}| = 1.5\text{ kHz}$$
- Conforme o guitarrista toca notas que **sobem** de afinação no braço do instrumento, as frequências de aliasing geradas **descem** de afinação na saída! Esse movimento espectral cruzado cria a assinatura futurista e inimitável de sintetizadores analógicos alienígenas.

---

## 3. Roteamento de Sinal e Mixagem Paralela no UltraRig

O erro mais comum ao utilizar bitcrushers é aplicar 100% de sinal processado diretamente no canal mestre, resultando em perda de peso grave e inteligibilidade. O UltraRig implementa uma estrutura em paralelo com filtragem dedicada:

```
                            [ ENTRADA DA GUITARRA / BAIXO ]
                                           │
            ┌──────────────────────────────┴──────────────────────────────┐
            │                                                             │
            ▼                                                             ▼
   [ SINAL DIRETO (DRY) ]                                       [ HPF PRÉ-CRUSH 100 Hz ]
   (Comp ──► Amp ──► Cab IR)                                    (Remove lama de subgraves)
            │                                                             │
            │                                                             ▼
            │                                                 [ BITCRUSHER ENGINE ]
            │                                                 (Bits: 4-12 | Rate: 2-16kHz)
            │                                                             │
            │                                                             ▼
            │                                                 [ TELEPHONE BAND-PASS ]
            │                                                 (Filtro 400Hz a 3.5kHz)
            │                                                             │
            └──────────────────────────────┬──────────────────────────────┘
                                           │
                                           ▼
                               [ MIXAGEM WET / DRY (L/R) ]
                                           │
                                           ▼
                               [ SAÍDAS MASTER DO PEDAL ]
```

---

## 4. Presets de Performance em 4 Cenas (Scenes A/B/C/D)

```
+---------------------------------------------------------------------------------------+
|                 BANCO DE PRESET ULTRA-BITCRUSHER: 4 CENAS LO-FI                       |
+---------------------+-------------------+---------------------+-----------------------+
| Cena A: 8-Bit       | Cena B: Vintage   | Cena C: Telephonic  | Cena D: Glitched      |
| Chiptune Arcade     | 12-Bit SP Sampler | Megaphone Lo-Fi     | Decimator Lead        |
+---------------------+-------------------+---------------------+-----------------------+
```

### Cena A: 8-Bit Chiptune Arcade Fuzz (Nintendo / Muse)
- **Objetivo**: Fuzz sintetizado quadrado e agressivo que transforma a guitarra em uma trilha sonora de fliperama dos anos 1980 (*estilo Muse - Plug In Baby / Daft Punk*).
- **Módulo Bitcrusher**:
  - `Bit Depth`: 6 bits
  - `Sample Rate`: 8.0 kHz
  - `Clock Jitter`: 15% (Leve instabilidade de videogame retro)
  - `Pre-Drive Overdrive`: TS-808 com ganho alto para estender a sustentação dos degraus
  - `Mix`: 65% Wet / 35% Dry (Garante o impacto percussivo da palheta)
  - `Post Low-Pass Filter`: 5.0 kHz (Amortece o chiado agudo irritante)

### Cena B: Vintage 12-Bit SP-1200 Sampler Grit (Hip-Hop 90s / Lo-Fi Beats)
- **Objetivo**: O calor rústico, granulado e crocante dos samplers lendários dos anos 1990 (*E-mu SP-1200, Akai MPC60*), ideal para acordes de neo-soul, batidas lo-fi e guitarras indie.
- **Módulo Bitcrusher**:
  - `Bit Depth`: 12 bits
  - `Sample Rate`: 26.0 kHz
  - `Mix`: 40% Wet / 60% Dry
  - `Tape Saturation`: 30% (Aveluda os degraus de quantização)
- **Amp**: Fender Princeton Tweed limpo com tremolo sutil.

### Cena C: Telephonic Megaphone Lo-Fi (Intro de Rádio / Megafone)
- **Objetivo**: O clássico efeito de introdução de rádio AM antigo, megafone ou alto-falante de brinquedo (*estilo Pink Floyd - Wish You Were Here intro / Green Day*).
- **Módulo Bitcrusher**:
  - `Bit Depth`: 8 bits
  - `Sample Rate`: 12.0 kHz
  - `Band-Pass Telephone Filter`: High-Pass em 450 Hz / Low-Pass em 3.2 kHz (Corta graves e agudos extremos)
  - `Resonance`: 3.5 (Pico estridente nos médios)
  - `Mix`: 100% Wet
- **Uso**: Excelente para iniciar a música e alternar no footswitch para a Cena A ou um amplificador estéreo pesado no refrão.

### Cena D: Glitched Decimator Lead (Aliasing Robótico Extremo)
- **Objetivo**: Decimação brutal de taxa de amostragem gerando sobretons inarmônicos de serrilhamento que descem enquanto o solo sobe (*estilo Nine Inch Nails, Tom Morello e St. Vincent*).
- **Módulo Bitcrusher**:
  - `Bit Depth`: 10 bits
  - `Sample Rate`: 2.4 kHz (Severamente abaixo do limite de Nyquist para excitar o aliasing)
  - `Mix`: 50% Wet / 50% Dry
  - `Stereo Delay`: Tempo 380 ms (Repete os ecos robóticos em ping-pong)
- **Amp**: Modern High-Gain Lead com gate rápido.

---

## 5. Dicas Práticas de Palco para Músicos de Lo-Fi

1. **Gate Transparente na Entrada**:
   - Como a redução de resolução para 6 ou 4 bits eleva o piso de ruído (*noise floor*) para até -30 dBFS, posicione sempre o `Noise Gate` do UltraRig **antes** do bitcrusher. Isso garante silêncio sepulcral nos intervalos entre as notas.
2. **Uso de Pedal de Expressão na Taxa de Amostragem**:
   - Mapear o pedal de expressão para o parâmetro `Sample Rate` permite varrer continuamente de 48 kHz (som normal cristalino) até 1.5 kHz (robô destruído) no clímax do solo.
