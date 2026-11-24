# Guia de Equalização e Normalização de Volume entre Presets (Preset Loudness Matching & LUFS) no UltraRig

Este documento estabelece o protocolo de engenharia de áudio para calibração, medição de intensidade percebida (**LUFS e RMS**) e normalização de volume entre os 32 presets e 128 cenas do firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

Um dos problemas mais graves e frequentes enfrentados por músicos em apresentações ao vivo é a **disparidade de volume entre presets**: ao trocar de um timbre limpo para um overdrive ou solo no meio de uma música, a guitarra ou desaparece no mix da banda (ficando inaudível) ou salta com um estrondo de +10 dB, assustando o público e forçando o técnico de som da casa a atenuar agressivamente o canal da guitarra.

---

## 1. A Ilusão dos Medidores de Pico (Peak vs. RMS / LUFS)

O erro fundamental cometido ao ajustar o volume de presets é confiar exclusivamente em medidores de pico (**Peak Meters**):

```
+-------------------------------------------------------------------------------+
|                       COMPARATIVO DE FATOR DE CRISTA (CREST FACTOR)           |
|                                                                               |
|  TIMBRE LIMPO (CLEAN):                                                        |
|  Peak: -2 dBFS [Transiente da Palheta] =============================> [ -2 dB ]
|  RMS: -18 dBFS [Sustentação do Corpo]  =====> [ -18 dB ]                      |
|                                                                               |
|  TIMBRE HIGH-GAIN METAL:                                                      |
|  Peak: -2 dBFS [Pico Ceifado]          =============================> [ -2 dB ]
|  RMS:  -8 dBFS [Compressão Valvular]   ====================> [ -8 dB ]        |
|                                                                               |
|  * RESULTADO ACÚSTICO: Ambos batem o mesmo pico (-2 dBFS), mas o timbre       |
|    High-Gain soa DUAS VEZES MAIS ALTO (+10 dB RMS) aos ouvidos humanos!      |
+-------------------------------------------------------------------------------+
```

- **Fator de Crista (Crest Factor):** A diferença entre o pico transitório mais alto e a média contínua do sinal.
  - Timbres limpos têm dinâmica aberta (crista alta de 16 dB).
  - Timbres saturados têm compressão valvulada extrema (crista baixa de 6 dB).
- **LUFS (Loudness Units relative to Full Scale):** O padrão internacional da indústria (EBU R128 / ITU-R BS.1770) que pondera as frequências de acordo com a sensibilidade do ouvido humano (curva K).

---

## 2. A Armadilha do Volume de Quarto (Curvas de Fletcher-Munson)

Presets calibrados em fones de ouvido ou no quarto a baixo volume (**60 a 70 dB SPL**) sofrem do efeito acústico de igual intensidade de Fletcher-Munson:
1. **Em Baixo Volume:** O ouvido humano perde imensamente a sensibilidade para frequências graves (< 100 Hz) e agudos extremos (> 6 kHz). O guitarrista tende a aumentar os graves e agudos no equalizador (*loudness smile*).
2. **Em Volume de Palco (95 a 105 dB SPL):** A resposta do ouvido se aplaina. Os graves antes ajustados no quarto se tornam um estrondo embolado de subgrave no PA, e os agudos se tornam estridentes e cortantes como vidro.

> [!IMPORTANT]
> Sempre faça a calibração final de volume e ganho dos seus presets ouvindo nos mesmos monitores ou fones *In-Ear* que você usará no show, operando em volume representativo de ensaio/palco (**ao menos 80–85 dB SPL**).

---

## 3. O Padrão de Nível Alvo do UltraRig: -14 LUFS / -16 dBFS RMS

Para que os 32 presets convivam em perfeita harmonia em qualquer PA de casa de show ou estúdio:

```
+-------------------------------------------------------------------------------+
|                      ESCALA DE EQUALIZAÇÃO DE VOLUME DO ULTRARIG              |
|                                                                               |
|  Função do Preset / Cena      Alvo Integrado (LUFS)     Nível RMS Típico      |
|  -----------------------      ---------------------     ----------------      |
|  Guitarra Base Limpa          -14.0 LUFS                -17 a -16 dBFS        |
|  Guitarra Base Crunch/Riffs   -14.0 LUFS                -15 a -14 dBFS        |
|  Guitarra Base High-Gain      -14.0 LUFS                -14 a -13 dBFS        |
|  Solo / Lead Hero (+3.5 dB)   -10.5 LUFS                -11 a -10 dBFS        |
+-------------------------------------------------------------------------------+
```

