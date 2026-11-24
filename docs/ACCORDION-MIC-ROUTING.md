# Guia de Roteamento, Pré-Amplificação e Efeitos para Acordeom / Sanfona Microfonada no UltraRig

Este documento estabelece as diretrizes de conexão estéreo, casamento de ganho, equalização corretiva e espacialização para **Acordeom, Sanfona e Gaita Ponto** no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

O acordeom é um instrumento acústico aerofone de palhetas livres com uma dinâmica sonora complexa e ampla resposta em frequência. Em palcos profissionais de *Forró, Baião, Sertanejo, Chamamé, Tango e Música Regional*, a sanfona é frequentemente captada por réguas de microfones condensadores internos (sistemas como *Harmonik*, *Microvox*, *Scandalli* ou *Shure/Sennheiser* clip-on), exigindo processamento desacoplado entre os **Baixos (Mão Esquerda)** e o **Teclado / Vozes (Mão Direita)**.

---

## 1. Topologia de Conexão: Desacoplamento Baixos vs. Teclado

A maioria dos sistemas de microfonação de alta fidelidade para acordeom entrega uma saída estéreo via conector P10 TRS ou cabo Y duplo (Dois P10 Mono):

```
+-------------------------------------------------------------------------------+
|         ROTEAMENTO ESTÉREO DE ACORDEOM / SANFONA NO ULTRARIG                  |
|                                                                               |
|  [ Microfone dos Baixos (Mão Esquerda) ]  ---> [ INPUT L ] ---> [ RAMO A ]    |
|  [ Microfone do Teclado (Mão Direita) ]   ---> [ INPUT R ] ---> [ RAMO B ]    |
|                                                                               |
|                             +---> [ RAMO A: BAIXOS / HARMONIA ] ------+       |
|                             |     - HPF em 40 Hz                      |       |
|                             |     - Fast Limiter (Segura botões)      |       |
|                             |     - Pan Centralizado (Mono Punch)     |       |
| [ Entrada de Sinal L/R ] --->+                                        +>[Merge|
|                             |                                         | (FOH) |
|                             +---> [ RAMO B: TECLADO / REGISTROS ] ----+       |
|                                   - De-Harshing Notch (3 kHz)         |       |
|                                   - Stereo Chorus / Musette Detune    |       |
|                                   - Plate/Hall Reverb Aveludado       |       |
+-------------------------------------------------------------------------------+
```

---

## 2. Processamento do Ramo A: Baixos (Mão Esquerda)

Os baixos do acordeom operam como a "bateria e contrabaixo" acústicos do instrumento:
1. **Filtro Passa-Altas (HPF em 38 Hz a 45 Hz):**
   - Elimina o impacto mecânico do fole abrindo e fechando e vibrações do tablado do palco.
2. **Compressão Rápida / Limiter:**
   - O impacto do dedo nos botões mecânicos da baixaria gera picos transitórios secos.
   - Ajuste um compressor rápido (**Attack: 3 ms, Release: 120 ms, Ratio: 4:1**) para nivelar os baixos fundamentais sem clipar a entrada da mesa de som.
3. **Equalização Corretiva dos Baixos:**
   - **Boost Suave em 80 Hz a 100 Hz:** Confere peso aveludado e corpo aos baixos de fole.
   - **Corte em 250 Hz a 350 Hz (-3 dB):** Limpa o som "abafado" da cavidade de madeira da mão esquerda.
4. **Posicionamento Panorâmico:** Mantenha os baixos rigorosamente no centro (**Pan: 0 / Center**) para estabilidade nos subwoofers do PA.

---

## 3. Processamento do Ramo B: Teclado e Registros (Mão Direita)

O lado do teclado abrange registros múltiplos (Clarinet, Bandoneon, Master, Musette, Piccolo):
1. **Atenuação de Estridência de Palhetas Livres (De-Harshing):**
   - Registros abertos com três ou quatro palhetas vibrando simultaneamente (*Musette*) geram batimento harmônico penetrante.
   - Aplique um corte com **Q médio (Q = 3.0) de -3.5 dB a -5 dB em 3.2 kHz a 4.2 kHz** para suavizar o timbre sem perder a presença melódica.
