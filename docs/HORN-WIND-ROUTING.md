# Guia de Configuração e Roteamento para Metais e Instrumentos de Sopro (Horn & Wind FX)

Este guia técnico aborda a configuração, ganho de entrada, roteamento de sinal e calibração de efeitos (Envelope Filter, Auto-Wah, Pitch Shifter, Delays e Reverbs) no **UltraRig** para instrumentos de sopro e metais acústicos (**Saxofone Alto/Tenor/Barítono/Soprano, Trompete, Flugelhorn e Trombone**).

O ecossistema M-VAVE (Tank-G, Tank-B, Black Box) com UltraRig tornou-se uma ferramenta compacta e extremamente poderosa para instrumentistas de sopro em gêneros como Jazz Fusion, Neo-Soul, Funk dos anos 70, Reggae/Dub, Ska e Música Eletrônica.

---

## 1. Desafios Acústicos e Eletroacústicos de Instrumentos de Sopro

Diferente de captadores magnéticos de guitarras elétricas, microfones acoplados a instrumentos de sopro possuem características acústicas distintas:

| Parâmetro | Guitarra Elétrica | Instrumentos de Sopro (Sax / Metais) |
| :--- | :--- | :--- |
| **Transdutor Primário** | Captador Magnético Passivo/Ativo | Cápsula Condensadora (Clip-on) ou Microfone Dinâmico |
| **Faixa Dinâmica (Dynamic Range)** | Média (picos moderados no ataque da palheta) | Extrema (*Pianissimo* suave a *Fortissimo* de +120 dB SPL no pavilhão) |
| **Formato de Onda e Ataque** | Ataque percussivo imediato seguido de decaimento | Coluna de ar contínua, ataque moldado pela embocadura e golpe de língua (*tonguing*) |
| **Suscetibilidade a Feedback** | Média/Alta (Microfonia de cordas e captadores) | Severa (Microfonia direta entre o monitor de palco e a campana do instrumento) |
| **Resposta em Frequência Natural** | Médios concentrados (80 Hz a 5 kHz) | Ampla (Sub-graves mecânicos de chaves até harmônicos de sopro a 12 kHz+) |

---

## 2. Ganho de Entrada e Interconexão de Sinal (Input Staging)

### 2.1 Conexão do Microfone ao UltraRig

