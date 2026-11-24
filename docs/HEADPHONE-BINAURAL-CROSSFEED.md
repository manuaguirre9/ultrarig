# Guia de Processamento Psicoacústico Binaural Crossfeed e Prática com Fones no UltraRig

Este documento estabelece os fundamentos psicoacústicos, equações de retardo e filtragem espectral craniana, eliminação de fadiga auditiva e calibração de estéreo tridimensional (*out-of-head localization*) através do algoritmo **Binaural Crossfeed** no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

Praticar guitarra ou baixo elétrico em fones de ouvido durante longas sessões noturnas é uma necessidade universal para músicos modernos. No entanto, tocar diretamente em fones com isolamento convencional gera um fenômeno auditivo desconfortável e antinatural: o som parece estar confinado "dentro do crânio" do músico (*in-the-head localization*). Isso causa rápida fadiga auditiva (*listener fatigue*), dor de cabeça, perda de julgamento de frequências e perda da sensação de ar e dinâmica que um amplificador real produz em uma sala.

---

## 1. A Psicoacústica: Por Que Fones Convencionais Causam Fadiga?

### Escuta no Espaço Livre (Alto-Falantes Reais) vs. Fones de Ouvido Isolados

```
     ESCUTA NATURAL EM SALA (ALTO-FALANTES)                    ESCUTA CONVENCIONAL EM FONES
   ┌─────────┐                 ┌─────────┐              ┌──────────────────────────────────────┐
   │ Caixa L │                 │ Caixa R │              │ Fone Esquerdo        Fone Direito    │
   └────┬────┘                 └────┬────┘              └───────┬──────────────────────┬───────┘
        │   \                   /   │                           │                      │
        │    \                 /    │                           │                      │
        │     \               /     │                     100% ISOLADO           100% ISOLADO
        │      \             /      │                           ▼                      ▼
        ▼       ▼           ▼       ▼                   [ Ouvido E ]           [ Ouvido D ]
   [Ouvido E] [Ouvido D] [Ouvido E] [Ouvido D]          (Sinal L puro)         (Sinal R puro)
   (Direto)   (Atrasado  (Atrasado (Direto)                     │                      │
               + Filtro   + Filtro                              └──────────┬───────────┘
               Cabeça)    Cabeça)                                          ▼
                                                              [ ILUSÃO DENTRO DO CRÂNIO ]
                                                               (Fadiga em 30-45 minutos)
```

No mundo acústico real, quando um som é gerado à sua esquerda:
1. **ITD (*Interaural Time Difference*)**: O som atinge o ouvido esquerdo primeiro. Para contornar a cabeça humana (diâmetro médio de 18 a 21 cm) e alcançar o ouvido direito, ele viaja aproximadamente 6 a 8 centímetros a mais pelo ar, gerando um atraso físico de **$250\ \mu\text{s}$ a $320\ \mu\text{s}$** ($0.25\text{ ms}$ a $0.32\text{ ms}$).
2. **ILD (*Interaural Level Difference*)**: A cabeça humana funciona como um obstáculo físico (*head shadow*). Frequências graves (abaixo de 500 Hz) contornam a cabeça por difração sem perda de energia. Porém, frequências médias e agudas (acima de 1 kHz) sofrem reflexão e absorção, chegando ao ouvido oposto atenuadas em até $-6\text{ dB}$ a $-12\text{ dB}$.

Em fones de ouvido estéreo diretos, o isolamento entre canais é de 100% (diafonia nula). Quando um efeito estéreo ou delay ping-pong toca apenas no canal L, o ouvido R recebe silêncio absoluto. O cérebro humano interpreta isso como uma anomalia sensorial biológica, gerando tensão neurológica e fadiga.

---

## 2. A Matriz DSP de Crossfeed de Bauer & Chu Moy no UltraRig

Para resolver a fadiga sem alterar a resposta tonal fundamental da guitarra, o UltraRig incorpora a clássica matriz de **Bauer-Chu Moy Crossfeed**, processada digitalmente com fase linear:

