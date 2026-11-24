# Guia de Modelagem de Filtro Formante Vocal e Talk-Box Virtual no UltraRig

Este documento estabelece as bases de engenharia acústica do trato vocal humano, equações de ressonância de formantes de vogais (F1 e F2), transições contínuas de pronúncia (*Vowel Morphing*) e roteamento de performance para **Filtros Formantes e Talk-Box Virtual** no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

O efeito de guitarra que "fala" é um dos recursos mais expressivos, hipnóticos e instantaneamente reconhecíveis do Rock e da música moderna (*Peter Frampton - "Do You Feel Like We Do" e "Show Me the Way", Joe Walsh - "Rocky Mountain Way", Bon Jovi / Richie Sambora - "Livin' on a Prayer", Stevie Wonder, Pink Floyd - "Pigs", Daft Punk*). Historicamente, obter esse efeito exigia caixas mecânicas pesadas (*Heil Talk Box ou Rocktron Banshee*), onde um driver de compressão de corneta disparava o som da guitarra através de uma mangueira plástica inserida na boca do músico, exigindo um microfone de voz separado no palco. O UltraRig elimina toda a complexidade mecânica através da modelagem digital em tempo real das cavidades ressonantes do trato vocal.

---

## 1. A Física Acústica das Vogais Humanas: Formantes F1 e F2

Na voz humana falada ou cantada, as cordas vocais atuam como uma fonte de oscilação rica em harmônicos (equivalente à guitarra elétrica distorcida). Conforme o som viaja pela laringe, faringe, boca e lábios, essas cavidades ressonantes amplificam frequências específicas denominadas **Formantes (F1 e F2)**:

```
+---------------------------------------------------------------------------------------+
|                    O MAPA ACÚSTICO DOS FORMANTES DE VOGAIS HUMANAS                    |
+---------------------+-----------------------------+-----------------------------------+
| Vogal Fonética      | 1º Formante (F1 - Boca)     | 2º Formante (F2 - Língua/Lábios)  |
+---------------------+-----------------------------+-----------------------------------+
| "U" (Oooh / Bico)   | ~300 Hz (Grave fechado)     | ~850 Hz (Médio-grave oco)         |
+---------------------+-----------------------------+-----------------------------------+
| "O" (Ohhh / Aberto) | ~500 Hz (Médio encorpado)   | ~1.000 Hz (Médio central)         |
+---------------------+-----------------------------+-----------------------------------+
| "A" (Aaah / Aberto) | ~800 Hz (Médio ressonante)  | ~1.300 Hz (Médio-agudo vocal)     |
+---------------------+-----------------------------+-----------------------------------+
| "E" (Eeeh / Médio)  | ~450 Hz (Médio suave)       | ~1.900 Hz (Agudo brilhante)       |
+---------------------+-----------------------------+-----------------------------------+
| "I" (Iiih / Fechado)| ~280 Hz (Grave fechado)     | ~2.400 Hz (Agudo nasal penetrante)|
+---------------------+-----------------------------+-----------------------------------+
```

```
                     [ ESPAÇO BIDIMENSIONAL DE VOGAIS (F1 x F2) ]

           F2 (Hz) ▲
            2400   │      [ "I" ]
            1900   │                    [ "E" ]
            1300   │                                  [ "A" ]
            1000   │                    [ "O" ]
             850   │      [ "U" ]
                   └────────────────────────────────────────► F1 (Hz)
                         250    450    550    800
```

---

## 2. A Arquitetura DSP do Talk-Box Virtual no UltraRig

O UltraRig modela a física da boca utilizando múltiplos filtros passa-faixa ressonantes de alto fator de qualidade ($Q \ge 6$) operando em paralelo e interpolados continuamente:

```
                                  [ GUITARRA COM DISTORÇÃO / LEAD ]
                                                  │
                                                  ▼
                                      [ DIVISOR DE SINAL DSP ]
                                                  │
                            ┌─────────────────────┴─────────────────────┐
                            │                                           │
                            ▼                                           ▼
                 [ FILTRO FORMANTED F1 ]                     [ FILTRO FORMANTED F2 ]
                 (Varredura 280 Hz a 850 Hz)                 (Varredura 850 Hz a 2400 Hz)
                            │                                           │
                            └─────────────────────┬─────────────────────┘
                                                  │
                                                  ▼
                                       [ CONTROLADOR DE VOGAL ]
                                       - Modo A: Pedal de Expressão (Oo -> Aa -> Ee)
                                       - Modo B: Envelope de Palhetada (Dinâmico)
                                       - Modo C: LFO Rítmico Sincronizado
                                                  │
                                                  ▼
                                       [ SOMA VOCALIZADA ]
                                                  │
                                                  ▼
                                      [ CABINET IR / PA OUTPUT ]
```

### Por Que a Distorção Prévia é Essencial?
Um sinal de guitarra limpo puro contém pouca energia harmônica em altas frequências. Se passarmos um som limpo pelo filtro formante em "I" (que necessita de energia em $2.4\text{ kHz}$), a vogal soará fraca e apagada. Ao posicionar o **Fuzz, Overdrive ou Amplificador Saturado antes do Filtro Formante**, o espectro fica denso e repleto de harmônicos pares e ímpares, permitindo que as vogais "falem" com inteligibilidade impressionante!

