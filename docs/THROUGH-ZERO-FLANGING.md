# Guia de Modelagem, Acústica e Roteamento de Through-Zero Flanging (TZF) no UltraRig

Este documento estabelece os fundamentos físicos, arquitetura de processamento digital de sinais (DSP), roteamento paralelo com âncora de atraso e técnicas de performance para **Through-Zero Flanging (TZF)** no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

O flanging com passagem pelo zero (*Through-Zero Flanging*) é o efeito de modulação de tempo mais dramático e cultuado da história do áudio analógico. Ao cruzar o ponto temporal em que a diferença entre o sinal de referência e o sinal modulado atinge exatamente zero milissegundos ($0\text{ ms}$) com polaridade invertida, ocorre cancelamento de fase destrutivo total em todo o espectro audível, produzindo uma ilusão auditiva espacial profunda frequentemente comparada a um caça a jato cruzando a velocidade do som (*jet-plane whoosh*).

---

## 1. Origem Histórica e Física do Ponto Zero

### O Experimento Original de Fita Magnética (Abbey Road Studios, 1966)
Nos anos 60, o engenheiro Ken Townsend e os Beatles em Abbey Road desenvolveram o flanging clássico utilizando dois gravadores de rolo de fita (*tape reels*) idênticos reproduzindo a mesma gravação em sincronia:

```
[ Pista de Áudio Original ]
           │
           ├──► [ Gravador de Fita A (Velocidade Constante) ] ──────► [ SOMA / MIXER ]
           │                                                               ▲
           └──► [ Gravador de Fita B (Pressionado pelo Dedo) ] ────────────┤
                     (Pressão na borda metálica / "Flange")
```

1. Quando o engenheiro pressionava o polegar na borda de alumínio (*flange*) do carretel B, a velocidade da fita diminuía ligeiramente, fazendo o sinal B atrasar em relação ao sinal A.
2. Ao soltar a borda, o motor do gravador B acelerava para restabelecer a velocidade normal.
3. No momento em que a fita B emparelhava e ultrapassava temporalmente a fita A, o retardo relativo passava por **$\Delta t = 0\text{ ms}$**.
4. Invertendo a polaridade do sinal B ($180^\circ$), o instante em que $\Delta t = 0$ gerava cancelamento de fase destrutivo perfeito ($A + (-A) = 0$), criando uma fração de segundo de silêncio absoluto no espectro antes do som "ressurgir do outro lado temporal".

### Por Que Flangers Convencionais Não Fazem Through-Zero?
A quase totalidade dos pedais de flanger de chão clássicos (como Boss BF-2, MXR Flanger, Electro-Harmonix Electric Mistress e ADA Flanger) utiliza circuitos analógicos BBD (*Bucket Brigade Device*, e.g., MN3007 ou SAD1024):
- Em um pedal BBD, o sinal seco (*dry*) é enviado sem retardo para a saída.
- O sinal modulado passa pelo chip BBD, que possui um atraso mínimo físico de aproximadamente $0.5\text{ ms}$ a $1.0\text{ ms}$ limitado pela frequência máxima de clock.
- O sinal modulado oscila entre $1\text{ ms}$ e $10\text{ ms}$, **sem nunca atingir 0 ms** e sem capacidade de transitar para o tempo "negativo" (adiantado em relação ao sinal seco).
- Esse tipo de flanger gera filtragem em pente (*comb filtering*), mas sem o desaparecimento repentino e a inversão tridimensional do ponto zero.

---

## 2. A Arquitetura DSP do Through-Zero Flanging no UltraRig

Para recriar a física exata de dois gravadores de fita em tempo real dentro do processador do Tank-G/B, o UltraRig utiliza uma topologia de linha de retardo dupla (*Dual-Delay Anchor Architecture*):

```
                                  [ ENTRADA DE GUITARRA ]
                                             │
                       ┌─────────────────────┴─────────────────────┐
                       │                                           │
                       ▼                                           ▼
          [ LINHA DE RETARDO ÂNCORA ]                [ LINHA DE RETARDO VARIÁVEL ]
          (Delay Fixo D_ref = 2.5 ms)                (Modulação LFO D_mod: 0.5 a 4.5 ms)
                       │                                           │
                       │                                           ▼
                       │                             [ MULTIPLICADOR DE FASE ]
                       │                             (Inversão de Polaridade -180°)
                       │                                           │
                       │                                           ▼
                       │                             [ FEEDBACK REGENERATIVO ]
                       │                               (Ressonância Metálica)
                       │                                           │
                       └─────────────────────┬─────────────────────┘
                                             │
                                             ▼
                                     [ SOMA DO SINAL ]
                                (Cancelamento Total em Δt = 0)
                                             │
                                             ▼
                                    [ SAÍDA PRINCIPAL ]
```