```
                           [ SINAL ESTÉREO DE ENTRADA ]
                           │                          │
                    CANAL ESQUERDO (L)         CANAL DIREITO (R)
                           │                          │
                 ┌─────────┴─────────┐      ┌─────────┴─────────┐
                 │                   │      │                   │
                 ▼                   ▼      ▼                   ▼
            [ CANAL L ]          [ FILTRO ] [ FILTRO ]      [ CANAL R ]
              DIRETO             (LP 700Hz) (LP 700Hz)        DIRETO
                 │               (Aten -8dB)(Aten -8dB)         │
                 │                   │      │                   │
                 │                   ▼      ▼                   │
                 │              [ DELAY ]  [ DELAY ]            │
                 │              (275 μs)   (275 μs)             │
                 │                   │      │                   │
                 │                   └─┐  ┌─┘                   │
                 │                     ▼  ▼                     │
                 │                     ╳  ╳  (Cruzamento)       │
                 │                   ┌─┘  └─┐                   │
                 ▼                   ▼      ▼                   ▼
              [ SOMA ] ◄─────────────┘      └─────────────► [ SOMA ]
           (L + R_cross)                                 (R + L_cross)
                 │                                              │
                 ▼                                              ▼
           SAÍDA FONE L                                   SAÍDA FONE R
```

### Parâmetros Fundamentais da Matriz:
- **Frequência de Corte Crossfeed ($f_c$)**: $650\text{ Hz}$ a $750\text{ Hz}$ com curva suave de 6 dB/oct. Graves abaixo de 300 Hz cruzam naturalmente para ancorar a sensação de impacto central; agudos acima de 2 kHz são filtrados para simular a sombra acústica da cabeça.
- **Atraso Interaural ($\Delta t$)**: $270\ \mu\text{s}$ (aproximadamente 13 amostras a $48\text{ kHz}$).
- **Nível de Injeção Cruzada (Crossfeed Amount)**:
  - `Baixo (-14 dB)`: Alívio sutil de fadiga, preservando ampla largura estéreo para modulações.
  - `Médio (-9.5 dB / Modo Padrão)`: Equilíbrio ideal correspondente a monitores de campo próximo a $60^\circ$.
  - `Alto (-6 dB)`: Simulação precisa de caixas acústicas distantes em sala tratada.

---

## 3. Roteamento Completo e Integração com Resposta de Sala (Room IR)

Para transformar a experiência em fones em algo indistinguível de estar sentado em frente a um amplificador valvulado real em um estúdio, combinamos o Crossfeed com um algoritmo de **Early Reflections (Room IR)**:

```
[ ENTRADA GUITARRA ] ──► [ OVERDRIVE / PREAMP ] ──► [ CABINET IR (Falante) ]
                                                            │
                                                            ▼
[ SAÍDA FONES 3.5mm ] ◄── [ CROSSFEED MATRIX ] ◄── [ ROOM REVERB / EARLY REFL ]
 (Out-of-Head Sound)      (Bauer-Moy 270 μs)        (Micro-ambientes de 12 a 20 ms)
```

1. **Cabinet IR**: Modela a resposta do alto-falante microfonado próximo ao cone (*close-mic SM57/R121*).
2. **Early Reflections (Room IR)**: Modela a primeira onda sonora refletida no piso de madeira e nas paredes laterais do estúdio, com duração de $15\text{ ms}$ a $30\text{ ms}$ e mix sutil de $10\%$ a $15\%$.
3. **Crossfeed Matrix**: Posicionado no ponto final da cadeia de fones (antes do DAC de saída). Aplica a física binaural da cabeça no som combinado.

---

## 4. Calibração por Categoria de Fones de Ouvido

Diferentes designs de fones interagem de maneira distinta com o ouvido humano:

```
+---------------------------------------------------------------------------------------+
|                 GUIA DE CALIBRAÇÃO POR DESIGN DE FONE DE OUVIDO                       |
+--------------------+-----------------------------+------------------------------------+
| Categoria de Fone  | Modelos de Referência       | Ajuste Recomendado no UltraRig     |
+--------------------+-----------------------------+------------------------------------+
| Closed-Back        | Audio-Technica ATH-M50x     | Crossfeed Médio (-9.5 dB).         |
| (Fechados)         | Sony MDR-7506, AKG K271     | HPF leve em 35 Hz para controlar   |
|                    | Shure SRH840                | acúmulo de subgrave de cavidade.   |
+--------------------+-----------------------------+------------------------------------+
| Open-Back          | Sennheiser HD600 / HD650    | Crossfeed Baixo (-12 dB).          |
| (Abertos)          | Beyerdynamic DT990 Pro      | Leve reforço de graves (+1.5 dB em |
|                    | Philips Fidelio X2HR        | 80 Hz) para compensar dispersão.   |
+--------------------+-----------------------------+------------------------------------+
| IEMs               | Shure SE215, KZ ZS10 Pro    | Crossfeed Alto (-7.5 dB) + Room    |
| (In-Ear Monitors)  | Moondrop Aria, Sennheiser IE| Reverb em 16%. Elimina a sensação  |
|                    |                             | de som "dentro dos tímpanos".      |
+--------------------+-----------------------------+------------------------------------+
```

