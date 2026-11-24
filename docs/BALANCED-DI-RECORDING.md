# Guia de Otimização e Interconexão para Palco Silencioso (Silent Stage) e Gravação Balanceada / XLR D.I. no UltraRig

Este documento estabelece os padrões de engenharia de áudio, conexão física, isolamento galvânico (*Ground Lift*), proteção contra tensão contínua (*Phantom Power*) e estrutura de ganho para apresentações em **Palco Silencioso (Silent Stage)** e gravações diretas de estúdio utilizando o firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

No paradigma moderno de palco silencioso — onde não há caixas de guitarra microfonadas gerando volume ensurdecedor e o monitoramento é feito 100% por fones de ouvido (*In-Ear Monitors - IEM*) —, a pedaleira atua como a fonte primária de sinal diretamente para a mesa de som (*FOH - Front of House*) e sistemas de gravação (*DAW*). Uma interconexão inadequada introduz ruídos de terra de 60 Hz, perda de dinâmica e risco elétrico ao hardware.

---

## 1. Desbalanceado (TS) vs. Balanceado (TRS / XLR)

A compreensão das limitações físicas de cada tipo de cabo evita ruídos devastadores em cabos longos:

```
CABO DESBALANCEADO (TS - Tip/Sleeve):
  [ Ponta (Sinal) ] -----------------------------------------------> Suscetível a RF e EMI
  [ Manga (Terra) ] -----------------------------------------------> Máximo seguro: 3 a 5 metros

CABO BALANCEADO (TRS / XLR - Pin 1, 2, 3):
  [ Pino 2 (Sinal Positivo +) ] ------------------------------------> Rejeição em Modo Comum
  [ Pino 3 (Sinal Negativo -) ] ------------------------------------> (CMRR)
  [ Pino 1 (Blindagem/Terra)  ] ------------------------------------> Seguro até 100+ metros!
```

- **Por que a Saída Direta da Pedaleira Precisa de Atenção:**
  - As saídas P10 da maioria das pedaleiras compactas são desbalanceadas (TS) ou balanceadas por impedância.
  - Conectar um cabo desbalanceado diretamente em uma medusa/multicabo de palco de 30 metros até a mesa de som transforma o cabo em uma antena receptora de ondas de rádio, chiados de dimmers de iluminação cênica e ronco de 60 Hz da rede elétrica.
  - **A Solução:** Uso obrigatório de uma **Direct Box (D.I. Box)** com saída balanceada XLR para trajetos longos.

---

## 2. Escolha da Direct Box: Passiva vs. Ativa com o UltraRig

```
+-------------------------------------------------------------------------------+
|                       D.I. PASSIVA (RECOMENDADA PARA O ULTRARIG)              |
|                                                                               |
|  UltraRig (Saída Linha ~100-600 Ω) ---> [ Transformador Magnético ] ---> Mesa |
|                                                    |                          |
|                                            ISOLAMENTO GALVÂNICO               |
|                                             (Sem contato elétrico)            |
|                                                                               |
|  - Não exige pilhas ou Phantom Power de 48V.                                  |
|  - Suporta altos níveis de sinal sem distorção harmônica.                     |
|  - O transformador de áudio (ex: Jensen, Neutrik) isola totalmente terras.    |
+-------------------------------------------------------------------------------+
```

- **Por que a D.I. Passiva é Superior neste Cenário:**
  - O UltraRig já possui uma saída ativa de baixa impedância e nível de linha (*Line Level*). Ele não necessita do pré-amplificador de alta impedância de uma D.I. ativa.
  - **D.I. Ativas** alimentadas por pilhas ou Phantom Power podem clipar e saturar se receberem o sinal de linha forte do UltraRig sem um atenuador (*Pad de -20 dB*) acionado.

---

## 3. O Perigo Oculto: Tensão Phantom Power (+48V)

Em palcos profissionais e igrejas, os técnicos de som frequentemente ligam o botão global de **Phantom Power (+48V)** na mesa de som para alimentar microfones condensadores:

> [!CAUTION]
> **Nunca utilize cabos adaptadores diretos P10 TRS para XLR Macho sem isolamento por transformador!**
> Se a mesa de som enviar +48V DC por um cabo direto conectado à saída da pedaleira, a tensão contínua pode atingir os transistores de saída do conversor D/A do hardware M-VAVE, gerando estalos de corrente contínua (*DC offset*) ou danos permanentes ao codec de áudio.
> **Uma D.I. Passiva com transformador bloqueia 100% da corrente contínua (+48V DC)**, protegendo o seu equipamento contra erros de operação na mesa de som.

