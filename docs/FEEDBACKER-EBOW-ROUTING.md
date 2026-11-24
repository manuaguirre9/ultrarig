# Guia de Modelagem de Feedback Sustentado Controlado e E-Bow Virtual no UltraRig

Este documento estabelece as diretrizes de processamento digital de sinais (DSP), física de acoplamento acústico eletromecânico, síntese de harmônicos superiores e técnicas de performance em palco para o gerador de **Feedback Sustentado e E-Bow Virtual (*Feedbacker & Infinite Sustainer*)** no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

A microfonia harmônica musical (*harmonic feedback*) e a sustentação infinita são dois dos recursos mais viscerais e icônicos da guitarra elétrica (*Jimi Hendrix - "Foxey Lady", Carlos Santana - "Europa", The Beatles - "I Feel Fine", The Edge / U2 - "With or Without You", Radiohead - "My Iron Lung"*). No entanto, em palcos modernos silenciosos (*silent stages*) com monitoração exclusiva por fones in-ear, ou em gravações de estúdio e prática em fones, o volume acústico do ambiente é nulo, tornando fisicamente impossível obter o acoplamento natural entre o alto-falante e as cordas da guitarra.

---

## 1. A Física da Realimentação Acústica Natural vs. Modelagem DSP

```
+---------------------------------------------------------------------------------------+
|                 FEEDBACK ACÚSTICO NATURAL vs. DSP FEEDBACKER NO ULTRARIG              |
+---------------------+-----------------------------+-----------------------------------+
| Abordagem           | Mecanismo Físico            | Limitações no Mundo Real          |
+---------------------+-----------------------------+-----------------------------------+
| Feedback Acústico   | O alto-falante de 12" emite | Requer volume ensurdecedor (>105  |
| Natural de Palco    | pressão sonora no ar que faz| dB SPL). Impossível em palcos com |
| (Amplificador Real) | a corda da guitarra vibrar  | in-ears, estúdios residenciais ou |
|                     | continuamente por simpatia. | gravações noturnas silenciosas.   |
+---------------------+-----------------------------+-----------------------------------+
| UltraRig Virtual    | O algoritmo detecta a nota  | Funciona em qualquer volume       |
| Feedbacker & E-Bow  | tocada e gera o harmônico   | (inclusive em fones de ouvido no  |
| DSP Engine          | com curva de fade-in gradual| quarto!). Controle total de ativação|
|                     | e sustentação infinita.     | via footswitch momentâneo (Hold). |
+---------------------+-----------------------------+-----------------------------------+
```

---

## 2. A Arquitetura DSP: Detecção de Pitch e Geração Harmônica

O módulo opera em paralelo com o sinal direto da guitarra para que o timbre original do amplificador não seja afetado:

```
                            [ ENTRADA DA GUITARRA ]
                                       │
            ┌──────────────────────────┴──────────────────────────┐
            │                                                     │
            ▼                                                     ▼
   [ SINAL PRINCIPAL (DRY) ]                            [ RASTREADOR DE PITCH ]
   (Comp ──► Amp ──► Cab IR)                            (Mede frequência fundamental f0)
            │                                                     │
            │                                                     ▼
            │                                           [ GERADOR DE HARMÔNICOS ]
            │                                           (Uníssono, +1 Oct, +5th, E-Bow)
            │                                                     │
            │                                                     ▼
            │                                           [ ONSET BLOOM / FADE-IN ]
            │                                           (Rampa gradual de 0.5s a 2.0s)
            │                                                     │
            │                                                     ▼
            │                                           [ FOSTER RESSONANT FILTER ]
            │                                           (Amortece agudos sintéticos)
            │                                                     │
            └──────────────────────────┬──────────────────────────┘
                                       │
                                       ▼
                            [ SOMA DE SINAIS WET/DRY ]
                                       │
                                       ▼
                            [ SAÍDAS MASTER DO PEDAL ]
```

### Modos Harmônicos Disponíveis:
1. **Unison (Fundamental)**:
   - Mantém a nota exata que foi tocada sustentando-se eternamente, sem salto de oitava. Ideal para baladas lentas e notas longas de violino.
2. **+1 Oitava Acima (Octave Bloom - Modo Hendrix/Santana)**:
   - A nota começa com o ataque natural da palheta na afinação original; após 1 segundo de sustentação, o harmônico da oitava superior desabrocha (*blooms*) com timbre cantado e brilhante.
3. **+5ª Harmônica (Natural 5th Overtone)**:
   - Simula o acoplamento físico em caixas 4x12 empurradas em volume de arena, onde o nó harmônico de quinta justa acima da oitava é excitado pela ressonância da sala.
4. **E-Bow Virtual (Arco Eletrônico Contínuo)**:
   - Emula o clássico dispositivo manual *Heet Sound E-Bow*. A nota perde o ataque percussivo da palheta e adquire um envelope contínuo com ataque macio e sustentação infinita estilo violoncelo (*estilo The Edge em "With or Without You"*).

