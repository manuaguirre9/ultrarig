# Guia de Calibração, Otimização de Headroom e Roteamento para Captadores Ativos no UltraRig

Este documento estabelece as diretrizes de engenharia eletroacústica, prevenção de ceifamento no conversor analógico-digital (ADC), calibração de faixa dinâmica e modelagem de amplificadores de alto ganho para guitarras equipadas com **Captadores Ativos e de Alta Saída** (*modelos estilo EMG 81/85/60, Fishman Fluence Modern/Classic, Seymour Duncan Blackouts e passivos de altíssimo ganho*) no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

Captadores ativos são o padrão da indústria para metal moderno, djent, rock progressivo e estilos pesados (*Metallica, Slayer, Slipknot, Animals as Leaders, Periphery*). Por incorporarem pré-amplificadores alimentados por bateria de 9V ou 18V embutidos no próprio instrumento, eles oferecem ruído de fundo praticamente nulo, imunidade a cabos longos e um sustain avassalador. No entanto, sua tensão de saída extremamente elevada apresenta um risco sério de distorção digital indesejada quando conectados à entrada física de processadores digitais.

---

## 1. A Eletrônica dos Captadores Ativos vs. Passivos

A diferença física e elétrica entre captadores passivos tradicionais e ativos modernos é drástica:

```
+---------------------------------------------------------------------------------------+
|                    COMPARAÇÃO ELÉTRICA: PASSIVOS vs. ATIVOS                           |
+---------------------+-----------------------------+-----------------------------------+
| Parâmetro           | Captadores Passivos (PAF/SC)| Captadores Ativos (EMG / Fishman) |
+---------------------+-----------------------------+-----------------------------------+
| Bobinas e Espiras   | 5.000 a 10.000 voltas de    | Bobinas menores com menos voltas; |
|                     | fio; alta indutância e C    | indutância muito baixa e ampla    |
|                     | parasita; agudos atenuados  | resposta de frequências planas    |
+---------------------+-----------------------------+-----------------------------------+
| Pré-Amplificador    | Nenhum (100% passivo)       | Pré-amp diferencial interno com   |
|                     |                             | alimentação ativa de 9V ou 18V    |
+---------------------+-----------------------------+-----------------------------------+
| Impedância de Saída | Alta (10 kΩ a 25 kΩ)        | Ultra-Baixa (< 2 kΩ)              |
|                     | sensível à perda por cabos  | sinal forte, estável e bufferizado|
+---------------------+-----------------------------+-----------------------------------+
| Tensão de Pico      | ~100 mV a 500 mV            | **2.0V a 3.5V de Pico a Pico**    |
| (Peak-to-Peak Out)  | pico de palhetada moderado  | palhetada forte atinge teto ADC   |
+---------------------+-----------------------------+-----------------------------------+
```

---

## 2. O Perigo do Ceifamento no Conversor ADC (Hardware Clipping)

A entrada física P10 dos pedais M-VAVE Tank-G/B e Black Box possui um conversor analógico-digital (ADC) projetado para suportar sinais de instrumentos elétricos padrão:

```
[ Sinal Ativo de Alta Tensão: ~3.0V Peak ]
                   │
                   ▼
[ ESTÁGIO DE ENTRADA DO HARDWARE M-VAVE ]
(Limite Máximo do ADC: ~1.8V - 2.0V RMS)
                   │
                   ├─► SEM CALIBRAÇÃO: Ceifamento do conversor analógico-digital!
                   │   Ocorre distorção digital estática (fizz metálico áspero)
                   │   que NÃO pode ser corrigida por equalizadores ou gates posteriores.
                   │
                   └─► COM ULTRA-PAD NO ULTRARIG (-6 dB a -10 dB):
                       O sinal é atenuado analogicamente / escalonado antes da conversão,
                       preservando 100% do headroom digital e dinâmica musical!
```

