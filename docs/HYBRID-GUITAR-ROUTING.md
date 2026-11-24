# Guia de Roteamento e Processamento Paralelo para Guitarras Híbridas (Piezo na Ponte + Captadores Magnéticos) no UltraRig

Este documento aborda a conexão física, o processamento desacoplado em ramos paralelos (*Parallel DSP Paths*), a convolução de respostas de impulso acústicas e as estratégias de controle ao vivo para **Guitarras Elétrico-Acústicas Híbridas** no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

Instrumentos híbridos de alto desempenho — como a *Music Man John Petrucci / Majesty*, *PRS Custom 24 / Hollowbody II Piezo*, *Godin Multiac / LGX-SA*, *Taylor T5z*, *Fender Acoustasonic* e *ESP LTD EC-1000 Piezo* — combinam captadores magnéticos tradicionais (humbuckers ou single-coils) com carrinhos piezoelétricos embutidos na ponte (*Fishman*, *Graphtech Ghost* ou *L.R. Baggs*). Com o UltraRig, é possível processar esses dois mundos simultaneamente com total fidelidade sem carregar dois amplificadores físicos separados.

---

## 1. O Desafio Técnico: Dois Instrumentos em Um

| Elemento | Captador Magnético Tradicional | Captador Piezo na Ponte |
| :--- | :--- | :--- |
| **Resposta Tonal** | Médios focados, compressão harmônica, sustain elétrico. | Resposta de frequência ultra-ampla, transientes percussivos secos. |
| **Exigência de Amplificação** | Precisa de saturação valvulada (NAM) e corte de agudos de gabinete (CAB IR 4x12). | **Destruído por saturação:** exige pré-amp limpo de alta fidelidade e IR de violão acústico. |
| **Problema da Cadeia Única** | Se o piezo passar pelo modelo de alto ganho (5150), produz chiado e microfonia estridente. Se a guitarra elétrica passar pela cadeia acústica, soa magra e áspera. |

---

## 2. Métodos de Conexão Física ao UltraRig

Existem dois esquemas de conexão para guitarras híbridas:

```
Opção 1: Cabo Y Estéreo (Recomendado para Separação Total)
Guitarra [Jack TRS Estéreo] ---> Cabo Y Breakout ---> [INPUT L: Magnético] (Ramo A)
(Ponta = Mag / Anel = Piezo)                     ---> [INPUT R: Piezo]     (Ramo B)

Opção 2: Cabo P10 Mono (Sinal Mesclado Onboard pelo Pré da Guitarra)
Guitarra [Jack Mono] ---> Cabo P10 TS Padrão -------> [INPUT UltraRig]
                                                              |
                                           (Divisão interna por Crossover Split)
```

1. **Cabo Y Breakout TRS (Ponta/Anel):** O canal esquerdo (`L`) recebe exclusivamente os captadores magnéticos; o canal direito (`R`) recebe o sinal do piezo. Isso permite isolamento analógico total antes do DSP.
2. **Cabo P10 Mono Padrão:** Utiliza a chave seletora interna da guitarra (*Mag / Both / Piezo*) ou o potenciômetro de blend onboard para enviar um sinal somado em um único cabo.

---

## 3. Topologia de DSP em Ramos Paralelos (Parallel Split & Merge)

No UltraRig, configure o roteamento em duas ramificações totalmente independentes:

```
+-------------------------------------------------------------------------------+
|         ROTEAMENTO PARALELO PARA GUITARRA HÍBRIDA NO ULTRARIG                 |
|                                                                               |
|                     +---> [ RAMO A: CAMINHO ELÉTRICO MAGNÉTICO ] ---+         |
|                     |     - Noise Gate com Sidechain                |         |
|                     |     - Overdrive / Booster (TS9 Style)         |         |
|                     |     - Bloco NAM High Gain / Crunch            |         |
|                     |     - Cabinet IR 4x12 (Closed Back)           |         |
|                     |     - Stereo Tape Delay                       |         |
| [ Entrada de Sinal ]+                                               +>[ Merge]|
| (Split L/R ou Freq) |                                               | (Master)|
|                     +---> [ RAMO B: CAMINHO ACÚSTICO PIEZO ] -------+         |
|                           - HPF em 50 Hz (Elimina rumble de ponte)  |         |
|                           - De-Quack EQ (-4 dB em 3.2 kHz)          |         |
|                           - Acoustic Body IR (Violão Martin/Taylor) |         |
|                           - Compressor Óptico de Estúdio            |         |
|                           - Reverb Hall Amplo e Aveludado           |         |
+-------------------------------------------------------------------------------+
```

