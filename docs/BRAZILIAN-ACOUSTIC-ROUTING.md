# Guia de Configuração e Roteamento de Pré-Amp para Cavaquinho, Bandolim e Viola Caipira no UltraRig

Este documento estabelece as diretrizes de ganho de entrada, equalização corretiva, convolução de corpo acústico e controle de dinâmica para instrumentos acústicos de cordas de alta tensão tradicionais da música brasileira — **Cavaquinho, Bandolim e Viola Caipira** — no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

Instrumentos como o cavaquinho no Samba e Choro, o bandolim em rodas instrumentais e a viola caipira na música sertaneja de raiz e MPB apresentam transientes percussivos extremamente afiados e cordas de aço sob alta tensão mecânica. Quando amplificados por captadores piezoelétricos convencionais de rastilho ou contato, o som tende a soar fino, estridente e "plástico" (*piezo quack*), com forte tendência a microfonar ao lado de percussões pesadas (surdo, tantã e pandeiro).

---

## 1. Características Eletroacústicas por Instrumento

| Instrumento | Afinação Típica | Frequência Fundamental Mais Grave | Desafio Acústico Principal |
| :--- | :--- | :--- | :--- |
| **Cavaquinho** | Ré-Sol-Si-Ré (D4-G4-B4-D5) | Ré4 (~293 Hz) | Estridência metálica em 3.5–5 kHz nas palhetadas de samba; subgraves de surdo invadindo a captação. |
| **Bandolim** | Sol-Ré-Lá-Mi (G3-D3-A4-E5) [Duplas] | Sol3 (~196 Hz) | Ataque percussivo seco no tremolo rápido; falta de sustentação de corpo de madeira. |
| **Viola Caipira** | Cebolão em Mi / Ré (10 cordas duplas) | Si1 (~61 Hz) ou Mi2 (~82 Hz) | Ressonância excessiva de cordas simpatéticas soltas; acúmulo de médios ocos no tampo. |

---

## 2. Ganho de Entrada e Proteção de Headroom (Input Staging)

As palhetadas rápidas e secas de palhetas pesadas de acrílico ou celuloide em cordas de aço geram picos instantâneos colossais:
- **Risco de Clipping Digital:** No visor de entrada do UltraRig, certifique-se de que a batida mais pesada de cavaquinho ou ponteio de viola permaneça abaixo de **-3 dBFS**.
- **Ajuste de Pad Global:** Em captadores piezo ativos com bateria de 9V (como *Fishman Matrix* ou *Shadow*), configure o `Input Trim` do UltraRig entre **-4 dB e -8 dB** para garantir *headroom* seguro no conversor ADC.

---

## 3. Tabela de Filtragem Passa-Altas (HPF) Cirúrgica

Como instrumentos como o cavaquinho e o bandolim não produzem notas graves, qualquer frequência abaixo da fundamental do instrumento é ruído mecânico de manuseio ou ressonância do palco:

```
+-------------------------------------------------------------------------------+
|         FILTRAGEM PASSA-ALTAS (HPF) CIRÚRGICA POR INSTRUMENTO                 |
|                                                                               |
|  Instrumento          Fundamental          Corte HPF Recomendado              |
|  -----------          -----------          ---------------------              |
|  Cavaquinho           Ré4 (~293 Hz)        180 Hz a 220 Hz (18 dB/oitava)     |
|  Bandolim             Sol3 (~196 Hz)       140 Hz a 160 Hz (18 dB/oitava)     |
|  Viola Caipira        Mi2 (~82 Hz)          75 Hz a 85 Hz   (18 dB/oitava)    |
+-------------------------------------------------------------------------------+
```

> [!TIP]
> Aplicar um corte HPF em 190 Hz no cavaquinho elimina completamente o estrondo mecânico gerado pelo impacto do bumbo da bateria ou do surdo de corte nos palcos de samba, sem roubar absolutamente nada do corpo acústico do instrumento.

---

## 4. Neutralização de Estridência Metálica (De-Clicking EQ)

O atrito rígido de palhetas pesadas em cordas de aço produz picos desagradáveis de alta frequência:
1. **Corte do "Quack" e Estalo de Palheta:**
   - No bloco de EQ Paramétrico, aplique uma atenuação com **Q estreito (Q = 3.5 a 4.5)** cortando de **-4 dB a -6 dB** centrado entre **3.8 kHz e 4.8 kHz**.
   - Isso transforma o estalo "seco de lata" em um estalo aveludado de madeira nobre.
