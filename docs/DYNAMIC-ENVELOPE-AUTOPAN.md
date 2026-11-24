# Guia de Roteamento Espacial, Psicoacústica e Auto-Pan Dinâmico Acionado por Envelope no UltraRig

Este documento estabelece as bases de engenharia eletroacústica, leis de distribuição panorâmica (*Pan Laws*), correlação de fase central mono-compatível e modulação estéreo espacial reativa à intensidade de palhetada através do módulo **Dynamic Envelope Auto-Pan** no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

O efeito de Auto-Pan tradicional (modulação periódica da posição estéreo entre os canais esquerdo e direito) é um elemento clássico de produções espaciais (*Jimi Hendrix - "Electric Ladyland", Pink Floyd - "Money", The Who - "Won't Get Fooled Again", Queen*). No entanto, o Auto-Pan convencional baseado apenas em osciladores LFO fixos move o som de forma mecânica e previsível. No UltraRig, a introdução do **Auto-Pan Acionado por Envelope Dinâmico** permite que a própria **força e dinâmica do músico** controlem o movimento do som no espaço estéreo.

---

## 1. Psicoacústica e Leis de Panorâmica (Pan Laws)

Quando um sinal mono é deslocado de uma extremidade à outra no campo estéreo, a potência acústica percebida pelo cérebro humano varia conforme a posição:

```
+---------------------------------------------------------------------------------------+
|                    COMPENSAÇÃO DE POTÊNCIA: A LEI DE PAN (-3 dB)                      |
|                                                                                       |
|  - CANAL ESQUERDO TOTAL (L 100%):  Ganho = 0 dB no canal L  | Ganho = -∞ no canal R   |
|  - CENTRO ACÚSTICO (PAN 0%):       Ganho = -3 dB no canal L | Ganho = -3 dB no canal R|
|  - CANAL DIREITO TOTAL (R 100%):   Ganho = -∞ no canal L    | Ganho = 0 dB no canal R |
|                                                                                       |
|  ──► Por que atenuar -3 dB no centro?                                                 |
|      Porque quando dois alto-falantes reproduzem o mesmo som no centro da sala,        |
|      a pressão acústica somada aumentaria em +3 dB. A lei de pan de -3 dB garante     |
|      que o volume aparente seja perfeitamente uniforme de um lado ao outro!           |
+---------------------------------------------------------------------------------------+
```

### Garantia de Compatibilidade Mono (Mono-Compatibility):
Em muitos palcos de shows, festivais e clubes, o sistema de PA opera com canais somados em mono. Se um efeito estéreo utilizar inversão de fase total de 180° entre L e R para gerar falsa largura, a soma mono causa o desaparecimento completo do sinal (*comb filtering cancelamento*). O algoritmo do UltraRig modula estritamente ganho e tempo em fase linear, garantindo que o sinal mantenha 100% de volume e integridade quando reproduzido em caixas de som mono.

---

## 2. Modos de Operação: LFO Cíclico vs. Envelope Dinâmico de Toque

```
+---------------------------------------------------------------------------------------+
|                 LFO CÍCLICO TRADICIONAL vs. DYNAMIC ENVELOPE AUTO-PAN                 |
+---------------------+-----------------------------+-----------------------------------+
| Abordagem           | Como se Movimenta no Espaço | Aplicação Musical                 |
+---------------------+-----------------------------+-----------------------------------+
| LFO Cíclico         | Oscilação periódica contínua| Psicodelia clássica, arpejos      |
| (Sine / Triangle)   | entre L e R em taxa fixa ou | rítmicos e delays espaciais       |
|                     | sincronizada por Tap Tempo. | com movimento contínuo.           |
+---------------------+-----------------------------+-----------------------------------+
| Dynamic Envelope    | A posição panorâmica é      | A palhetada forte joga a nota para|
| Auto-Pan            | governada pela força com que| a esquerda; conforme ela sustenta,|
| (Toque Dinâmico)    | a palheta ataca as cordas!  | o som migra suavemente ao centro  |
|                     |                             | e viaja para a direita!           |
+---------------------+-----------------------------+-----------------------------------+
```

```
                     [ TRAJETÓRIA DINÂMICA ENVELOPE-PAN ]

 Palhetada Forte (Ataque) ────────► [ CANAL ESQUERDO (L 100%) ]
                                                 │
                                                 ▼
 Nota Sustenta (Decaimento) ──────► [ CENTRO FANTASMA (L/R Equilibrado) ]
                                                 │
                                                 ▼
 Cauda Final da Nota ────────────► [ CANAL DIREITO (R 100%) ]
```

---

## 3. Arquitetura DSP e Roteamento de Sinal no UltraRig

Para que a imagem estéreo tenha máxima clareza e impacto espacial, o bloco Auto-Pan é posicionado na seção final de efeitos:

