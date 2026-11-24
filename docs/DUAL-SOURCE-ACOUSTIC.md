# Guia de Roteamento e Processamento para Violões com Captação Dupla (Dual-Source) no UltraRig

Este documento aborda as técnicas avançadas de conexão, equalização corretiva, controle de fase e roteamento paralelo no **UltraRig** para violões equipados com sistemas de captação dupla (**Dual-Source**: *Piezo de rastilho ou magnético de boca + Microfone condensador interno*).

Sistemas renomados de captação mista (como *L.R. Baggs Anthem*, *Fishman Rare Earth Blend*, *Fishman Matrix Infinity Mic Blend*, *K&K Trinity* e *Maton AP5 Pro*) oferecem o melhor dos dois mundos: o peso e resistência a feedback do piezo combinados ao ar, textura de palheta e ressonância de corpo do microfone acústico. No entanto, sem o processamento digital adequado, essa combinação pode gerar cancelamento de fase grave e microfonia incontrolável no palco.

---

## 1. Características Tímbricas das Fontes

| Elemento Transdutor | Pontos Fortes | Limitações e Desafios |
| :--- | :--- | :--- |
| **Piezo sob o rastilho (Under-Saddle)** | - Excelente ataque percussivo e definição de notas.<br>- Resposta consistente nos graves.<br>- Quase imune a microfonias de ar. | - Ataque artificial e estalado ("*Piezo Quack*" em 2.5–4 kHz).<br>- Ausência de ressonância de corpo e ar acústico.<br>- Resposta seca e bidimensional. |
| **Microfone Condensador Interno** | - Ar acústico natural e brilho de agudos (8–14 kHz).<br>- Captação de técnicas percussivas no tampo.<br>- Som "amadeirado" autêntico de estúdio. | - Altamente suscetível a feedback na cavidade (120–250 Hz).<br>- Graves embolados e ressonância de onda estacionária.<br>- Cancelamento de fase por defasagem com o piezo. |

---

## 2. Métodos de Conexão Física ao UltraRig

Existem duas configurações comuns para violões dual-source:

```
Opção 1: Saída Mono P10 (Sinal pré-misturado pelo pré-amplificador interno do violão)
Violão [Jack P10 Mono] ---> Cabo P10 TS ---> [INPUT UltraRig]
                                                     |
                                   (Processamento via Split Crossover Paralelo)

Opção 2: Saída Estéreo TRS (Sinal com canais independentes por cabo balanceado/split)
Violão [Jack P10 Estéreo TRS] ---> Cabo Y Breakout ---> [INPUT L/R UltraRig]
(Tip = Piezo / Ring = Mic)
```

1. **Entrada Mono com Split Interno (Mais comum):**
   - O pré-amplificador onboard do instrumento soma as fontes. No UltraRig, utilizamos um divisor paralelo de frequência (*Crossover Split*) para processar os graves/médios do piezo separadamente dos agudos e ar do microfone.
2. **Entrada Estéreo Independente (Cabo TRS Breakout):**
   - O piezo entra pelo canal esquerdo (`L`) e o microfone pelo direito (`R`), permitindo cadeias de efeitos totalmente desacopladas antes do bloco de mixagem final.

---

## 3. Roteamento Paralelo de DSP no UltraRig (Parallel Split & Merge)

Para extrair o som definitivo de violão acústico, configure o UltraRig com uma topologia de ramificação paralela:

```
                            +---> [ Ramo A: Piezo / Ataque ] ---+
                            |     - HPF 45 Hz                   |
                            |     - Fast Peak Limiter           |
                            |     - De-Quack EQ (Corte 3 kHz)   |
                            |     - Body Impulse Response (IR)  |
[ Entrada de Áudio ] ---> [ Split ]                             | ---> [ Merge / Master ]
                            |                                   |      - Stereo Reverb
                            |                                   |      - Master HPF/LPF
                            +---> [ Ramo B: Microfone de Ar ] --+
                                  - Inversão de Fase (0°/180°)
                                  - Notch Filter (180 Hz)
                                  - Air Shelf Boost (+2dB @ 10kHz)
                                  - Slow Optical Compressor
```

### 3.1 Ramo A: Otimização do Transdutor Piezo (Fundação e Peso)

O objetivo no Ramo A é domar a aspereza mecânica do cristal piezoelétrico:
1. **Filtro Passa-Altas (HPF):** Ajustado em **45 Hz (18 dB/oitava)** para eliminar estrondos de manuseio e vibrações de palco.
2. **Compressor / Fast Limiter:** Com taxa de compressão moderada (3:1) e ataque ultrarrápido (1 ms a 5 ms) para segurar os picos perfurantes de palhetadas fortes.
3. **Neutralização do "Quack" (De-Quack EQ):** Atenuação paramétrica com Q médio (Q = 2.0 a 3.0) cortando de **-4 dB a -6 dB** centrado entre **2.8 kHz e 3.4 kHz**.
4. **Convolução de IR de Corpo (Acoustic Body IR):** Insira uma resposta de impulso de violão acústico (1024 pontos) **exclusivamente no Ramo A**. Isso injeta a ressonância física da madeira sem introduzir microfonia no microfone interno.