### O Momento do Cruzamento Nulo ($\Delta t = 0$):
- **Tempo Relativo**: $\Delta t(t) = D_{\text{mod}}(t) - D_{\text{ref}}$.
- Quando o LFO passa pelo centro de sua excursão:
  $$D_{\text{mod}} = 2.5\text{ ms} \implies \Delta t = 2.5\text{ ms} - 2.5\text{ ms} = 0.0\text{ ms}$$
- Com inversão de fase ($180^\circ$), o sinal modulado cancela exatamente o sinal âncora:
  $$V_{\text{out}}(t) = V_{\text{ancora}}(t) - V_{\text{mod}}(t) = 0$$
- Quando o LFO avança para $0.5\text{ ms}$, $\Delta t = -2.0\text{ ms}$ (o canal modulado comporta-se como se estivesse adiantado no tempo relativo!). Esse cruzamento dinâmico produz o efeito psicoacústico de rotação esférica e vácuo sônico.

---

## 3. Roteamento de Sinal e Parâmetros Chave no UltraRig

Para programar o Through-Zero Flanging no UltraRig com fidelidade analógica:

```
[ ENTRADA ] ──► [ COMPRESSOR ] ──► [ PREAMP / DRIVE ] ──► [ TZF ENGINE ] ──► [ CABINET IR ]
                (Nivela o ataque     (Harmônicos ricos      (Âncora + LFO      (Filtro de
                 para sustentação)    alimentam os nulos)    Polaridade Inv)    Agudos)
```

### Parâmetros Críticos do Bloco TZF:
1. **Anchor Delay ($D_{\text{ref}}$)**:
   - Valor típico: `2.0 ms` a `3.0 ms`.
   - Define o ponto de repouso temporal onde a anulação ocorrerá no ciclo do LFO.
2. **Sweep Width / Depth**:
   - Para que o efeito Through-Zero ocorra, a excursão de profundidade deve obrigatoriamente cruzar a âncora ($D_{\text{min}} < D_{\text{ref}} < D_{\text{max}}$).
   - Excursão recomendada: `0.5 ms` a `4.5 ms` (Varredura simétrica de $\pm 2.0\text{ ms}$ em torno da âncora de 2.5 ms).
3. **Polarity / Phase Option**:
   - `Negative Flanging (-180°)`: O modo TZF clássico com cancelamento espectral pleno.
   - `Positive Flanging (0°)`: Nulo em frequências específicas, com reforço de graves na passagem pelo zero.
4. **Regeneration / Feedback**:
   - Feedback em torno de `45%` a `65%` acentua as cristas ressonantes antes e depois do ponto zero, aumentando a dramaticidade da descida sônica.
5. **Tone / HF Damping**:
   - O flanging analógico de fita original amortecia os agudos acima de 6 kHz devido à saturação magnética. Um filtro passa-baixas (*damping*) a 5.5 kHz no loop de regeneração evita chiados digitais artificiais.

---

## 4. Presets de Performance em 4 Cenas (Scenes A/B/C/D)

```
+---------------------------------------------------------------------------------------+
|                    BANCO DE PRESET ULTRA-TZF: 4 CENAS DE MODULAÇÃO                    |
+---------------------+-------------------+---------------------+-----------------------+
| Cena A: Abbey Road  | Cena B: Jet Plane | Cena C: Servo-Flange| Cena D: Barber-Pole   |
| Authentic Tape TZF  | Extreme Resonant  | Manual via Exp Pedal| Infinite Downward     |
+---------------------+-------------------+---------------------+-----------------------+
```

