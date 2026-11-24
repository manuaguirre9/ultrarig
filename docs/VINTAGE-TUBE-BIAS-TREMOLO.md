# Guia de Modelagem, Física Valvulada e Roteamento de Bias Tremolo Vintage no UltraRig

Este documento estabelece as bases de engenharia analógica, comportamento não-linear de polarização de válvulas de potência (*Power Tube Bias Wiggle*), comparação contra tremolos ópticos (*Opto-Roach*) e técnicas de controle dinâmico de taxa por envelope para **Bias Tremolo Valvulado Vintage** no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

O efeito de tremolo (modulação periódica de amplitude de volume) foi o primeiro efeito embutido da história dos amplificadores valvulados nos anos 1950 e 1960 (*Link Wray - "Rumble", Creedence Clearwater Revival - "Born on the Bayou", The Smiths - "How Soon Is Now?", REM - "Monster", The Black Keys*). Embora muitos músicos considerem o tremolo um simples botão de volume subindo e descendo, a topologia do circuito determina se o som será estéril e mecânico ou pulsante, aveludado e saturado de calor analógico.

---

## 1. Topologias Históricas: Tube Bias Tremolo vs. Optical Tremolo

```
+---------------------------------------------------------------------------------------+
|                    COMPARAÇÃO: TUBE BIAS TREMOLO vs. OPTICAL TREMOLO                  |
+---------------------+-----------------------------+-----------------------------------+
| Topologia           | Como Opera no Circuito      | Assinatura Sonora e Dinâmica      |
+---------------------+-----------------------------+-----------------------------------+
| Tube Bias Tremolo   | O LFO oscila a tensão de    | O som não apenas sobe e desce de  |
| (Fender Brownface / | polarização (bias) das      | volume: no pico da onda a válvula |
|  Tweed Princeton /  | válvulas de potência (6V6/  | satura e comprime suavemente;     |
|  Vox AC15 1959-62)  | EL84), modulando o ganho.   | no vale, ela esfria. É aveludado, |
|                     |                             | quente, pantanoso e musical.      |
+---------------------+-----------------------------+-----------------------------------+
| Optical Tremolo     | Uma lâmpada de neon acoplada| Corte de volume abrupto, seco e   |
| (Fender Blackface / | a um fotoresistor LDR desvia| percussivo (*choppy*). O clássico |
|  Twin Reverb 1965)  | o sinal de áudio para o     | som do Surf Rock californiano e   |
|                     | terra ciclicamente.         | trilhas de faroeste (Spaghetti).  |
+---------------------+-----------------------------+-----------------------------------+
```

```
                        [ FÍSICA DO TUBE BIAS TREMOLO ]

             Voltagem de Bias Oscila
                        │
                        ▼
       [ PICO DO VOLUME: Válvula Conduz Mais ] ──► Leve saturação harmônica e calor
                        │
                        ▼
       [ VALE DO VOLUME: Válvula Conduz Menos ] ──► Som limpo e aveludado
```

No UltraRig, o modelo `TUBE-BIAS-VINTAGE` não se limita a atenuar os decibéis matematicamente: ele emula em tempo real a curva de condução e saturação dinâmica das válvulas de potência, fazendo com que o som ganhe um "respiro" analógico e harmônicos ricos a cada pulsação.

---

## 2. Formas de Onda e Modulação Dinâmica de Velocidade (Touch-Rate)

O UltraRig oferece três formas de onda e um algoritmo reativo ao toque da palheta:

```
+---------------------------------------------------------------------------------------+
|                    FORMAS DE ONDA E DINÂMICA DE MODULAÇÃO                             |
+---------------------+-------------------+---------------------------------------------+
| Forma de Onda       | Curva Matemática  | Aplicação Musical Recomendada               |
+---------------------+-------------------+---------------------------------------------+
| Parabolic Bias      | Senóide distorcida| O pulsar aveludado clássico de amplificador |
| (Tweed / Brownface) | com picos quentes | vintage. Ideal para Blues, Swamp Rock e R&B.|
+---------------------+-------------------+---------------------------------------------+
| Optical Sine / Saw  | Senóide com rampa | O estalo seco dos amplificadores Blackface  |
| (Blackface Roach)   | rápida e corte    | para Surf Rock e Spaghetti Western.         |
+---------------------+-------------------+---------------------------------------------+
| Square (Chopper)    | Onda quadrada pura| Corte liga/desliga liga/desliga agressivo   |
| (Modern Slicer)     | de transição nula | para Rock alternativo e efeitos eletrônicos.|
+---------------------+-------------------+---------------------------------------------+
```

### Dinâmica Reativa ao Toque (*Speed Envelope Tracking*):
- O parâmetro `Dynamic Speed` do UltraRig permite que o envelope de palhetada module a velocidade do LFO:
  - Ao atacar um acorde com força: o tremolo acelera instantaneamente para um pulsar rápido e frenético ($7\text{ Hz}$).
  - Conforme a nota sustenta e o volume cai: o tremolo desacelera gradualmente para uma pulsação lenta e relaxante ($2\text{ Hz}$).

---

## 3. Roteamento de Sinal no UltraRig

