# Guia de Otimização e Roteamento de Timbres para Guitarras Barítono e Afinações Drop Extremas no UltraRig

Este guia técnico aborda a física eletroacústica de cordas grossas, filtragem de subgraves pré-ganho (*Pre-Drive Tightening*), calibração de modelos **NAM (Neural Amp Modeler)** e seleção de respostas de impulso (Cabinet IRs) para **Guitarras Barítono e Afinações Graves / Drop Extremas** (**Drop C, Drop B, Drop A, Drop G e afinações de 7/8 cordas**) no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

Tocar em afinações graves com timbres modernos de alto ganho (*modern metal, djent, prog, deathcore, post-metal*) apresenta um desafio sonoro imediato: **o excesso de energia nas frequências graves sobrecarrega os estágios de saturação do amplificador**, gerando um som embolado, sem ataque de palheta, com abafamentos frouxos (*muddy / flubby palm-mutes*) e perda total de definição em passagens rápidas.

---

## 1. A Física das Afinações Graves e Escalas Estendidas

| Parâmetro | Guitarra Padrão (E Standard) | Afinação Drop Extrema (Drop A / Barítono) |
| :--- | :--- | :--- |
| **Comprimento de Escala** | 24.75" a 25.5" | 26.5" a 30.0" |
| **Calibre da Corda Mais Grave** | .042 a .046 | .062 a .074 (corda de baixo elétrico leve) |
| **Frequência Fundamental** | Mi2 (~82.4 Hz) | Lá1 (~55.0 Hz) ou Sol1 (~49.0 Hz) |
| **Comportamento no Pré-Amp** | Graves controlados no estágio de drive. | **Overload de graves:** satura as válvulas virtuais antes dos médios, matando o corte percussivo. |

Quando uma corda grossa (.068 afinada em Lá) é palhetada com força, ela gera uma onda com amplitude física enorme e transientes subgraves concentrados entre 40 Hz e 90 Hz. Se esse sinal entrar cru em um modelo NAM valvulado (*como 5150, Dual Rectifier ou Soldano SLO*), os estágios virtuais de ganho saturam os graves instantaneamente, transformando o som em uma distorção sem foco.

---

## 2. A Técnica do "Pre-Gain Tightening" (O Segredo do Metal Moderno)

A solução definitiva na engenharia de áudio para afinações graves é cortar os subgraves **antes** da saturação e restaurar o corpo do timbre **depois** do amplificador:

```
+-------------------------------------------------------------------------------+
|                 CADEIA "TIGHT CHUG" PARA DROP TUNINGS NO ULTRARIG             |
|                                                                               |
|  [ Guitarra Barítono / Drop A ]                                               |
|               |                                                               |
|               v                                                               |
|  [ Pré-EQ / Overdrive Tightener ] ----> Corta graves < 90 Hz + Boost 1.5 kHz  |
|               |                         (Elimina a frouxidão do pré-amp)      |
|               v                                                               |
|  [ Bloco NAM High-Gain (5150) ] ------> Satura apenas os médios percussivos   |
|               |                                                               |
|               v                                                               |
|  [ Sidechain Noise Gate (VCA) ] ------> Silencia chiado entre riffs staccato  |
|               |                                                               |
|               v                                                               |
|  [ Pós-EQ / Master Shelf ] -----------> Restaura peso seguro e limpo em 80 Hz |
|               |                                                               |
|               v                                                               |
|  [ Cabinet IR 4x12 Oversized ] -------> Convolução focada em médios fechados  |
+-------------------------------------------------------------------------------+
```

### 2.1 Configuração do Overdrive / Booster Pré-Ganho
No UltraRig, insira um bloco de Overdrive no início da cadeia com os seguintes valores:
- **Drive / Gain:** `0% a 5%` (Sem distorção adicional gerada pelo pedal).
- **Tone / Brightness:** `60% a 75%` (Realça o ataque da palheta entre 1.5 kHz e 3.0 kHz).
- **Level / Volume:** `75% a 85%` (Empurra a entrada do modelo NAM com transientes firmes).
- *Efeito Prático:* O circuito emula a curva de EQ do clássico *Tube Screamer* ou *Horizon Precision Drive*, limpando a região abaixo de 700 Hz e focando a distorção nas frequências que cortam a mixagem da bateria.

---

## 3. Tabela de Filtragem Passa-Altas (HPF) por Afinação

No bloco de equalizador ou configurações de entrada, ajuste o filtro passa-altas de corte subgrave conforme a afinação do instrumento:

| Afinação | Nota Mais Grave | Frequência Fundamental | Corte HPF Pré-Drive Sugerido |
| :--- | :--- | :--- | :--- |
| **E Standard / Drop D** | E2 / D2 | 82 Hz / 73 Hz | **70 Hz a 75 Hz** |
| **D Standard / Drop C** | D2 / C2 | 73 Hz / 65 Hz | **65 Hz a 70 Hz** |
| **C Standard / Drop B** | C2 / B1 | 65 Hz / 62 Hz | **60 Hz a 65 Hz** |
| **B Standard / Drop A** | B1 / A1 | 62 Hz / 55 Hz | **55 Hz a 60 Hz** |
| **Drop G / Drop F# (8-String)** | G1 / F#1 | 49 Hz / 46 Hz | **45 Hz a 50 Hz** |

