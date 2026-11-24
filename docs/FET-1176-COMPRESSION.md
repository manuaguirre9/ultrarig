# Guia de Modelagem de Compressão FET Ultra-Rápida Estilo Urei 1176 no UltraRig

Este documento estabelece as diretrizes de processamento analógico-digital, atenuação por transistor de efeito de campo (FET), resposta transitória em microssegundos ($\mu\text{s}$), saturação de transformadores e calibração do lendário modo **All-Buttons-In ("British Mode")** para o compressor **FET 1176 Peak Limiter** no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

Concebido no final dos anos 1960 pelo pioneiro Bill Putnam Sr. (Universal Audio / Urei), o 1176 foi o primeiro compressor transistorizado de estado sólido a conquistar o mundo dos estúdios profissionais (*Led Zeppelin, Jimi Hendrix, Queen, Red Hot Chili Peppers, Green Day, Nirvana*). Se o óptico LA-2A é conhecido por sua suavidade aveludada e lenta, o FET 1176 é a antítese absoluta: é um processador dinâmico relâmpago, agressivo, percussivo e cheio de atitude harmônica nos médios, capaz de transformar notas frouxas de guitarra e baixo em socos sonoros definidos.

---

## 1. A Física do Atenuador FET e os Tempos em Microssegundos

Em vez de depender de lâmpadas fotoquímicas ou amplificadores operacionais integrados, o 1176 utiliza um **Transistor de Efeito de Campo (JFET)** operando em sua região ôhmica como um resistor variável governado por voltagem:

```
+---------------------------------------------------------------------------------------+
|                    DIAGRAMA DE ATENUAÇÃO DINÂMICA POR JFET (1176)                     |
|                                                                                       |
|   [ SINAL DE ÁUDIO ] ──────► [ RESISTOR FIXO ] ──┬──► [ AMP CLASSE A 1176 ] ──► SAÍDA|
|                                                  │                                    |
|                                                  ▼                                    |
|                                        [ TRANSISTOR JFET ]                            |
|                                        (Resistor Controlado por V)                    |
|                                                  │                                    |
|                                                  ▼                                    |
|                                               [ TERRA ]                               |
|                                                                                       |
|   ──► O circuito detector gera uma voltagem de controle negativa no Gate do JFET.     |
|       Conforme o sinal ultrapassa o limiar, o JFET drena o excesso instantaneamente   |
|       para o terra antes que qualquer overshoot atinja a saída!                       |
+---------------------------------------------------------------------------------------+
```

### A Velocidade em Microssegundos ($\mu\text{s}$):
- **Tempo de Ataque**: Varia de **$20\ \mu\text{s}$ a $800\ \mu\text{s}$** ($0.02\text{ ms}$ a $0.8\text{ ms}$)! É até 100 vezes mais rápido do que compressores convencionais, garantindo agarre imediato sobre o transiente inicial mais violento da palheta.
- **Tempo de Release**: Varia de **$50\text{ ms}$ a $1.100\text{ ms}$** ($1.1\text{ s}$).
- **Regra Contraintuitiva dos Controles**:
  - No 1176, a numeração dos knobs é invertida: **7 é o mais rápido e 1 é o mais lento**!

---

## 2. A Saturação de Transformadores e o Modo "All-Buttons-In" (British Mode)

No hardware original, a seleção de ratio era feita por quatro botões mecânicos de pressão independentes: `4:1`, `8:1`, `12:1` e `20:1`.

```
+---------------------------------------------------------------------------------------+
|                 O LENDÁRIO MODO "ALL-BUTTONS-IN" (MODO BRITÂNICO)                     |
|                                                                                       |
|  Na década de 1970, engenheiros de gravação em Londres descobriram que era possível   |
|  pressionar os quatro botões de ratio SIMULTANEAMENTE!                                |
|                                                                                       |
|  O que acontece eletricamente no circuito do 1176:                                   |
|  1. A tensão de polarização (bias) das linhas de controle do JFET é descalibrada.     |
|  2. O joelho de compressão se deforma em uma curva irregular e hiper-agressiva.       |
|  3. O tempo de release adquire um atraso inicial antes de recuperar o ganho.          |
|  4. Os transformadores de saída entram em saturação pesada de 3ª ordem.               |
|                                                                                       |
|  ──► Efeito Sonoro: Uma compressão esmagadora, violenta e explosiva que faz os        |
|      harmônicos de médios "saltarem da caixa" com atitude crua de Rock pesado!        |
+---------------------------------------------------------------------------------------+
```

No UltraRig, o seletor de ratio inclui explicitamente a emulação `ALL-BUTTONS-IN (BRITISH CRUSH)`, recriando com exatidão a deformação não-linear e a saturação harmônica lendária do hardware analógico.

---

## 3. Aplicações Tímbricas na Guitarra e no Contrabaixo