### Cena A: Abbey Road Authentic Tape TZF
- **Objetivo**: Modulação orgânica e suave de fita magnética master, recriando o efeito psicoacústico sutil dos anos 60 (*Strawberry Fields Forever, Axis: Bold as Love*).
- **Parâmetros TZF**:
  - `Anchor Delay`: 2.5 ms
  - `LFO Rate`: 0.18 Hz (Varredura ultra lenta de ~5.5 segundos por ciclo)
  - `Sweep Depth`: 1.8 ms (Oscilação de 1.6 ms a 3.4 ms)
  - `Phase`: Inverted (-180°)
  - `Feedback`: 22% (Ressonância discreta)
  - `Tape Saturation / Drive`: 15% (Leve calor analógico de fita)
  - `Mix`: 50% (Equilíbrio exato entre âncora e modulador para cancelamento perfeito)
- **Drive / Amp**: Clean valvulado americano levemente aquecido (Fender Twin).

### Cena B: Jet Plane Extreme TZF
- **Objetivo**: O som definitivo de turbina a jato cortando o ar, com ressonância tubular agressiva e passagem dramática pelo zero estéreo (*The Police - Walking on the Moon, Van Halen - Unchained, Heart - Barracuda*).
- **Parâmetros TZF**:
  - `Anchor Delay`: 2.0 ms
  - `LFO Rate`: 0.35 Hz (~3 segundos por ciclo)
  - `Sweep Depth`: 3.0 ms (Oscilação de 0.5 ms a 3.5 ms cruzando amplamente o zero)
  - `Phase`: Inverted (-180°)
  - `Feedback`: 72% (Ressonância metálica aguda intensa)
  - `Mix`: 50%
- **Drive / Amp**: Overdrive clássico British Plexi ou JCM800 com ganho moderado para excitar todas as harmônicas da filtragem em pente.

### Cena C: Manual Servo-Flange (Expression Pedal Control)
- **Objetivo**: Desativação do LFO automático e controle total da varredura pelo **Pedal de Expressão** externo conectado ao UltraRig. O músico controla com o pé o ponto exato da passagem pelo zero, podendo "estacionar" o som no nulo absoluto de fase para solos expressivos ou acelerar a varredura nos acordes finais.
- **Mapeamento de Expressão**:
  - `Target Parameter`: `TZF Variable Delay Time`
  - `Exp Heel (0%)`: 0.6 ms (Acima do ponto zero)
  - `Exp Middle (50%)`: 2.5 ms (Exatamente no Ponto Zero de cancelamento absoluto!)
  - `Exp Toe (100%)`: 4.4 ms (Abaixo do ponto zero)
  - `Feedback`: 55%
  - `Phase`: Inverted (-180°)
- **Uso**: Posicionar o pedal de expressão no centro (~50%) gera um efeito estático oco e espacial, ideal para introduções misteriosas de guitarra.

### Cena D: Barber-Pole Infinite Flanger
- **Objetivo**: Ilusão acústica baseada na escala de Shepard-Risset (*Barber-Pole Flange*). O flanger parece descer ou subir infinitamente através do espectro sonoro sem nunca reiniciar perceptivelmente o ciclo.
- **Parâmetros TZF**:
  - `Engine`: `BARBER-POLE MULTI-TAP TZF`
  - `Direction`: Downward (Descida infinita)
  - `Rate`: 0.25 Hz
  - `Crossfade Windows`: 3 fases em quadratura (0°, 120°, 240°)
  - `Feedback`: 40%
  - `Mix`: 45%
- **Ambiência**: Delay analógico pontilhado (Dotted 8th) em 420 ms para reforçar a espiral cósmica.

---

## 5. Cuidados Técnicos e Boas Práticas de Mixagem

1. **Evite Clipes Digitais com Feedback Elevado**:
   - Quando o feedback regenerativo ultrapassa 70%, as cristas ressonantes da filtragem em pente podem adicionar até +9 dB de ganho em frequências isoladas. Monitore a saída digital no medidor do UltraRig para evitar *inter-sample clipping*.
2. **Mono vs. Estéreo**:
   - Em sistemas estéreo, envie a modulação TZF invertida em polaridade para o canal esquerdo e não-invertida para o canal direito. O som parecerá girar ao redor da cabeça do ouvinte em 360 graus quando escutado em fones de ouvido ou no PA.
3. **Posicionamento Antes vs. Depois do Ganho**:
   - **Antes do Pré-Amp**: Som mais vintage, mastigado e comprimido pelas válvulas (estilo Eddie Van Halen).
   - **Depois do Pré-Amp (No Loop de Efeitos/Pós-Drive)**: Efeito Through-Zero límpido, nítido e com cancelamento muito mais profundo e espetacular.