---

## 4. Onde Ajustar o Volume sem Modificar o Timbre

Quando um preset está muito alto ou muito baixo, **nunca altere os seguintes parâmetros**:
- **NÃO MEXA no Ganho do Bloco NAM (Amp Gain):** Mudar o ganho altera a saturação harmônica e compressão do amplificador.
- **NÃO MEXA no Drive ou Level do Overdrive:** Mudar o level do pedal de drive altera como ele excita o pré-amplificador neural subsequente.

### O Local Correto para Normalizar:
1. **`Preset Master Level` (Nível Geral do Preset):** Use este controle para nivelar o preset inteiro em relação aos outros 31 presets da pedaleira.
2. **`Scene Level` (Nível da Cena):** Use este controle dentro do preset para dar o boost exato de **+3.0 dB a +4.0 dB na Cena de Solo (Cena C)** em relação às cenas de base rítmica.
3. Ambos os parâmetros atuam como faders lineares transparentes de 32-bit no final da cadeia DSP, sem afetar a resposta dinâmica ou timbre de nenhum efeito.

---

## 5. Procedimento Prático de Calibração em 5 Passos

Siga este método infalível para nivelar seus presets:

### Passo 1: Defina o Preset Âncora (Reference Anchor)
1. Escolha o seu preset de **Base Rítmica Principal** (por exemplo, um crunch de rock britânico ou ritmo pop limpo).
2. Conecte a saída USB do UltraRig ou a saída de áudio ao seu computador com um plugin medidor de LUFS gratuito (ex: *Youlean Loudness Meter* no Reaper, OBS ou DAW).
3. Toque acordes abertos cheios em dinâmica confortável de show e ajuste o `Preset Master Level` até registrar exatamente **-14.0 LUFS Integrado**.

### Passo 2: Nivele os Timbres Limpos (Clean Presets)
1. Carregue o preset limpo. Toque a mesma intensidade rítmica.
2. Observe o medidor LUFS: timbres limpos frequentemente batem -18 LUFS devido à falta de compressão.
3. Suba o `Preset Master Level` em +2.5 dB a +4 dB até atingir o alvo de **-14.0 LUFS**.
4. Verifique o medidor de pico: assegure-se de que os ataques não estejam clipando em 0 dBFS. Se necessário, ative um compressor óptico suave no bloco de entrada do preset limpo.

### Passo 3: Nivele os Timbres Pesados (High-Gain Metal)
1. Carregue os presets de alto ganho.
2. Como esses timbres são densos e altamente comprimidos, reduza o `Preset Master Level` até que o medidor leia os mesmos **-14.0 LUFS**.

### Passo 4: Calibre o Boost de Solo (+3.5 dB)
1. No preset de solo, configure a Cena de Solo com exatamente **+3.5 dB** acima da base rítmica.
2. Isso garante corte cirúrgico da mixagem da banda sem forçar o técnico de PA a abaixar o seu canal.

### Passo 5: O Teste Rápido de Comutação A/B/C
1. Feche os olhos e alterne rapidamente entre os presets nos footswitches físicos enquanto toca um acorde contínuo.
2. Seus ouvidos não devem perceber nenhum salto abrupto de volume perceptível; apenas a mudança estética de timbre e ganho.

---

## 6. Checklist de Passagem de Som com o Técnico de FOH

- [ ] **Alinhamento do Master Fader:** O knob master físico do UltraRig deve ser posicionado na mesma marcação em todos os shows (recomendado: 80% do curso).
- [ ] **Envio de Som de Referência:** Na passagem de som, toque primeiro a sua base rítmica de volume nominal (-14 LUFS) para que o técnico ajuste o ganho do pré-amp da mesa.
- [ ] **Demonstração do Solo Boost:** Acione a Cena de Solo durante a passagem de som para que o técnico saiba que o volume aumentará +3.5 dB intencionalmente, evitando que ele compense com o fader.
