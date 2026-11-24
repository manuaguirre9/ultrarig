# Guia de Engenharia Eletroacústica, Dinâmica e Convolução de IR para Banjo de 5 Cordas no UltraRig

Este documento estabelece as diretrizes de processamento eletroacústico, controle dinâmico de transientes percussivos de dedeiras metálicas (*fingerpicks*), filtragem de ressonância de pele plástica e convolução de respostas de impulsos (IR) de anel de bronze (*Tone Ring*) para **Banjos de 5 Cordas (*5-String Bluegrass & Clawhammer Banjo*)** no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

O banjo de 5 cordas é o instrumento condutor supremo do *Bluegrass, Country tradicional, Old-Time e Folk contemporâneo* (*Earl Scruggs, Béla Fleck, Pete Seeger, Ralph Stanley, Mumford & Sons*). Com sua afinação aberta reentrante (*Open G: g4-D3-G3-B3-D4*), onde a 5ª corda funciona como um drone agudo percussivo, o banjo possui uma velocidade de ataque quase instantânea. No entanto, quando amplificado no palco por captadores piezoelétricos de cavalete (*Fishman Rare Earth Banjo, Schatten BJ-02*) ou microfones de contato, o instrumento torna-se notório por produzir uma estridência metálica dolorosa, estalos excessivos e microfonia descontrolada.

---

## 1. A Física Mecânica e Eletroacústica do Banjo

Diferente de violões que dependem da vibração de um tampo de madeira rígido, o banjo opera como um tambor acústico com cordas esticadas sobre uma membrana flexível:

```
+---------------------------------------------------------------------------------------+
|                    ESTRUTURA MECÂNICA DE UM BANJO DE 5 CORDAS                         |
|                                                                                       |
|    [ 5 CORDAS DE AÇO ] ──► [ PONTE FLUTUANTE DE MAPLE/ÉBANO (Floating Bridge) ]       |
|                                         │                                             |
|                                         ▼                                             |
|                   [ PELE DE MYLAR / COURO TENSIONADA (Head) ]                         |
|                                         │                                             |
|                                         ▼                                             |
|                   [ ANEL DE BRONZE FUNDIDO (Bell Bronze Tone Ring) ]                  |
|                                         │                                             |
|                                         ▼                                             |
|                   [ ARO DE MADEIRA + RESSONADOR TRASEIRO (Resonator) ]                |
+---------------------------------------------------------------------------------------+
```

### O Desafio dos Picos Transitórios e da Ressonância da Pele:
1. **Transientes Brutais de Dedeiras de Metal**:
   - Os dedos indicador e médio utilizam dedeiras de níquel-prata ou aço (*metal fingerpicks*), enquanto o polegar usa uma dedeira plástica (*thumbpick*). O choque do metal contra as cordas de aço sobre uma pele plástica tensionada gera tempos de ataque inferiores a $2\text{ ms}$, com picos transitórios de até $+18\text{ dB}$ acima do nível RMS médio.
