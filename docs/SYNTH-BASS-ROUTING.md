# Guia de Modelagem e Roteamento de Baixo Synth (Moog Bass & TB-303) em Paralelo no UltraRig

Este documento orienta sobre a construção, equalização harmônica e dinâmica de resposta para timbres de **Sintetizador de Baixo Analógico (Moog Bass, Roland TB-303, Novation Bass Station)** utilizando o contrabaixo elétrico no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

No repertório de *Funk dos anos 70/80 (P-Funk / Bootsy Collins / Bernie Worrell), Synthwave, Disco, EDM e Pop Moderno (Dua Lipa, Bruno Mars, Daft Punk)*, o contrabaixista precisa recriar timbres de sintetizador analógico. Pedais convencionais de synth com rastreamento digital frequentemente sofrem com latência perceptível, notas falsas (*glitches*) e dinâmica rígida. O UltraRig permite construir um baixo synth analógico autêntico em **ramos paralelos**, combinando um sub-oscilador analógico com saturação de onda quadrada e filtro ressonante de 24 dB/oitava.

---

## 1. A Física do Som de Sintetizador vs. Contrabaixo Elétrico

| Elemento | Contrabaixo Elétrico | Sintetizador Analógico (Minimoog / TB-303) |
| :--- | :--- | :--- |
| **Formato de Onda Primário** | Senoide fundamental com harmônicos decrescentes suaves. | Ondas puras **Dente-de-Serra (Saw)** ou **Quadrada (Square)** ricas em harmônicos ímpares. |
| **Sub-Grave** | Decai naturalmente conforme a vibração da corda perde energia. | **Sub-Oscilador Contínuo:** Onda pura de 30 Hz a 80 Hz sustentada com amplitude constante. |
| **Filtro de Varredura** | Tonalidade passiva com corte suave de 6 dB/oitava sem ressonância. | **Filtro Ladder Transistorizado de 24 dB/oitava:** Ressonância afiada (*Q*) com envelope de varredura. |
| **Articulação de Teclado** | Ataque percussivo de dedo e ruído de traste. | Ligações e cortes instantâneos tipo *Gate ON/OFF* com envelopes precisos. |

---

## 2. A Topologia em Ramos Paralelos (Parallel Split & Merge)

Para conseguir um som que preencha a pista de dança sem perder o peso do subgrave no PA, o sinal do baixo é dividido em duas ramificações especializadas:

```
+-------------------------------------------------------------------------------+
|         TOPOLOGIA PARALELA PARA MOOG SYNTH BASS NO ULTRARIG                   |
|                                                                               |
|                             +---> [ RAMO A: SUB-OSCILADOR ANALÓGICO ] -------+ |
|                             |     - Monophonic Octaver (-1 Oitava)           | |
|                             |     - Brickwall LPF em 110 Hz                  | |
|                             |     - Brickwall Peak Limiter (Sustain Puro)    | |
| [ Contrabaixo Elétrico ] -->+                                                +>[Merge]
|                             |                                                | (Master)
|                             +---> [ RAMO B: ONDA QUADRADA & FILTRO LADDER ] -+ |
|                                   - Gated Silicon Fuzz (Onda Quadrada)       |
|                                   - 24dB Resonant Envelope Filter            |
|                                   - Hard Noise Gate (Teclado Key-Off)        |
+-------------------------------------------------------------------------------+
```

---

## 3. Configuração dos Ramos Passo a Passo

### 3.1 Ramo A: A Fundação do Sub-Oscilador (The Low-End Anchor)
O objetivo do Ramo A é produzir o impacto visceral de frequências subgraves sentidas no peito (30 Hz a 100 Hz):
1. **Oitavador Monofônico (-1 Oitava):**
   - Transpõe a nota para a oitava inferior (-12 semitons).
   - Ajuste o Mix em **100% Wet** (sem sinal original).
2. **Filtro Passa-Baixas Estrito (Brickwall LPF em 110 Hz):**
   - Elimina qualquer conteúdo harmônico acima de 110 Hz.
   - Isso transforma a saída do oitavador em uma onda quase senoidal perfeita de sub-grave, livre de chiados ou ruídos de traste.
3. **Limitador Rápido de Pico (Peak Limiter):**
   - Nivelamento extremo (Ratio 8:1) para que a sustentação da nota grave permaneça com volume 100% uniforme, exatamente como as teclas de um teclado Moog.