> [!IMPORTANT]
> Cortar abaixo de 55 Hz em uma guitarra em Drop A não enfraquece o som. Pelo contrário: libera o amplificador NAM para focar 100% de sua energia nos harmônicos secundários que dão a ilusão psicoacústica de graves colossais, sem embolar com o bumbo e com o contrabaixo.

---

## 4. Escolha de Cabinet IRs para Afinações Graves

Respostas de impulso genéricas para afinações padrão frequentemente soam estridentes e frouxas em afinações extremas:
1. **Evite Caixas Abertas (Open-Back) ou IRs de Alto-Falantes Alnico:** Caixas abertas cancelam graves e dispersam energia de forma desordenada.
2. **Priorize Gabinetes 4x12 Fechados (Closed-Back Oversized):**
   - Emulações de gabinetes *Mesa Boogie Rectifier Standard 4x12* ou *Orange PPC412* possuem volume interno maior, oferecendo graves firmes e controlados sem ressonâncias frouxas em 100 Hz.
3. **Microfonação Mista (Blend SM57 + Royer R-121):**
   - O microfone dinâmico *Shure SM57* fornece a mordida agressiva nos médios (2 kHz – 4 kHz).
   - O microfone de fita *Royer R-121* adiciona corpo natural e aveludado nos graves, eliminando o "chiado de abelha" digital nos agudos extremos.

---

## 5. Roteamento Paralelo Avançado: Otimização de Riffs Modernos

Para timbres de djent e metal progressivo com afinações abaixo de Drop A:

```
                            +---> [ Ramo A: High-Gain Crunch ] -----------+
                            |     - HPF em 110 Hz                         |
                            |     - Overdrive Boost ativo                 |
                            |     - NAM 5150 / Peavey High-Gain           |
[ Guitarra Drop A / G ] --->+                                             +---> [ Master Merge ]
                            |                                             |
                            +---> [ Ramo B: Sub-Foundation Limpo ] -------+
                                  - LPF em 120 Hz
                                  - Compressor rápido (Ratio 4:1)
                                  - Pré-amp limpo (Punch puro de corda)
```

- **Ramo A:** Recebe a distorção total, mas com graves cortados para garantir que cada palhetada rápida soe cirurgicamente definida.
- **Ramo B:** Mantém uma camada limpa e ultra-comprimida dos subgraves, adicionando o impacto físico do peso no peito sem sujar a distorção do pré-amp.

---

## 6. Arquitetura de 4 Cenas para Shows ao Vivo

```
+-------------------------------------------------------------------------------+
|         PRESET: "BARITONE-METAL-PRO" (4 CENAS PROGRAMADAS EM DROP A)          |
|                                                                               |
|  [Scene A] MODERN DJENT CHUG (Riffs Estacatos Rápidos)                        |
|   - Pre-EQ HPF: 60 Hz + Mid Boost em 1.6 kHz                                  |
|   - NAM Amp: High Gain Britânico/Americano (Gain 6.0)                         |
|   - Sidechain Gate: Hard Gate (Threshold -42 dBFS, Release 35ms)              |
|   - Timbre seco, cortante e ultrarrápido para paradas de palheta               |
|                                                                               |
|  [Scene B] MELODIC HIGH-GAIN SOLO (Sustain e Extensão de Palco)               |
|   - Pre-EQ HPF relaxado para 50 Hz                                            |
|   - Scene Level: +3.0 dB                                                      |
|   - Stereo Tape Delay: ON (Colcheia pontuada, 28% mix com trails)             |
|   - Reverb Hall amplo (Decay 2.2s) + Gate com Release suave de 220ms          |
|                                                                               |
|  [Scene C] ETHEREAL PRISTINE CLEAN (Arpejos Ambientais)                       |
|   - NAM Amp: Clean Headroom Americano (Gain 2.5)                              |
|   - Analog Chorus: ON (Rate 0.9 Hz, Depth 40%)                                |
|   - Shimmer Reverb: ON (Mix 35%)                                              |
|   - Graves abertos e profundos sem distorção indesejada                       |
|                                                                               |
|  [Scene D] DOOM / SLUDGE CRUSH (Peso Massivo Intencional)                     |
|   - Pre-EQ HPF desativado (graves liberados para saturar o pré-amp)           |
|   - Bloco Fuzz ativado em paralelo                                            |
|   - Som colossal, arrastado e com compressão extrema de graves                |
+-------------------------------------------------------------------------------+
```

---

## 7. Ajustes Físicos Essenciais do Instrumento

Mesmo o melhor DSP digital não pode corrigir problemas mecânicos graves de cordas:
- **Tensão Adequada:** Utilize calculadoras de tensão (como *Stringjoy* ou *D'Addario Tension Guide*) buscando manter entre **17 e 21 libras de tensão por corda**. Cordas frouxas oscilam fora do eixo de afinação logo após o impacto da palheta (*pitch drift* inicial de até +40 cents).
- **Compensação de Oitavas no Carrinho (Intonação da Ponte):** Cordas grossas (.064 ou .070) exigem que o carrinho da ponte seja recuado significativamente para trás para manter a oitava na 12ª casa perfeitamente alinhada.
- **Altura dos Captadores:** Afaste os captadores em 1 mm a mais das cordas mais grossas. A massa magnética elevada de cordas espessas atrai o campo magnético dos ímãs de alnico/cerâmica (*magnetic pull*), causando desafinação harmônica contínua (*wolf tones*).