1. **Microfones Clip-on Condensadores (DPA 4099, Shure Beta 98H/C, Sennheiser e908, AMT):**
   - Exigem alimentação *Phantom Power* (+48V) ou transmissores sem fio (Shure, Sennheiser, AKG).
   - A saída do receptor sem fio (Wireless Receiver) deve ser conectada à entrada `INPUT` do pedal via cabo P10 (1/4" TS/TRS).
   - Ajuste o receptor sem fio para o nível **Line** ou **Instrument (-10 dBV)**.
2. **Microfones Dinâmicos com Fio (Shure SM57, SM58, Electro-Voice RE20):**
   - Requerem um transformador casador de impedância (XLR fêmea para P10 macho, como o Shure A85F) ou um pré-amplificador compacto antes da entrada do UltraRig.

### 2.2 Prevenção de Clipping Digital (A/D Clipping)

Instrumentos de sopro geram transientes de pressão sonora colossais em ataques de *slap-tongue* ou passagens fortíssimas (*ff*):
- No menu do UltraRig (`Global Settings > Audio Input`):
  - Configure `Input Level / Trim` entre **-6 dB e -12 dB** dependendo da saída do receptor sem fio.
  - Observe o medidor de entrada do UltraRig: mesmo na nota mais aguda e com maior pressão de ar do show, os picos não devem ultrapassar **-3 dBFS**.
  - Deixe um *headroom* acústico generoso; a dinâmica é restaurada de forma linear internamente no processador DSP de 32-bit.

---

## 3. Topologia da Cadeia de DSP: O Que Ativar e O Que Desativar

### 3.1 O Erro Clássico: Amp Sim & Cabinet IR

Por padrão, presets de guitarra elétrica no UltraRig contêm emulações de amplificador valvulado (NAM / Neural Amp Modeler) e respostas de impulso de gabinetes de guitarra (Cabinet IRs):
- **Gabinete de Guitarra (IR 4x12 / 2x12):** Corta brutalmente todas as frequências acima de 5 kHz e gera picos estridentes nos médios, destruindo o brilho natural e o timbre acústico do saxofone ou trompete.
- **Modelos de Amplificador de Alto Ganho:** Geram distorção excessiva e microfonia descontrolada ao menor aumento de volume de palco.

> [!IMPORTANT]
> Para timbres acústicos transparentes com efeitos espaciais e modulações, **desative completamente o bloco de Gabinete IR (`CAB: BYPASS`)** e utilize o bloco de **Pré-Amp em modo Flat/Clean Studio** ou contorne-o inteiramente (`AMP: BYPASS`).

### 3.2 Uso Intencional de Amp Sim (Lo-Fi Megafone / Solo Distorcido)

Se o objetivo estético for um timbre sujo estilo *vintage blues harmonica*, rádio antigo ou solo industrial moderno:
1. Ative um modelo NAM de baixo ganho (*Tweed Clean* ou *Fender Champ Crunch*).
2. Insira um filtro passa-faixa acentuado (HPF em 400 Hz e LPF em 3 kHz).
3. Reduza a sensibilidade de entrada para conter o feedback de palco.

---

## 4. Calibração de Envelope Filter e Auto-Wah para Sopro

O Envelope Filter responde à amplitude do sinal para abrir e fechar a frequência de corte de um filtro ressonante (efeito vocal "quack" clássico de funk/fusion). Como instrumentos de sopro sustentam a nota com pressão de ar constante, a calibração difere radicalmente da guitarra elétrica.

```
+--------------------------------------------------------------------------+
|                 CALIBRAÇÃO DE ENVELOPE FILTER PARA SOPRO                 |
|                                                                          |
|   Dinâmica de Ar (Ataque de Língua) ---> Detetor de Amplitude            |
|                                                 |                        |
|                                         Ajuste de Sensibilidade          |
|                                                 v                        |
|   Sinal Limpo ---> [ Filtro Passa-Baixas Ressonante (Sweep) ] ---> Saída |
|                                   ^                                      |
|                                   | (Envelope Attack: 15-25ms)           |
|                                   | (Envelope Decay: 120-200ms)          |
+--------------------------------------------------------------------------+
```

### 4.1 Parâmetros Críticos do Envelope Filter

1. **Sensitivity / Threshold:**
   - Para guitarra: ajustado alto para responder ao golpe da palheta.
   - Para sopro: ajuste de modo que a nota tocada em *mezzo-forte (mf)* abra o filtro até 70% da extensão, reservando o pico máximo ("abertura total") apenas para ataques intencionais em *fortissimo (ff)*.
2. **Attack Time:**
   - Configure entre **15 ms e 30 ms**. Um ataque ultrarrápido (< 5 ms) soará áspero e metálico no início de cada articulação de língua.
3. **Decay / Release Time:**
   - Configure entre **120 ms e 250 ms**. Se for curto demais (< 80 ms), o filtro fechará no meio de uma nota longa sustentada, provocando perda de volume e corpo.
4. **Resonance / Q:**
   - Mantenha entre **40% e 65%**. Valores acima de 70% geram picos harmônicos tão intensos que provocam microfonia instantânea com os monitores de palco.
5. **Filter Sweep Direction:**
   - `UP (Passa-Baixas abrindo para agudos)`: Ideal para linhas funk estaladas de sax alto e trompete.
   - `DOWN (Invertido)`: Cria um som fechado e aveludado estilo "muter" (Harmon Mute em trompete).

---

## 5. Roteamento de Pitch Shifting e Oitavadores (Sub-Octave & Synth Horns)

Oitavadores analógicos ou polifônicos no UltraRig permitem transformar um saxofone tenor em um sax barítono ou trombone baixo, criando linhas de baixo sintetizadas impressionantes (estilo Michael Brecker / Seamus Blake).

### 5.1 Boas Práticas de Tracking com Instrumentos de Sopro

1. **Posicionamento do Bloco:**
   - Posicione o bloco de **Pitch / Octaver** imediatamente após o bloco de entrada e equalização corretiva, antes de qualquer modulação, delay ou saturação.
2. **Filtragem de Ruído de Chaves e Ressonâncias Subgraves:**
   - Microfones clip-on captam ruídos mecânicos de sapatas e chaves fechando. Esses ruídos graves confundem o algoritmo de detecção de frequência do oitavador, causando instabilidade e "engasgos" (*glitches*).
   - Insira um filtro passa-altas (HPF) cortando frequências abaixo da nota fundamental mais grave do instrumento antes do pitch shifter.
3. **Equilíbrio Wet / Dry:**
   - Para emulação de seção de metais dobrada: `Dry 60% / Wet (-1 Oct) 40%`.
   - Para linha de sintetizador/baixo solo: `Dry 15% / Wet (-1 Oct) 85%` combinado com um filtro envelope.

---

## 6. Prevenção de Microfonia e Acústica de Palco

A proximidade entre o microfone de campana e as caixas de retorno de palco (ou PA frontal) torna o uso de pedais de ganho e filtro um desafio acústico.

```
+--------------------------------------------------------------------+
|          FILTRAGEM GLOBAL CORRETIVA DE FREQUÊNCIAS (HPF)           |
|                                                                    |
| Instrumento         Nota Mais Grave    Corte HPF Sugerido          |
| -----------------   ----------------   ------------------          |
| Trompete            F#3 (~185 Hz)      140 Hz - 160 Hz (18dB/oct)  |
| Saxofone Alto       Db3 (~138 Hz)      110 Hz - 120 Hz (18dB/oct)  |
| Saxofone Tenor      Ab2 (~103 Hz)      80 Hz - 90 Hz   (18dB/oct)  |
| Trombone / Barítono E2 (~82 Hz)        55 Hz - 65 Hz   (18dB/oct)  |
+--------------------------------------------------------------------+
```

### 6.1 Equalização Paramétrica Notch para Ressonância da Campana

A campana metálica de trompetes e saxofones possui frequências ressonantes naturais que entram em ciclo de feedback com muita facilidade ao usar modulação ou saturação:
1. No bloco de EQ Paramétrico, crie um corte cirúrgico (*Notch*) com **Q estreito (Q = 6.0 a 8.0)** atenuando de **-4 dB a -8 dB**.
2. Frequências comuns de ressonância de campana:
   - **Saxofone Alto:** 1.2 kHz e 2.8 kHz.
   - **Saxofone Tenor:** 850 Hz e 1.9 kHz.
   - **Trompete:** 1.5 kHz e 3.4 kHz.

---

## 7. Delays Espaciais e Efeitos Dub / Reggae

Instrumentos de sopro brilham com repetições longas e ecos espaciais:
- **Ping-Pong Tape Delay:** Em conexões estéreo (via cabo TRS 3.5mm para 2x P10), o delay estéreo abre o som da trompa no campo sonoro, separando o instrumento solo das frequências centrais da bateria e baixo.
- **Dynamic Ducking no Delay:** Configure o parâmetro de ducking para atenuar as repetições em -6 dB enquanto o músico estiver soprando frases rápidas, permitindo que os ecos "desabrochem" nos finais de frase e pausas de respiração.

---

## 8. Arquitetura de Preset Recomendada: 4 Cenas para Show

Estruture os 4 bancos de cena do UltraRig para alternar instantaneamente durante a apresentação:

```
+---------------------------------------------------------------------+
|         PRESET: "HORN-STUDIO-PRO" (4 CENAS PROGRAMADAS)             |
|                                                                     |
|  [Scene A] ACOUSTIC CLEAN STUDIO                                    |
|   - Opto Comp (transparência e controle de dinâmicas fortes)        |
|   - EQ Paramétrico (HPF de instrumento + Notch de campana)          |
|   - Room Reverb suave (350ms, mix 18%)                              |
|                                                                     |
|  [Scene B] 70s FUNK AUTO-WAH                                        |
|   - Envelope Filter (Sweep UP, Decay 160ms, Resonance 55%)          |
|   - Fast Compressor pós-filtro (para conter picos de ressonância)   |
|   - Slapback Delay curto (85ms, mix 15%)                            |
|                                                                     |
|  [Scene C] SYNTH SUB-OCTAVE BASS                                    |
|   - Octaver Monofônico (-1 Oitava 75%, Dry 25%)                     |
|   - Analog Chorus sutil (Rate 0.8 Hz, Depth 35%)                    |
|   - Plate Reverb atmosférico                                        |
|                                                                     |
|  [Scene D] SPACE DUB ECHO                                           |
|   - Tape Delay sincronizado por Tap-Tempo (Pontuada de Semínima)    |
|   - Ducking ativado (-8 dB durante sopro ativo)                     |
|   - Lush Hall Reverb (Decay 2.8s, mix 30%)                          |
+---------------------------------------------------------------------+
```

---

## 9. Lista de Verificação Rápida Antes do Show (Soundcheck Checklist)

- [ ] **Ganho do Receptor Sem Fio:** Definido em nível de instrumento sem clipar o receptor.
- [ ] **UltraRig Input Trim:** Verificado na passagem de som em fortissimo (*ff*); pico em -3 dBFS.
- [ ] **Cab Sim Desativado:** Bloco `CAB: BYPASS` confirmado em todas as 4 cenas acústicas.
- [ ] **Filtro HPF Ativado:** Frequência de corte ajustada para a nota fundamental do instrumento.
- [ ] **Ressonância do Envelope Filter:** Testada no volume de palco para garantir que picos do filtro não disparem feedback nos monitores.
- [ ] **Posição dos Monitores de Palco:** Monitores de chão apontados para a parte de trás da cabeça do instrumentista ou uso de fones *In-Ear Monitors (IEM)* para isolamento perfeito.
