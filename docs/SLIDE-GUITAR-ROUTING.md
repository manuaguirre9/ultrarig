# Guia de Roteamento, Dinâmica e Modelagem para Guitarra Slide / Bottleneck no UltraRig

Este documento estabelece as diretrizes de engenharia de som, compressão de sustentação, atenuação de ruídos de fricção (*slide scrape*) e modelagem tonal para **Guitarra Slide e Bottleneck** (estilo Duane Allman, Derek Trucks, Ry Cooder, Lowell George, Bonnie Raitt e Sonny Landreth) no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

Tocar com slide exige uma abordagem eletroacústica radicalmente diferente da guitarra convencional: como o tubo de vidro, latão, cerâmica ou aço flutua sobre as cordas sem pressioná-las contra os trastes metálicos da escala, o instrumento perde sustentação mecânica natural e ganha ruídos estridentes de atrito (*raspagem de tubo*). O UltraRig permite esculpir uma voz cantante, infinita e expressiva, livre de chiados e asperezas.

---

## 1. A Física do Slide vs. Guitarra Convencional

```
+-------------------------------------------------------------------------------+
|                       MECÂNICA DE CONTACTO DO SLIDE                           |
|                                                                               |
|  GUITARRA CONVENCIONAL:                                                       |
|  Dedo na corda ---> [ Traste Metálico de Níquel ] ---> Sustentação Rígida     |
|                                                                               |
|  GUITARRA SLIDE (BOTTLENECK):                                                 |
|  Tubo de Vidro/Latão desliza sobre a corda solta                              |
|  - Sem ponto de ancoragem rígido = Decaimento natural 40% mais rápido.       |
|  - Atrito contínuo do tubo nas espiras das cordas = Ruído agudo em 4-7 kHz.   |
|  - Pequenos esbarros nos trastes adjacentes = Estalos transitórios secos.     |
+-------------------------------------------------------------------------------+
```

---

## 2. A Estratégia de Compressão Pré-Drive (O Segredo de Lowell George)

Para que o slide "cante" como uma voz humana através de várias oitavas sem morrer no meio de um vibrato longo:
1. **Compressor Óptico no Início da Cadeia (Pré-Ganho):**
   - **Attack Time:** Moderado (**12 ms a 20 ms**). Permite que o estalo inicial da palheta ou do dedo passe com impacto musical.
   - **Release Time:** Longo (**350 ms a 550 ms**). Acompanha a dissipação de energia da corda, aplicando ganho progressivo para manter a nota soando infinitamente no mesmo volume.
   - **Ratio:** **4:1 a 6:1** com atenuação de **4 dB a 7 dB**.
2. **Por que isso é Superior à Distorção Pura:**
   - Adicionar mais ganho de pré-amp apenas gera chiado (*hiss*) e perda de dinâmica. A compressão óptica transparente sustenta as notas mantendo a definição harmônica limpa.

---

## 3. Filtragem de Ruído de Fricção (De-Scraping EQ)

O deslizamento do tubo de vidro ou metal sobre cordas de níquel/aço gera um atrito penetrante que polui o áudio em gravações e monitores *In-Ear*:
1. **Filtro Passa-Baixas Superior (LPF em 5.5 kHz a 6.5 kHz):**
   - O conteúdo melódico e vocal da guitarra slide raramente ultrapassa 5 kHz.
   - Cortar frequências acima de 6 kHz amortece o "chiado de lixa" do tubo sem comprometer o brilho do timbre.
2. **Corte Cirúrgico de Fricção (Notch em 4.2 kHz):**
   - Aplique uma atenuação com **Q estreito (Q = 4.0)** de **-3.5 dB a -5 dB em 4.2 kHz** para eliminar o impacto de cliques metálicos involuntários contra os trastes.

---

## 4. Modelagem de Médios Vocais e Escolha de Amplificadores NAM

