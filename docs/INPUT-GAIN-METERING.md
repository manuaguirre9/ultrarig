# Guia Técnico de Medição, Calibração e Ganho de Entrada (Input Gain & Digital Metering) no UltraRig

Este guia detalha os princípios de conversão eletroacústica, medição digital (Peak vs. RMS), relação sinal-ruído (SNR) e procedimentos práticos de calibração do ganho de entrada (*Input Trim / Pad*) no firmware **UltraRig** para pedaleiras da família M-VAVE (**Tank-G v1/v2, Tank-B e Black Box**).

Uma estrutura de ganho incorreta na entrada é a principal causa de timbres estéreis, excesso de ruído de fundo (*hiss*), distorção digital estalada (*clipping*) e comportamento anômalo em modelos de amplificadores **NAM (Neural Amp Modeler)**.

---

## 1. Fundamentos da Conversão A/D e Escala Digital (dBFS)

Os dispositivos de hardware M-VAVE utilizam conversores analógico-digitais (ADC) de 24-bit operando a 48 kHz. Na escala digital:

```
[ Sinal Analógico da Guitarra ] ---> [ Pré-Amp Analógico / Pad ] ---> [ Conversor ADC 24-bit ] ---> [ DSP 32-bit Float ]
                                                                                |
                                                                        Teto Absoluto: 0 dBFS
```

- **0 dBFS (Decibels Relative to Full Scale):** Representa a tensão máxima suportada pelo conversor ADC. Se o sinal de entrada ultrapassar 0 dBFS por 1 milissegundo sequer, ocorre o **Clipping Digital** (achatamento da onda em onda quadrada imperfeita), gerando artefatos harmônicos ímpares ásperos e estridentes.
- **Diferença entre Clipping Analógico e Digital:**
  - Em um circuito valvulado analógico, o excesso de sinal gera compressão musical e saturação aveludada.
  - Em um conversor digital A/D, o excesso de sinal destrói a fidelidade e não pode ser corrigido por nenhum plugin ou equalizador posterior no DSP.

---

## 2. Medição Peak (Pico) vs. Medição RMS (Potência Contínua)

O UltraRig disponibiliza medições visuais no painel de controle web e aplicativo mobile:

| Tipo de Medidor | O Que Mede? | Função Crítica na Guitarra / Baixo |
| :--- | :--- | :--- |
| **Peak Meter (dBFS Peak)** | A amplitude instantânea dos transientes mais rápidos (microsegundos). | Prevenir *clipping* digital no ataque da palhetada ou no estalo do polegar (*slap*). |
| **RMS Meter (dBFS RMS)** | A média quadrática da energia contínua do sinal ao longo do tempo. | Determina quanta saturação e dinâmica real serão enviadas aos modelos NAM e drives. |

```
Amplitude
  ^
  |      |   <- Pico Transitório (Peak: -3 dBFS) [Ataque da Palheta]
  |     / \
  |    /   \_______
  |   /            \_____  <- Nível Contínuo (RMS: -14 dBFS) [Sustentação da Nota]
  |  /                   \
  +------------------------------------------------------------> Tempo
```

---

## 3. O Desafio das Saídas de Captadores (Pickups Output)

Guitarras e baixos possuem saídas elétricas imensamente distintas:

| Tipo de Captador | Tensão Típica de Saída | Faixa de Nível no UltraRig sem Ajuste |
| :--- | :--- | :--- |
| **Single-Coils Vintage (Strat/Tele anos 50/60)** | ~80 mV a 200 mV RMS | Nível baixo (-24 a -18 dBFS). Pode exigir aumento de ganho limpo para melhorar SNR. |
| **Humbuckers Passivos Médios (PAF)** | ~250 mV a 400 mV RMS | Faixa ideal de fábrica (-16 a -10 dBFS). |
| **Humbuckers High-Output (JB, Invader, Super Dist.)** | ~500 mV a 900 mV RMS | Picos frequentes perto do teto (-6 a -1 dBFS). |
| **Captadores Ativos 9V/18V (EMG, Fishman Fluence)** | Até 2.0 V de pico | Risco iminente de *clipping* direto no conversor (0 dBFS intermitente). |
| **Piezos e Pré-Amps de Violão / Baixo Ativo** | Até 3.0 V de pico | Clipam a entrada analógica se não houver *Pad* ativado. |

---

## 4. O "NAM Reference Target": Como o Nível Afeta os Amplificadores Neurais

Os modelos de rede neural do **Neural Amp Modeler (NAM A2-Lite)** são treinados a partir de respostas a sinais de teste com níveis de ganho padronizados:
- **Se o seu sinal entrar 10 dB mais alto do que o alvo de treino:**
  - Um amplificador limpo (*Fender Twin Reverb*) entrará em *overdrive* pesado mesmo com o knob de ganho virtual no mínimo.