2. **Corte de Ressonância da Cavidade (Boxiness):**
   - Em cavaquinhos e bandolins com tampo de faia ou pinho, corte **-3 dB em 850 Hz a 1.1 kHz** para remover a sensação de "som oco".

---

## 5. Convolução de Acoustic Body IR (1024 Pontos)

O bloco de convolução de IR do UltraRig é essencial para devolver a ressonância de caixa acústica:
- Desative totalmente modelos de caixas elétricas (`CAB IR Bypass`).
- Carregue uma resposta de impulso acústica de alta resolução (**Acoustic Body IR de violão clássico de tampo maciço ou bandolim acústico de luthier**).
- **Ajuste de Blend (Mix):** Utilize entre **40% e 65% Wet**. A porção *Dry* preserva a precisão rítmica nos dedos do músico, enquanto a porção *Wet* adiciona o ar da madeira nobre e do tampo vibratório.

---

## 6. Controle de Dinâmica: Limiter Rápido + Compressor Óptico

A diferença de volume entre um dedilhado suave (*choro dolente*) e uma batida forte de samba (*levada de partido alto*) pode ultrapassar 25 dB:
1. **Fast Peak Limiter:**
   - Threshold ajustado para segurar picos repentinos sem distorcer o sinal.
   - Attack ultrarrápido (**1 ms a 3 ms**) para evitar clipping no PA.
2. **Compressor Óptico Suave:**
   - Ratio: **2.5:1 a 3.5:1**.
   - Attack: **15 ms a 25 ms** (mantém o ataque inicial da palheta intacto).
   - Release: **150 ms a 220 ms** (nivela a sustentação das cordas soltas).

---

## 7. Arquitetura de 4 Cenas para Shows ao Vivo

```
+-------------------------------------------------------------------------------+
|             PRESET: "BRAZILIAN-ACOUSTIC-PRO" (4 CENAS PROGRAMADAS)            |
|                                                                               |
|  [Scene A] RODA DE SAMBA CAVAQUINHO                                           |
|   - HPF em 190 Hz + Notch em 4.2 kHz (De-Clicking)                            |
|   - Fast Limiter contendo batidas pesadas de palheta                          |
|   - Room Reverb curto e discreto (10% mix) para ambiência acústica            |
|                                                                               |
|  [Scene B] CHORO BANDOLIM VIRTUOSO                                            |
|   - HPF em 150 Hz + Body IR de bandolim maciço (mix 55%)                      |
|   - Stereo Detune sutil (+/- 4 cents) duplicando o brilho das cordas duplas   |
|   - Plate Reverb suave (Decay 1.6s, mix 18%) para solos melódicos             |
|                                                                               |
|  [Scene C] VIOLA CAIPIRA PONTEIO                                              |
|   - HPF em 80 Hz + Realce suave em 2.2 kHz para o canto do ponteio            |
|   - Compressor óptico com sustentação estendida                               |
|   - Lush Hall Reverb amplo para temas de viola instrumental                   |
|                                                                               |
|  [Scene D] HIGH-STAGE ANTI-FEEDBACK (Modo Emergência Palco Aberto)            |
|   - HPF elevado em +20 Hz + Duplo Notch ativo em 220 Hz e 1.2 kHz             |
|   - Saída estritamente somada em mono                                         |
|   - Imunidade total a vazamento de microfones de percussão e monitores de chão|
+-------------------------------------------------------------------------------+
```

---

## 8. Checklist de Passagem de Som (Soundcheck Checklist)

- [ ] **Bateria do Captador Verificada:** Garantido que a pilha de 9V do pré onboard do cavaquinho/viola não esteja descarregada.
- [ ] **Filtro HPF Ativado:** Confirmado corte passa-altas acima de 150 Hz para cavaquinho/bandolim.
- [ ] **Ajuste de Ganho de Entrada:** Picos de palhetada fortíssima no partido-alto permanecem abaixo de -3 dBFS no visor do UltraRig.
- [ ] **Gabinete de Guitarra Elétrica Desativado:** Confirmado bypass total de caixas elétricas de 12" ou 10".
- [ ] **Posição em Relação ao Surdo/Percussão:** Evitar posicionar a boca do instrumento acústico diretamente alinhada ao bumbo ou surdo para impedir feedback por indução de ar.
