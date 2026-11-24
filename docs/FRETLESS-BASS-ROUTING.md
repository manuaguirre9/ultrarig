# Guia de Roteamento, Equalização Harmônica e Efeitos para Contrabaixo Fretless no UltraRig

Este documento aborda a física acústica, a equalização de médios vocais, a dinâmica de compressão e o processamento de modulação para **Contrabaixo Sem Trastes (Fretless Bass)** no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

Ao contrário do baixo elétrico convencional com trastes metálicos de níquel, o contrabaixo fretless depende do contato físico direto da corda de aço ou níquel contra a madeira crua ou resinada da escala (ébano, jacarandá, pau-ferro ou resina epóxi). Esse atrito dinâmico cria o lendário efeito vocal conhecido como **"Mwah"** (consagrado por Jaco Pastorius, Pino Palladino, Gary Willis e Mick Karn), que exige calibração tímbrica e dinâmica especializada.

---

## 1. A Física do Fenômeno "Mwah"

No contrabaixo com trastes, a nota é delimitada por um ponto fixo de metal rígido, resultando em um ataque percussivo imediato e decaimento com harmônicos estáveis.

No contrabaixo fretless:
1. **Ataque Suave e Arredondado:** A ponta do dedo do músico comprime a corda contra a madeira, absorvendo transientes ultrarrápidos e entregando um ataque aveludado.
2. **Florescimento Harmônico Dinâmico (The Bloom):** Conforme a corda vibra com grande amplitude nos primeiros milissegundos, ela roça suavemente contra a superfície plana do espelho de madeira. Esse micro-atrito contínuo introduz harmônicos superiores que "abrem" e cantam ao longo da sustentação da nota.
3. **Vibrato Longitudinal:** O vibrato no fretless é executado rolando a polpa do dedo paralelamente à corda (como em um violoncelo), gerando modulação contínua de pitch que exige espacialidade limpa no sinal.

---

## 2. Mapa de Frequências Críticas do Contrabaixo Fretless

```
+-------------------------------------------------------------------------------+
|                 ESPECTRO HARMÔNICO DO FRETLESS NO ULTRARIG                    |
|                                                                               |
|  [35-45 Hz]   [200-350 Hz]      [600-900 Hz]       [2.5-4 kHz]     [> 5 kHz]  |
|  Filtro HPF   Corte de "Mud"    ZONA DO "MWAH"     Atrito de Dedo  Ar / Estalo|
|  (Subgraves)  (Encaixe na mix)  (Médios Vocais)    (Atenuação)     (Smooth LPF|
+-------------------------------------------------------------------------------+
```

### 2.1 Subgraves e Fundamentais (HPF em 38 Hz – 45 Hz)
- O fretless precisa de graves limpos e firmes. Subgraves descontrolados abaixo de 40 Hz fazem o cone do alto-falante excursionar sem necessidade, mascarando a sutil florada de médios.
- Aplique um **High-Pass Filter (HPF) em 40 Hz (18 dB/oitava)**.

### 2.2 Controle de Ressonância Baixa (200 Hz – 350 Hz)
- Região propensa a acúmulo de som "oco" ou embolado, especialmente em instrumentos com corpo de mogno ou braço inteiriço (*neck-through*).
- Uma atenuação sutil de **-2.5 dB a -4.0 dB com Q médio (Q = 2.0)** em **250 Hz** limpa o timbre e dá espaço para o bumbo da bateria.

### 2.3 A Região Mágica do "Mwah" (600 Hz – 900 Hz)
- É aqui que reside a voz cantante e expressiva do fretless:
  - **Frequência Central Ideal:** **700 Hz a 800 Hz**.
  - **Ajuste no EQ Paramétrico:** Ganho suave de **+3.0 dB a +4.5 dB com Q musical (Q = 1.4 a 2.0)**.
  - Isso projeta o som das cordas roçando no espelho para a frente da mixagem sem soar nasal ou irritante.

### 2.4 Ruído de Atrito e Raspagem (2.5 kHz – 4 kHz)
- O atrito contínuo da pele dos dedos e unhas contra cordas *roundwound* pode soar excessivamente estalado ou áspero.
- Crie um corte leve do tipo *Bell* de **-2.0 dB a -3.0 dB em 3.2 kHz** para suavizar as passagens de mão.

---

## 3. Dinâmica e Compressão: Como Não Destruir o "Mwah"