---

## 3. Modos de Controle de Performance

1. **Expression Pedal Morph (O Controle do Pé Estilo Frampton / Sambora)**:
   - O pedal de expressão varre o caminho fonético contínuo:
     - `Calcanhar (0%)`: Vogal **"U"** (Grave, oco e fechado).
     - `Meio do Curso (50%)`: Vogal **"O" / "A"** (Abertura encorpada).
     - `Ponta do Pé (100%)`: Vogal **"E" / "I"** (Brilhante, cortante e estridente).
2. **Envelope-Driven Vowel (Articulação Automática pela Força da Palhetada)**:
   - Dispensa pedais: golpear a corda com força abre instantaneamente a vogal "Aaah", e conforme a nota perde volume e sustenta, a boca virtual fecha suavemente em "Oooh", gerando um efeito vocal orgânico e expressivo a cada frase de solo.

---

## 4. Presets de Performance em 4 Cenas (Scenes A/B/C/D)

```
+---------------------------------------------------------------------------------------+
|                 BANCO DE PRESET ULTRA-TALKBOX: 4 CENAS VOCALIZADAS                    |
+---------------------+-------------------+---------------------+-----------------------+
| Cena A: 1976        | Cena B: Funky     | Cena C: Vowel       | Cena D: Robot Choir   |
| Frampton Talk-Box   | Vocal Wah Morph   | Dynamic Lead        | Vocal Synthesizer     |
+---------------------+-------------------+---------------------+-----------------------+
```

### Cena A: 1976 Frampton Talk-Box Solo ("Do You Feel Like We Do")
- **Objetivo**: A lendária emulação do Heil Talk Box de Peter Frampton com controle total de vogais pelo **Pedal de Expressão**.
- **Módulo Formant Filter**:
  - `Control Source`: `EXPRESSION PEDAL`
  - `Start Vowel (Heel 0%)`: "U" (Oooh)
  - `Mid Vowel (50%)`: "A" (Aaah)
  - `End Vowel (Toe 100%)`: "E" (Eeeh)
  - `Resonance / Q`: 7.5 (Picos formantes pronunciados e vocais)
  - `Pre-Drive Engine`: British Plexi Cranked com booster limpo
- **Ambiência**: Analog Slapback Delay (Tempo 140 ms, Mix 22%) e Room Reverb.

### Cena B: Funky Vocal Wah Morph (Bon Jovi / Richie Sambora)
- **Objetivo**: O famoso riff rítmico falado de *"Livin' on a Prayer"*, com articulação rápida e percussiva casada com o andamento da bateria.
- **Módulo Formant Filter**:
  - `Control Source`: `LFO TEMPO SYNC`
  - `Vowel Sequence`: "O" -> "A" -> "O" -> "U"
  - `Rate`: Sincronizado em Colcheias (1/8)
  - `Pre-Drive`: Overdrive TS-808 denso nos médios
  - `Mix`: 85% Wet / 15% Dry

### Cena C: Vowel Dynamic Lead (Solos Melódicos Expressivos)
- **Objetivo**: Solo de alto ganho com articulação de vogais acionada pela dinâmica de palhetada (*estilo Joe Walsh / Steve Vai*).
- **Módulo Formant Filter**:
  - `Control Source`: `ENVELOPE DYNAMICS`
  - `Sensitivity`: 60%
  - `Resting Vowel (Sem Palhetar)`: "U"
  - `Hard Attack Vowel (Palhetada Forte)`: "A" e "E"
  - `Smoothing Decay`: 280 ms
- **Amp**: Modern Soldano SLO Lead channel com sustain infinito.

### Cena D: Robot Choir Vocal Synthesizer (Daft Punk / Sci-Fi)
- **Objetivo**: Textura polifônica de coral robótico espacial com formantes estéreo e delays espaciais.
- **Módulo Formant Filter**:
  - `Control Source`: `STEREO QUADRATURE LFO`
  - `Vowel Trajectory`: Canal L ("A" -> "E") | Canal R ("O" -> "U")
  - `Rate`: 0.35 Hz (Movimento lento de coral)
  - `Stereo Shimmer Reverb`: Cauda de 4.5s com oitava aguda (+12 semitons)

---

## 5. Dicas de Otimização e Execução Musical

1. **Equalização Pós-Formante**:
   - Como os filtros formantes possuem ressonâncias altas em $F_1$ e $F_2$, utilize um limitador suave pós-filtro para evitar que certas notas saltem de volume excessivamente quando coincidirem com a frequência central dos picos.
2. **Uso de Captador da Ponte**:
   - Para máxima clareza e inteligibilidade das vogais, utilize preferencialmente o **captador da ponte (Bridge)** com o tom aberto no máximo (10), garantindo um sinal farto em sobretons agudos para alimentar os formantes $F_2$.
