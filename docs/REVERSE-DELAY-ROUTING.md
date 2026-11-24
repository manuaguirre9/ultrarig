# Guia de Criação de Efeito Reverse Delay e Texturas Reversas Psicodélicas no UltraRig

Este documento aborda a física de fragmentação de memória circular (*Buffer Chunking*), janelamento de transição sem cliques (*Window Crossfading*), sincronismo métrico e topologias de roteamento para o efeito de **Reverse Delay (Eco Reverso)** no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

O efeito de fita invertida (*Backwards Tape*) — imortalizado por George Martin e The Beatles (*"Tomorrow Never Knows" e "I'm Only Sleeping"*), Jimi Hendrix (*"Castles Made of Sand"*), My Bloody Valentine no Shoegaze dos anos 90 e bandas modernas de Post-Rock e Dream Pop — transforma o decaimento percussivo de uma nota em um crescendo crescente (*swell*) que viaja de trás para frente no tempo. No processamento DSP de tempo real, o Reverse Delay exige calibração precisa de buffer e sincronismo rítmico para soar musical.

---

## 1. A Física do Reverse Delay Digital (O Paradoxo do Buffer)

Em estúdios analógicos dos anos 60, fitas de rolo magnético de 1/4" eram fisicamente desenroladas, viradas de cabeça para baixo e reproduzidas de trás para frente.

Em um processador digital de áudio em tempo real (DSP):
- **O Desafio:** O processador não pode adivinhar o futuro; ele só pode reproduzir o que já foi tocado.
- **A Solução (Ping-Pong Double Buffering):**
  1. O UltraRig grava o áudio que você toca em um bloco de memória RAM (*Buffer 1*) por uma janela de tempo definida (ex: 500 ms = uma semínima).
  2. No instante em que o Buffer 1 fica cheio, o firmware começa a ler e tocar essas amostras **de trás para frente (do final para o início)**.
  3. Simultaneamente, enquanto o Buffer 1 toca ao contrário, o UltraRig já está gravando as novas notas em um segundo bloco (*Buffer 2*).
  4. **Latência Inerente:** A primeira nota invertida só começará a soar exatamente após o tempo de uma janela de buffer completa.

```
Tempo:       0ms               500ms             1000ms            1500ms
Gravação:    [ Grava Bloco 1 ] [ Grava Bloco 2 ] [ Grava Bloco 3 ]
Reprodução:                    [ Toca Bloco 1 <] [ Toca Bloco 2 <] [ Toca Bloco 3 <]
                               (De trás p/ frente)
```

---

## 2. Eliminação de Cliques: Janelamento e Crossfading (Windowing)

Um problema clássico em algoritmos mal programados de reverse delay é o aparecimento de pequenos estalos digitais periódicos (*clicks / ticks*):
- **A Causa do Clique:** A última amostra lida ao contrário não termina no ponto zero de voltagem (*zero-crossing*), gerando uma descontinuidade abrupta na forma de onda.
- **A Solução no UltraRig:** O bloco de Reverse Delay aplica uma janela de envelope (*Hanning / Cosine Window*) com um micro-crossfade de **5 ms a 10 ms** nas extremidades de cada bloco gravado, garantindo transições perfeitamente contínuas e sem ruídos mecânicos.

---

## 3. Topologias de Roteamento no UltraRig

### 3.1 Modo 1: 100% Wet Killdry (Guitarra Reversa Pura)
- O sinal original direto da guitarra é completamente mutado (`Mix: 100% Wet` ou `Killdry: ON`).
- O ouvinte não ouve o ataque da palheta. Ouve-se apenas notas surgindo do silêncio em ondas crescentes aveludadas, criando a ilusão perfeita de violoncelos tocados ao contrário.
- Ideal para introduções psicodélicas, solos experimentais e trilhas sonoras.

### 3.2 Modo 2: Eco Reverso em Paralelo (Parallel Ghost Echoes)
- A guitarra seca permanece no Ramo A em tempo real (sem latência nos dedos).
- O Ramo B recebe o Reverse Delay com repetições ecoando ao contrário no fundo da mixagem.
- Permite manter o ritmo e a melodia perfeitamente inteligíveis enquanto uma cauda fantasmagórica cresce atrás de cada frase.

