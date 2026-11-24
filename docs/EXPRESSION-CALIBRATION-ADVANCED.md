# Guia Avançado de Diagnóstico, Calibração e Mapeamento de Pedais de Expressão no UltraRig

Este documento aborda a física de sensores ópticos e potenciométricos, polaridades elétricas TRS, eliminação de ruído de leitura (*ADC Jitter*), calibração de curvas de resposta e mapeamento avançado de macro-parâmetros para **Pedais de Expressão** no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

Um pedal de expressão mal calibrado é a causa de comportamentos frustrantes no palco: cursos mecânicos com resposta irregular (*bunching*), falta de alcance em 100% ou 0%, oscilações indesejadas de parâmetros com o pé parado (*parameter jitter*) e filtros de wah que fecham de maneira abrupta.

---

## 1. Tipos de Sensores: Ópticos vs. Potenciométricos

| Característica | Sensores Potenciométricos (Mecânicos) | Sensores Ópticos / Efeito Hall (Magnéticos) |
| :--- | :--- | :--- |
| **Exemplos de Pedais** | *Moog EP-3*, *Roland EV-5*, *Dunlop DVP*, *Boss FV-500* | *M-VAVE Chocolate Expression*, *Morley Wah*, *Mission Engineering VM-PRO* |
| **Princípio Físico** | Cursor mecânico de metal deslizando sobre trilha de carbono. | LED infravermelho com fototransistor ou ímã com sensor Hall. |
| **Resistência Típica** | 10 kΩ a 25 kΩ lineares (B10K / B25K). | Saída de tensão analógica direta ou codificação digital MIDI. |
| **Vantagens** | Construção simples, resposta tátil e baixo custo. | Sem desgaste por atrito mecânico, livre de chiados por poeira. |
| **Desvantagens** | Desgaste com o tempo, suscetível a poeira e ruído elétrico (*jitter*). | Exige alimentação ativa ou bateria interna. |

---

## 2. Polaridade Elétrica e Descasamento de Impedância

### 2.1 Conexão TRS: Padrão Roland/Boss vs. Yamaha/Korg

A entrada de expressão física do hardware M-VAVE utiliza um conector P10 fêmea estéreo (**TRS - Tip, Ring, Sleeve**):

```
Conexão TRS:
  [ TIP (Ponta) ] --------> Sinal de Retorno da Tensão (Wiper) [Padrão Roland / Padrão UltraRig]
  [ RING (Anel) ] --------> Tensão de Referência (+3.3V)
  [ SLEEVE (Manga) ] -----> Terra Elétrico (GND 0V)
```

- **Padrão Roland / Boss / UltraRig (Wiper no Tip):** Conforme o pedal é pressionado para a frente (*Toe Down*), a tensão no Tip sobe progressivamente de 0V até +3.3V.
- **Padrão Yamaha / Korg (Wiper no Ring):** Se você conectar um pedal com essa fiação invertida, o curso ficará ao contrário ou responderá apenas nos últimos milímetros de curso.
- *Solução no UltraRig:* Caso o seu pedal opere com polaridade invertida e não possua chave física (*Polarity Switch*), ative a opção **`Invert Polarity (0% <-> 100%)`** no menu de calibração do UltraRig.

### 2.2 O Erro de Usar Pedais de Volume Passivos de Guitarra (250 kΩ / 500 kΩ)

- Pedais de expressão dedicados utilizam potenciômetros de **10 kΩ a 25 kΩ Lineares**.
- Se você usar a saída de um pedal de volume passivo para guitarra de alta impedância (250 kΩ ou 500 kΩ Logarítmico):
  - 80% da mudança de parâmetro acontecerá comprimida nos primeiros 15% do movimento do pedal, tornando o controle fino praticamente impossível.
  - Utilize sempre pedais de expressão com impedância nominal entre 10 kΩ e 25 kΩ lineares.

---

## 3. Eliminação de Zonas Mortas e Ruído de Leitura (ADC Jitter)

### 3.1 Calibração de Limiares Mecânicos (Dead-Zones)

Pedais mecânicos raramente retornam à exata mesma posição física de repouso devido ao amortecimento de borrachas e folgas mecânicas:
- **Heel Dead-Zone (Zona Morta do Calcanhar):**
  - Configure entre **3% e 5%**.
  - Garante que, ao recuar o pedal completamente, o parâmetro atinja impreterivelmente `0%` (volume 100% mudo ou wah completamente fechado), mesmo que a borracha do calcanhar impeça o potenciômetro de girar até o fim físico do curso.
- **Toe Dead-Zone (Zona Morta da Ponta):**
  - Configure entre **95% e 98%**.
  - Garante que a pressão natural do pé no final do curso atinja `100%` da saturação ou frequência sem exigir que o guitarrista suba com todo o peso do corpo sobre o pedal.