```
[ GUITARRA ] ──► [ COMP / DRIVE ] ──► [ AMP + CAB IR ]
                                             │
                       ┌─────────────────────┴─────────────────────┐
                       │                                           │
                       ▼                                           ▼
            [ SEGUIDOR DE ENVELOPE ]                     [ STEREO WIDE PANNER ]
            (Mede dinâmica de palheta)                   (Lei de Pan -3 dB Linear)
                       │                                           │
                       └─────────────────────┬─────────────────────┘
                                             │
                                             ▼
                                 [ MODULAÇÃO ESTÉREO L/R ]
                                             │
                                             ▼
                                 [ STEREO DELAY & REVERB ]
                                             │
                                             ▼
                                 [ SAÍDAS MASTER XLR L/R ]
```

---

## 4. Presets de Performance em 4 Cenas (Scenes A/B/C/D)

```
+---------------------------------------------------------------------------------------+
|                 BANCO DE PRESET ULTRA-AUTOPAN: 4 CENAS TRIDIMENSIONAIS                |
+---------------------+-------------------+---------------------+-----------------------+
| Cena A: Psychedelic | Cena B: Velocity  | Cena C: Rhythmic    | Cena D: Ambient       |
| Ping-Pong Sweep     | Orbit L -> R      | 8th-Note Slicer     | Rotary Pan Swell      |
+---------------------+-------------------+---------------------+-----------------------+
```

### Cena A: Psychedelic Ping-Pong Sweep (Jimi Hendrix / Pink Floyd)
- **Objetivo**: Movimento senoidal hipnótico, aveludado e relaxante cruzando os fones de ouvido e o PA estéreo no andamento da música.
- **Módulo Auto-Pan**:
  - `Mode`: `LFO TEMPO SYNC`
  - `LFO Waveform`: Smooth Sine
  - `Rate`: Sincronizado em Semínimas (1/4) via Tap Tempo
  - `Stereo Width`: 100% (Varredura total de L 100% a R 100%)
  - `Pan Law`: -3.0 dB Constant Power
- **Amp / Drive**: Clean Fender Twin Reverb com overdrive suave TS-808.
- **Ambiência**: Tape Delay pontilhado (Mix 22%) e Hall Reverb 2.2s.

### Cena B: Velocity Orbit L -> R (Toque Dinâmico por Palhetada)
- **Objetivo**: O solo viaja tridimensionalmente pelo palco guiado pela intensidade expressiva da mão direita do guitarrista.
- **Módulo Auto-Pan**:
  - `Mode`: `DYNAMIC ENVELOPE TRACKER`
  - `Sensitivity`: 65% (Calibrado para captadores de saída média)
  - `Attack Pan Position`: Hard Left (L 90%)
  - `Release Pan Direction`: Escorrega para o centro e repousa em Hard Right (R 90%)
  - `Slew Smoothing`: 320 ms (Transição orgânica sem pulos)
- **Amp**: Marshall JCM800 lead channel com sustain encorpado.

### Cena C: Rhythmic 8th-Note Slicer Pan (Rock Alternativo / Eletrônico)
- **Objetivo**: Alternância percussiva e recortada em onda quadrada entre as caixas L e R em colcheias sincopadas (*estilo The Who e Radiohead*).
- **Módulo Auto-Pan**:
  - `Mode`: `LFO SYNC HARD SQUARE`
  - `Rate`: Colcheias (1/8)
  - `Transition Smooth`: 5 ms (Corte seco sem estalo de clique digital)
  - `Width`: 100%
- **Amp**: Modern British Crunch com booster de agudos.

### Cena D: Ambient Rotary Pan Swell (Post-Rock e Trilhas Sonoras)
- **Objetivo**: Acordes lentos e passagens com pedal de volume que ondulam em círculos espaciais tridimensionais, alimentando caudas de reverb infinitas.
- **Módulo Auto-Pan**:
  - `Mode`: `LFO ULTRA-SLOW`
  - `Rate`: 0.15 Hz (Varredura ultra lenta de quase 7 segundos por ciclo completo)
  - `Waveform`: Triangle Suave
  - `Stereo Spread`: 85%
- **Ambiência**: Shimmer Reverb espacial (Mix 45%, Decay 6.5s) e Reverse Delay.

---

## 5. Dicas de Otimização e Performance ao Vivo

1. **Monitoração In-Ear Estéreo**:
   - Para guitarristas que utilizam fones in-ear no palco, o Dynamic Auto-Pan abre um espaço acústico tridimensional enorme no centro da mix, permitindo ouvir a voz do vocalista e a caixa da bateria com nitidez cristalina enquanto a guitarra circula ao redor.
2. **Posição em Relação ao Delay**:
   - **Auto-Pan Antes do Delay**: As repetições do delay ecoam no ponto exato onde a nota foi disparada no espaço.
   - **Auto-Pan Depois do Delay**: As repetições viajam juntas pelo campo estéreo, criando uma sensação cinematográfica de movimento panorâmico contínuo.
