# Guia de Modelagem, Acústica Doppler e Roteamento de Gabinete Rotativo Leslie no UltraRig

Este documento estabelece os princípios mecânicos e psicoacústicos, equações de modulação Doppler, inércia de aceleração assimétrica de rotores e técnicas de roteamento estéreo para **Alto-falantes Rotativos tipo Leslie (*Rotary Speaker Cabinets*, modelos 122 e 147)** no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

Criado originalmente por Donald Leslie nos anos 1940 para dar ambiência espacial tridimensional aos órgãos eletromecânicos Hammond, o gabinete rotativo tornou-se um dos pilares tímbricos mais expressivos da guitarra elétrica e do rock clássico (*Pink Floyd - Any Colour You Like/Breathe, George Harrison - Badge, Jimi Hendrix - Little Wing, Stevie Ray Vaughan - Cold Shot, The Beatles - Let It Be*). Diferente de pedais simples de chorus ou phaser, o efeito Leslie nasce da rotação mecânica real de cornetas e tambores de madeira no espaço físico.

---

## 1. A Física Mecânica e Acústica do Gabinete Leslie

Um gabinete clássico Leslie (como os lendários 122 e 147) é composto por duas vias acústicas independentes separadas por um crossover passivo em **$800\text{ Hz}$**:

```
+---------------------------------------------------------------------------------------+
|                    ESTRUTURA MECÂNICA DE UM GABINETE LESLIE REAL                      |
|                                                                                       |
|   ┌───────────────────────────────────────────────────────────────────────────────┐   |
|   │ [ COMPARTIMENTO SUPERIOR: CORNETA ROTATIVA DE AGUDOS (Upper Horn) ]           │   |
|   │ - Driver de compressão disparando em 2 cornetas giratórias (1 ativa, 1 dummy) │   |
|   │ - Frequências: > 800 Hz                                                       │   |
|   │ - Massa leve / baixa inércia: Acelera em ~1.2s / Desacelera em ~1.6s          │   |
|   └──────────────────────────────────────┬────────────────────────────────────────┘   |
|                                          │ Crossover 800 Hz                           |
|   ┌──────────────────────────────────────┴────────────────────────────────────────┐   |
|   │ [ PRÉ-AMPLIFICADOR VALVULADO CENTRAL ]                                        │   |
|   │ - Válvulas 6550 / 12AU7 introduzindo calor harmônico e compressão suave       │   |
|   └──────────────────────────────────────┬────────────────────────────────────────┘   |
|                                          │                                            |
|   ┌──────────────────────────────────────┴────────────────────────────────────────┐   |
|   │ [ COMPARTIMENTO INFERIOR: ROTOR DE GRAVES / TAMBOR (Lower Bass Rotor) ]       │   |
|   │ - Alto-falante de 15" disparando para baixo dentro de um tambor de madeira    │   |
|   │ - Frequências: < 800 Hz                                                       │   |
|   │ - Massa pesada / alta inércia: Acelera em ~4.5s / Desacelera em ~5.5s         │   |
|   └───────────────────────────────────────────────────────────────────────────────┘   |
+---------------------------------------------------------------------------------------+
```

### Os Três Fenômenos Acústicos Fundamentais do Leslie:
1. **Efeito Doppler (Modulação de Frequência / Pitch)**:
   - Quando a corneta gira em direção ao microfone ou ouvinte, as ondas sonoras são comprimidas no espaço, elevando ligeiramente a frequência percebida. Quando se afasta, a frequência cai. Isso gera um vibrato Doppler contínuo.
2. **Modulação de Amplitude (Tremolo Direcional)**:
   - As cornetas e o defletor de graves possuem alta diretividade. O volume é máximo quando o bocal aponta diretamente para o microfone e cai drasticamente ao apontar para o fundo da cabine.
3. **Reflexões de Gabinete e Filtragem Dinâmica (Comb Filtering)**:
   - O som ricocheteia nas paredes internas de madeira compensada (*plywood*) e nas frestas de saída (*louvers*), criando reflexões de fase móveis que envolvem a sala.