### 3.2 Filtro de Suavização Anti-Jitter (EMA Smoothing Filter)

Trilhas de carbono com sujeira ou oxidação produzem flutuações microscópicas de milivolts no conversor ADC, gerando o fenômeno de "parâmetro dançante" no visor:
- No UltraRig, o parâmetro **`ADC Filter / Smoothing`** aplica uma média móvel exponencial (*Exponential Moving Average*):
  - **Fast / Off:** Resposta imediata para Whammy percussivo estilo Tom Morello.
  - **Medium (Recomendado):** Filtra ruídos térmicos e tremores sutis do pé sem introduzir latência perceptível (menos de 2 ms).
  - **Smooth:** Ideal para transições lentas de volume ambiental (*ambient swells*).

---

## 4. Curvas de Resposta de Parâmetro (Taper Curves)

Mapear um movimento físico linear para um parâmetro digital exige curvas adaptadas à percepção humana:

```
Valor do Parâmetro
  ^
  |        .--- Logarítmica (Ideal para Volume / Swells)
  |       /
  |      /----- Linear (Ideal para Whammy / Pitch / Blend)
  |     /
  |    /------- Reverse-Log (Ideal para Wah-Wah e Filtros Ressonantes)
  |   /
  +------------------------------------------------------------> Posição Física (0 a 100%)
     Calcanhar                                           Ponta
```

1. **Curva Linear (1:1):**
   - O valor do parâmetro progride proporcionalmente à rotação física.
   - *Aplicações:* Pitch Shifter / Whammy (-1 a +2 oitavas), velocidade de Rotary Speaker, balanço de ramos paralelos (*Wet/Dry Blend*).
2. **Curva Logarítmica (Audio Taper):**
   - O volume cresce suavemente no início e de forma mais acentuada no final, casando perfeitamente com a resposta auditiva humana em decibéis.
   - *Aplicações:* Volume Master e volume de entrada de drives.
3. **Curva Reverse-Log (Anti-Log):**
   - Dedica maior extensão física de curso aos médios graves e médios, onde o ouvido humano percebe as nuances vocais do filtro.
   - *Aplicações:* Efeito Wah-Wah clássico (CryBaby / Vox) e filtros de envelope manuais.

---

## 5. Mapeamento de Macro-Parâmetros Simultâneos (Multi-Target Morphing)

O UltraRig permite que um único pedal de expressão controle múltiplos parâmetros de blocos diferentes em direções simultâneas ou invertidas:

```
+-------------------------------------------------------------------------------+
|             EXEMPLO DE MORFISMO COM PEDAL DE EXPRESSÃO (MACRO)                |
|                                                                               |
|  Posição do Pedal:       CALCANHAR (0%)               PONTA (100%)            |
|  -----------------       --------------               ------------            |
|  1. NAM Amp Gain:        2.5 (Limpo)       ------->   8.0 (Lead Sombrio)      |
|  2. Overdrive Tone:      40% (Fechado)     ------->   75% (Agressivo)         |
|  3. Delay Wet Mix:       35% (Eco Visível) ------->   12% (Seco e Direto)     |
|  4. Master Solo Boost:   0.0 dB            ------->   +3.5 dB (Volume Solo)   |
+-------------------------------------------------------------------------------+
```

Ao pressionar o pedal da posição de calcanhar para a ponta, a guitarra transita organicamente de um timbre limpo com delay longo para um solo distorcido, cortante e seco, sem nenhum footswitch adicional.

---

## 6. Auto-Engage (Acionamento Inteligente por Movimento)

Para quem utiliza pedais de expressão sem chave física de acionamento sob a ponta (*toe switch*):
- **Modo Auto-Engage (Heel-Off Trigger):**
  - Quando o pedal está repousado no calcanhar (0% a 4%), o bloco de Wah-Wah permanece em `Bypass`.
  - No momento em que o pé move o pedal acima de `5%`, o Wah é ativado instantaneamente.
  - Ao retornar o pedal para o calcanhar por mais de **350 ms (Off-Delay)**, o efeito é desativado de forma automática e silenciosa.

---

## 7. Procedimento Prático de Calibração Passo a Passo

1. Conecte o cabo P10 TRS do pedal de expressão à porta `EXP` do dispositivo.
2. Abra o painel web do UltraRig em `Settings > Expression Calibration`.
3. Clique em **`Start Auto-Calibrate`**.
4. Mova o pedal lentamente até o calcanhar máximo (*Heel*); o visor lerá a voltagem mínima do conversor (ex: `0.05 V`).
5. Empurre o pedal firmemente até a ponta máxima (*Toe*); o visor lerá a voltagem máxima (ex: `3.22 V`).
6. Clique em **`Apply Limits & Save`**.
7. Teste o medidor percentual visual: ele deve responder suavemente de 0% a 100% sem oscilar parado.
