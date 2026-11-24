# Guia de Calibração e Roteamento de Auto-Pan Dinâmico e Espacialização Rítmica no UltraRig

Este documento estabelece os fundamentos psicoacústicos, leis de pan (*Pan Laws*), compatibilidade mono e métodos de calibração para o efeito de **Auto-Pan Dinâmico controlado por Envelope Follower** no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

Enquanto um auto-pan tradicional opera cegamente através de um oscilador de baixa frequência (LFO cíclico fixo), o **Auto-Pan Dinâmico** responde em tempo real à intensidade da palhetada e articulação do guitarrista: notas suaves permanecem focadas no centro estéreo, enquanto ataques fortes abrem o campo sonoro ou aceleram a rotação espacial, criando uma experiência tridimensional imersiva sem poluir a mixagem da banda.

---

## 1. Princípios Psicoacústicos e Leis de Pan (Pan Laws)

O movimento de uma fonte sonora no plano estéreo entre os canais Esquerdo (`L`) e Direito (`R`) envolve a conservação de potência acústica:

```
+-------------------------------------------------------------------------------+
|                       LEI DE PAN DE POTÊNCIA CONSTANTE (-3 dB)                |
|                                                                               |
|  Canal L: [ 0 dB ] --------> [ -3 dB no Centro ] --------> [ -infinito em R ] |
|  Canal R: [ -infinito em L ] -> [ -3 dB no Centro ] --------> [ 0 dB em R ]   |
|                                                                               |
|  * Resultado: Ao varrer de L para R, a soma da energia percebida pelo ouvido  |
|               humano permanece perfeitamente estável, sem quedas no centro.   |
+-------------------------------------------------------------------------------+
```

- **A Regra de Ouro da Compatibilidade Mono:**
  - Em sistemas de PA de clubes ou caixas bluetooth mono, os canais L e R são somados eletricamente (`L + R`).
  - Se o efeito estéreo utilizar cancelamento de fase artificial (como moduladores de fase estilo Haas sem proteção), a guitarra desaparece ao ser somada em mono.
  - O Auto-Pan Dinâmico do UltraRig utiliza modulação de amplitude e ganho cruzado real, garantindo **100% de compatibilidade mono** sem cancelamentos destrutivos.

---

## 2. LFO Cíclico Fixo vs. Envelope Follower Dinâmico

| Parâmetro | Auto-Pan Tradicional (LFO) | Auto-Pan Dinâmico (UltraRig Envelope) |
| :--- | :--- | :--- |
| **Gatilho de Controle** | Onda senoide/triangular contínua no tempo. | Dinâmica de palhetada da mão direita (milivolts do sinal). |
| **Comportamento em Palhetadas Suaves** | Continua rodando de um lado para o outro. | Permanece estável no centro estéreo, mantendo o foco harmônico. |
| **Comportamento em Ataques Acentuados** | Ignora a intensidade da execução. | Dispara varreduras rápidas para os extremos (`Hard L / Hard R`). |
| **Musicalidade no Palco** | Pode soar mecânico e cansativo após alguns compassos. | Soa como uma extensão orgânica da expressividade do músico. |

---

## 3. Topologias de Roteamento no UltraRig

### 3.1 Topologia 1: Pre-Delay Dynamic Panning (Ecos Saltitantes)

O sinal da guitarra passa pelo Auto-Pan Dinâmico antes de alimentar o bloco de Delay Estéreo:

```
Guitarra ---> [ Auto-Pan Dinâmico ] ---> [ Stereo Tape Delay ] ---> Saída L/R
                     |
         (Ataque forte joga para L) ----> Alimenta repetições da Esquerda
         (Próximo toque joga para R) ---> Alimenta repetições da Direita
```

- Ataques sucessivos de palheta distribuem sementes de eco alternadas entre a esquerda e a direita, criando um ping-pong natural que reflete a intensidade da levada rítmica.

### 3.2 Topologia 2: Wet-Only Ambient Panning (Guitarra Seca Firme no Centro)

Em solos de alto ganho, perder o centro da mixagem pode desorientar o público ou o próprio guitarrista nos fones:

```
                            +---> [ Ramo A: Solo Lead Direto ] ----------+
                            |     - Centro Fixo (Pan 0)                  |
                            |     - NAM High-Gain + 4x12 Cab             |
[ Entrada da Guitarra ] --->+                                            +---> [ Master ]
                            |                                            |
                            +---> [ Ramo B: Nuvem Espacial Dinâmica ] ---+
                                  - Reverb Hall Amplo (100% Wet)
                                  - Auto-Pan Dinâmico modulando a cauda
```

