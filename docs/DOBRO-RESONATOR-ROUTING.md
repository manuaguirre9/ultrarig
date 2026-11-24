# Guia de Engenharia Eletroacústica, Dinâmica de Slide e Roteamento para Violões Ressonadores (Dobro & National) no UltraRig

Este documento estabelece as diretrizes de processamento eletroacústico, controle dinâmico de transientes de palheta dedeira (*thumbpick/fingerpicks*), modelagem de ressonância mecânica de cones de alumínio e convolução de impulso (IR) para **Guitarras e Violões Ressonadores (*Resonator Guitars / Dobro, National e Tricone*)** no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

Desenvolvidos na década de 1920 pelos irmãos Dopyera antes da invenção dos amplificadores eletrônicos de guitarra, os instrumentos ressonadores foram projetados para que a guitarra acústica conseguisse competir em pressão sonora com instrumentos de sopro e baterias no jazz e vaudeville. Tornaram-se o pilar tímbrico definitivo do *Delta Blues, Bluegrass, Country acústico e Rock de raiz* (*Robert Johnson, Son House, Bukka White, Jerry Douglas, Mark Knopfler - Dire Straits "Brothers in Arms"*).

---

## 1. A Física Mecânica dos Cones de Alumínio

Em vez de depender da flexibilidade do tampo de madeira para irradiar o som, as cordas do ressonador transmitem a energia vibratória das cordas diretamente a um ou três cones côncavos de alumínio (*resonator cones*), que funcionam como alto-falantes mecânicos acústicos:

```
+---------------------------------------------------------------------------------------+
|                    COMPARAÇÃO DAS TOPOLOGIAS DE CONES RESSONADORES                    |
+---------------------+-----------------------------+-----------------------------------+
| Topologia           | Construção & Ponte          | Resposta Tímbrica e Aplicação     |
+---------------------+-----------------------------+-----------------------------------+
| Spider Bridge Cone  | Cone invertido (côncavo) com| Timbre doce, focado, vocal e com  |
| (Dobro Tradicional) | aranha de alumínio de 8     | longo sustain cantante. O padrão  |
|                     | pernas sobre o cone; corpo  | absoluto do Bluegrass e Country   |
|                     | quase sempre em madeira.    | acústico (*Jerry Douglas*).       |
+---------------------+-----------------------------+-----------------------------------+
| Biscuit Bridge Cone | Cone voltado para baixo     | Ataque cru, gutural, metálico,    |
| (National Clássico) | (convexo) com bloco de      | cortante e percussivo. Decaimento |
|                     | madeira dura central; corpo | rápido. O som definitivo do Delta |
|                     | de latão, aço ou madeira.   | Blues e slide acústico cru.       |
+---------------------+-----------------------------+-----------------------------------+
| Tricone             | Três cones menores de 6"    | Altíssima riqueza harmônica, som  |
| (National Tricone)  | unidos por uma barra em T   | elegante, dispersão espacial ampla|
|                     | de alumínio fundido.        | e sustain aveludado tridimensional|
+---------------------+-----------------------------+-----------------------------------+
```

---

## 2. Os Desafios da Amplificação Eletroacústica no Palco

Quando amplificados ao vivo por captadores piezoelétricos sob a aranha/biscoito (*Fishman Nashville Series, K&K Pure Resonator, L.R. Baggs*) ou microfones de contato:
1. **O Pico Metálico Nasal (Nasal Harshness)**:
   - O cone de alumínio projeta um pico de ressonância natural intenso e estreito entre **$1.8\text{ kHz}$ e $2.6\text{ kHz}$**. Diretamente no PA, esse pico soa áspero, fino e como "lata cortante".
2. **Microfonia de Caixa em Frequências Médio-Graves**:
   - A tampa perfurada com orifícios em forma de leque ou f-holes ressoa com força em torno de **$450\text{ Hz}$ a $600\text{ Hz}$**, realimentando descontroladamente em palcos com monitores de chão.
3. **Picos Transitórios Brutais de Dedeiras de Metal**:
   - O toque com dedeiras de polegar (*plastic thumbpick*) e dedeiras de dedo de níquel/aço (*metal fingerpicks*) acoplado ao slide de latão ou vidro gera transientes percussivos com picos de até $+14\text{ dB}$ acima do nível médio da nota.

---

## 3. Arquitetura de Sinal e Roteamento DSP no UltraRig

Para domar a estridência metálica, proteger o headroom e restaurar o corpo amadeirado ou metálico tridimensional no UltraRig:

```
[ RESSONADOR COM PIEZO / MAGNÉTICO ]
                 │
                 ▼
     [ COMPRESSOR ÓTICO RÁPIDO ] ──► [ NOTCH ANTI-FEEDBACK ] ──► [ EQUALIZADOR PARAMÉTRICO ]
     (Amortece estalo de metal,       (Corte cirúrgico em          (Atenua pico 2.1 kHz cone,
      preserva sustain do slide)       520 Hz na tampa)             reforça ar em 8 kHz)
                                                                            │
                                                                            ▼
 [ SAÍDA XLR BAL / FONE ] ◄── [ AMBIÊNCIA PLATE / HALL ] ◄── [ RESO CONE / BODY IR ] ◄─┘
  (Mixagem rica e quente)     (Decay 1.8s a 2.5s, madeira)     (Convolução 2048 pts)
```

### Blocos de Modelagem:
1. **Compressor Ótico com Tempo de Ataque Calibrado**:
   - `Attack Time`: $20\text{ ms}$ a $30\text{ ms}$. Permite que o "clique" articulado do metal seja ouvido, mas intervém rapidamente antes que o pico sobrecarregue o sistema.
   - `Release Time`: $160\text{ ms}$. Sustenta as notas arrastadas pelo slide (*singing sustain*).