### Sintomas de ADC Clipping no Palco ou Estúdio:
- Um estalo metálico estridente e desagradável no instante exato do ataque de palheta em acordes pesados.
- Sensação de que o amplificador de alto ganho soa "áspero", "frio" ou "digitalizado".
- Perda de definição de notas em acordes estendidos (*dissonâncias sujas*).

---

## 3. Calibração de Ganho e Roteamento DSP no UltraRig

Para extrair o poder máximo dos captadores ativos sem comprometer a fidelidade do conversor:

```
[ GUITARRA ATIVA (EMG/FISHMAN) ]
              │
              ▼
    [ INPUT PAD: -6 dB ] ──► [ NOISE GATE ULTRA-RÁPIDO ] ──► [ OVERDRIVE OD-808 ]
    (Proteção contra ADC       (Atenua ruído de alto ganho    (Corta graves 720Hz,
     Clipping analógico)        sem comer cauda da nota)       empurra médios 1kHz)
                                                                       │
                                                                       ▼
[ SAÍDAS XLR / FONES ] ◄── [ RESPOSTA DE CABINE (IR) ] ◄── [ HIGH-GAIN AMP (5150) ]
 (Sinal Balanceado          (Roll-off acima de 6.8 kHz     (Atenuação de graves
  para gravação / PA)        para eliminar fizz ativo)      no estágio de pré-amp)
```

### Otimizações Essenciais:
1. **Ativação do Input Pad (-6 dB ou -10 dB)**:
   - No menu global de entrada do UltraRig, configure `Input Level` para `-6 dB` para guitarras com EMGs de 9V e `-10 dB` para guitarras com mod de 18V ou Fishman Fluence em Voice 1.
2. **Ajuste de Compressores**:
   - Como os captadores ativos já realizam uma pré-compressão natural através de seus circuitos operacionais internos, **evite** compressores agressivos antes do amplificador. Se usar compressor, aumente o limiar (*Threshold*) e use taxas baixas (*Ratio 2:1*) para não estagnar o ataque.
3. **Equalização Pré-Ganho (Tight Djent Low-Cut)**:
   - Captadores ativos modernos empurram muita energia em frequências graves. Ative o filtro passa-altas (*Low-Cut*) pré-distorção ajustado entre **$90\text{ Hz}$ e $120\text{ Hz}$** para que os palm-mutes soem ultra-apertados e percussivos sem embolar o amplificador valvulado.
4. **Controle de Aspereza de Agudos (*De-Fizz*)**:
   - Pela ausência de capacitância de cabo, os agudos de captadores ativos estendem-se até 15 kHz. Ajuste o filtro passa-baixas (*High-Cut*) do bloco de IR ou saída entre **$6.5\text{ kHz}$ e $7.2\text{ kHz}$** para simular o comportamento de alto-falantes reais de guitarra (*Celestion V30*).

---

## 4. Fishman Fluence Multi-Voicing e Modificação de 18V

### Fishman Fluence Multi-Voicing no UltraRig:
- **Voice 1 (Modern Active)**: Saída maciça, médios ligeiramente cavados, agudos estendidos. Ideal para riffs djent e afinações baixas (Drop D, Drop A, Drop C). Necessita `Input Pad: -8 dB`.
- **Voice 2 (Crisp / Clean / Organic)**: Menor tensão de saída, dinâmica mais aberta, calor orgânico de captador passivo. No UltraRig, permite abrir o ganho do amplificador e usar o botão de volume para transitar suavemente para timbres semi-limpos.

### O Mod de 18V nos Captadores EMG:
- Conectar duas baterias de 9V em série nos captadores EMG 81/85 não dobra o volume de saída, mas dobra o **teto de headroom interno** do pré-amplificador integrado (de 9V para 18V). Isso reduz a compressão interna do captador em palhetadas brutas, oferecendo um ataque muito mais percussivo e dinâmico, que brilha quando calibrado no UltraRig com o Input Pad adequado.

---

## 5. Presets de Performance em 4 Cenas (Scenes A/B/C/D)

