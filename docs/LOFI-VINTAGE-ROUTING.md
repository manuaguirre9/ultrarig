# Guia de Modelagem e Roteamento de Efeitos Lo-Fi Vintage (Cassete, Vinil, Megafone e Rádio AM) no UltraRig

Este documento orienta sobre a modelagem de degradação analógica intencional, restrição de largura de banda, instabilidade mecânica de afinação (*Wow & Flutter*), saturação de fita magnética e compressão de vinil para timbres **Lo-Fi (Low Fidelity)** e vintage no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

Enquanto os processadores modernos de guitarra buscam conversores cristalinos e respostas de frequência perfeitas (20 Hz a 20 kHz), a estética Lo-Fi (popularizada no *Neo-Soul, Indie Pop, Lo-Fi Hip-Hop, Dream Pop e Shoegaze* — artistas como Mac DeMarco, Tom Misch, Boy Pablo e Khruangbin) exige a escultura deliberada de imperfeições mecânicas analógicas.

---

## 1. Os Quatro Pilares Acústicos do Timbre Lo-Fi

Para criar um timbre vintage autêntico no UltraRig, é necessário combinar quatro processos físicos fundamentais:

```
+-------------------------------------------------------------------------------+
|                       ARQUITETURA DE MODELAGEM LO-FI                          |
|                                                                               |
|  [ Sinal Puro da Guitarra ]                                                   |
|             |                                                                 |
|             v                                                                 |
|  [ 1. Saturação Harmônica / Tape Drive ] ----> Compressão aveludada de fita   |
|             |                                                                 |
|             v                                                                 |
|  [ 2. Pitch Instability (Wow & Flutter) ] ---> Modulação mecânica de pitch    |
|             |                                                                 |
|             v                                                                 |
|  [ 3. Bandwidth Limiter (HPF / LPF) ] -------> Corta extremos de frequência   |
|             |                                                                 |
|             v                                                                 |
|  [ 4. Ambiência Analógica (Spring/Room) ] ---> Espaço sonoro nostálgico       |
+-------------------------------------------------------------------------------+
```

---

## 2. Restrição de Banda: O Efeito Megafone, Telefone e Rádio AM

A assinatura mais marcante de transmissões analógicas antigas ou alto-falantes de baixa potência é a ausência de subgraves e agudos arejados:

### 2.1 Efeito Telefone Antigo / Intercomunicador
- **Filtro Passa-Altas (HPF):** Corte agressivo em **450 Hz a 550 Hz (24 dB/oitava)**. Elimina qualquer corpo de grave.
- **Filtro Passa-Baixas (LPF):** Corte em **3.0 kHz a 3.5 kHz (24 dB/oitava)**. Remove o brilho moderno das cordas.
- **Pico Ressonante de Médios:** Aplique um ganho estreito (Q = 3.5) de **+4 dB a +6 dB em 1.8 kHz**. Isso emula a ressonância mecânica do diafragma metálico de um fone antigo.

### 2.2 Efeito Rádio AM / Transistor Portátil
- **HPF:** **300 Hz**.
- **LPF:** **4.2 kHz**.
- **Saturação:** Adicione uma leve saturação assimétrica (bloco de Overdrive com ganho em 15%) para gerar distorção harmônica típica de transistores de germânio operando no limite.

---

## 3. Instabilidade Mecânica de Fita: Wow & Flutter

Fitas cassete antigas (Walkman, decks Tascam Portastudio de 4 canais) sofrem de imperfeições de rotação no motor mecânico e correias de borracha ressecadas:

```
          [ Wow: Oscilação Lenta (0.3 Hz a 1.2 Hz) - Deriva de afinação ]
Forma de Onda: ~~~~~~~~~~/\~~~~~~~~~~~~~~\/~~~~~~~~~~~~
          [ Flutter: Vibração Rápida (4 Hz a 8 Hz) - Tremor mecânico ]
```

### 3.1 Como Criar "Tape Wow" no UltraRig
1. Insira um bloco de **Vibrato / Modulação**.
2. Configure o parâmetro de **Mix em 100% Wet** (sem sinal direto misturado; todo o áudio passa pelo modulador de tempo).
3. **LFO Waveform:** Selecione onda Triangular ou Aleatória (*Random / Sample & Hold*).
4. **Rate (Velocidade):** Ajuste entre **0.6 Hz e 1.1 Hz**.
5. **Depth (Profundidade):** Ajuste sutil entre **12% e 22%**.
   - *Resultado Sonoro:* As notas e acordes dedilhados flutuam sutilmente para cima e para baixo de afinação, recriando a sensação nostálgica de uma fita cassete gasta pelo tempo.

