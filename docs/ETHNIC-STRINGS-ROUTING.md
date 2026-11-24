# Guia de Roteamento, Pré-Amplificação e Modelagem para Harpa e Instrumentos Étnicos de Cordas (Koto, Oud, Cítara, Bouzouki) no UltraRig

Este documento estabelece as diretrizes de ganho, filtragem espectral, controle de transientes percussivos e espacialização modal para **Harpa Acústica/Celta e Instrumentos Étnicos de Cordas Dedilhadas** (**Koto japonês, Oud/Alaúde árabe, Cítara indiana e Bouzouki grego/irlandês**) no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

Instrumentos étnicos e tradicionais de cordas vêm sendo cada vez mais incorporados em produções modernas de *World Music, Trilha Sonora, Progressive Rock, Ambient, Folk e Jazz Contemporâneo*. Esses instrumentos apresentam desafios acústicos singulares: transientes de palheta extremamente afiados (palhetas de madeira, chifre, osso ou anéis *tsume*), dezenas de cordas simpatéticas soltas que vibram em conjunto (*sympathetic resonance*) e caixas acústicas delicadas altamente suscetíveis a microfonias de palco.

---

## 1. Perfis Eletroacústicos dos Instrumentos

| Instrumento | Número de Cordas / Construção | Frequência Mais Grave | Desafio de Amplificação Principal |
| :--- | :--- | :--- | :--- |
| **Harpa Acústica / Celta** | 34 a 47 cordas (tripa, nylon e aço) | Dó1 (~32.7 Hz) a Sol7 | Extensão colossal de frequência; graves profundos e ressonância massiva do tampo. |
| **Oud / Alaúde** | 11 ou 12 cordas em pares (sem trastes) | Dó2 (~65.4 Hz) | Caixa em formato de gota (bojo abaulado); excesso de ressonância oca em 180–300 Hz. |
| **Koto Japonês** | 13 ou 17 cordas com cavaletes móveis | Sol2 (~98 Hz) ou Ré2 | Palhetas de dedo de marfim/acrílico (*tsume*) gerando estalidos agressivos em 4–6 kHz. |
| **Cítara Indiana** | 18 a 21 cordas (cordas melódicas + *taraf*) | Dó2 (~65 Hz) | Cordas simpatéticas (*taraf*) geram realimentação harmônica contínua no palco. |
| **Bouzouki Grego / Irlandês** | 8 cordas duplas (aço de alta tensão) | Dó3 (~130 Hz) ou Ré3 | Estridência metálica excessiva nos agudos; falta de graves em captadores magnéticos. |

---

## 2. Filtragem Passa-Altas (HPF) por Extensão Mecânica

Como o corpo desses instrumentos atua como uma antena acústica gigante, o filtro passa-altas deve ser calibrado com precisão cirúrgica para proteger o sistema de PA sem castrar as fundamentais:

```
+-------------------------------------------------------------------------------+
|         CALIBRAÇÃO DE FILTRO PASSA-ALTAS (HPF) POR INSTRUMENTO                |
|                                                                               |
|  Instrumento          Fundamental          Corte HPF Recomendado              |
|  -----------          -----------          ---------------------              |
|  Harpa de Concerto    Dó1 (~32.7 Hz)       28 Hz a 32 Hz (18 dB/oitava)       |
|  Oud / Alaúde         Dó2 (~65.4 Hz)       70 Hz a 80 Hz (18 dB/oitava)       |
|  Bouzouki Irlandês    Ré3 (~146.8 Hz)      100 Hz a 115 Hz (18 dB/oitava)     |
|  Koto Japonês         Sol2 (~98 Hz)        85 Hz a 95 Hz (18 dB/oitava)       |
|  Cítara               Dó2 (~65 Hz)         75 Hz a 85 Hz (18 dB/oitava)       |
+-------------------------------------------------------------------------------+
```

---

## 3. Controle de Transientes Ultrarrápidos (De-Harshing & Soft Limiting)

Palhetadas de *risha* (palheta fina de osso ou plástico flexível usada no Oud) e unhas *tsume* no Koto criam picos instantâneos que saturam conversores digitais:
1. **Soft Tape Saturation / Pré-Amp Neve:**
   - No início da cadeia do UltraRig, insira uma leve saturação analógica com ganho mínimo (10% a 15%).
   - *Efeito:* Arredonda a ponta agressiva do ataque mecânico de palheta, aquecendo o timbre antes da equalização.