---

## 2. A Inércia Mecânica e os Modos de Rotação no UltraRig

O charme inimitável do Leslie acontece durante a **transição de velocidades**: como a corneta de agudos é muito mais leve que o pesado tambor de graves, ao alternar entre as velocidades lenta e rápida, a corneta atinge a rotação máxima quase imediatamente, enquanto os graves sobem de velocidade lentamente ao longo de 4 a 5 segundos.

```
Modo Chorale (Lento)  ──────────────────────────►  Modo Tremolo (Rápido)
Horn: 0.8 Hz (48 RPM)    ═══[ Acelera em 1.2s ]═══►   Horn: 6.8 Hz (408 RPM)
Drum: 0.7 Hz (42 RPM)    ───[ Acelera em 4.5s ]───►   Drum: 5.9 Hz (354 RPM)

                         ▲
                         │ (A defasagem temporária entre agudos e graves
                         │  cria a textura acústica mais rica do efeito!)
```

### Estados Operacionais Mapeados no UltraRig:
- **Chorale (Slow)**: Rotação suave e majestosa (~0.8 Hz na corneta e ~0.7 Hz no tambor). Ideal para acordes limpos, dedilhados e introduções espaciais.
- **Tremolo (Fast)**: Rotação intensa e pulsante (~6.8 Hz e ~5.9 Hz). Gera o efeito "turbilhão" vibrante para solos e clímaxes musicais.
- **Brake (Stop)**: Desliga a rotação mecânica. Os rotores desaceleram até parar gradualmente por atrito, mantendo o som passando pela filtragem física da cabine de madeira.

---

## 3. Roteamento de Sinal e Microfonação Estéreo no UltraRig

Para posicionar o Leslie com realismo no palco ou gravação de estúdio:

```
[ ENTRADA GUITARRA ] ──► [ OVERDRIVE / PREAMP ] ──► [ TUBE SATURATION ]
                         (Booster transparente     (Saturação 6550/12AU7)
                          ou fuzz clássico)                    │
                                                               ▼
[ SAÍDAS ESTÉREO ] ◄── [ ROOM REVERB ] ◄── [ ROTARY ENGINE (HORN & DRUM) ]
(L e R Balanceados)    (Reflexões de sala) (Crossover 800Hz, Doppler, Pan L/R)
```

### Parâmetros de Microfonação Virtual:
1. **Ângulo dos Microfones da Corneta (Horn Mic Angle)**:
   - `90° (Estreito)`: Foco central clássico, preserva clareza de mixagens densas.
   - `180° (Aberto / Dual Panned)`: Máxima separação estéreo; a modulação Doppler viaja dramaticamente do canal esquerdo para o direito.
2. **Horn / Drum Balance (Balanço Agudo/Grave)**:
   - Configuração equilibrada em `50/50` ou com leve favorecimento da corneta (`55% Horn / 45% Drum`) para destacar a articulação da palhetada.
3. **Drive Valvulado Prévio**:
   - Uma leve saturação antes do bloco Rotary amortece os picos transitórios e adiciona uma sustentação cantante que se mistura perfeitamente com a rotação.

---

## 4. Presets de Performance em 4 Cenas (Scenes A/B/C/D)

```
+---------------------------------------------------------------------------------------+
|                    BANCO DE PRESET ULTRA-ROTARY: 4 CENAS DE PALCO                     |
+---------------------+-------------------+---------------------+-----------------------+
| Cena A: Chorale     | Cena B: Tremolo   | Cena C: Brake       | Cena D: Driven        |
| Slow Wood Swirl     | Fast Doppler Spin | Mechanical Stop     | Cold Shot Crunch      |
+---------------------+-------------------+---------------------+-----------------------+
```