### 3.2 Ramo B: Condicionamento do Microfone Interno (Ar e Textura)

O microfone interno deve fornecer exclusivamente o brilho superior e a ambiência da caixa de ressonância:
1. **Filtro Passa-Altas Alto (High HPF):** Corte frequências abaixo de **100 Hz a 120 Hz**. As baixas frequências do microfone geram embolamento e disputam fase com o piezo.
2. **Filtro Notch Anti-Feedback Cirúrgico:** Aplique um corte agudo (Q = 6.0 a 8.0) de **-6 dB a -10 dB** na frequência de ressonância da boca do instrumento (geralmente entre **160 Hz e 220 Hz**).
3. **Realce de Ar (Air Shelf):** Ganho suave do tipo *High-Shelf* de **+2 dB a +3 dB em 10 kHz** para trazer respiração e estalido de cordas de aço/nylon.
4. **Compressor Óptico Suave:** Ataque lento (30 ms) e liberação suave (200 ms) para nivelar as notas sem matar o dinamismo percussivo de batidas no tampo.

---

## 4. O Alinhamento de Fase (Phase Coherence)

Quando duas fontes captam a mesma vibração a distâncias microscópicas distintas (o piezo na base das cordas e a cápsula suspensa no ar dentro do corpo), ocorre defasagem temporal:

```
Sinal do Piezo:        /\    /\    /\    /\
Sinal do Mic (Defasado): \/    \/    \/    \/
------------------------------------------------
Soma Cancelada:        ------------------------  (Som magro, oco e sem graves!)
```

### 4.1 Teste Prático de Inversão de Fase no UltraRig

1. No bloco de entrada ou no Ramo B, localize a chave **Phase Invert (0° / 180°)**.
2. Toque acordes cheios com notas graves soltas (corda Mi grave / E2 e Lá / A2).
3. Alterne a chave de fase:
   - Na posição **Em Fase (In-Phase)**, o som ganha peso imediato, o grave fica encorpado e a dinâmica preenche a sala.
   - Na posição **Fora de Fase (Out-of-Phase)**, o som soa distante, magro, nasal e perde sustentação nas notas fundamentais.
4. Mantenha a configuração que entregar o som mais robusto e natural.

---

## 5. Estrutura de Cenas Recomendadas para Palco

Programe as 4 Cenas do preset do UltraRig para se adaptar a diferentes momentos do show:

```
+-------------------------------------------------------------------------------+
|             PRESET: "DUAL-ACOUSTIC-PRO" (4 CENAS PROGRAMADAS)                 |
|                                                                               |
|  [Scene A] SOLO FINGERSTYLE (Equilíbrio de Estúdio)                           |
|   - Piezo 40% / Mic 60%                                                       |
|   - Reverb Hall amplo (1.8s) + Stereo Detune sutil                            |
|   - Máxima resposta dinâmica para toques com os dedos e percussão de tampo     |
|                                                                               |
|  [Scene B] STRUMMING BAND MIX (Corte Limpo em Banda Completa)                 |
|   - Piezo 75% / Mic 25%                                                       |
|   - Reverb curto Room (800ms) + Corte HPF elevado em 80 Hz                    |
|   - Compressão mais firme para nivelar levadas rítmicas de palheta            |
|                                                                               |
|  [Scene C] PERCUSSIVE FINGERSTYLE (Slap & Body Taps)                          |
|   - Piezo 50% / Mic 50%                                                       |
|   - Equalização do Mic com reforço em 80 Hz para batida de bumbo no corpo     |
|   - Compressor multibanda contendo picos estridentes de unhas                 |
|                                                                               |
|  [Scene D] HIGH-STAGE ANTI-FEEDBACK (Modo Emergência Palco Alto)              |
|   - Piezo 90% / Mic 10% (ou Mic totalmente mutado)                           |
|   - Duplo filtro Notch ativado (180 Hz e 2.8 kHz)                             |
|   - Imunidade total a retorno de monitores e pressão sonora de bateria        |
+-------------------------------------------------------------------------------+
```

---

## 6. Checklist de Passagem de Som (Acoustic Soundcheck)

- [ ] **Alinhamento de Fase Concluído:** Teste de inversão 0°/180° realizado ouvindo a resposta de graves.
- [ ] **Bateria e Pilha do Pré-Amp do Violão:** Verificada antes de subir ao palco (pilhas fracas causam distorção áspera no piezo).
- [ ] **Posicionamento do Feedback Buster (Tampa de Boca):** Caso use tampa de borracha na boca do violão, reduza o ganho do microfone interno, pois o som dentro da caixa selada fica excessivamente ressonante.
- [ ] **Gabinete de Guitarra Desativado:** Certifique-se de que nenhum bloco de emulação de caixa de guitarra (`CAB IR`) esteja ativo na cadeia.
- [ ] **Ajuste de Ganho de Entrada:** Picos de palhetada fortíssima não devem ultrapassar **-3 dBFS** no visor do UltraRig.