Um erro frequente ao processar o baixo fretless é utilizar compressores ultrarrápidos (como emulações de *1176 FET* com ataque em microssegundos):
- **O Problema do Compressor Agressivo:** Um ataque ultrarrápido esmaga a dinâmica inicial e tenta nivelar a nota inteira, achatando a curva de subida natural dos harmônicos e eliminando a sensação de "canto" do instrumento.
- **A Solução (Compressor Óptico / Tube Style):**
  - **Attack Time:** Lento a moderado (**20 ms a 35 ms**). Permite que o transiente suave do dedo passe ileso.
  - **Release Time:** Suave e estendido (**250 ms a 400 ms**). Acompanha o decaimento vocal da nota enquanto o músico executa o vibrato.
  - **Ratio:** Entre **2.5:1 e 3.5:1** com atenuação máxima de **3 dB a 4 dB**.

---

## 4. Modulação Estéreo e Ambiência Espacial

O timbre do contrabaixo fretless é mundialmente associado a modulações aveludadas dos anos 80:

```
                            +---> [ Ramo A: Subgraves Mono ] --------+
                            |     - LPF 180 Hz                       |
                            |     - Som Direto / Punch Firme         |
[ Entrada do Fretless ] --->+                                        +---> [ Saída Master ]
                            |                                        |
                            +---> [ Ramo B: Harmônicos Estéreo ] ----+
                                  - HPF 180 Hz
                                  - Analog Stereo Chorus (Rate: 0.8 Hz)
                                  - Warm Plate Reverb (Decay: 1.6s)
```

### 4.1 Analog Chorus com Crossover de Frequência (Bass Chorus)
- O uso de chorus comum em todo o espectro faz com que as fundamentais graves oscilem de fase, perdendo peso e definição na bateria.
- No UltraRig, divida o sinal em ramos paralelos:
  - **Ramo A (Mono Lows):** Mantém as notas fundamentais abaixo de 180 Hz centradas e puras.
  - **Ramo B (Stereo Highs):** Aplica chorus analógico com *Rate* lento (0.7 Hz a 1.0 Hz) e *Depth* em 40% apenas nos médios e agudos, criando a clássica sonoridade de Pino Palladino.

### 4.2 Reverbs e Delays de Ambiência
- **Plate Reverb Suave:** Decay curto (1.4 s a 1.8 s) com corte de agudos em 4.5 kHz confere profundidade tridimensional para solos lentos e baladas.
- **Tape Delay Pontuado:** Em passagens melódicas, um delay suave de fita (mix 18%, feedback 25%) adiciona textura sem embolar a precisão da afinação.

---

## 5. Arquitetura de 4 Cenas para Shows ao Vivo

```
+-------------------------------------------------------------------------------+
|             PRESET: "FRETLESS-VOCAL-PRO" (4 CENAS PROGRAMADAS)                |
|                                                                               |
|  [Scene A] JACO PASTINI TONE (Puro Jazz Fusion)                               |
|   - Captador da ponte priorizado                                              |
|   - EQ: Boost +3.5 dB em 800 Hz (Mwah) + HPF 42 Hz                            |
|   - Compressor Óptico suave (Attack 25ms, Release 300ms)                      |
|   - Reverb Room curto (10% mix) para ambiência de madeira                     |
|                                                                               |
|  [Scene B] PINO 80s LUSH CHORUS (Pop & Baladas)                               |
|   - Crossover ativo: Graves limpos mono + Chorus estéreo nos agudos           |
|   - Warm Plate Reverb (1.8s decay, mix 22%)                                   |
|   - Timbre aveludado, cinematográfico e amplo                                 |
|                                                                               |
|  [Scene C] CONTEMPORARY MELODIC SOLO (Linhas Melódicas)                       |
|   - Scene Level: +3.0 dB                                                      |
|   - Boost adicional em 1.2 kHz para cortar a mixagem da banda                 |
|   - Tape Delay sincronizado (semínima pontuada, mix 24% com trails)           |
|   - Sustain cantado e vibrato estendido                                       |
|                                                                               |
|  [Scene D] DEEP UPRIGHT ACOUSTIC SIM (Pizzicato Amadeirado)                   |
|   - LPF suave em 4.0 kHz cortando ruídos de corda                             |
|   - Acoustic Body IR de contrabaixo acústico (mix 50%)                        |
|   - Som encorpado estilo contrabaixo acústico para MPB e Bossa Nova           |
+-------------------------------------------------------------------------------+
```

---

## 6. Dicas de Intonação e Afinação no UltraRig

Como o fretless não possui trastes físicos, a precisão microtonal do instrumentista é posta à prova:
- Ative o **Afinador Estroboscópico do UltraRig** (via *Hold* em um footswitch dedicado) no início e no meio do show.
- O modo estroboscópico oferece resolução de **0.1 centésimo**, permitindo checar não apenas as cordas soltas, mas calibrar a memória muscular das oitavas e quintas no espelho antes da apresentação.