---

## 4. Saturação de Fita Magnética e Compressão Não-Linear

Ao contrário da distorção digital estridente (que gera harmônicos ímpares duros em clipping), a fita magnética satura de forma suave e progressiva:
- **Compressão Natural de Transientes:** Ataques fortes de palheta são suavemente limitados (*soft clipping* analógico), gerando sustentação quente.
- **No UltraRig:**
  - Utilize um modelo NAM de amplificador valvulado clássico de baixa potência (*Fender Tweed Deluxe* ou *Champ*) operando em ponto de quebra (*edge of breakup*).
  - Ou ative um pedal de drive estilo *Tape Saturation / Transparent Overdrive* com Ganho em 18% e Tone suavemente fechado.

---

## 5. Roteamento Paralelo: O Segredo da Textura Lo-Fi sem Perder a Clareza

Para performances ao vivo onde você deseja o charme do efeito lo-fi sem que a guitarra desapareça no fundo da mixagem da banda:

```
                            +---> [ Ramo A: Guitarra Limpa Principal ] -----+
                            |     - Som encorpado, estéreo e brilhante      |
                            |     - Mix equilibrado no centro               |
[ Entrada da Guitarra ] --->+                                               +---> [ Master Merge ]
                            |                                               |
                            +---> [ Ramo B: Camada Lo-Fi Degradada ] -------+
                                  - Banda estreita (500 Hz a 3 kHz)
                                  - Wow/Flutter 100% Wet
                                  - Tape Slapback Delay com repetições sujas
                                  - Mix 35% ao fundo
```

Essa topologia garante que a base da harmonia permaneça estável e audível para o público, enquanto uma "fantasia" de fita analógica flutua ao redor do som principal.

---

## 6. Arquitetura de 4 Cenas para Shows ao Vivo

```
+-------------------------------------------------------------------------------+
|             PRESET: "VINTAGE-LOFI-STUDIO" (4 CENAS PROGRAMADAS)               |
|                                                                               |
|  [Scene A] WOBBLY CASSETTE TAPE (Indie Pop / Mac DeMarco)                     |
|   - Vibrato 100% Wet (Rate 0.8 Hz, Depth 18%)                                 |
|   - LPF suave em 6.5 kHz + HPF em 90 Hz                                       |
|   - Tape Saturation quente + Room Reverb analógico                            |
|   - Textura melancólica e aveludada para dedilhados                           |
|                                                                               |
|  [Scene B] AM RADIO & TELEPHONE (Intro / Efeito Dramático)                     |
|   - HPF em 500 Hz + LPF em 3.2 kHz                                            |
|   - Boost ressonante em 1.8 kHz (+5 dB)                                       |
|   - Overdrive estilo transistor com corte estrito de graves                   |
|   - Perfeito para introduções de músicas ou quebras de estrofe                |
|                                                                               |
|  [Scene C] DUSTY VINYL 33 RPM (Neo-Soul / Lo-Fi Hip Hop)                      |
|   - Micro-Pitch Detune (+/- 6 cents) + Slapback Delay de 85ms                 |
|   - Spring Reverb vintage com cauda escura                                    |
|   - Compressor óptico com ataque lento e pumping suave                        |
|                                                                               |
|  [Scene D] 8-BIT RETRO ARCADE (Chiptune / Lo-Fi Digital)                      |
|   - Bitcrusher / Fuzz com redução de resolução digital                        |
|   - Gate de corte seco (Release 25ms)                                         |
|   - Som percussivo e sintetizado estilo videogame anos 80                     |
+-------------------------------------------------------------------------------+
```

---

## 7. Dicas de Produção e Performance no Palco

- **Uso do Knob de Volume da Guitarra:** Fechar o volume da guitarra em 7 ou 8 amortece naturalmente os agudos dos captadores passivos, ajudando a arredondar o som antes de atingir os filtros digitais.
- **Cabo P10 Longo ou Enrolado (Coiled Cable):** Guitarristas vintage costumam usar cabos espirais de 6 a 9 metros; a capacitância natural do cabo longo corta agudos estridentes de forma musical.
- **Transição ao Vivo:** Utilize o footswitch do UltraRig para disparar a Cena B (Megafone) durante os primeiros 4 compassos de uma introdução e, no primeiro tempo do verso com a entrada da bateria completa, comute para a Cena A ou para o som principal com transição 100% contínua (*gapless*).