### 3.1 Ramo A: Otimização Elétrica (Rhythm & Lead)
- O sinal magnético alimenta a cadeia tradicional de guitarra elétrica de alto ganho.
- O bloco de **Cabinet IR (4x12)** é inserido exclusivamente neste ramo para moldar a resposta das distorções sem abafar o piezo.

### 3.2 Ramo B: Transformação Acústica via Body IR
- O cristal piezo sob as cordas de aço de uma guitarra de corpo sólido soa extremamente estalado e artificial ("plástico").
- O bloco convolutivo de **Acoustic Body IR (1024 pontos)** injeta a ressonância de caixa de madeira de um violão acústico *Dreadnought* ou *Grand Auditorium*.
- Um filtro passa-altas (**HPF em 50 Hz**) elimina estrondos causados pela palma da mão encostando na ponte flutuante.
- Um corte cirúrgico de EQ de **-4 dB em 3.2 kHz** neutraliza o pico agressivo do piezo elétrico.

---

## 4. O Efeito "Muralha Sonora" (Layered Wall of Sound)

Uma das técnicas mais consagradas por John Petrucci (*Dream Theater*) e Steve Lukather (*Toto*) é acionar **os dois ramos simultaneamente**:
- O Ramo A fornece a base rítmica pesada com distorção cortante nos médios.
- O Ramo B fornece o estalido brilhante de cordas de aço e o ar acústico de estúdio.
- O resultado é uma textura sonora cinematográfica impossível de ser alcançada com apenas uma guitarra convencional, preenchendo a mixagem com peso e definição percussiva.

---

## 5. Morfismo em Tempo Real com Pedal de Expressão

Ao conectar um pedal de expressão ao UltraRig, você pode transitar continuamente entre os dois mundos com o movimento do pé:

```
Posição do Pedal:       CALCANHAR (0%)               MEIO (50%)              PONTA (100%)
-----------------       --------------               ----------              ------------
Volume Ramo A (Mag):    0% (Mudo)        ------->    70%        ------->     100% (Solo Pesado)
Volume Ramo B (Piezo):  100% (Violão)    ------->    70% (Wall of Sound) ->  0% (Mudo)
```

- Em uma balada progressiva, o músico dedilha uma introdução puramente acústica e, ao pisar no pedal para a frente na entrada do refrão, a guitarra se transforma organicamente em um riff elétrico pesado sem nenhum clique de footswitch.

---

## 6. Arquitetura de 4 Cenas para Shows ao Vivo

```
+-------------------------------------------------------------------------------+
|             PRESET: "HYBRID-PRO-STAGE" (4 CENAS PROGRAMADAS)                  |
|                                                                               |
|  [Scene A] PURE ACOUSTIC DREADNOUGHT                                          |
|   - Ramo A (Magnético): MUTADO                                                |
|   - Ramo B (Piezo): 100% ATIVO + Body IR Taylor + Reverb Hall amplo           |
|   - Som autêntico de violão eletroacústico para estrofes limpas               |
|                                                                               |
|  [Scene B] HEAVY ELECTRIC CRUNCH                                              |
|   - Ramo A (Magnético): 100% ATIVO + NAM High-Gain + 4x12 Cab IR             |
|   - Ramo B (Piezo): MUTADO                                                    |
|   - Timbre moderno, seco e cortante para riffs pesados de metal/rock          |
|                                                                               |
|  [Scene C] LAYERED WALL OF SOUND (Petrucci Signature Blend)                   |
|   - Ramo A: 75% Mix (Crunch encorpado)                                        |
|   - Ramo B: 40% Mix (Brilho acústico percussivo por cima do drive)            |
|   - Impacto sonoro massivo com definição impecável de palhetadas              |
|                                                                               |
|  [Scene D] EPIC LEAD SOLO                                                     |
|   - Ramo A: 100% ATIVO + Solo Boost +3.5 dB + Stereo Delay sincronizado       |
|   - Ramo B: Cauda residual de ambiência aberta (spillover)                    |
|   - Sustentação infinita e presença no topo da mixagem da banda               |
+-------------------------------------------------------------------------------+
```

---

## 7. Checklist de Palco e Alinhamento de Fase (Stage Checklist)

- [ ] **Alinhamento de Fase (Phase Check):** Ao combinar os dois ramos na Cena C, faça um teste rápido de inversão de fase (0°/180°) no Ramo B. Escolha a posição que mantiver os graves mais encorpados e firmes.
- [ ] **Bateria do Pré-Amp Onboard:** Verifique a pilha de 9V da guitarra híbrida antes da apresentação (pré-amps de piezo distorcem de forma áspera quando a bateria enfraquece).
- [ ] **Roteamento para FOH (Front of House):** Se desejar enviar o violão direto para o sistema de PA estéreo e a guitarra elétrica para um amplificador/retorno no palco, utilize as saídas L e R desacopladas do UltraRig.