O slide precisa habitar a faixa de médios da voz humana (**800 Hz a 2.5 kHz**) para cortar o mix da bateria e do contrabaixo:
- **Modelos NAM Ideais:**
  - *Fender Tweed Deluxe (5E3) ou Bassman:* Saturação rica em harmônicos pares de 2ª e 4ª ordem, comprimindo o ataque com calor aveludado estilo Duane Allman.
  - *Dumble Overdrive Special / Supro Vintage:* Médios encorpados e dinâmicos com ponto de quebra suave (*edge of breakup*).
- **Overdrive Pré-Amp Estilo TS9 / Klon:**
  - Ganho baixo (15%), volume alto (80%) e corte suave de graves. O pico de médios característico projeta as frases de slide para a frente do palco.

---

## 5. Efeitos Espaciais: Delay Analógico e Reverbs Aveludados

- **Analog BBD / Tape Delay:**
  - Tempo de atraso entre **320 ms e 380 ms** (colcheia pontuada em andamento médio).
  - Mix de **20% a 28%** com 3 a 4 repetições quentes que perdem agudos a cada eco. O delay "carrega" o slide como um coro de resposta.
- **Plate / Spring Reverb com Amortecimento de Agudos:**
  - Decay de **1.8s a 2.5s** com filtro passa-baixas interno fechado em 4 kHz para que as caudas não soem metálicas.

---

## 6. Arquitetura de 4 Cenas para Shows ao Vivo

```
+-------------------------------------------------------------------------------+
|             PRESET: "SLIDE-VOCAL-PRO" (4 CENAS PROGRAMADAS EM OPEN E)         |
|                                                                               |
|  [Scene A] SOUTHERN SINGING LEAD (Allman & Trucks Style)                      |
|   - Tweed Crunch NAM Amp + Opto Compressor (Attack 15ms, Release 450ms)       |
|   - Pre-Drive Mid Boost em 1.2 kHz + LPF em 6.0 kHz                           |
|   - Analog Tape Delay suave (340ms, mix 22%)                                  |
|   - Sustentação vocal infinita para solos melódicos expressivos               |
|                                                                               |
|  [Scene B] RY COODER RESONATOR (Acústico / Dobro Vintage)                     |
|   - Convolução de Acoustic Resonator Body IR (1024 pontos)                    |
|   - Compressor transparente nivelando dedilhados com os dedos                 |
|   - Room Reverb analógico de estúdio vintage para blues acústico              |
|                                                                               |
|  [Scene C] LOWELL GEORGE CLEAN COMPRESSION (Funk & Little Feat)               |
|   - Amplificador Limpo Americano de alto headroom                             |
|   - Duplo estágio de compressão (Opto + VCA) com sustain máximo               |
|   - Som limpo, percussivo e que nunca perde volume nas notas agudas           |
|                                                                               |
|  [Scene D] DIRTY DELTA BLUES (Saturação Supro / Elmore James)                 |
|   - Small Tube Combo Saturado + Fuzz leve vintage                             |
|   - Spring Reverb longo com cauda escura                                      |
|   - Raspagem de slide aberta intencionalmente para crueza e atitude           |
+-------------------------------------------------------------------------------+
```

---

## 7. Ajustes Mecânicos e Dicas de Instrumento

- **Ação das Cordas:** Ajuste a ação das cordas na ponte e no capotraste (*nut*) ligeiramente mais alta (cerca de 2.0 a 2.5 mm na 12ª casa) para evitar que o slide bata nos trastes ao deslizar.
- **Calibre das Cordas:** Para tocar com afinações abertas (*Open E: E-B-E-G#-B-E* ou *Open G: D-G-D-G-B-D*), utilize encordoamento mais pesado (**mínimo .011 ou .012**) para manter a tensão mecânica firme sob o peso do slide.
- **Material do Tubo:**
  - **Vidro / Pyrex:** Timbre mais aveludado, suave e quente; menor ruído de fricção mecânica.
  - **Latão / Bronze (Brass):** Mais pesado, entrega mais sustain natural e médios encorpados.
  - **Aço Cromado:** Ataque metálico penetrante e brilhante, ideal para ressonadores e guitarras acústicas.