2. **Equalização Corretiva Esculpidora**:
   - `Corte Nasal Paramétrico`: $-4.0\text{ dB}$ em **$2.2\text{ kHz}$** ($Q: 2.2$). Suaviza a dureza do alumínio sem descaracterizar a alma do instrumento.
   - `Low-Mid Warmth`: $+2.5\text{ dB}$ em **$180\text{ Hz}$** para conferir espessura ao corpo.
   - `High-Pass Filter (HPF)`: $65\text{ Hz}$ (12 dB/oct) para limpar batidas de palma da mão nas cordas (*palm thumps*).
3. **Convolução de Resposta de Impulso de Cone de Ressonador (Reso IR)**:
   - A convolução de um IR capturado com microfone de fita (*Royer R-121*) em frente a um National Style O autêntico de 1932 restaura o calor acústico da sala que o captador piezo no cavalete perde por completo.

---

## 4. Presets de Performance em 4 Cenas (Scenes A/B/C/D)

```
+---------------------------------------------------------------------------------------+
|                 BANCO DE PRESET ULTRA-RESONATOR: 4 CENAS DE PALCO                     |
+---------------------+-------------------+---------------------+-----------------------+
| Cena A: Delta Blues | Cena B: Bluegrass | Cena C: Acoustic    | Cena D: Clean Studio  |
| Metal National      | Spider Dobro      | Slide Ambient Bloom | Magnetic/Piezo Blend  |
+---------------------+-------------------+---------------------+-----------------------+
```

### Cena A: Delta Blues Metal National (Estilo Son House / Robert Johnson)
- **Objetivo**: Ataque cru, metálico, percussivo e estrondoso para slide em afinações abertas (*Open D ou Open G*), com a pegada rústica dos instrumentos de corpo de aço/latão.
- **Blocos DSP**:
  - `Optical Compressor`: Ratio 3.8:1, Attack 22 ms, Release 140 ms, Gain Reduction -4 dB
  - `Parametric EQ`: Low-Cut 70 Hz, Low +2.0 dB @ 160 Hz, Mid Dip -3.5 dB @ 2.1 kHz, High-Shelf +1.5 dB @ 7.5 kHz
  - `Resonator IR`: 1934 National Duolian Steel Body (Mix 55%)
  - `Ambiência`: Small Vintage Room (Decay 0.9s, Mix 12%)
- **Técnica Recomendada**: Slide de latão pesado (*brass slide*) no dedo mínimo com abafamento atrás do slide.

### Cena B: Bluegrass Spider Dobro (Jerry Douglas / Flatt & Scruggs)
- **Objetivo**: A doçura cantante e aveludada do cone aranha em corpo de mogno, com sustentação infinita para passagens melódicas velozes.
- **Blocos DSP**:
  - `Optical Compressor`: Ratio 3.0:1, Attack 35 ms, Release 180 ms
  - `Parametric EQ`: Notch -8 dB @ 540 Hz (elimina microfonia de tampa), Mid -2.5 dB @ 2.4 kHz, High +2.0 dB @ 9 kHz (brilho aéreo)
  - `Resonator IR`: Pre-War Dobro Wood Body Spider Cone (Mix 60%)
  - `Ambiência`: Warm Hall Reverb (Decay 1.8s, Mix 18%, Pre-delay 25 ms)

### Cena C: Acoustic Slide Ambient Bloom (Baladas Atmosféricas)
- **Objetivo**: Sustentação etérea e cinematográfica para baladas de slide (*estilo Dire Straits / Pink Floyd*), onde cada nota de slide se transforma em uma onda espacial.
- **Blocos DSP**:
  - `Compressor`: Ratio 4.5:1, Attack 15 ms, Release 250 ms (Longa sustentação)
  - `Tape Delay`: Tempo 460 ms (pontilhado), Wow 20%, Feedback 35%, Mix 25%
  - `Lush Plate Reverb`: Decay 3.2s, High-Damp 4.5 kHz, Mix 30%
  - `Resonator IR`: Tricone Vintage (Mix 50%)

### Cena D: Clean Studio Magnetic/Piezo Blend (Versatilidade em Estúdio)
- **Objetivo**: Para instrumentos modernos equipados com captador duplo (piezo no cone + captador magnético no braço).
- **Blocos DSP**:
  - `HPF`: 60 Hz
  - `Compressor Suave`: Ratio 2.2:1
  - `EQ Linear`: De-quack sutil em 2.2 kHz (-2.0 dB)
  - `Reso IR`: Bypass ou Mix sutil de 20%
  - `Saída`: Direta para gravação USB DAW com máxima integridade de sinal

---

## 5. Dicas Práticas de Palco para Músicos de Slide

1. **Escolha do Material do Slide**:
   - **Slide de Vidro / Pyrex**: Som mais quente, suave e com menor ruído de fricção no metal das cordas. Ideal para a Cena B e C.
   - **Slide de Latão / Aço Cromado**: Maior massa, sustentação incomparavelmente mais longa e ataque cortante. Perfeito para a crueza do Delta Blues na Cena A.
2. **Ajuste de Ação das Cordas**:
   - Para tocar com slide sem bater nos trastes (*fret clatter*), a ação das cordas no rastilho deve ser ajustada ligeiramente mais alta que em violões comuns (cerca de 2.8 mm a 3.2 mm na 12ª casa).
3. **Calibração de Nível LUFS**:
   - Como os transientes de dedeiras metálicas possuem alta energia de crista, calibre o ganho de saída das 4 cenas para patamares uniformes de -16 LUFS integrado, evitando que passagens com dedeira saturem a entrada da mesa de som.
