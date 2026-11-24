# Guia de Roteamento, Pré-Amplificação e Otimização para Contrabaixo Acústico (Upright / Double Bass) no UltraRig

Este guia técnico aborda o casamento de impedância, filtragem subsônica, mitigação de microfonia mecânica e emulação de microfonação de estúdio para contrabaixo acústico vertical (**Upright Bass, Double Bass ou Rabecão**) no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

Amplificar um contrabaixo acústico em palcos modernos (especialmente ao lado de baterias acústicas e subwoofers potentes) é um dos maiores desafios da engenharia de áudio. O UltraRig permite transformar o sinal cru e estridente de captadores piezo em um som encorpado de estúdio, com total estabilidade contra feedback.

---

## 1. O Problema da Impedância de Entrada (Piezo Loading)

Captadores comuns de contrabaixo acústico (*The Realist David Gage*, *Fishman Full Circle*, *Underwood*, *K&K Bass Max*):
- São transdutores piezoelétricos passivos de alta impedância capacitiva.
- **Exigência Eletroacústica:** Para responder linearmente desde a nota fundamental mais grave (Mi1 = 41.2 Hz ou Si0 = 30.9 Hz), o piezo requer uma impedância de entrada entre **1 Megaohm (1 MΩ) e 10 Megaohms (10 MΩ)**.
- **Consequência do Descasamento:** Se conectado a uma entrada com impedância inferior a 500 kΩ, ocorre o efeito de carga (*loading*), provocando corte drástico nos subgraves e resultando em um som anêmico, nasal e com excesso de médios estalados (*quack*).

> [!TIP]
> Caso utilize captadores passivos puros sem pré-amplificador ativo na correia ou no corpo do contrabaixo, conecte o instrumento à entrada direta do UltraRig com o circuito de ganho ajustado em modo de alta impedância, ou utilize um buffer piezo simples (como o *Fishman Platinum* ou *Lehle RMI*) antes do pedal.

---

## 2. Topologia de DSP Recomendada no UltraRig

```
+-------------------------------------------------------------------------------+
|         CADEIA DE PROCESSAMENTO PARA CONTRABAIXO ACÚSTICO NO ULTRARIG         |
|                                                                               |
|  [ Entrada P10 / Buffer ]                                                     |
|            |                                                                  |
|            v                                                                  |
|  [ HPF Subsônico (38 Hz) ] --------> Elimina excursão inaudível do cone       |
|            |                                                                  |
|            v                                                                  |
|  [ Notch Filters Cirúrgicos ] ------> Corta ressonância de corpo (110 Hz)     |
|            |                                                                  |
|            v                                                                  |
|  [ Compressor Óptico Transparente ] > Suaviza transientes de pizzicato        |
|            |                                                                  |
|            v                                                                  |
|  [ Convolução de Acoustic Body IR ] > Emula microfone Neumann U47 de estúdio  |
|            |                                                                  |
|            v                                                                  |
|  [ Pré-Amp Limpo de Estúdio / DI ] -> Sat. aveludada estilo Neve/Avalon       |
|            |                                                                  |
|            v                                                                  |
|  [ LPF de Espelho (5.5 kHz) ] ------> Amortece atrito de arco / sapatas       |
|            |                                                                  |
|            v                                                                  |
|  [ Saída P10 / Fones ] -------------> Direto para PA frontal e monitor IEM    |
+-------------------------------------------------------------------------------+
```

---

## 3. Filtragem de Frequências Críticas

### 3.1 Filtro Passa-Altas Subsônico (Subsonic HPF)

O tampo massivo do contrabaixo capta vibrações do tablado e baixas frequências do bumbo da bateria:
- **Corte Sugerido:** **35 Hz a 42 Hz com inclinação de 18 dB/oitava**.
- **Benefício Acústico:** Não afeta a percepção do grave da corda Mi (41.2 Hz), mas economiza imensa potência do amplificador e do sistema de PA, evitando que o alto-falante excursione descontroladamente em frequências inaudíveis.

### 3.2 Eliminação de Ressonâncias de Caixa (Helmholtz Notch Filter)

Contrabaixos acústicos possuem frequências físicas naturais que entram em ciclo de feedback com monitores de chão:
1. **Ressonância de Ar da Cavidade (Helmholtz Air Resonance):**
   - Ocorre tipicamente entre **95 Hz e 125 Hz**. Gera um "boom" embolado e descontrolado nas notas Sol e Lá na corda Mi.
   - *Ação:* Crie um corte cirúrgico com **Q = 6.0**, atenuando de **-4 dB a -8 dB** na frequência exata do uivo.
2. **Ressonância de Tampo Superior (Top Plate Resonance):**
   - Ocorre entre **200 Hz e 260 Hz**. Faz o instrumento soar como uma "caixa oca" de papelão.
   - *Ação:* Atenue em -3 dB com Q médio (Q = 3.0) para limpar a definição dos médios.

### 3.3 Filtro Passa-Baixas Superior (Smooth LPF)

