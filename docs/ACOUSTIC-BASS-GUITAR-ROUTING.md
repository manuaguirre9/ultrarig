# Guia de Roteamento, Dinâmica e Otimização para Baixolão Eletroacústico no UltraRig

Este documento estabelece as diretrizes de engenharia eletroacústica, supressão de microfonia de sub-graves (*anti-feedback*), controle dinâmico de transientes piezo e convolução de ressonância de corpo para **Baixolão Eletroacústico (*Acoustic Bass Guitar*)** no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

O baixolão acústico é um dos instrumentos mais desafiadores da sonorização moderna (*Folk, MPB, Reggae acústico, Pop e Acústicos MTV*). Suas frequências fundamentais estendem-se de $41.2\text{ Hz}$ (E1 em 4 cordas) ou $30.8\text{ Hz}$ (B0 em 5 cordas) até os sobretons percussivos de palhetada ou slap. Por possuir uma caixa de ressonância volumosa de madeira acoplada a captadores piezoelétricos de rastilho, o instrumento sofre cronicamente com realimentação descontrolada no palco (*low-end howl*), estridência no ataque (*piezo quack*) e falta de sustentação natural.

---

## 1. A Física Acústica do Baixolão: O Desafio dos Graves

```
+---------------------------------------------------------------------------------------+
|                      O DILEMA FÍSICO DO BAIXOLÃO ACÚSTICO                            |
|                                                                                       |
|  Comprimento de onda da nota Mi grave (E1 = 41.2 Hz) no ar: ~8.3 metros!              |
|  Volume de ar de uma caixa acústica Jumbo comum: ~0.04 m³ a 0.06 m³                   |
|                                                                                       |
|  ──► Conclusão: A caixa física é acusticamente pequena demais para projetar o grave   |
|      fundamental desplugado com eficiência. O instrumento depende criticamente        |
|      da amplificação eletrônica do captador piezoelétrico sob o rastilho!             |
+---------------------------------------------------------------------------------------+
```