---

## 3. Controle de Performance: Footswitch Momentâneo (Hold Mode)

A maior vantagem do gerador virtual no UltraRig é o **controle absoluto**: em amplificadores reais, o feedback muitas vezes foge do controle e se transforma em um apito agudo incontrolável. No UltraRig:

```
Pisar no Footswitch (Hold) ──► O harmônico desabrocha suavemente (Onset Bloom)
Segurar o Footswitch       ──► Sustentação infinita da nota pelo tempo que desejar
Soltar o Footswitch        ──► O feedback cessa instantaneamente com cauda natural
```

- **Mapeamento Prático**: Configure o Footswitch 3 (ou pedal auxiliar externo) no modo `MOMENTARY FEEDBACK`. Ao final de um solo de guitarra, basta pisar e manter o pé no botão para congelar a nota final em uma onda harmônica majestosa.

---

## 4. Presets de Performance em 4 Cenas (Scenes A/B/C/D)

```
+---------------------------------------------------------------------------------------+
|                 BANCO DE PRESET ULTRA-FEEDBACK: 4 CENAS DE SUSTENTAÇÃO                |
+---------------------+-------------------+---------------------+-----------------------+
| Cena A: Hendrix     | Cena B: 80s Rock  | Cena C: Virtual     | Cena D: Feedbacker    |
| Woodstock Bloom     | Sustainer Lead    | E-Bow Cello Pad     | Whammy Dive           |
+---------------------+-------------------+---------------------+-----------------------+
```

### Cena A: Jimi Hendrix Woodstock Bloom (+1 Oitava Cantante)
- **Objetivo**: A simulação definitiva de aproximar a guitarra a 30 centímetros dos cones de um amplificador Marshall valvulado saturado.
- **Módulo Feedbacker**:
  - `Harmonic Mode`: `+1 OCTAVE ABOVE`
  - `Onset Time (Rampa de Início)`: 0.9 s (Permite palhetar notas rápidas sem disparar o feedback)
  - `Feedback Gain`: 75%
  - `High-Cut Filter`: 4.8 kHz (Evita estridência de apito)
  - `Footswitch Trigger`: Momentary Hold
- **Amp / Drive**: Marshall 1959 Super Lead com Fuzz Face de Silício.

### Cena B: 80s Rock Sustainer Lead (Carlos Santana / Neal Schon)
- **Objetivo**: Sustentação lírica perfeita para solos lentos e melódicos em estádios, onde cada nota se transforma em uma onda aveludada.
- **Módulo Feedbacker**:
  - `Harmonic Mode`: `5TH OVERTONE (Quinta Harmônica Natural)`
  - `Onset Time`: 1.4 s
  - `Feedback Gain`: 68%
  - `Vibrato Sensitivity`: Alta (Acompanha o vibrato manual de dedos sem engasgos)
- **Ambiência**: Stereo Tape Delay (Tempo 420 ms, Mix 25%) + Hall Reverb (Decay 2.4s).

### Cena C: Virtual E-Bow Cello Pad (The Edge / Post-Rock)
- **Objetivo**: Som contínuo de arco eletrônico, sem ruído de palheta, transformando a guitarra em um violoncelo orquestral cósmico.
- **Módulo Feedbacker**:
  - `Harmonic Mode`: `UNISON E-BOW`
  - `Onset Time`: 0.3 s (Ataque ultra rápido com rampa macia)
  - `Dry Signal Level`: 40% (Atenuado para dar destaque ao arco sustentado)
  - `Feedback Gain`: 90% (Sustentação 100% contínua)
- **Ambiência**: Shimmer Reverb catedral com oitava acima (Mix 40%, Decay 6.0s).

### Cena D: Feedbacker Whammy Dive (Pitch Shift Dinâmico)
- **Objetivo**: Acoplar o harmônico sustentado ao **Pedal de Expressão**, permitindo fazer mergulhos de alavanca (*dive bombs*) e subidas de oitava na nota que está sustentando.
- **Mapeamento de Expressão**:
  - `Exp Pedal Target`: `Feedback Pitch Shift (-24 a +12 semitons)`
  - `Harmonic Mode`: Unison / +1 Octave Blend
  - `Gain`: 85%
- **Uso**: Segure a nota com o footswitch e mova o pedal de expressão para criar bends cósmicos infinitos estilo David Gilmour ou Tom Morello.

---

## 5. Dicas de Otimização e Execução Musical

1. **Evite Cordas Soltas Vibrando Simultanamente**:
   - Para que o rastreador de pitch gere um harmônico puro e cantante, silencie as cordas adjacentes com a mão direita (*palm muting*) ou esquerda.
2. **Uso de Captador do Braço vs. Ponte**:
   - **Captador do Braço (Neck)**: Produz o feedback mais redondo, aveludado e vocal (ideal para as Cenas A e C).
   - **Captador da Ponte (Bridge)**: Gera harmônicos mais agudos, cortantes e agressivos (ideal para as Cenas B e D).
