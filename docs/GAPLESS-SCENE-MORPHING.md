# Guia Técnico de Configuração e Uso de Cenas sem Interrupção de Áudio (Gapless Scene Morphing) no UltraRig

Este documento detalha os fundamentos arquiteturais, os limites de hardware, as técnicas de interpolação de parâmetros e as estratégias práticas de composição sonora utilizando as **4 Cenas (Scenes A, B, C, D) por Preset** no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

No palco, a troca de timbres entre estrofes, refrões e solos de uma mesma música exige transições musicais imperceptíveis. A compreensão profunda do modo de **Cenas** elimina definitivamente quedas de áudio (*audio dropouts*), estalos digitais e cortes abruptos de caudas de efeitos (*spillover truncation*).

---

## 1. Presets vs. Cenas: A Física da Troca de Áudio Digital

Compreender a diferença computacional entre trocar de **Preset** e trocar de **Cena** é crucial para arquitetar o seu show:

```
+-------------------------------------------------------------------------------+
|                       TROCA DE PRESET INTEIRO (PATCH CHANGE)                  |
|                                                                               |
|  [ Preset 01 Ativo ] ---> [ Esvaziamento de Memória ] ---> [ Preset 02 Novo ] |
|                                   |                                           |
|                            DROPOUT DE ÁUDIO                                   |
|                             (30ms a 80ms)                                     |
|                                                                               |
|  - Descarrega e recarrega os pesos da rede neural NAM (SRAM flush).           |
|  - Reinicializa buffers do convolver de Cabinet IR.                           |
|  - Zera completamente a memória circular de Delays e Reverbs (corte de cauda).|
+-------------------------------------------------------------------------------+

+-------------------------------------------------------------------------------+
|                       TROCA DE CENA (GAPLESS SCENE MORPHING)                  |
|                                                                               |
|  [ Cena A (Verso) ] ===================================> [ Cena B (Solo) ]    |
|                                   |                                           |
|                           TRANSIÇÃO CONTÍNUA                                  |
|                            (Latência Zero)                                    |
|                                                                               |
|  - O grafo DSP, o modelo NAM e a Cabinet IR permanecem fixos na memória.     |
|  - Apenas parâmetros contínuos sofrem interpolação suave (crossfade de 5ms).  |
|  - As caudas de Delay e Reverb continuam soando naturalmente no espaço.       |
+-------------------------------------------------------------------------------+
```

---

## 2. O Que Pode Mudar Entre Cenas vs. O Que Deve Ficar Fixo

Para garantir latência zero e ausência total de repiques de áudio no processador JieLi, o UltraRig estabelece fronteiras claras entre os elementos de uma cena:

| Elemento do Preset | Pode Mudar Entre Cenas A, B, C, D? | Impacto no Áudio |
| :--- | :---: | :--- |
| **Bypass de Blocos DSP** | **SIM** | Liga/desliga blocos individuais (ex: Overdrive On em B, Off em A). |
| **Parâmetros Contínuos** | **SIM** | Ganho do amplificador, corte de EQ, tempo e mix de delay, nível de solo (+3 dB). |
| **Balanço de Ramos Paralelos** | **SIM** | Morfismo do mix entre Ramo A e Ramo B (ex: 80/20 em base, 50/50 em solo). |
| **Modelo Neural NAM Carregado** | **NÃO** | O arquivo de captura neural é compartilhado por todas as 4 cenas do preset. |
| **Arquivo de Cabinet IR** | **NÃO** | A resposta de impulso convolutiva carregada no bloco CAB é fixa para o preset. |
| **Ordem Topológica dos Blocos** | **NÃO** | A estrutura de blocos em série/paralelo é idêntica nas 4 cenas. |

---

## 3. O Mecanismo de Interpolação de Parâmetros (Slew-Rate Smoothing)

Quando um footswitch comuta de uma cena para outra com valores de parâmetros radicalmente diferentes (por exemplo, um ganho de amplificador que salta de `3.0` para `8.5`):
- **O Risco do Salto Instantâneo:** Uma mudança instantânea entre amostras adjacentes cria uma descontinuidade abrupta na forma de onda digital, percebida pelo ouvido como um "clique" ou "estalo" digital (*zipper noise*).
- **A Solução do UltraRig (Linear Slew Smoothing):** O firmware aplica uma rampa de interpolação linear rápida de **5 ms a 10 ms** em todos os parâmetros contínuos alterados. Essa janela é curta o suficiente para soar instantânea ao toque do pé, mas longa o suficiente para eliminar qualquer descontinuidade matemática no sinal.

---

## 4. Preservação de Caudas de Efeitos Espaciais (Mute-Input Trails Spillover)