---

## 4. Eliminação de Loops de Terra (Ground Loop & Hum)

Quando a sua pedaleira está ligada à tomada do palco e a mesa de som está conectada a um quadro de energia distante em outra fase elétrica:
- Forma-se uma antena de aterramento circular (*Ground Loop*), manifestando-se como um ronco constante e pesado de **60 Hz ou 120 Hz**.
- **A Solução: Chave Ground Lift:**
  - Na Direct Box, localize a chave **`GND / LIFT`** e mude para a posição **`LIFT`**.
  - Isso desconecta o pino 1 (blindagem de terra) no lado da mesa de som, quebrando o circuito fechado sem interromper a transmissão balanceada do áudio. O ronco desaparece instantaneamente.

---

## 5. Estrutura de Níveis: Casamento de Sinal (Gain Staging)

Mesas de som digitais modernas (*Behringer X32/Wing, Allen & Heath SQ, Yamaha CL/TF*) possuem pré-amplificadores de microfone extremamente sensíveis:

```
Escala de Níveis:
  [ Nível de Microfone (Mic Level) ] --------> -40 dBV a -20 dBV (Muito fraco)
  [ Nível de Instrumento (Guitar/Bass) ] ----> -20 dBV a -10 dBV (Médio)
  [ Nível de Linha Profissional (Line Level) ] -> +4 dBu (~1.23 V RMS) [UltraRig em Volume Alto]
```

### 5.1 Calibração para a Mesa de Som
1. **Ative o Pad na D.I. Box:** Acione a chave **`-15 dB` ou `-20 dB`** na Direct Box. Isso rebaixa o sinal de linha da pedaleira para o nível nominal de microfone esperado pela entrada XLR da mesa.
2. **Knob Master do UltraRig:** Ajuste o volume físico de saída da pedaleira entre **70% e 85%**.
3. **Ganho na Mesa (Trim de FOH):** O operador de áudio da mesa deve aplicar ganho moderado no pré-amp da mesa para que os picos mais fortes da sua guitarra fiquem entre **-18 dBFS e -12 dBFS**.
   - Isso garante uma margem de segurança de mais de 12 dB de *headroom*, impedindo que solos ou ataques de drive clipem o conversor da mesa digital.

---

## 6. Diagrama de Roteamento Estéreo para Palco Silencioso

Para aproveitar todo o potencial espacial dos delays estéreo, reverbs dimensionais e gabinetes duplos do UltraRig:

```
+-------------------------------------------------------------------------------+
|         ROTEAMENTO ESTÉREO DEFINITIVO PARA PALCO SILENCIOSO                   |
|                                                                               |
|                   [ Saída L / Mono ] ---> Cabo P10 TS ---> [ D.I. Passiva 1 ] |
|  [ UltraRig ]                                                    | (XLR L)    |
|                   [ Saída R Estéreo] ---> Cabo P10 TS ---> [ D.I. Passiva 2 ] |
|                          |                                       | (XLR R)    |
|                          |                                       v            |
|                  [ Fones P2 / IEM ]                        [ Medusa / PA ]    |
|                  (Retorno Pessoal)                        (Pan L100% / R100%) |
+-------------------------------------------------------------------------------+
```

- Peça ao técnico de som para abrir o canal esquerdo 100% para a esquerda (*Hard Left*) e o direito 100% para a direita (*Hard Right*).
- O som nos fones de ouvido dos outros músicos da banda e na plateia ganhará tridimensionalidade cinematográfica, deixando o centro da mixagem livre para a voz principal e a caixa da bateria.

---

## 7. Checklist de Passagem de Som (Silent Stage Checklist)

- [ ] **Gabinete IR Ativo:** Certifique-se de que o bloco de **Cabinet IR (CAB)** esteja ligado em todos os presets. Sem caixa microfonada física no palco, tocar direto em PA sem IR resultará em um som estridente e insuportável de distorção de linha.
- [ ] **Direct Box Conectada:** Sinal saindo via P10 TS curto (máx 1 metro) para D.I. Passiva com saída XLR balanceada para a medusa.
- [ ] **Chave Ground Lift Testada:** Caso haja qualquer zumbido no PA com a guitarra parada, mudar a chave da D.I. de `GND` para `LIFT`.
- [ ] **Pad de -20 dB Acionado na D.I.:** Evita saturar o pré-amplificador de microfone da mesa digital.
- [ ] **Nível de Fones Calibrado:** Testar o volume do fone de ouvido pessoal no conector P2 para garantir monitoramento seguro contra fadiga auditiva em shows longos.