2. **Filtro Passa-Baixas Superior (LPF em 8.5 kHz a 10 kHz):**
   - Microfones colados nas válvulas do teclado captam o sopro de ar do fole e o ruído mecânico das teclas. Um corte suave amortece esses ruídos sem abafar o instrumento.
3. **Espacialização e Reverb de Sala:**
   - **Stereo Detune / Chorus Suave:** Micro-afinação de **+/- 3 cents** alarga a imagem estéreo da mão direita, criando uma experiência imersiva de sanfona italiana ou francesa.
   - **Plate / Room Reverb:** Decay de **1.6s a 2.2s** para conferir a sensação de uma sala de concerto natural.

---

## 4. Prevenção de Microfonia de Palco (Bellows & Stage Feedback)

O fole atua como uma bomba de sucção e expulsão de ar. Em palcos barulhentos com bateria e monitores de chão:
- **O Fenômeno do Uivo Acústico:** O som dos monitores entra pelas frestas das palhetas do acordeom, entrando em ciclo de feedback ressonante.
- **Filtros Notch Anti-Feedback no UltraRig:**
  - Identifique e aplique cortes cirúrgicos estreitos (**Q = 6.0 a 8.0**) nas frequências mais suscetíveis de microfonia de sanfona: **750 Hz** (ressonância do fole) e **2.4 kHz** (ressonância da câmara de válvulas).

---

## 5. Arquitetura de 4 Cenas para Shows ao Vivo

```
+-------------------------------------------------------------------------------+
|             PRESET: "ACCORDION-PRO-STAGE" (4 CENAS PROGRAMADAS)               |
|                                                                               |
|  [Scene A] FORRÓ & BAIÃO TRADICIONAL                                          |
|   - Baixos firmes e percussivos (Compressão rápida, HPF 42 Hz)                |
|   - Teclado seco, cortante e definido para passagens rápidas de semicolcheias |
|   - Room Reverb curto e discreto (12% mix)                                    |
|                                                                               |
|  [Scene B] TANGO & BANDONEON (Astor Piazzolla Expressivo)                     |
|   - Equalização escura e encorpada (LPF 7.5 kHz)                              |
|   - Plate Reverb quente e aveludado (Decay 2.4s)                              |
|   - Compressão de ataque lento permitindo dinâmicas dramáticas de fole        |
|                                                                               |
|  [Scene C] MUSETTE & VALSA FRANCESA (Estéreo Expandido)                       |
|   - Stereo Chorus ativo no Ramo B (+/- 4 cents de detune)                    |
|   - Hall Reverb amplo e tridimensional                                        |
|   - Timbre aveludado e rico para temas lentos e solenes                       |
|                                                                               |
|  [Scene D] HIGH-STAGE ANTI-FEEDBACK (Modo Emergência Palco Alto)              |
|   - Duplo filtro Notch ativo em 750 Hz e 2.4 kHz                              |
|   - Limitador de pico ativado nos dois canais                                 |
|   - Imunidade total a vazamento de bateria e retornos de palco                |
+-------------------------------------------------------------------------------+
```

---

## 6. Checklist de Passagem de Som (Soundcheck Checklist)

- [ ] **Bateria da Régua Interna:** Verificar se a bateria de 9V do sistema de microfones internos da sanfona está 100% carregada.
- [ ] **Desconexão de Gabinete Elétrico:** Confirmar que modelos de caixas de guitarra ou baixo elétrico estão em `Bypass` total.
- [ ] **Balanço entre Baixos e Teclado:** Ajustar o ganho relativo para que os baixos sustentem a levada rítmica sem encobrir o solo do teclado.
- [ ] **Posição em Relação aos Monitores:** Evitar apontar a baixaria diretamente para a corneta dos retornos de chão; priorizar fones *In-Ear Monitors (IEM)*.