Diferente do contrabaixo elétrico, o contrabaixo acústico tradicionalmente não possui conteúdo musical útil acima de 6 kHz:
- **Corte Sugerido:** **LPF em 5.0 kHz a 6.0 kHz (12 dB/oitava)**.
- **Função:** Amortece o ruído áspero de unhas raspando no espelho de ébano e o atrito estridente da crina do arco (*arco scratch*).

---

## 4. Dinâmica: Pizzicato vs. Arco (Bowed)

| Técnica de Execução | Características Dinâmicas | Calibração de Compressão no UltraRig |
| :--- | :--- | :--- |
| **Pizzicato (Jazz / Blues)** | Transiente inicial extremamente rápido e agressivo com decaimento amadeirado curto. | **Compressor Óptico:**<br>- Attack: 8–15 ms<br>- Release: 150–250 ms<br>- Ratio: 2.5:1 a 3.5:1<br>- Nivelamento sem achatamento percussivo. |
| **Slap / Rockabilly** | Estalo seco do clique do espelho seguido de impacto de grave. | **Fast Limiter / Parallel Branch:**<br>- Attack ultrarrápido (< 2 ms) no clique.<br>- Corte de graves em 1 kHz no ramo do estalo. |
| **Arco (Com Arco de Crina)** | Formato de onda dente-de-serra contínuo, dinâmica sustentada e picos harmônicos intensos. | **Compressor Suave:**<br>- Attack lento: 35–50 ms<br>- Release longo: 350 ms<br>- LPF reduzido para 4.2 kHz. |

---

## 5. Convolução de IR de Corpo Acústico (Upright Body IR)

O bloco de convolução de IR do UltraRig (1024 pontos / 21.3 ms a 48 kHz) é a chave para transformar o som plástico do piezo no timbre nobre de um contrabaixo alemão artesanal microfonado com Neumann U47 ou Royer R-121:
- **Desative totalmente gabinetes de baixo elétrico (8x10 ou 4x10):** Eles adicionam coloração de caixa de guitarra/baixo e distorção em cones de papelão.
- **Carregue uma Acoustic Body IR:** Essa resposta de impulso contém a ressonância de caixa de madeira e ar gravada por microfones de fita em estúdio.
- **Ajuste de Blend (Mix):** Utilize entre **50% e 75% Wet**. Manter de 25% a 50% do sinal direto (*Dry*) preserva a precisão do ataque nos dedos para monitoração de palco.

---

## 6. Arquitetura de 4 Cenas para Shows ao Vivo

Programe o preset do UltraRig para transições instantâneas durante a apresentação:

```
+-------------------------------------------------------------------------------+
|             PRESET: "UPRIGHT-PRO-STAGE" (4 CENAS PROGRAMADAS)                 |
|                                                                               |
|  [Scene A] JAZZ PIZZICATO STUDIO                                              |
|   - Body IR (Mix 65%) + Opto Comp sutil + HPF 38 Hz                           |
|   - EQ: Corte leve em 115 Hz (cavidade) + Room Reverb suave (12% mix)         |
|   - Tonalidade natural, quente e amadeirada estilo Ron Carter                 |
|                                                                               |
|  [Scene B] ARCO / BOWED WARMTH                                                |
|   - LPF suave em 4.5 kHz para conter atrito estridente da crina de cavalo     |
|   - Compressão de ataque lento (40ms) + Plate Reverb amplo                    |
|   - Resposta aveludada e profunda para passagens orquestrais e baladas        |
|                                                                               |
|  [Scene C] ROCKABILLY SLAP & CLACK                                            |
|   - Ramo paralelo com boost em 1.5 kHz para o estalo da batida no espelho    |
|   - Fast Peak Limiter nos subgraves para estabilizar o bumbo                  |
|   - Slapback Delay curto (90ms) vintage                                       |
|                                                                               |
|  [Scene D] HIGH-VOLUME ANTI-FEEDBACK (Modo Emergência)                        |
|   - HPF elevado para 45 Hz + Duplo Notch ativo (115 Hz e 220 Hz)              |
|   - IR Mix reduzido para 35% (priorizando estabilidade de fase do piezo)      |
|   - Volume master calibrado para competir com bateria pesada sem microfonia   |
+-------------------------------------------------------------------------------+
```

---

## 7. Checklist de Passagem de Som (Soundcheck Checklist)

- [ ] **Impedância Adequada:** Verificado se o piezo passivo não está sofrendo atenuação drástica de graves por descasamento elétrico.
- [ ] **Filtro HPF Ativo em 38 Hz:** Confirmado para evitar excursão excessiva dos cones de subgraves da casa de show.
- [ ] **Teste de Ressonância da Cavidade:** Tocar a corda Lá (A1) e Mi (E1) no volume de palco; se o instrumento começar a vibrar sozinho, ajustar o ponto central do filtro *Notch* entre 100 Hz e 125 Hz.
- [ ] **Gabinete Elétrico Bypassed:** Garantido que não há modelos de caixas elétricas de 10" ou 15" ativas colorindo o timbre.
- [ ] **Monitores de Chão Desacoplados:** Posicionar o contrabaixo fora do eixo direto das cornetas dos monitores de palco ou priorizar fones *In-Ear Monitors (IEM)*.