- **Se o seu sinal entrar 10 dB mais baixo:**
  - Um amplificador *High-Gain* (*Peavey 5150* ou *Mesa Boogie Dual Rectifier*) soará sem peso, magro e sem a compressão natural característica das válvulas.

---

## 5. Procedimento Prático de Calibração Passo a Passo

Siga este procedimento para calibrar perfeitamente a sua guitarra no UltraRig:

```
+-------------------------------------------------------------------------------+
|                      ESCALA DE CALIBRAÇÃO VISUAL DO ULTRARIG                  |
|                                                                               |
|  [-48 dBFS]        [-18 dBFS]        [-12 dBFS]       [-3 dBFS]     [0 dBFS]  |
|  [==== Seguro =====] [=== Zona Ideal RMS ===] [= Pico Max =] [! CLIPPING !]   |
|  [  Verde          ] [     Amarelo          ] [  Laranja   ] [  Vermelho  ]   |
+-------------------------------------------------------------------------------+
```

### Passo 1: Preparação do Instrumento
1. Conecte sua guitarra diretamente na entrada `INPUT` do pedal (sem outros pedais antes).
2. Abra todos os knobs de **Volume e Tone da guitarra no máximo (10)**.
3. Selecione o captador de maior saída do seu instrumento (geralmente o captador da ponte).

### Passo 2: O Teste da Palhetada Mais Forte ("Hardest Strum Test")
1. No painel web do UltraRig, acesse `Settings > Audio Input > Input Trim / Pad`.
2. Toque com a palhetada mais pesada e agressiva que você daria no momento de maior empolgação de um show ao vivo (palhetada descendente em um acorde aberto cheio, como Mi Maior / E).
3. Observe o indicador de pico (**Peak**):
   - **Objetivo Ideal:** O pico máximo registrado deve atingir entre **-6 dBFS e -3 dBFS**.
   - Se a barra atingir a zona vermelha (**0 dBFS** ou indicar *CLIP*): **reduza o Input Trim** (ex: -3 dB, -6 dB ou ative o *Input Pad*).
   - Se o pico mais forte não passar de **-15 dBFS**: **aumente o Input Trim** em incrementos de +2 dB até atingir a margem ideal.

### Passo 3: Verificação do Nível RMS de Sustentação
1. Toque acordes convencionais em dinâmica média de base (*mezzo-forte*).
2. O medidor de potência contínua (**RMS**) deve oscilar confortavelmente entre **-18 dBFS e -12 dBFS**.
3. Isso garante uma relação sinal-ruído superior a 90 dB e margem de dinâmica (*headroom*) suficiente para pedais de booster analógicos ou wah-wah pré-conversor.

---

## 6. Criação de Perfis para Múltiplas Guitarras (Multi-Guitar Profiles)

Se você utiliza mais de um instrumento no mesmo show (ex: uma Fender Stratocaster vintage e uma Ibanez com captadores ativos):
- **Não altere o ganho dos 32 presets individualmente!**
- Utilize o recurso de compensação de ganho global do UltraRig:
  - **Perfil 1 (Vintage Single-Coil):** `Input Trim: +3.0 dB` (iguala a energia enviada aos drives).
  - **Perfil 2 (Humbucker Standard):** `Input Trim: 0.0 dB` (neutro).
  - **Perfil 3 (Active Pickups / 9V):** `Input Trim: -6.0 dB / Pad Ativado`.

Dessa forma, todos os seus presets manterão a exata mesma quantidade de saturação, timbre e volume relativo, independente da guitarra conectada.

---

## 7. Diagnóstico e Resolução de Problemas (Troubleshooting)

- **"Meus presets de alto ganho possuem um chiado (hiss) ensurdecedor":**
  - *Causa provável:* O ganho de entrada estava calibrado muito baixo (-25 dBFS), obrigando o bloco NAM ou o volume do preset a aplicar ganho excessivo no domínio digital, amplificando o piso de ruído do conversor.
  - *Solução:* Aumente o `Input Trim` para posicionar os picos em -3 dBFS.
- **"O som limpo apresenta estalos e distorção áspera no ataque das notas":**
  - *Causa provável:* Clipping no estágio A/D. O conversor está saturando antes mesmo do sinal alcançar o bloco de efeitos.
  - *Solução:* Reduza o `Input Trim` em 3 a 6 dB até que o medidor de pico permaneça abaixo de -3 dBFS.
- **"O pedal de Envelope Filter / Auto-Wah quase não responde":**
  - *Causa provável:* Sinal fraco de entrada. O envelope follower digital não atinge o limiar de amplitude para abrir o filtro passa-baixas.
  - *Solução:* Calibre o ganho de entrada antes de reconfigurar a sensibilidade do efeito.
