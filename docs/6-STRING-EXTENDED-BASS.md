# Guia de Engenharia Eletroacústica, Gerenciamento de Sub-Headroom e Roteamento para Contrabaixo de 6 Cordas e Afinações Estendidas no UltraRig

Este documento estabelece as diretrizes de engenharia eletroacústica, proteção contra sobre-excursão mecânica de alto-falantes (*sub-woofer blowout*), compressão multibanda de 3 zonas e clareza polifônica para **Contrabaixos de 6 Cordas e Instrumentos de Alcance Estendido (*Extended Range Bass - ERB*)** no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

O baixo de 6 cordas e afinações baixas extremas (*John Patitucci, Anthony Jackson, Thundercat, Henrik Linder / Dirty Loops, Meshuggah*) expandiram drasticamente a tessitura do contrabaixo elétrico. Ao combinar a corda Si grave (B0 a $30.87\text{ Hz}$) — ou até afinações extremas como Fá sustenido grave (Low F#0 a $23.12\text{ Hz}$) — com uma corda Dó aguda (C3 com harmônicos alcançando $10\text{ kHz}$), o instrumento impõe desafios brutais de headroom elétrico, resposta dinâmica e separação de frequências em sistemas digitais.

---

## 1. A Física Acústica das Frequências Infrassônicas (F#0 / B0)

```
+---------------------------------------------------------------------------------------+
|                    TESSITURA DE FREQUÊNCIAS NO BAIXO DE 6 CORDAS                      |
|                                                                                       |
|  Corda F#0 (Drop / Afinação Estendida): 23.12 Hz (Comprimento de onda: ~14.8 metros!)|
|  Corda B0 (Si grave padrão):            30.87 Hz (Comprimento de onda: ~11.1 metros!) |
|  Corda E1 (Mi grave tradicional):       41.20 Hz                                      |
|  Corda A1 (Lá):                         55.00 Hz                                      |
|  Corda D2 (Ré):                         73.42 Hz                                      |
|  Corda G2 (Sol):                        98.00 Hz                                      |
|  Corda C3 (Dó agudo):                   130.81 Hz (Harmônicos até 10 kHz!)            |
+---------------------------------------------------------------------------------------+
```

### O Desafio Crítico do Headroom e Excursão de Cones:
1. **Consumo Inútil de Potência Elétrica**:
   - Frequências abaixo de $30\text{ Hz}$ são quase inaudíveis ao ouvido humano como notas melódicas (são percebidas como vibração mecânica tátil). No entanto, demandam até 70% de toda a energia elétrica de um amplificador de potência!
2. **Sobre-Excursão Mecânica (*Woofer Chuffing*)**:
   - Enviar energia pesada de 23 Hz para caixas de 4x10" ou 1x15" faz os cones ultrapassarem seus limites de excursão física máxima ($X_{\text{max}}$), gerando distorção intermodular feia e risco iminente de queima da bobina móvel.
3. **A Solução no UltraRig**:
   - Um **Filtro Passa-Altas Infrassônico de 4ª Ordem (HPF 24 dB/oct)** sintonizado entre **$26\text{ Hz}$ e $30\text{ Hz}$**. Ele elimina o sub-rumble destruidor de caixas enquanto preserva 100% da sensação de peso sísmico e foco tonal da corda B0/F#0.

---

## 2. A Arquitetura de Compressão Multibanda de 3 Zonas no UltraRig

Um compressor convencional de banda única falha no baixo de 6 cordas: se for ajustado para segurar a enorme energia da corda B grave, ele esmagará e silenciará as notas melódicas tocadas na corda C aguda.

O UltraRig resolve isso dividindo a faixa em **3 zonas dinâmicas independentes**:

```
[ ENTRADA DO BAIXO 6 CORDAS ]
              │
              ▼
    [ HPF INFRASSÔNICO 28 Hz ]
              │
              ▼
   ┌─────────────────────────────────────────────────────────────┐
   │ DIVISÃO DE CROSSOVER MULTIBANDA                             │
   │                                                             │
   │ ──► [ ZONA 1: SUB-GRAVE (28 Hz a 90 Hz) ]                   │
   │     - Ratio Alto (6:1), Attack Rápido (10 ms)               │
   │     - Ancora o grave em uma linha sólida e sem oscilação    │
   │                                                             │
   │ ──► [ ZONA 2: PUNCH MÉDIO (90 Hz a 1.2 kHz) ]               │
   │     - Ratio Moderado (3:1), Attack Musical (35 ms)          │
   │     - Preserva o impacto percussivo do slap e da palheta    │
   │                                                             │
   │ ──► [ ZONA 3: CHIME & SOLOS (1.2 kHz a 8 kHz) ]             │
   │     - Ratio Suave (2:1), Release Aveludado                  │
   │     - Deixa a corda C aguda cantar com clareza polifônica   │
   └──────────────────────────────┬──────────────────────────────┘
                                  │
                                  ▼
                      [ SOMA LINEAR EM FASE ]
                                  │
                                  ▼
                   [ SIMULAÇÃO DE AMP BASS / CAB IR ]
```

---

## 3. Equalização Anti-Lama para Acordes Polifônicos

Um dos maiores usos do baixo de 6 cordas é a execução de acordes estendidos (*chords* estilo jazz, gospel e neo-soul nas cordas D, G e C):
- **O Ponto de Conflito (220 Hz a 350 Hz)**: Quando acordes são tocados nas cordas médias-altas com a corda B solta ressoando, a região de $250\text{ Hz}$ acumula harmônicos que embolam a mixagem.
- **Ajuste Corretivo no UltraRig**:
  - Aplicação de um corte suave de $-3.0\text{ dB}$ em **$280\text{ Hz}$** ($Q: 1.4$).
  - Reforço de presença em **$2.2\text{ kHz}$** ($+2.5\text{ dB}$) para destacar a articulação dos trastes e definição das notas individuais do acorde.
  - Reforço aéreo em **$6.5\text{ kHz}$** ($+1.5\text{ dB}$) para brilho sedoso sem chiado ativo.

---

## 4. Presets de Performance em 4 Cenas (Scenes A/B/C/D)

```
+---------------------------------------------------------------------------------------+
|                 BANCO DE PRESET ULTRA-6STRING BASS: 4 CENAS DE PALCO                  |
+---------------------+-------------------+---------------------+-----------------------+
| Cena A: Modern Prog | Cena B: Gospel    | Cena C: Thumpin'    | Cena D: Pristine      |
| Metal Sub-Tight     | Chords & Solos    | Extended Slap       | Hi-Fi Studio DI       |
+---------------------+-------------------+---------------------+-----------------------+
```

### Cena A: Modern Prog Metal Sub-Tight (Afinação B0 / Drop A / Low F#0)
- **Objetivo**: Foco cirúrgico, rápido e percussivo para riffs sincronizados com bumbo de bateria rápida em metal progressivo e djent (*estilo Meshuggah, Periphery, Haken*).
- **Módulos DSP**:
  - `Infrasonic HPF`: 28 Hz (24 dB/oct)
  - `Multiband Split`: Zona Sub (< 90 Hz) comprimida em 6:1 (GR -6 dB)
  - `Drive / Distortion`: Darkglass Microtubes B7K emulação no ramo médio (Drive 45%, Blend 50%)
  - `Amp Model`: Modern Solid-State High-Power Bass Head
  - `Cab IR`: 8x10 Ampeg SVT com microfone dinâmico próximo ao cone
  - `Noise Gate`: Rápido (-52 dB threshold)

### Cena B: Gospel Chords & Solo Clarity (Acordes Ricos de 6 Cordas)
- **Objetivo**: Clareza cristalina para acordes de 9ª, 11ª e 13ª tocados nas casas agudas sem perder o alicerce encorpado dos graves (*estilo Andrew Gouché, Thundercat*).
- **Módulos DSP**:
  - `HPF`: 32 Hz
  - `Multiband Compressor`: Suave na Zona 3 (Ratio 2:1, Release 180 ms)
  - `Parametric EQ`: Dip em 280 Hz (-3 dB), Boost em 1.5 kHz (+2 dB), High Shelf em 7 kHz (+2 dB)
  - `Amp Model`: Tube Preamp Eden World Tour / Aguilar DB751
  - `Chorus Sutil`: Dimension Chorus L/R (Mix 15%)
  - `Cab IR`: 4x10 Neodymium com tweeter de alta frequência

### Cena C: Thumpin' Extended Slap (Marcus Miller / Dirty Loops)
- **Objetivo**: Polegar sísmico estrondoso na corda Si grave (B0) combinado com puxadas (*pops*) ultra-estaladas e percussivas na corda Dó aguda (C3).
- **Módulos DSP**:
  - `HPF`: 30 Hz
  - `Peak Limiter`: Limiar em -4 dBFS na saída para segurar puxadas de slap
  - `EQ Curve`: Scoop tradicional de médios (corte em 600 Hz -4 dB, reforço em 80 Hz +3 dB e 3.5 kHz +3.5 dB)
  - `Optical Compressor`: Attack 30 ms (preserva estalo de unha), Release 100 ms
  - `Cab IR`: 4x10 Hartke com cones de alumínio

### Cena D: Pristine Hi-Fi Studio DI (Gravação Direta para DAW)
- **Objetivo**: Resposta 100% linear, aberta e de baixíssimo ruído para estúdio de gravação profissional via USB áudio digital.
- **Módulos DSP**:
  - `HPF`: 24 Hz (proteção cirúrgica de conversores)
  - `Multiband Dynamics`: Ativa com nivelamento transparente
  - `Amp / IR`: Bypass (Sinal DI puro para re-amp posterior na DAW)
  - `Output Meter`: Calibrado em -16 LUFS integrado com teto de pico em -1.0 dBFS

---

## 5. Dicas Técnicas de Palco para Baixistas de 6 Cordas

1. **Ajuste de Ação e Espaçamento de Cordas**:
   - Em baixos de 6 cordas, o espaçamento entre cordas na ponte é frequentemente mais estreito (16.5 mm a 17 mm, contra 19 mm de baixos de 4 cordas). Pratique o abafamento (*muting*) com a palma da mão direita para que as cordas graves adjacentes não vibrem por simpatia durante solos na corda C aguda.
2. **Monitoração no Palco**:
   - Caixas convencionais de retorno de chão de 12" não conseguem reproduzir o Si grave (30 Hz). Para apresentações de grande porte, certifique-se de que o técnico de som envie seu sinal diretamente para os subwoofers do PA ou utilize fones in-ear profissionais de armadura balanceada múltipla com driver dedicado para subgraves.
