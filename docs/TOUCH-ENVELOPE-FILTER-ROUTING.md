# Guia de Modelagem, Dinâmica de Toque e Roteamento de Envelope Filter / Auto-Wah no UltraRig

Este documento estabelece as bases de engenharia analógica, física de filtros de estado variável (*State-Variable Filters - SVF*), calibração de sensibilidade dinâmica ao toque e roteamento de efeitos de **Envelope Filter / Auto-Wah** (*modelos estilo Musitronics Mu-Tron III, EHX Q-Tron e MXR Bass Auto-Q*) no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

O envelope filter é um dos efeitos mais viscerais e expressivos da história da guitarra e do contrabaixo (*Stevie Wonder - Higher Ground, Jerry Garcia / Grateful Dead - Estimated Prophet, Bootsy Collins / Parliament-Funkadelic, Flea / Red Hot Chili Peppers - Sir Psycho Sexy, John Mayer - I Don't Trust Myself*). Ao contrário de um pedal tradicional de Wah-Wah controlado pelo movimento do pé, o envelope filter é controlado diretamente pela **força de palhetada e articulação dinâmica dos dedos do músico**, criando uma simbiose orgânica entre técnica instrumental e resposta tímbrica vocal.

---

## 1. Como Funciona a Física do Envelope Filter Analógico

O circuito do clássico Mu-Tron III e de seus sucessores opera através da conversão do envelope de amplitude da corda em uma tensão de controle (CV) que comanda filtros óticos ou resistores controlados por tensão (VCRs / opto-acopladores vactrol):

```
                                [ SINAL DA GUITARRA / BAIXO ]
                                              │
                       ┌──────────────────────┴──────────────────────┐
                       │                                             │
                       ▼                                             ▼
            [ SEGUIDOR DE ENVELOPE ]                      [ FILTRO DE ESTADO VARIÁVEL ]
            (Retificador de Onda Completa                  (2 ou 4 Polos Ressonantes:
             + Integrador RC com Attack/Decay)              Low-Pass, Band-Pass, High-Pass)
                       │                                             ▲
                       ▼                                             │
            [ TENSÃO DE CONTROLE (CV) ] ─────────────────────────────┘
            (Varia dinamicamente de 0V a +5V)
            - Palhetada forte ──► CV sobe ──► Abre a frequência de corte (fc)
            - Nota decai      ──► CV desce ──► Filtro fecha gradualmente
```

### Topologias de Filtragem e Resposta Sonora:
1. **Band-Pass (Passa-Faixa - Modo Clássico Funk)**:
   - Filtra simultaneamente graves e agudos extremos, deixando passar apenas uma janela ressonante móvel de médios. Produz o estalo vocal mais cortante e percussivo (*o clássico som "Quack" ou "Ow"*).
2. **Low-Pass (Passa-Baixas - Modo Baixo Funk / Bootsy)**:
   - Deixa passar todos os graves subjacentes abaixo do ponto de corte enquanto a crista ressonante varre os médios e agudos. É a escolha definitiva para contrabaixo, garantindo que o peso fundamental de 40 Hz - 100 Hz nunca desapareça durante o slap.
3. **High-Pass (Passa-Altas)**:
   - Corta as frequências graves e deixa passar agudos ressonantes. Excelente para texturas psicodélicas finas e efeitos rítmicos percussivos cortantes.

---

## 2. Direção da Varredura: Up-Sweep vs. Down-Sweep

O UltraRig permite alternar a polaridade da tensão de controle, invertendo a direção do movimento do filtro:

```
+---------------------------------------------------------------------------------------+
|                    DIREÇÃO DE VARREDURA: UP-SWEEP vs. DOWN-SWEEP                      |
+---------------------+-------------------+---------------------------------------------+
| Modo de Varredura   | Resposta ao Toque | Características Sonoras e Aplicação         |
+---------------------+-------------------+---------------------------------------------+
| UP-SWEEP            | Palhetada Fraca:  | O som clássico de Auto-Wah: "Wah", "Quack". |
| (Ascendente)        | Filtro fechado no | Começa escuro e abre brilhantemente com a   |
|                     | grave (200 Hz).   | força do ataque. Usado em 90% do Funk, Soul,|
|                     | Palhetada Forte:  | Rock e R&B clássico.                        |
|                     | Abre até 3.5 kHz. |                                             |
+---------------------+-------------------+---------------------------------------------+
| DOWN-SWEEP          | Palhetada Fraca:  | Timbre vocal gutural: "Oww", "Yowww".       |
| (Descendente)       | Filtro aberto no  | Começa brilhante e mergulha nos graves com a|
|                     | topo (3.0 kHz).   | força da palhetada. Lembra sintetizadores   |
|                     | Palhetada Forte:  | analógicos Moog e vocais robóticos.         |
|                     | Mergulha em 180Hz |                                             |
+---------------------+-------------------+---------------------------------------------+
```

---

## 3. Calibração Crítica de Sensibilidade e Prevenção de Clipping

O maior obstáculo enfrentado por músicos ao usar envelope filters digitais é o descompasso entre a saída do captador e o limiar (*threshold*) do seguidor de envelope:

```
[ Captador Single-Coil Vintage (Saída Baixa: ~80 mV) ]  ──► Necessita Sensitivity: 75% a 85%
[ Captador Humbucker Moderno   (Saída Média: ~250 mV) ] ──► Necessita Sensitivity: 50% a 65%
[ Baixo com Pré-Amp Ativo 9V   (Saída Alta:  ~900 mV) ] ──► Necessita Sensitivity: 25% a 40%
```

### O Perigo do Pico de Ressonância (Resonance / Q):
- Quando a ressonância (*Peak / Q*) é ajustada acima de `7.0`, o circuito do filtro introduz um ganho ressonante estreito de até **$+16\text{ dB}$** na frequência de corte!
- Se o ganho geral da cadeia não for devidamente atenuado na saída do bloco (*Output Makeup Level: -4 dB*), esse pico causará saturação digital desagradável (*digital clipping*).
- **Regra de Ouro no UltraRig**: Mantenha o compressor **após** o envelope filter se desejar nivelar o volume final dos picos ressonantes, ou **antes** do envelope filter apenas se quiser limitar a excursão máxima para tocar de forma uniforme.

---

## 4. Presets de Performance em 4 Cenas (Scenes A/B/C/D)

```
+---------------------------------------------------------------------------------------+
|                 BANCO DE PRESET ULTRA-ENVELOPE: 4 CENAS DINÂMICAS                     |
+---------------------+-------------------+---------------------+-----------------------+
| Cena A: 1977 Mu-Tron| Cena B: Downward  | Cena C: Bootsy      | Cena D: Dynamic       |
| Funk Wah (Up-Sweep) | Vocal Talking Q   | Resonant Bass Slap  | Express Lead Solo     |
+---------------------+-------------------+---------------------+-----------------------+
```

### Cena A: 1977 Mu-Tron Funk Wah (Up-Sweep Clássico)
- **Objetivo**: O timbre imortal do Mu-Tron III em modo Band-Pass (*Stevie Wonder - Higher Ground, Grateful Dead*).
- **Parâmetros do Filtro**:
  - `Filter Type`: `BAND-PASS (BP)`
  - `Sweep Direction`: `UP`
  - `Sensitivity / Range`: 68% (Calibrado para captadores Stratocaster / Telecaster)
  - `Peak / Resonance (Q)`: 6.5 (Morno, estalado e vocal sem estridência)
  - `Filter Range`: Low/High Blend (Varredura de 300 Hz a 2.8 kHz)
  - `Attack Time`: 12 ms
  - `Decay Time`: 220 ms
  - `Output Gain`: -2.0 dB
- **Amp / Cab**: Fender Blackface Twin Reverb limpo com leve compressor pós-filtro.

### Cena B: Downward Vocal Talking Q (Descendente Gutural)
- **Objetivo**: Timbre de sintetizador analógico vocal com varredura invertida (*Down-Sweep*). Ideal para riffs sincopados pesados e introduções espaciais (*John Mayer - I Don't Trust Myself*).
- **Parâmetros do Filtro**:
  - `Filter Type`: `LOW-PASS (LP)`
  - `Sweep Direction`: `DOWN`
  - `Sensitivity`: 58%
  - `Peak / Resonance (Q)`: 7.2 (Ressonância pronunciada)
  - `Base Frequency`: 2.6 kHz (Ponto inicial agudo antes do mergulho)
  - `Attack Time`: 8 ms
  - `Decay Time`: 320 ms
- **Ambiência**: Analog Slapback Delay (Tempo 140 ms, Mix 22%) para adicionar textura espacial.

### Cena C: Bootsy Resonant Bass Slap (Funk Bass Supremo)
- **Objetivo**: Projetado especificamente para contrabaixo elétrico. Graves profundos inabaláveis com abertura rápida em estalos percussivos no slap (*Parliament, Red Hot Chili Peppers*).
- **Parâmetros do Filtro**:
  - `Filter Type`: `LOW-PASS DUAL POLE` (Garante retenção de 100% dos sub-graves)
  - `Sweep Direction`: `UP`
  - `Sensitivity`: 42% (Adaptado para a saída alta de contrabaixos ativos/passivos)
  - `Peak / Resonance`: 5.8
  - `Low-End Dry Blend`: 35% (Mistura de sinal limpo para manter peso absoluto)
  - `Attack Time`: 6 ms (Abertura instantânea no polegar)
  - `Decay Time`: 180 ms
- **Amp / Cab**: Ampeg SVT com caixa 8x10.

### Cena D: Dynamic Express Lead Solo (Solo Melódico Aveludado)
- **Objetivo**: Filtro de envelope sutil posicionado antes de um overdrive macio. Notas tocadas pianíssimo soam escuras e aveludadas; notas palhetadas com força abrem o topo harmônico para solos expressivos de blues/fusion.
- **Parâmetros do Filtro**:
  - `Filter Type`: `BAND-PASS SUAVE`
  - `Sweep Direction`: `UP`
  - `Sensitivity`: 50%
  - `Peak / Resonance (Q)`: 3.2 (Sem pico ressonante exagerado)
  - `Drive Pós-Filtro`: Tube Screamer (Gain 45%, Tone 55%)
  - `Decay Time`: 450 ms (Decaimento lento para solos sustentados)
- **Ambiência**: Warm Plate Reverb (Decay 2.0s, Mix 25%).

---

## 5. Dicas de Ouro para Execução com Envelope Filter

1. **Ajuste Físico do Volume na Guitarra/Baixo**:
   - O envelope filter depende da voltagem de entrada para disparar o filtro. Nunca abaixe o potenciômetro de volume do instrumento para diminuir o som da banda; tocar com o volume em 5 fará o filtro parar de abrir! Mantenha sempre o volume do instrumento no máximo e controle a dinâmica exclusivamente na força física da mão direita.
2. **Posição na Cadeia de Pedais**:
   - Posicione o envelope filter **como o primeiríssimo pedal da cadeia**, antes de compressores, overdrives, distorções ou modulações. Distorções comprimem o sinal e destroem a faixa dinâmica que o detector de envelope necessita para modular.