### Principais Problemas Acústicos no Palco:
1. **Ressonância de Helmholtz (Air Resonance)**:
   - A cavidade de ar interna que vibra através da boca (*soundhole*) atua como um ressonador de Helmholtz com pico pronunciado entre **$55\text{ Hz}$ e $85\text{ Hz}$** (entre La1 e Fa#2).
   - Em palcos altos com caixas de retorno (*floor monitors*) ou subwoofers próximos, a pressão sonora dessas frequências excita a caixa do baixolão, criando um loop de realimentação contínuo e estrondoso que destrói a mixagem.
2. **Estridência e Rigidez dos Captadores Piezo**:
   - O piezo capta a deformação mecânica direta sob as cordas de bronze fosforoso (*phosphor bronze*) ou níquel. O resultado é um transiente excessivamente duro e estalado em $2.5\text{ kHz} - 3.5\text{ kHz}$ sem o calor do tampo de abeto/mogno.
3. **Batidas Físicas e Ruído de Manuseio (Handling Noise)**:
   - Vibrações do polegar apoiado no tampo, atrito dos dedos nas cordas e batidas percussivas geram transientes infrassônicos descontrolados abaixo de $35\text{ Hz}$.

---

## 2. Cadeia de Roteamento de Sinal no UltraRig

Para transformar o sinal cru de um baixolão em um timbre profundo, amadeirado, estável e livre de microfonia, o UltraRig implementa a seguinte cadeia DSP:

```
[ BAIXOLÃO PIEZO ]
        │
        ▼
[ HPF INFRASSÔNICO ] ──► [ NOTCH FILTER DUPLO ] ──► [ COMPRESSOR ÓTICO ]
(Sub-cut em 35 Hz,         (Corte cirúrgico em        (Suaviza transientes,
 18 dB/oct roll-off)        62 Hz e 125 Hz)            eleva o sustain)
                                                              │
                                                              ▼
[ SAÍDAS XLR / P10 ] ◄── [ REVERB DE SALA / AMB ] ◄── [ ACOUSTIC BODY IR ] ◄─┘
 (Sinal Balanceado        (Madeira sutil 1.2s,          (Convolução 2048 pts,
  para PA / Retorno)       High-Damp 4 kHz)              Ressonância de Tampo)
```

### Blocos Críticos da Arquitetura:
1. **Filtro Passa-Altas Infrassônico (Sub-Cut HPF)**:
   - Configurado entre **$35\text{ Hz}$ e $40\text{ Hz}$** com inclinação acentuada de 18 dB/octave.
   - Elimina o consumo desnecessário de headroom nos amplificadores e impede a excursão perigosa dos cones de subwoofers causada por batidas no corpo do instrumento.
2. **Filtros Notch Anti-Feedback Paramétricos**:
   - Utilizam fator de qualidade ultra-estreito ($Q \ge 10$) para não afetar as notas vizinhas.
   - O primeiro notch é posicionado na ressonância primária da cavidade de ar (geralmente entre $60\text{ Hz}$ e $68\text{ Hz}$) com atenuação de $-9\text{ dB}$ a $-14\text{ dB}$.
   - O segundo notch é configurado para combater ressonâncias de tampo em torno de $120\text{ Hz} - 135\text{ Hz}$.
3. **Inversor de Polaridade / Fase (180°)**:
   - Em caso de microfonia persistente no palco, alternar a fase global no UltraRig cancela acusticamente a onda que atinge o tampo vinda do monitor de chão.

---

## 3. Dinâmica: Compressão Ótica e De-Quack de Médios

O baixolão acústico necessita de uma curva de compressão muito diferente de um baixo elétrico sólido:

```
+---------------------------------------------------------------------------------------+
|                    COMPRESSÃO DINÂMICA ÓTICA PARA BAIXOLÃO                            |
+---------------------+-------------------+---------------------------------------------+
| Parâmetro           | Ajuste Padrão     | Justificativa Técnica                       |
+---------------------+-------------------+---------------------------------------------+
| Attack Time         | 30 ms - 45 ms     | Preserva o ataque percussivo natural do     |
|                     |                   | dedo na corda antes de iniciar a compressão.|
+---------------------+-------------------+---------------------------------------------+
| Release Time        | 140 ms - 180 ms   | Garante decaimento orgânico e suave,        |
|                     |                   | estendendo o sustain natural da madeira.    |
+---------------------+-------------------+---------------------------------------------+
| Compression Ratio   | 3.2:1 a 4.0:1     | Compressão musical sem achatar a dinâmica.  |
+---------------------+-------------------+---------------------------------------------+
| Threshold           | -22 dBFS          | Atua com 4 a 6 dB de redução de ganho (GR). |
+---------------------+-------------------+---------------------------------------------+
```

### Equalização de Esculpir Médios (Piezo De-Quack):
- **Corte de Médios Nasais**: Atenuação de $-3.5\text{ dB}$ em **$850\text{ Hz}$ a $1.2\text{ kHz}$** ($Q: 1.4$). Essa região é responsável pelo som plástico característico de pré-amplificadores piezo embutidos.
- **Reforço de Corpo Grave**: Reforço suave de $+2.0\text{ dB}$ em **$100\text{ Hz}$** ($Q: 0.8$) para dar sustentação aveludada aos acordes.
- **Controle de Estridência Aguda**: Corte tipo *high-cut* suave acima de **$6.5\text{ kHz}$** para eliminar ruídos de trastes e chiado metálico de cordas de bronze novas.

---

## 4. Presets de Performance em 4 Cenas (Scenes A/B/C/D)

```
+---------------------------------------------------------------------------------------+
|                 BANCO DE PRESET ULTRA-ACOUSTIC BASS: 4 CENAS DE PALCO                 |
+---------------------+-------------------+---------------------+-----------------------+
| Cena A: Acoustic    | Cena B: Modern    | Cena C: Muted       | Cena D: Direct        |
| Folk Warmth         | Percussive Slap   | Walking Jazz        | Balanced Studio DI    |
+---------------------+-------------------+---------------------+-----------------------+
```

### Cena A: Acoustic Folk Warmth (Padrão de Palco)
- **Objetivo**: Timbre amadeirado, encorpado e profundo para baladas, MPB, Folk e apresentações desplugadas com voz e violões.
- **Blocos DSP**:
  - `HPF`: 38 Hz (18 dB/oct)
  - `Notch Filter 1`: 64 Hz, Q: 12, Ganho: -10 dB
  - `Notch Filter 2`: 128 Hz, Q: 8, Ganho: -5 dB
  - `Optical Compressor`: Ratio 3.5:1, Attack 35 ms, Release 160 ms, Gain Reduction -5 dB
  - `Parametric EQ`: Low +2.0 dB @ 100 Hz, Mid -3.5 dB @ 950 Hz, High -1.5 dB @ 5 kHz
  - `Body IR`: Jumbo Acoustic Bass Spruce/Rosewood (2048 pts, Mix 45%)
  - `Wood Room Reverb`: Mix 14%, Decay 1.2s, Pre-delay 25 ms
- **Saída**: XLR Balanceada direta para o PA e retorno in-ear.

### Cena B: Modern Percussive Slap Baixolão
- **Objetivo**: Ataque definido com estalo brilhante e graves percussivos firmes para passagens de slap e técnicas percussivas no tampo estilo *acoustic funk / fingerstyle moderno*.
- **Blocos DSP**:
  - `HPF`: 42 Hz (corta excessos de pancadas no tampo)
  - `Fast Peak Limiter`: Limiar em -6 dBFS para segurar os estalos de puxada de slap
  - `Compressor`: Ratio 4.5:1, Attack 15 ms, Release 100 ms
  - `Parametric EQ`: Scoop em 500 Hz (-4 dB), reforço brilhante em 3.2 kHz (+3 dB) para definir o popping das cordas agudas
  - `Body IR`: Grand Concert Maple/Spruce (Mix 35%)
  - `Chorus Sutil`: Mix 15%, Rate 0.4 Hz, Depth 1.2 ms (adiciona largura estéreo tridimensional)

### Cena C: Muted Walking Jazz (Simulação Upright Bass)
- **Objetivo**: Emula a resposta escura, percussiva e aveludada de um contrabaixo acústico vertical acústico (*Upright/Double Bass*) com cordas lisas (*flatwound*) ou abafamento com a palma da mão (*palm mute*).
- **Blocos DSP**:
  - `High-Cut Filter`: 3.2 kHz (atenuação drástica de agudos metálicos)
  - `Low-Mid Bump`: +3.0 dB em 180 Hz (ressonância de madeira maciça)
  - `Optical Compressor`: Attack 45 ms, Release 90 ms (decaimento rápido e seco tipo pizzicato acústico)
  - `Body IR`: 3/4 Double Bass Upright IR (Mix 65%)
  - `Plate Reverb`: Mix 10%, Decay 0.9s

### Cena D: Direct Balanced Studio DI (Gravação Limpa)
- **Objetivo**: Rastreamento linear de altíssima fidelidade para estúdio de gravação via áudio USB ou saída direta XLR, entregando faixa dinâmica pura para mixagem posterior na DAW.
- **Blocos DSP**:
  - `HPF`: 32 Hz (proteção cirúrgica de subgrave)
  - `Compressor`: Bypass ou Ratio ultra-suave 1.8:1
  - `EQ`: Resposta 100% plana com apenas o de-quack sutil em 1.1 kHz (-2.0 dB)
  - `IR & Reverb`: Bypass (sinal limpo e direto)

---

## 5. Dicas Práticas de Palco para Baixolistas

1. **Uso de Tampador de Boca (*Feedback Buster / Soundhole Cover*)**:
   - Em shows com volume de bateria acústica elevado, utilize um protetor emborrachado na boca do baixolão junto com os filtros notch do UltraRig. Isso reduz em até 18 dB a energia do ar que entra na caixa.
2. **Cordas Recomendadas**:
   - Para timbres acústicos mais doces e menos chiados de dedo no piezo, experimente cordas revestidas (*Coated Phosphor Bronze*) ou cordas *Nylon Tapewound*. Elas reduzem drasticamente a aspereza acima de 3 kHz.
3. **Calibração de Nível de Entrada**:
   - O pré-amplificador embutido no baixolão (bateria de 9V) possui ganho ativo. Ajuste o controle de volume físico no instrumento para aproximadamente 75% a 80% para evitar ceifamento na entrada analógica do Tank-G/B.