### 3.3 Modo 3: Pre-Fuzz Reverse Swell (A Técnica Secreta do Shoegaze)
- Em cadeias convencionais, o delay fica no final (pós-distorção).
- Ao posicionar o **Reverse Delay ANTES de um pedal de Fuzz de alto ganho**:
  - Conforme a nota invertida cresce em volume (*crescendo*), ela satura as válvulas ou transistores de fuzz progressivamente com mais intensidade.
  - A nota "explode" em distorção harmônica e sustentação no ápice de cada repetição, criando o som massivo de guitarras de Kevin Shields (*My Bloody Valentine*).

---

## 4. Calibração Rítmica: Tamanho de Janela vs. Andamento (BPM Sync)

O tamanho da janela de amostragem define a textura estética do efeito:

| Tamanho da Janela | Subdivisão Rítmica | Efeito Musical |
| :--- | :--- | :--- |
| **Curto (150 ms a 250 ms)** | Colcheia ou Semicolcheia | Repetições rápidas, estacatas e nervosas; textura glitch moderna. |
| **Médio (450 ms a 600 ms)** | Semínima (Quarter Note) | O clássico crescendo psicodélico dos Beatles e Hendrix. Tempo ideal para solos líricos. |
| **Longo (900 ms a 1500 ms)** | Mínima ou Semibreve | Nuvens majestosas e lentas de áudio; ideal para acordes abertos e post-rock ambiental. |

---

## 5. Arquitetura de 4 Cenas para Shows ao Vivo

```
+-------------------------------------------------------------------------------+
|             PRESET: "PSYCHEDELIC-REVERSE-PRO" (4 CENAS PROGRAMADAS)           |
|                                                                               |
|  [Scene A] BEATLES REVOLVER 100% WET (Backwards Solo Puro)                    |
|   - Mix: 100% Wet (Sem sinal direto)                                          |
|   - Buffer Chunk: Semínima sincronizada por Tap-Tempo (520ms)                  |
|   - Saturação quente de fita analógica + LPF em 5.0 kHz                       |
|   - Efeito psicodélico autêntico estilo "I'm Only Sleeping"                   |
|                                                                               |
|  [Scene B] CASTLES MADE OF SAND (Eco Reverso Paralelo)                        |
|   - Ramo A: Guitarra Limpa Fender Stratocaster (65% volume)                   |
|   - Ramo B: Reverse Delay (35% mix, Feedback 30%)                             |
|   - Ecos reversos flutuando suavemente atrás das frases de base               |
|                                                                               |
|  [Scene C] SHOEGAZE PRE-FUZZ EXPLOSION                                        |
|   - Reverse Delay posicionado ANTES do Silicon Fuzz                           |
|   - Crescendo de volume explodindo em saturação harmônica                     |
|   - Lush Plate Reverb posterior preenchendo a parede sonora                   |
|                                                                               |
|  [Scene D] INFINITE AMBIENT REVERSE CLOUD                                     |
|   - Buffer longo (1200ms) + Feedback elevado (70% com spillover)              |
|   - Pitch Shifter leve com micro-detune (+/- 4 cents)                         |
|   - Reverb Hall cósmico criando camadas infinitas para transições             |
+-------------------------------------------------------------------------------+
```

---

## 6. Dicas de Execução para Tocar em Reverse

1. **Compense a Latência de Janela:** Como a nota só começa a soar após o término da primeira janela do buffer, toque levemente adiantado ou deixe a primeira nota respirar antes de iniciar o tema.
2. **Uso de Palhetada Staccato:** Notas soltas tocadas com pausas claras entre si produzem os crescendos reversos mais definidos e dramáticos.
3. **Controle de Feedback:** Para evitar que o buffer acumule excesso de graves em repetições infinitas, ative o filtro passa-altas interno do delay (**HPF em 120 Hz**).