---

## 5. Presets de Performance em 4 Cenas (Scenes A/B/C/D)

```
+---------------------------------------------------------------------------------------+
|                  BANCO DE PRESET HEADPHONE IMMERSION: 4 CENAS DE ESCUTA               |
+---------------------+-------------------+---------------------+-----------------------+
| Cena A: Studio      | Cena B: Living    | Cena C: High-Gain   | Cena D: Pure Wide     |
| Control Room        | Room Acoustic     | 4x12 Cranked Room   | Direct DAW Bypass     |
+---------------------+-------------------+---------------------+-----------------------+
```

### Cena A: Studio Control Room (Referência Universal)
- **Objetivo**: Emula com fidelidade cirúrgica a sensação de estar sentado na cadeira do engenheiro de som ouvindo monitores estúdio de campo próximo (*Yamaha NS-10 / Genelec 8040*) angulados a $60^\circ$ e a 1.5 metros de distância.
- **Crossfeed Engine**:
  - `Amount`: -9.5 dB
  - `Cutoff Frequency`: 700 Hz
  - `Delay`: 280 μs
- **Room Modeling**:
  - `Early Reflections Mix`: 12%
  - `Room Size`: 18 m² (Acabamento acusticamente tratado)
  - `Predelay`: 10 ms
- **Uso Recomendado**: Prática geral diária, estudo de solos e ajuste de timbres balanceados.

### Cena B: Intimate Living Room Acoustic
- **Objetivo**: Ambiência calorosa e envolvente para violão acústico de nylon/aço, guitarras semi-acústicas hollowbody e jazz. Elimina a esterilidade do captador piezoelétrico.
- **Crossfeed Engine**:
  - `Amount`: -8.0 dB
  - `Cutoff Frequency`: 650 Hz
  - `Delay`: 300 μs
- **Ambiência / Sala**:
  - `Wood Room Reverb`: Mix 20%, Decay 1.4s, High Damp 4.2 kHz
  - `Air Presence`: +1.0 dB em 10 kHz
- **Uso Recomendado**: Fingerstyle, Bossa Nova, Folk e prática acústica descontraída.

### Cena C: High-Gain 4x12 Cranked Room
- **Objetivo**: Para guitarristas de Rock e Metal que sentem falta da "pressão do ar" de uma caixa 4x12 em volume de palco. Recria a reverberação percussiva da sala vibrando com acordes pesados e palm-mutes sem estourar os tímpanos.
- **Crossfeed Engine**:
  - `Amount`: -10 dB
  - `Cutoff Frequency`: 750 Hz
  - `Delay`: 260 μs
- **Resonador & Dinâmica**:
  - `Cabinet IR`: 4x12 Mesa Rectifier V30 com SM57 + Royer R121
  - `Live Room Reverb`: Mix 15%, Decay 1.1s, Low-Cut 120 Hz (mantém os graves firmes)
- **Uso Recomendado**: Riffs pesados, shredding e ensaio de alta intensidade sem fadiga.

### Cena D: Pure Wide Direct (Bypass de Processamento)
- **Objetivo**: Desativa completamente a matriz de crossfeed e a resposta de sala na saída de fones. O sinal estéreo puro (100% de separação) é entregue sem interferências psicoacústicas.
- **Configurações**:
  - `Crossfeed`: Bypass (0% mix)
  - `Room Reverb`: Off
  - `Stereo Width`: 100% Flat
- **Uso Recomendado**: Gravação direta via áudio USB na DAW, edição cirúrgica de pan estéreo e verificação de fase mono.

---

## 6. Recomendações de Saúde Auditiva

1. **A Regra dos 60/60**:
   - Nunca ultrapasse 60% do volume máximo do fone de ouvido do pedal e faça pausas de 10 minutos a cada 60 minutos de prática contínua.
2. **Preservação de Frequências Médias e Agudas**:
   - Quando o crossfeed está ativo, o cérebro percebe a dinâmica espacial com clareza mesmo em volumes físicos menores. Resista à tentação de aumentar o volume geral para "sentir" o som; a ilusão espacial do UltraRig fornece a sensação de corpo sem necessidade de SPL destrutivo.