```
+---------------------------------------------------------------------------------------+
|                    APLICAÇÕES PRINCIPAIS DO FET 1176 NO ULTRARIG                      |
+---------------------+-------------------+---------------------------------------------+
| Instrumento         | Ajuste Típico     | Resultado Acústico                          |
+---------------------+-------------------+---------------------------------------------+
| Guitarra Funk / Pop | Ratio 4:1         | O estalo percussivo clássico de Nile        |
| (Nile Rodgers / R&B)| Attack 3 / Rel 7  | Rodgers: palhetadas rápidas em semicolcheias|
|                     |                   | com nível uniforme e estalo brilhante.      |
+---------------------+-------------------+---------------------------------------------+
| Solos de Rock & Lead| All-Buttons-In    | Sustentação infinita e agressiva, onde cada |
| (Led Zeppelin/Slash)| Attack 5 / Rel 6  | nota mastiga os médios com punch demolidor. |
+---------------------+-------------------+---------------------------------------------+
| Slap Bass Agressivo | Ratio 8:1         | Segura com velocidade relâmpago os picos das|
| (Flea / Funk Rock)  | Attack 7 / Rel 5  | puxadas de slap sem clipar os alto-falantes.|
+---------------------+-------------------+---------------------------------------------+
```

---

## 4. Presets de Performance em 4 Cenas (Scenes A/B/C/D)

```
+---------------------------------------------------------------------------------------+
|                 BANCO DE PRESET ULTRA-1176: 4 CENAS DE IMPACTO DINÂMICO               |
+---------------------+-------------------+---------------------+-----------------------+
| Cena A: Classic     | Cena B: British   | Cena C: Aggressive  | Cena D: Super-Fast    |
| Punchy Clean Funk   | All-Buttons Crush | Bass Rock Snarl     | Slap Peak Tamer       |
+---------------------+-------------------+---------------------+-----------------------+
```

### Cena A: Classic Punchy Clean Funk (Nile Rodgers / Chic / Daft Punk)
- **Objetivo**: A lendária base limpa, percussiva, rápida e brilhante para palhetadas rápidas de funk e pop moderno.
- **Módulo FET 1176**:
  - `Model`: `FET 1176 VINTAGE BLACKFACE`
  - `Ratio`: 4:1 (Aperto musical transparente)
  - `Input (Threshold Drive)`: Ajustado para -4 dB a -6 dB de Gain Reduction
  - `Attack Time`: 3 (Ataque moderado de ~400 μs, deixa passar o estalo inicial)
  - `Release Time`: 7 (Recuperação ultra rápida de 50 ms para não amassar as próximas notas)
  - `Output (Makeup)`: +4.0 dB
- **Amp / Cab**: Roland JC-120 limpo com chorus suave desativável.

### Cena B: British All-Buttons Crush (Led Zeppelin / Hard Rock Solos)
- **Objetivo**: O som explosivo, esmagador e saturado de guitarras de arena dos anos 1970 (*estilo Jimmy Page e Slash*).
- **Módulo FET 1176**:
  - `Model`: `FET 1176 BRITISH MODE`
  - `Ratio`: `ALL-BUTTONS-IN (4/8/12/20)`
  - `Input`: Ganho pesado atingindo -10 dB a -12 dB de compressão violenta
  - `Attack Time`: 5 (Rápido)
  - `Release Time`: 6 (Recuperação agressiva com respiração rítmica)
  - `Transformer Saturation`: 45% (Ricas harmônicas ímpares nos médios)
- **Amp**: British Marshall Plexi 1959 no canal saturado com IR 4x12 Greenback.

### Cena C: Aggressive Bass Rock Snarl (Duff McKagan / Tim Commerford)
- **Objetivo**: Baixo elétrico com mordida percussiva, rosnado nos médios e sustentação sólida para cortar duas guitarras pesadas no palco.
- **Módulo FET 1176**:
  - `Ratio`: 8:1
  - `Attack Time`: 4
  - `Release Time`: 6
  - `Input`: Nivelado para -6 dB de atenuação contínua
  - `SVT Tube Preamp`: Ganho moderado adicionando sujeira analógica
- **Amp / Cab**: Ampeg SVT Classic com caixa 8x10.

### Cena D: Super-Fast Slap Peak Tamer (Baixo Moderno / Violão Percussivo)
- **Objetivo**: Tolerância zero para disparos de volume descontrolados em puxadas fortes (*pops*) de slap ou batidas no tampo.
- **Módulo FET 1176**:
  - `Ratio`: 12:1 (Quase limitador puro)
  - `Attack Time`: 7 (Velocidade máxima de 20 microssegundos!)
  - `Release Time`: 4
  - `Output Ceiling`: -1.5 dBFS (Proteção estrita de conversores)
- **Uso**: Ideal para manter consistência absoluta em apresentações ao vivo.

---

## 5. Dicas de Otimização no UltraRig

1. **Ajuste de Ganho de Entrada (*Input*) como Limiar**:
   - Como no 1176 não existe um controle separado de "Threshold", aumentar o knob `Input` empurra o sinal mais fundo contra o limiar fixo, aumentando simultaneamente o ganho e a quantidade de compressão. Em seguida, use o knob `Output` para compensar o nível final.
2. **Combinação Lendária LA-2A + 1176 (Serial Stacking)**:
   - Uma das cadeias de estúdio mais reverenciadas do mundo é colocar o **1176 primeiro** (com ataque rápido de 20 μs segurando apenas os 2 ou 3 dB dos picos mais rápidos) seguido do **LA-2A segundo** (com sua célula T4B aveludada oferecendo 2 a 3 dB de sustentação cremosa). No UltraRig, essa combinação produz o timbre definitivo de guitarra solo.