### 3.2 Ramo B: A Textura de Onda Quadrada e o Filtro de 24 dB (The Synth Growl)
O Ramo B é responsável pelo ataque vocal, ácido e agressivo do sintetizador:
1. **Silicon Fuzz / Square-Wave Drive:**
   - A distorção pesada ceifa os topos e fundos da onda do baixo, convertendo a vibração da corda em uma onda quadrada rica em harmônicos impares.
   - Ajuste o Ganho em **60% a 75%** e o Tone em **65%**.
2. **Envelope Filter Ressonante (Simulação de Filtro Moog Ladder de 4 Polos):**
   - **Filter Mode:** Passa-Baixas de 24 dB/oitava (*4-Pole Low-Pass*).
   - **Resonance / Q:** Configure alto (**60% a 75%**). A alta ressonância cria o clássico pico estridente no ponto de corte que gera o efeito vocal "*ow-wah*".
   - **Sensitivity:** Calibre para que notas tocadas em *mezzo-forte* abram o filtro até 80% do curso.
   - **Decay Time:** **140 ms a 240 ms** para varreduras rápidas e percussivas estilo Minimoog.
3. **Hard Noise Gate:**
   - Para emular a liberação instantânea de uma tecla de sintetizador (*Keyboard Key-Off*), insira um gate no fim do Ramo B com **Release de 30 ms a 45 ms**.

---

## 4. Técnicas de Execução do Instrumentista (Playing Like a Synth)

Tocar baixo synth exige adaptar a técnica manual para imitar as limitações e articulações de um teclado:
1. **Mute de Palma da Mão Esquerda (Left-Hand Palm Mute):** Toque notas curtas e estacatas. Não deixe cordas adjacentes ressoarem soltas, pois duas notas simultâneas confundem o rastreamento do oitavador no Ramo A.
2. **Palhetada ou Polegar Próximo ao Braço:** Tocar com o polegar ou usar abafamento com esponja na ponte encurta a cauda natural da corda, intensificando a sensação percussiva de sintetizador.
3. **Glissando / Sliders Contínuos:** Deslizar o dedo pelas casas do braço (*slides*) cria o clássico efeito de *Portamento / Pitch Glide* analógico do Minimoog.

---

## 5. Arquitetura de 4 Cenas para Shows ao Vivo

```
+-------------------------------------------------------------------------------+
|             PRESET: "ANALOG-SYNTH-PRO" (4 CENAS PROGRAMADAS)                  |
|                                                                               |
|  [Scene A] 70s P-FUNK BERNIE WORRELL MOOG                                     |
|   - Ramo A (Sub 100Hz): 50% Mix                                               |
|   - Ramo B (Fuzz + Envelope Filter moderado): 50% Mix                         |
|   - Resonance em 65%, Decay 180ms                                             |
|   - Timbre clássico de Flash Light / Parliament para funk clássico            |
|                                                                               |
|  [Scene B] ACID 303 TECHNO SQUELCH                                            |
|   - Ramo B com Resonance em 85% (quase em auto-oscilação ácida)              |
|   - Hard Gate com Release ultrarrápido (25ms)                                 |
|   - Ataques curtos gerando estalos de filtro agressivos para música eletrônica |
|                                                                               |
|  [Scene C] DUA LIPA / DISCO 80s BASS                                          |
|   - Ramo A reforçado em 60% (Subgraves colossais)                             |
|   - Ramo B com Analog Phaser lento (Rate 0.5 Hz) pós-filtro                   |
|   - Som aveludado, encorpado e moderno para pop contemporâneo                 |
|                                                                               |
|  [Scene D] 808 SUB BOOM (Armadilha Trap / Hip Hop)                            |
|   - Ramo A em 80% (Sub-graves massivos de 40 Hz)                              |
|   - Ramo B com saturação suave e filtro fechado em 400 Hz                     |
|   - Longa sustentação para graves de preenchimento de estúdio                 |
+-------------------------------------------------------------------------------+
```

---

## 6. Dicas de Palco e Solução de Problemas

- **O subgrave parece cancelar e perder peso quando o fuzz é ligado:**
  - *Causa:* Inversão de fase entre o oitavador do Ramo A e o pedal de fuzz do Ramo B.
  - *Solução:* Localize a chave **Phase Invert (0°/180°)** no Ramo B e inverta a fase. O grave voltará imediatamente com impacto duplo.
- **O filtro abre demais em algumas notas e quase nada em outras:**
  - *Causa:* Variação de volume entre cordas diferentes do contrabaixo.
  - *Solução:* Insira um compressor de pico transparente antes da divisão dos ramos (*Pre-Split Compressor*) com ataque de 5 ms para nivelar a intensidade de entrada do envelope follower.