Ao alternar de um solo exuberante (Cena C) de volta para uma estrofe seca e minimalista (Cena A):
- O bloco de **Delay** na Cena A é colocado em modo `Bypass (Mute-Input Trails)`.
- **Como Funciona:** O UltraRig interrompe a injeção de novas notas da guitarra na linha de atraso, mas **não apaga** as notas antigas que já estavam circulando na memória de eco.
- O eco e a reverberação do solo continuam flutuando e desaparecendo musicalmente no fundo enquanto a guitarra base limpa já começou a tocar a estrofe seguinte.

---

## 5. Estratégia Prática: Construindo uma Música Completa em 1 Preset

A melhor prática no UltraRig é dedicar **um único Preset para cada música do repertório**, distribuindo a dinâmica nos 4 botões de cena:

```
+-------------------------------------------------------------------------------+
|         ESTRUTURA DE 4 CENAS: PRESET "SONG-01-TITLE" (MODELO NAM: JCM800)     |
|                                                                               |
|  [SCENE A: INTRO / VERSO LIMPO]                                               |
|   - NAM Amp Gain: 2.2 (Som limpo dinâmico no limiar da quebra)               |
|   - Overdrive: BYPASS                                                         |
|   - Chorus Sutil: ON (Rate 0.8 Hz, Mix 20%)                                   |
|   - Reverb Room Curto: ON (Mix 15%)                                           |
|   - Delay: BYPASS                                                             |
|   - Scene Level: 0.0 dB                                                       |
|                                                                               |
|  [SCENE B: REFRÃO CRUNCH / RITMO PESADO]                                      |
|   - NAM Amp Gain: 5.5 (Crunch encorpado clássico de rock britânico)           |
|   - Overdrive: ON (Modo Transparent Boost: Drive 10%, Level 80%)              |
|   - Chorus: BYPASS                                                            |
|   - Reverb Room Curto: ON (Mix 12%)                                           |
|   - Delay: BYPASS                                                             |
|   - Scene Level: +1.0 dB                                                      |
|                                                                               |
|  [SCENE C: SOLO / LEAD HERO]                                                  |
|   - NAM Amp Gain: 7.0 (Sustentação pesada com compressão valvulada)           |
|   - Overdrive: ON (Modo TS9 Mid-Hump: Drive 35%, Tone 60%, Level 85%)        |
|   - Stereo Ping-Pong Delay: ON (Colcheia pontuada, Feedback 40%, Mix 28%)     |
|   - Reverb Hall: ON (Decay 2.4s, Mix 25%)                                     |
|   - Scene Level: +3.5 dB (Volume elevado para cortar a mix da banda)          |
|                                                                               |
|  [SCENE D: PONTE / AMBIENT SWELL]                                             |
|   - NAM Amp Gain: 3.0                                                         |
|   - Overdrive: BYPASS                                                         |
|   - Shimmer / Cloud Reverb Amplo: ON (Decay 4.5s, Mix 55%)                    |
|   - Tape Delay Modulado: ON (Feedback 60%, Mix 45% com spillover)             |
|   - Scene Level: -0.5 dB                                                      |
+-------------------------------------------------------------------------------+
```

---

## 6. Equalização de Volume Entre Cenas (Scene Level Staging)

Um erro comum ao programar cenas é aumentar o ganho do bloco NAM para solos sem compensar o volume geral:
1. **Modelos NAM High-Gain Comprimem a Dinâmica:** Ao aumentar o ganho de 4.0 para 8.0, o amplificador neural não fica substancialmente mais alto; ele apenas satura mais e comprime os picos.
2. **Utilize o Parâmetro `Scene Level`:** Para solos que precisam se destacar sobre a bateria e o baixo, deixe o amplificador no ganho desejado e aplique **+3.0 dB a +4.0 dB diretamente no parâmetro `Scene Level`** (ou em um bloco de Equalizador pós-amp).
3. **Monitore o Teto Digital:** Certifique-se de que o boost de solo na Cena C não empurre o medidor de saída master para a zona vermelha (**0 dBFS**).

---

## 7. Solução de Dúvidas e Problemas Frequentes

- **"Posso usar um modelo de Fender Twin na Cena A e um Mesa Boogie Dual Rectifier na Cena B?"**
  - *Resposta técnica:* Não dentro do mesmo preset. Mudar o arquivo NAM exige recarga dos coeficientes neurais na SRAM do processador, o que forçaria um dropout de áudio de 50 ms.
  - *Solução recomendada:* Escolha um modelo NAM de amplificador limpo/pedal-platform de alta fidelidade para o preset e utilize pedais de distorção de alto ganho com emulação analógica nos blocos de drive para a cena pesada, ou escolha um amplificador versátil (como Marshall JCM800 ou Friedman) modulando o ganho de 2.0 para 8.0 entre as cenas.
- **"Ouço um pequeno estalo ao comutar para a Cena de solo":**
  - *Causa:* O ganho master do preset ou o booster de solo está clipando a saída D/A em 0 dBFS no exato momento da transição.
  - *Solução:* Reduza o nível geral do preset em 2 dB e utilize o `Scene Level` de forma controlada.