```
+---------------------------------------------------------------------------------------+
|                 BANCO DE PRESET ULTRA-ACTIVE: 4 CENAS DE PERFORMANCE                  |
+---------------------+-------------------+---------------------+-----------------------+
| Cena A: Modern      | Cena B: Fishman   | Cena C: 18V Dynamic | Cena D: Pristine      |
| Djent Tightness     | Multi-Voice Lead  | High-Gain Crunch    | High-Headroom Clean   |
+---------------------+-------------------+---------------------+-----------------------+
```

### Cena A: Modern Djent Tightness (Drop Tunings & Riffs Perfeitas)
- **Objetivo**: Resposta percussiva ultra-rápida para palm-mutes em afinações graves (Drop A / Drop G), com silêncio cirúrgico entre as notas.
- **Blocos DSP**:
  - `Input Pad`: -8 dB
  - `Fast Noise Gate`: Threshold -48 dB, Attack 1 ms, Release 25 ms (Corte seco)
  - `Pre-Drive Overdrive`: Model TS-808, Drive 0%, Tone 65%, Level 85% (Filtro tight de médios)
  - `Low-Cut Pré-Amp`: 110 Hz
  - `Amp Model`: High-Gain Peavey 5150 / EVH Lead Channel
  - `Cab IR`: 4x12 Oversized com Celestion V30 (High-Cut em 6.8 kHz)

### Cena B: Fishman Multi-Voice Lead (Solo Virtuoso Sustentado)
- **Objetivo**: Sustentação infinita tipo violino, solo encorpado e harmônicos artificiais explodindo com facilidade na palhetada.
- **Blocos DSP**:
  - `Input Pad`: -6 dB
  - `Noise Gate`: Threshold -56 dB, Release 140 ms (Permite decaimento musical)
  - `Amp Model`: Soldano SLO-100 Lead
  - `Equalização`: Mid Boost +2.5 dB @ 1.2 kHz, Treble 60%
  - `Ambiência`: Stereo Dual Delay (380 ms L / 500 ms R, Feedback 30%) + Hall Reverb (Decay 2.2s, Mix 20%)

### Cena C: 18V Dynamic High-Gain Crunch (Rock / Heavy Tradicional)
- **Objetivo**: Para guitarristas que utilizam o mod de 18V nos EMGs e desejam dinâmica e clareza de acordes com pegada orgânica (*estilo Metallica Master of Puppets / Alice in Chains*).
- **Blocos DSP**:
  - `Input Pad`: -10 dB (Headroom analógico total)
  - `Amp Model`: British Marshall JCM800 modificado com booster transparente
  - `Low-Cut`: 85 Hz
  - `Presence`: 55%
  - `Cab IR`: 4x12 Marshall 1960A Greenback (Mix 100%)

### Cena D: Pristine High-Headroom Active Clean (Limpo Cristalino Moderno)
- **Objetivo**: Som limpo cristalino, brilhante e sem nenhum ceifamento de transientes. Perfeito para introduções limpas de metal, acordes de neo-soul e arpejos espaciais.
- **Blocos DSP**:
  - `Input Pad`: -6 dB
  - `Compressor Suave`: Ratio 2.2:1, Attack 40 ms, Release 120 ms
  - `Amp Model`: Roland JC-120 Jazz Chorus ou Fender Twin limpo
  - `Stereo Detune Chorus`: Modulação sutil sem oscilação cíclica
  - `Lush Space Reverb`: Mix 35%, Decay 3.8s, High-Damp 5.0 kHz

---

## 6. Cuidados e Manutenção com Baterias no Palco

1. **Troca Preventiva de Baterias**:
   - Quando a bateria de 9V do captador ativo atinge menos de 7.5V, o pré-amp interno começa a distorcer prematuramente mesmo com volume baixo. Meça a voltagem antes de shows importantes.
2. **Desconexão do Cabo P10**:
   - O jack estéreo de saída da guitarra funciona como chave liga/desliga da bateria. Deixar a guitarra plugada no pedal durante o intervalo do show consome a bateria desnecessariamente.