### Cena A: Chorale Slow Wood Swirl (Pink Floyd / Beatles)
- **Objetivo**: Textura lenta, majestosa e tridimensional para baladas e arpejos (*estilo Breathe / Any Colour You Like de Pink Floyd e Badge de Eric Clapton*).
- **Parâmetros Rotary**:
  - `Speed Mode`: `CHORALE (SLOW)`
  - `Horn Speed`: 0.82 Hz
  - `Drum Speed`: 0.70 Hz
  - `Doppler Depth`: 45%
  - `Mic Angle`: 140° (Ampla dispersão estéreo)
  - `Horn/Drum Balance`: 50% / 50%
  - `Preamp Drive`: 18% (Válvula limpa levemente aquecida)
  - `Mix`: 65% Wet / 35% Dry (Equilíbrio entre definição da nota e rotação)
- **Ambiência**: Warm Plate Reverb (Decay 1.8s, Mix 15%).

### Cena B: Tremolo Fast Doppler Spin (Turbilhão de Alta Energia)
- **Objetivo**: Giro rápido e percussivo, perfeito para solos energéticos, refrões e acordes marcados estilo órgão de igreja psicodélico.
- **Parâmetros Rotary**:
  - `Speed Mode`: `TREMOLO (FAST)`
  - `Horn Speed`: 6.75 Hz
  - `Drum Speed`: 5.85 Hz
  - `Doppler Depth`: 70% (Vibrato pronunciado)
  - `Amplitude Modulation (Tremolo)`: 65%
  - `Mic Angle`: 180° (Giro completo de ponta a ponta)
  - `Mix`: 80% Wet / 20% Dry
- **Ambiência**: Slapback sutil de sala.

### Cena C: Brake Mechanical Stop (Parada Gradual com Timbre Estacionário)
- **Objetivo**: Ao pisar no footswitch, os motores mecânicos são desligados e os rotores desaceleram suavemente até parar. Quando estacionados, a guitarra adquire um timbre ressonante e oco característico de caixas de madeira sem modulação contínua (*estilo wah estacionado*).
- **Parâmetros Rotary**:
  - `Speed Mode`: `BRAKE (RAMP TO ZERO)`
  - `Horn Deceleration Time`: 1.8 s
  - `Drum Deceleration Time`: 5.2 s
  - `Cabinet Resonance Filter`: Ativo (Pico em 750 Hz simulando a madeira estática)
  - `Mix`: 50%

### Cena D: Driven Cold Shot Crunch (Stevie Ray Vaughan / Jon Lord)
- **Objetivo**: Timbre cru, saturado e percussivo com forte presença de overdrive pré-rotary, simulando o famoso setup de Stevie Ray Vaughan com amplificador Fender acoplado a um Leslie 16/Vibratone (*Cold Shot*).
- **Parâmetros Rotary**:
  - `Preamp Overdrive`: 65% (Saturação valvulada densa)
  - `Speed Mode`: `CHORALE (SLOW)` acelerando dinamicamente para `TREMOLO (FAST)` via pedal de expressão
  - `Horn/Drum Balance`: 60% Horn / 40% Drum (Agudos cortantes)
  - `Low-Cut`: 100 Hz (Evita embolamento de palhetadas nos bordões)
  - `Mix`: 85% Wet

---

## 5. Dicas de Otimização e Controle em Tempo Real

1. **Troca Dinâmica de Velocidade via Footswitch**:
   - No UltraRig, configure um dos footswitches físicos para a função `ROTARY SPEED TOGGLE (Slow <-> Fast)`. Pressionar o botão aciona a rampa gradual com tempos de inércia separados, permitindo acelerar a rotação exatamente na nota final de um solo.
2. **Compatibilidade Mono vs Estéreo**:
   - Em locais onde o sistema de PA for estritamente mono, reduza a largura estéreo dos microfones da corneta (*Horn Mic Spread*) para 45° ou utilize o modo mono sum com compensação de fase para evitar cancelamento acústico quando os canais L e R forem combinados na mesa de som.
3. **Casamento com Amplificadores no UltraRig**:
   - Para o clássico som de guitarra, posicione o bloco Rotary **após o amplificador e antes do delay/reverb**, garantindo que a resposta de saturação do amp seja modulada pelo gabinete rotativo.
