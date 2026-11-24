# Guia de Afinação Microtonal, Teoria dos Maqamat Orientais e Roteamento no UltraRig

Este documento estabelece as diretrizes de engenharia eletroacústica, quantização microtonal em tempo real, tabelas de afinação não-temperadas (*Custom Cents Tuning Tables*) e técnicas de performance para **Escalas Microtonais, Maqamat do Oriente Médio e Ragas Indianas** no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

O sistema temperado ocidental padrão de 12 semitons iguais (*12-EDO / 12 Equal Divisions of the Octave*) é apenas uma convenção geométrica moderna que dividiu a oitava em 12 fatias de 100 cents. No entanto, civilizações milenares e tradições musicais monumentais como a Música Árabe, Turca, Persa e Indiana utilizam sistemas microtonais complexos baseados em quartos de tom (*quarter-tones / 24-EDO*) e comas microtonais (*shrutis e komas*). Instrumentos ancestrais como o *Oud, o Saz / Bağlama turco, a Cítara (Sitar) e o Tar persa* alcançam notas que residem exatamente "no espaço vazio entre os trastes de metal" de uma guitarra comum ocidental.

---

## 1. A Teoria Musical dos Maqamat: Quartos de Tom e Meio-Bemóis

Na música modal do Oriente Médio (*Maqam* no plural *Maqamat*), o semitom temperado ocidental de 100 cents é frequentemente substituído por intervalos neutros de **três quartos de tom ($\approx 150\text{ cents}$)**, gerando notas microtonais emblemáticas como o **meio-bemol ($\text{d}$)** e o **meio-sustenido ($\ddagger$)**:

```
+---------------------------------------------------------------------------------------+
|                    COMPARAÇÃO: ESCALA TEMPERADA vs. MAQAMAT ORIENTAIS                |
+---------------------+-----------------------------+-----------------------------------+
| Escala / Modo       | Estrutura de Notas e Cents  | Clima Emocional e Aplicação       |
+---------------------+-----------------------------+-----------------------------------+
| Escala Ocidental    | C (0) - D (200) - E (400)   | Tonalidade temperada com terças   |
| Maior Tradicional   | - F (500) - G (700) - A(900)| maiores puras ou menores estritas.|
+---------------------+-----------------------------+-----------------------------------+
| Maqam Bayati        | D (0) - E d (150) - F (300) | O som mais icônico e melancólico  |
| (Tônica em Ré)      | - G (500) - A (700) - Bb    | do Oriente Médio; a 2ª nota (Mi)  |
|                     | (800) - C (1000) - D (1200) | é afinada 50 cents abaixo de E!   |
+---------------------+-----------------------------+-----------------------------------+
| Maqam Rast          | C (0) - D (200) - E d (350) | Majestoso, solene e alegre; possui|
| (Tônica em Dó)      | - F (500) - G (700) - A(900)| a famosa 3ª neutra (350 cents)    |
|                     | - B d (1050) - C (1200)     | e a 7ª neutra (1050 cents).       |
+---------------------+-----------------------------+-----------------------------------+
| Maqam Hijaz         | D (0) - Eb (100) - F# (400) | Tensão mística com segunda menor  |
| (Tônica em Ré)      | - G (500) - A (700) - Bb    | e segunda aumentada expressiva.   |
|                     | (800) - C (1000) - D (1200) |                                   |
+---------------------+-----------------------------+-----------------------------------+
```

---

## 2. A Arquitetura DSP: Quantizador Microtonal em Tempo Real

Em guitarras convencionais ocidentais com trastes retos de metal (*fretted guitars*), é fisicamente impossível tocar um Mi meio-bemol ($E\text{d}$) pressionando um traste sem fazer um bend microtonal cirúrgico.

O UltraRig soluciona essa barreira física através de um **Módulo Retuner Microtonal em Ponto Flutuante**:

```
                            [ GUITARRA OCIDENTAL COM TRASTES ]
                                            │
                                            ▼
                           [ DETECTOR DE PITCH ULTRA-RÁPIDO ]
                           (Mede frequência fundamental f0 em < 8 ms)
                                            │
                                            ▼
                           [ TABELA DE QUANTIZAÇÃO MAQAM ]
                           (Aplica offset em cents para cada nota tocada:
                            Ex: ao pressionar a nota Mi, reduz -50 cents)
                                            │
                                            ▼
                           [ PITCH-SHIFTER MICROTONAL TRANSPARENTE ]
                           (Sem alteração de formantes de madeira)
                                            │
                       ┌────────────────────┴────────────────────┐
                       │                                         │
                       ▼                                         ▼
            [ SINAL MICROTONAL LEAD ]                 [ GERADOR DE DRONE MODAL ]
            (Solo expressivo afinado)                 (Tanpura virtual contínua tônica)
                       │                                         │
                       └────────────────────┬────────────────────┘
                                            │
                                            ▼
                               [ TAPE DELAY + HALL REVERB ]
                                            │
                                            ▼
                               [ SAÍDAS ESTÉREO MASTER ]
```