- A guitarra solo permanece firme, cortante e ancorada no centro do palco, enquanto a reverberação cósmica gira e se expande dinamicamente ao redor da cabeça do ouvinte.

### 3.3 Topologia 3: Frequency-Crossover Panning (Segurança de Subgraves)

Frequências abaixo de 150 Hz nunca devem oscilar no estéreo de um show, sob pena de desbalancear os subwoofers da casa:
- O divisor de frequência interno do UltraRig trava as frequências fundamentais (< 160 Hz) no centro mono.
- O Auto-Pan atua exclusivamente nos harmônicos médios e agudos (> 160 Hz).

---

## 4. Calibração Prática de Parâmetros

### 4.1 Sensitivity (Sensibilidade do Detector de Envelope)
- Ajuste de modo que um toque com dinâmica média (*mezzo-forte*) gere uma abertura estéreo moderada (**40% a 50% L/R**), reservando os extremos de **100%** apenas para palhetadas acentuadas de impacto.

### 4.2 Attack Time (Tempo de Resposta ao Ataque)
- **Para Efeito Percussivo Imediato:** **5 ms a 15 ms**. O sinal salta para o lado estéreo no mesmo instante em que a palheta encosta na corda.
- **Para Efeito de "Crescendo":** **30 ms a 60 ms**. O som começa no centro e viaja para a lateral suavemente conforme a nota sustenta.

### 4.3 Decay / Return Time (Tempo de Retorno ao Centro)
- **120 ms a 220 ms (Rápido):** Ideal para linhas rápidas de funk e riffs sincopados, retornando ao centro a tempo da próxima nota.
- **400 ms a 800 ms (Longo / Orgânico):** Ideal para baladas, dedilhados de violão e acordes ambientais sustentados.

### 4.4 Modos de Direção: Uni-direcional vs. Alternado (Ping-Pong)
- **Alternating (Flip-Flop):** Cada palhetada sucessiva inverte a direção (Nota 1 -> Esquerda, Nota 2 -> Direita, Nota 3 -> Esquerda).
- **Center-to-Sides (Dual Width):** O sinal se expande em largura estéreo simultaneamente para os dois lados conforme a dinâmica aumenta.

---

## 5. Arquitetura de 4 Cenas para Shows ao Vivo

```
+-------------------------------------------------------------------------------+
|             PRESET: "DYNAMIC-SPATIAL-PRO" (4 CENAS PROGRAMADAS)               |
|                                                                               |
|  [Scene A] CENTERED STUDIO RHYTHM (Foco e Clareza)                            |
|   - Auto-Pan: BYPASS (Pan fixo no centro)                                     |
|   - Compressor sutil + Room Reverb discreto (12% mix)                         |
|   - Máxima firmeza para bases rítmicas e levadas de apoio                     |
|                                                                               |
|  [Scene B] TOUCH DYNAMIC AUTO-PAN (Neo-Soul & Funk Chords)                    |
|   - Auto-Pan ativo (Sensitivity 60%, Width 75%)                              |
|   - Retorno rápido ao centro (Decay 180ms)                                    |
|   - Dedilhados suaves no centro; batidas fortes abrem o palco estéreo         |
|                                                                               |
|  [Scene C] WHIRLING ROTARY ACCELERATE (Emulação Leslie Dinâmica)              |
|   - O envelope de palhetada acelera o LFO de 0.8 Hz para 6.5 Hz              |
|   - Ataque com palheta pesada faz o som girar em redemoinho                   |
|   - Decaimento suave retornando à rotação lenta conforme a nota morre         |
|                                                                               |
|  [Scene D] PSYCHEDELIC PING-PONG DUB (Dub / Ambient Espacial)                 |
|   - Pre-Delay Dynamic Pan alternado (Flip-Flop)                               |
|   - Tape Delay estéreo com cross-feedback ativo (40% mix)                     |
|   - Cada acorde salta de um lado para o outro alimentando ecos infinitos      |
+-------------------------------------------------------------------------------+
```

---

## 6. Dicas de Monitoramento em Fones In-Ear (IEM Safety)

- **Cuidado com a Fadiga Auditiva:** Uma movimentação estéreo violenta de 0% a 100% em alta velocidade pode causar sensação de tontura ou labirintite em palcos usando fones *In-Ear*.
- **Ajuste Confortável para IEM:** Limite a largura máxima (**Stereo Width**) em **65% a 75%** nos seus fones pessoais, mantendo uma âncora perceptiva que preserve o equilíbrio espacial durante a performance.