```
[ ENTRADA GUITARRA ] ──► [ OVERDRIVE / DRIVE ] ──► [ BIAS TREMOLO ] ──► [ REVERB DE MOLA ]
                         (Saturação vintage        (Modulação valvulada (Ambiência clássica
                          ou Fuzz clássico)         antes do reverb)     com cauda viva)
```

### Ordem Crítica: Tremolo Antes vs. Depois do Reverb
- **Regra de Ouro Vintage (Tremolo Antes do Reverb)**:
  Nos amplificadores Fender clássicos, o circuito de tremolo fica **antes** do tanque de reverb de mola. Isso faz com que as notas da guitarra pulsem e cortem com nitidez, enquanto a cauda do reverb de mola continua soando contínua no fundo, preenchendo os vales de silêncio e soando infinitamente mais natural.
- **Tremolo Depois do Reverb**:
  Corta tanto a guitarra quanto a cauda do reverb, criando um efeito artificial de corte digital (*chopped slice*).

---

## 4. Presets de Performance em 4 Cenas (Scenes A/B/C/D)

```
+---------------------------------------------------------------------------------------+
|                 BANCO DE PRESET ULTRA-TREMOLO: 4 CENAS VINTAGE E MODERNAS             |
+---------------------+-------------------+---------------------+-----------------------+
| Cena A: 1962 Tube   | Cena B: 1965 Opto | Cena C: Rhythmic    | Cena D: Dynamic       |
| Bias Swamp Warmth   | Surf Blackface    | Chopper Slicer      | Touch Speed Tremolo   |
+---------------------+-------------------+---------------------+-----------------------+
```

### Cena A: 1962 Tube Bias Swamp Warmth (Creedence / Link Wray)
- **Objetivo**: O pulsar quente, pantanoso e aveludado dos amplificadores Fender Brownface com válvulas 6V6 moduladas em bias (*Born on the Bayou*).
- **Módulo Tremolo**:
  - `Model`: `TUBE BIAS 6V6`
  - `Waveform`: Parabolic Smooth
  - `Speed / Rate`: 3.8 Hz
  - `Depth`: 72%
  - `Tube Saturation on Peak`: 35% (Gera leve compressão e calor no topo do ciclo)
- **Amp / Cab**: Tweed Princeton / Brownface Deluxe cranked com leve saturação natural.
- **Ambiência**: Spring Reverb vintage posicionado após o tremolo (Mix 22%, Dwell 2.2s).

### Cena B: 1965 Opto Surf Blackface (Dick Dale / Tarantino Surf Rock)
- **Objetivo**: Corte percussivo, brilhante e recortado do fotoacoplador opto-bug do Twin Reverb para Surf Rock californiano.
- **Módulo Tremolo**:
  - `Model`: `OPTICAL BLACKFACE ROACH`
  - `Waveform`: Opto Sine
  - `Speed / Rate`: 5.8 Hz (Rápido e enérgico)
  - `Depth`: 88% (Corte quase total de volume)
- **Amp / Cab**: 1965 Blackface Twin Reverb limpo e cristalino com falantes JBL D120F.
- **Ambiência**: Heavy Drip Spring Reverb (Mix 45%, Dwell 3.5s).

### Cena C: Rhythmic Chopper Slicer (The Smiths / Boulevard of Broken Dreams)
- **Objetivo**: Corte agressivo em onda quadrada sincronizado com o andamento musical (*Tap Tempo*) para batidas rítmicas modernas e Rock alternativo.
- **Módulo Tremolo**:
  - `Model`: `SQUARE CHOPPER SLICER`
  - `Waveform`: Hard Square (Transição de 2 ms)
  - `Sync`: Tap Tempo sincronizado em Colcheias (1/8)
  - `Depth`: 100% (Silêncio absoluto entre as fatias)
  - `Duty Cycle / Symmetry`: 50% ligado / 50% desligado
- **Amp**: Marshall JCM800 com overdrive TS-808 apertado.

### Cena D: Dynamic Touch Speed Tremolo (Reativo à Dinâmica)
- **Objetivo**: Velocidade reativa ao toque: palhetada forte dispara modulação rápida e enérgica; decaimento desacelera para um pulsar lento e aveludado.
- **Módulo Tremolo**:
  - `Model`: `DYNAMIC BIAS ENVELOPE`
  - `Base Speed (Pianíssimo)`: 1.8 Hz
  - `Max Speed (Fortíssimo)`: 6.5 Hz
  - `Dynamic Sensitivity`: 65%
  - `Decay Smoothing`: 450 ms (Desaceleração gradual e orgânica)
  - `Depth`: 65%
- **Amp**: Vox AC15 Top Boost no ponto de quebra (*edge of breakup*).

---

## 5. Dicas Práticas de Ajuste no Palco

1. **Compensação de Volume Percebido**:
   - Como o tremolo passa parte do tempo cortando o sinal para criar a ilusão de oscilação, o volume RMS percebido da guitarra cai ligeiramente. Sempre compense o ganho de saída do bloco (*Output Makeup Level: +1.5 dB a +2.5 dB*) para que o volume aparente com o tremolo ligado seja idêntico ao sinal bypassado.
2. **Sincronização com a Bateria ao Vivo**:
   - Em canções com andamento fixo, configure o footswitch do UltraRig para `TAP TEMPO` e bata 3 toques no ritmo da caixa da bateria antes de iniciar a música, garantindo que o tremolo pulse perfeitamente casado com o groove da banda.