---

## 3. O Gerador de Drone Virtual (Virtual Tanpura / Drone)

A música oriental e as ragas indianas não utilizam progressões de acordes ocidentais funcionais (I - IV - V): todo o movimento harmônico acontece em relação a uma nota tônica sustentada continuamente (*Drone* ou *Tanpura*).

No UltraRig, o gerador de drone integrado permite sintetizar em segundo plano a fundamental ($D$) e a quinta justa ($A$) com harmônicos aveludados de cítara ou oud, criando o alicerce acústico perfeito para o guitarrista solar por cima com escalas microtonais autênticas.

---

## 4. Presets de Performance em 4 Cenas (Scenes A/B/C/D)

```
+---------------------------------------------------------------------------------------+
|                 BANCO DE PRESET ULTRA-MAQAM: 4 CENAS ORIENTAIS                        |
+---------------------+-------------------+---------------------+-----------------------+
| Cena A: Maqam       | Cena B: Indian    | Cena C: 24-TET      | Cena D: Turkish       |
| Bayati Solo         | Raga Sitar Drone  | Microtonal Blues    | Saz / Baglama Chime   |
+---------------------+-------------------+---------------------+-----------------------+
```

### Cena A: Maqam Bayati Solo (Melodia Árabe Melancólica)
- **Objetivo**: O solo oriental definitivo no modo Bayati, onde a segunda nota da escala (Mi) é convertida automaticamente em meio-bemol (-50 cents).
- **Módulo Microtonal Retuner**:
  - `Scale Mode`: `MAQAM BAYATI (Key: D)`
  - `Cent Offsets`: D: 0, E: -50 cents, F: 0, G: 0, A: 0, Bb: 0, C: 0
  - `Glissando Bending Smoothing`: Fluido (Preserva bends de até 1/4 de tom perfeitamente)
  - `Formant Lock`: Ativo (Preserva o timbre natural das cordas da guitarra)
- **Drone de Fundo**: Ativo na nota D com 15% de volume de mix.
- **Ambiência**: Warm Plate Reverb (Decay 2.5s, Mix 25%) e Tape Delay (Tempo 440 ms, Mix 20%).

### Cena B: Indian Raga Sitar Drone (Raga Bhairav / Ravi Shankar)
- **Objetivo**: Emulação de cítara indiana com zumbido harmônico de cordas simpáticas (*jawari buzz*) e drone contínuo de tambura em D e A.
- **Módulo Microtonal**:
  - `Scale Mode`: `RAGA BHAIRAV` (Offsets precisos de shrutis na 2ª e na 6ª notas)
  - `Jawari Resonance Filter`: Ativo (Gera o estalo característico de cítara na ponte de osso)
  - `Drone Oscillator`: Ativo em D2 + A2 (Mix 22%)
- **Amp**: Clean acústico com alto-falante JBL de resposta plana.

### Cena C: 24-TET Microtonal Blues Shifting (King Gizzard / Blues Oriental)
- **Objetivo**: Acesso a todos os 24 quartos de tom da oitava (passos exatos de 50 cents). Permite tocar a lendária "Blue Note Neutra" (a terça neutra entre o menor e o maior) utilizada por lendas do blues elétrico (*King Gizzard & The Lizard Wizard*).
- **Módulo Microtonal**:
  - `Scale Mode`: `24-EDO CHROMATIC QUARTER-TONES`
  - `Drive`: Fuzz Face moderado com saturação espessa
  - `Mix`: 100% Retuned
- **Amp**: British Plexi vintage cranked.

### Cena D: Turkish Saz / Bağlama Chime (Cordas Duplas Brilhantes)
- **Objetivo**: O ataque brilhante, percussivo e metálico do Saz turco de braço longo (*Uzun Sap Bağlama*), com afinação microtonal do modo Ussak.
- **Módulo Microtonal**:
  - `Scale Mode`: `TURKISH USSAK / RAST`
  - `Stereo Doubler`: Emulação de cordas duplas metálicas com detune de $\pm 5\text{ cents}$
  - `High-Pass Filter`: 140 Hz
  - `Presence Boost`: +3.5 dB em 4.5 kHz para destacar o estalo de palheta de cerejeira (*mızrap*)
- **Ambiência**: Small Eastern Hall Reverb (Decay 1.6s).

---

## 5. Dicas de Otimização e Execução Musical

1. **Clareza de Notas em Solos Microtonais**:
   - Para que o quantizador microtonal identifique a nota com perfeição e aplique o deslocamento de cents correto em tempo real, toque melodias monofônicas límpidas, abafando as cordas soltas com a mão esquerda.
2. **Combinação com Bends Expressivos**:
   - Ao executar bends na guitarra, o algoritmo do UltraRig reconhece a intenção de vibrato contínuo e permite que o bend escorregue suavemente através dos microtons sem "travar" ou dar saltos artificiais de afinação.