2. **O Pico Nasal da Membrana de Mylar**:
   - A pele de mylar altamente tensionada (afinada tipicamente na nota Sol# ou Lá em cerca de 90 a 92 na escala drum-dial) possui um pico de ressonância natural estridente e concentrado entre **$1.8\text{ kHz}$ e $2.6\text{ kHz}$**. Diretamente no sistema de PA, esse pico soa fino, estridente e oco.

---

## 2. Roteamento de Sinal e Cadeia DSP no UltraRig

Para domar a aspereza mecânica, nivelar os disparos de volume e devolver o corpo amadeirado do ressonador, o UltraRig organiza os blocos da seguinte forma:

```
[ BANJO COM CAPTADOR PIEZO ]
              │
              ▼
   [ LIMITADOR DE PICO RÁPIDO ] ──► [ HPF CIRÚRGICO 100 Hz ] ──► [ NOTCH DA PELE 2.2 kHz ]
   (Segura disparos de metal)        (Corta baques no aro)        (Elimina som de lata)
                                                                            │
                                                                            ▼
 [ SAÍDAS XLR / FONES ] ◄── [ REVERB DE SALA DE MADEIRA ] ◄── [ TONE RING BANJO IR ] ◄─┘
  (Sinal doce e estalado)    (Decay 1.2s, ambiência rica)     (Convolução 2048 pts)
```

### Blocos Críticos da Arquitetura:
1. **Limitador de Pico Rápido (*Fast Peak Limiter*)**:
   - Posicionado no início da cadeia para interceptar os estalos pontiagudos de metal antes que atinjam o estágio de ganho do pedal. Limiar (*Ceiling*) ajustado em $-3\text{ dBFS}$ com tempo de ataque quase instantâneo ($0.5\text{ ms}$).
2. **Filtro Passa-Altas (HPF)**:
   - Configurado em **$95\text{ Hz}$ a $110\text{ Hz}$** ($18\text{ dB/octave}$). O Ré grave do banjo ($D_3$) vibra a $146.8\text{ Hz}$. Portanto, qualquer frequência abaixo de $100\text{ Hz}$ consiste puramente em baques do calcanhar da mão apoiado na pele e ruídos de palco.
3. **Filtro Notch Anti-Ressonância da Pele**:
   - Corte estreito de $-4.5\text{ dB}$ a $-6.0\text{ dB}$ em **$2.1\text{ kHz} - 2.4\text{ kHz}$** ($Q: 2.5$). Esse ajuste remove imediatamente o timbre de "lata vazia" e devolve a nobreza ao ataque.
4. **Convolução de Resposta de Impulso de Banjo (Tone Ring IR)**:
   - Um IR capturado com microfone de fita (*Coles 4038*) em frente a um Gibson Mastertone de 1930 com anel de bronze e ressonador de maple. Transforma um piezo de rastilho seco em um banjo microfonado em estúdio profissional.

---

## 3. Presets de Performance em 4 Cenas (Scenes A/B/C/D)

```
+---------------------------------------------------------------------------------------+
|                  BANCO DE PRESET ULTRA-BANJO: 4 CENAS DE PERFORMANCE                  |
+---------------------+-------------------+---------------------+-----------------------+
| Cena A: Bluegrass   | Cena B: Clawhammer| Cena C: Progressive | Cena D: Direct Stage  |
| Scruggs Drive       | Old-Time Mellow   | Bela Fleck Modern   | Anti-Clatter DI       |
+---------------------+-------------------+---------------------+-----------------------+
```

### Cena A: Bluegrass Scruggs Drive (Earl Scruggs / Flatt & Scruggs)
- **Objetivo**: O ataque relâmpago, focado, cortante e galopante de 3 dedos (*Scruggs style roll*), perfeitamente equilibrado para cortar violões, bandolins e violinos.
- **Módulos DSP**:
  - `Fast Peak Limiter`: Ceiling -3 dBFS, Release 45 ms
  - `HPF`: 105 Hz
  - `Parametric EQ`: Notch -5 dB @ 2.2 kHz, Low-Mid +2.0 dB @ 320 Hz (corpo de madeira), High Shelf +1.5 dB @ 7.5 kHz
  - `Optical Compressor`: Ratio 3.2:1, Attack 25 ms, Release 120 ms
  - `Banjo Tone Ring IR`: Pre-War Mastertone Bronze Ring (Mix 55%)
  - `Wood Room Reverb`: Mix 12%, Decay 0.9s
- **Saída**: XLR balanceada direta para o PA.

### Cena B: Clawhammer Old-Time Mellow (Pete Seeger / Round Peak)
- **Objetivo**: Toque tradicional sem dedeiras de metal (*clawhammer / frailing*), onde o polegar e a parte de trás das unhas golpeiam a corda de cima para baixo. Timbre amadeirado, escuro e rústico.
- **Módulos DSP**:
  - `HPF`: 95 Hz
  - `High-Cut Filter`: 5.8 kHz (atenua agudos modernos para uma sonoridade vintage de pele de couro)
  - `Parametric EQ`: Reforço aveludado em 250 Hz (+3 dB)
  - `Compressor Suave`: Ratio 2:1, Attack 35 ms, Release 160 ms
  - `Banjo Open-Back IR`: 11" Maple Open-Back Rim (Mix 65%)
  - `Ambiência`: Small Barn Room (Decay 1.1s, Mix 18%)

### Cena C: Progressive Bela Fleck Modern (Jazz Acústico & Fusion)
- **Objetivo**: Clareza polifônica para acordes complexos de jazz, sustentação aveludada e panorama estéreo refinado (*estilo Béla Fleck and the Flecktones*).
- **Módulos DSP**:
  - `Limiter`: Moderado
  - `Stereo Dimension Chorus`: Modulação tridimensional sem oscilação cíclica (Mix 15%)
  - `Analog Tape Delay`: Tempo sincronizado em semínima pontuada (420 ms, Feedback 22%, Mix 18%)
  - `Hall Reverb`: Cauda suave de 2.2s com High-Damp em 4.5 kHz
  - `Banjo IR`: Custom Mahogany Resonator (Mix 50%)

### Cena D: Direct Stage Anti-Clatter DI (Palcos Barulhentos)
- **Objetivo**: Máxima tolerância contra microfonia e batidas percussivas em palcos altos com baterias acústicas pesadas.
- **Módulos DSP**:
  - `HPF`: 120 Hz (corte rigoroso de ressonâncias de palco)
  - `Dual Notch Filters`: -6 dB @ 2.1 kHz e -4 dB @ 650 Hz (ressonância do bojo)
  - `Inversão de Fase (180°)`: Ativável para cancelamento de retornos de chão
  - `IR & Reverb`: Bypass para sinal direto cirúrgico na mesa de som

---

## 4. Dicas de Otimização e Cuidados no Palco

1. **Apoio da Mão Direita na Pele**:
   - A técnica de 3 dedos do Bluegrass requer apoiar firmemente o dedo anelar e o mindinho na pele plástica próxima à ponte. Esse apoio físico funciona como um abafador natural de frequências graves. Ao usar captadores piezo, calibre a sensibilidade do UltraRig para que esse contato físico não gere estalos indesejados.
2. **Posição do Captador Piezo**:
   - Se o captador estiver instalado diretamente no pé da ponte, o som terá o máximo de ataque; se estiver colado na parte interna da pele a 2 centímetros da ponte, o som terá mais corpo e menos estridência.