2. **Corte Paramétrico de Estridência Metálica:**
   - Aplique uma atenuação com **Q estreito (Q = 4.0)** de **-4 dB a -6 dB** entre **3.6 kHz e 5.0 kHz**.
   - Isso remove o ruído plástico do impacto da unha/palheta sem roubar o brilho aéreo das cordas.

---

## 4. Convolução de Acoustic Body IRs (1024 Pontos)

Captadores piezo colados na madeira (como *K&K Pure Mini*, *Schatten*, *Ovation* ou *Fishman*) captam apenas a vibração local do ponto de contato, soando finos e bidimensionais:
- **Desative modelos de caixas elétricas (`CAB IR Bypass`).**
- Carregue respostas de impulso acústicas de alta resolução (**Acoustic Body IR de instrumentos acústicos de madeira maciça de luthier**).
- **Ajuste de Blend (Mix):** Configure entre **45% e 65% Wet**. A porção acústica convolutiva adiciona o ar da madeira, o peso do bojo abaulado e o espaço tridimensional de uma sala de estúdio tratada.

---

## 5. Espacialização Modal e Modulação Estéreo

Instrumentos étnicos operam frequentemente em modos e escalas microtonais (*Maqam árabe, Ragas indianos, Hirajoshi japonês*):
- **O Risco dos Efeitos Estéreo Agressivos:** Coros com desafinação pesada (+/- 15 cents) entram em conflito com as notas microtonais puras dos instrumentos sem trastes (como o Oud).
- **A Solução no UltraRig:**
  - **Stereo Micro-Pitch Detune:** Desafinação mínima de apenas **+/- 2 a 3 centésimos**, alargando a imagem estéreo sem alterar a precisão modal da afinação.
  - **Cathedral / Large Plate Reverb:** Decay longo (**3.0 a 4.5 segundos**) com amortecimento acentuado de agudos (*High Damping* em 3.5 kHz), criando uma cauda etérea e cinematográfica sem embolar os dedilhados rápidos.

---

## 6. Arquitetura de 4 Cenas para Shows ao Vivo

```
+-------------------------------------------------------------------------------+
|             PRESET: "ETHNIC-STRINGS-PRO" (4 CENAS PROGRAMADAS)                |
|                                                                               |
|  [Scene A] CELTIC HARPA CATHEDRAL                                             |
|   - HPF em 30 Hz (Graves majestosos preservados)                              |
|   - Compressor Óptico suave (Attack 30ms, Release 350ms)                      |
|   - Cathedral Reverb amplo (Decay 4.2s, mix 28%)                              |
|   - Som celestial de harpa de concerto com ar imersivo                       |
|                                                                               |
|  [Scene B] MIDDLE-EASTERN OUD WOOD (Alaúde / Arabesco)                        |
|   - HPF em 75 Hz + Notch cirúrgico em 220 Hz (Corta ressonância de bojo)      |
|   - Body IR de madeira de jacarandá maciço (mix 60%)                          |
|   - Tape Delay discreto (140ms, mix 15%) com cauda escura                    |
|   - Timbre quente, orgânico e sem estalidos artificiais                       |
|                                                                               |
|  [Scene C] MEDITATIVE JAPANESE KOTO                                           |
|   - Suavizador de transientes de palheta tsume (De-Harshing em 4.5 kHz)       |
|   - Room Reverb de madeira tradicional (Decay 1.8s)                           |
|   - Stereo Width ampliado (70%) para espalhamento das cordas no palco         |
|                                                                               |
|  [Scene D] PSYCHEDELIC DRONE SITAR & BOUZOUKI                                 |
|   - Resonator Shimmer sutil em paralelo                                       |
|   - Tape Echo sincronizado com feedback moderado (30% mix)                    |
|   - Sustentação infinita de cordas simpatéticas para ambient e world rock     |
+-------------------------------------------------------------------------------+
```

---

## 7. Checklist de Palco e Prevenção de Feedback

- [ ] **Filtro HPF Confirmado:** Verificado ponto de corte passa-altas para evitar excursão descontrolada de graves em harpas e ouds.
- [ ] **Resistência a Realimentação de Cordas Simpatéticas:** Em cítaras e harpas com muitas cordas soltas, ative o *Noise Gate Suave* no final da cadeia para cortar o som quando a mão silencia o instrumento.
- [ ] **Desacoplamento de Monitores de Chão:** Em instrumentos com tampo fino (harpa e koto), evite monitores de chão apontados diretamente para o corpo acústico; priorize fones de ouvido *In-Ear*.
