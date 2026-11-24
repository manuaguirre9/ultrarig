# Guia de Modelagem de Compressão VCA de Barramento Master (Master Bus Glue) no UltraRig

Este documento estabelece os princípios de processamento dinâmico de mixagem, engenharia de amplificadores controlados por tensão (VCA), filtragem de detecção em sidechain e calibração de coesão psicoacústica (*Mix Bus Glue*) através do módulo **Master Bus Compressor** no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

Em gravações comerciais clássicas e palcos profissionais de grande porte, o timbre de guitarra e baixo não é finalizado apenas pelo amplificador e caixa acústica. Ele passa pela lendária seção de saída do console de estúdio — mais notavelmente o compressor de barramento mestre das mesas **Solid State Logic (SSL 4000 G-Series Bus Compressor)** e **Neve (33609)**. Esse processamento final confere o cobiçado efeito de "cola" (*glue*): a sensação auditiva de que instrumentos estéreo, guitarras dobradas, delays e reverbs deixam de soar como elementos separados e passam a se fundir em uma massa sonora única, polida e pronta para rádio (*record-ready tone*).

---

## 1. O Conceito de "Glue": Compressão de Pista vs. Compressão de Barramento

```
+---------------------------------------------------------------------------------------+
|                    COMPRESSÃO DE CANAL vs. COMPRESSÃO DE MASTER BUS                   |
+---------------------+-----------------------------+-----------------------------------+
| Topologia           | Posição & Objetivo          | Comportamento Psicoacústico       |
+---------------------+-----------------------------+-----------------------------------+
| Compressor de Canal | Inserido no início da cadeia| Controla a dinâmica individual da |
| Individual (Input)  | da guitarra (após o input). | palhetada; eleva o sustain ou     |
|                     | Modela o ataque da corda.   | doma picos pontuais do captador.  |
+---------------------+-----------------------------+-----------------------------------+
| Master Bus Glue     | Inserido na saída final     | Atua sobre a soma estéreo global. |
| Compressor (Output) | estéreo (pós-amp, IR e FX). | Faz os reverbs, delays e canais   |
|                     | Amarra a mixagem completa.  | L/R "respirarem" juntos no ritmo  |
|                     |                             | da música com punch inabalável.   |
+---------------------+-----------------------------+-----------------------------------+
```

```
                        [ FLUXO DE PROCESSAMENTO NO ULTRARIG ]

[ GUITARRA L ] ──► [ AMP + IR ] ──► [ STEREO FX ] ──┐
                                                    ├──► [ MASTER VCA GLUE ] ──► [ SAÍDAS ]
[ GUITARRA R ] ──► [ AMP + IR ] ──► [ STEREO FX ] ──┘    (Ratio 2:1 / 4:1,       (PA / USB)
                                                          Sidechain HPF 100Hz)
```

---

## 2. A Engenharia do Circuito VCA e os Três Parâmetros de Ouro

Ao contrário de compressores ópticos lentos (como o LA-2A) ou limitadores FET ultra-agressivos (como o 1176), os compressores baseados em VCA (*Voltage-Controlled Amplifier*, e.g., chips DBX 202 ou THAT 2180) destacam-se pela linearidade impecável, taxa de distorção harmônica extremamente baixa e resposta de ganho previsível.

### Os Três Ajustes Críticos para Obter o "Glue" Perfeito:
1. **Ataque Lento / Moderado ($30\text{ ms}$)**:
   - Este é o segredo número um da mixagem: o tempo de ataque do compressor de barramento **deve ser lento** o suficiente para permitir que o estalo inicial da palheta (*pick transient*) passe totalmente intacto antes que o circuito comece a atenuar o ganho.
   - Se o ataque for rápido demais ($0.1\text{ ms} - 3\text{ ms}$), a vida, a pegada e a clareza da guitarra são destruídas, tornando o som frouxo e sem impacto.
2. **Auto-Release Musical (Dependente de Programa)**:
   - O clássico modo `AUTO` do SSL combina duas constantes de tempo internas: uma recuperação rápida para picos isolados de palhetada e uma recuperação suave e lenta para notas sustentadas e acordes. Isso impede qualquer artefato de oscilação audível.
3. **Ratio Suave ($2:1$ ou $4:1$) com Redução de Ganho Moderada ($2\text{ dB}$ a $4\text{ dB}$)**:
   - O objetivo do Master Bus Glue nunca é esmagar a dinâmica. A agulha do medidor de redução de ganho (*Gain Reduction - GR*) deve oscilar suavemente entre $-1.5\text{ dB}$ e $-3.5\text{ dB}$ no compasso da música.

---

## 3. O Filtro Passa-Altas de Detecção (Sidechain HPF)

As frequências graves da guitarra (especialmente em afinações baixas como Drop D, Drop C e guitarras de 7/8 cordas) contêm muito mais energia mecânica do que os médios e agudos:

```
[ SOMA ESTÉREO COMPLETA ]
           │
           ├─► [ CANAL DE ÁUDIO PRINCIPAL ] ────────────────────────► [ VCA ATTENUATOR ]
           │                                                                 ▲
           └─► [ CIRCUITO DE DETECÇÃO (SIDECHAIN) ]                          │
                     │                                                       │
                     ▼                                                       │
               [ FILTRO SIDECHAIN HPF (100 Hz a 120 Hz) ]                    │
               (Remove graves pesados da detecção do detector)               │
                     │                                                       │
                     ▼                                                       │
               [ RETIFICADOR DE PICO / RMS ] ────────────────────────────────┘
               (Gera tensão de controle proporcional aos médios musicais!)
```

- **Sem Sidechain HPF**: Cada vez que o guitarrista toca um acorde grave pesado ou palm-mute, a grande energia dos graves ativa o compressor, fazendo todo o espectro de agudos e as caudas de reverb caírem de volume (efeito "bombeamento" ou *pumping* indesejado).
- **Com Sidechain HPF em $100\text{ Hz}$**: O circuito detector ignora a energia bruta de subgraves e foca nos médios percussivos da guitarra. O grave passa com autoridade e peso total, enquanto a coesão é aplicada de forma cirúrgica sobre os médios e agudos.

---

## 4. Presets de Performance em 4 Cenas (Scenes A/B/C/D)

```
+---------------------------------------------------------------------------------------+
|                    BANCO DE PRESET MASTER GLUE: 4 CENAS DE POLIMENTO                  |
+---------------------+-------------------+---------------------+-----------------------+
| Cena A: Studio      | Cena B: Modern    | Cena C: Dynamic     | Cena D: Transparent   |
| Master Glue (SSL)   | Rock Wall Punch   | Acoustic Cohesion   | Clean Peak Leveler    |
+---------------------+-------------------+---------------------+-----------------------+
```

### Cena A: Studio Master Glue (Referência Universal SSL 4000 G-Bus)
- **Objetivo**: A lendária cola de console de estúdio britânica para gravações e palco estéreo. Amarra a banda com coesão, calor e profundidade tridimensional.
- **Parâmetros do Master Compressor**:
  - `Model`: `SSL G-BUS VCA VINTAGE`
  - `Threshold`: Ajustado para atingir -2 dB a -3 dB de Gain Reduction nos picos
  - `Ratio`: 2:1 (Compressão suave e transparente)
  - `Attack Time`: 30 ms (Preserva todo o ataque da palheta)
  - `Release Time`: Auto (Adaptação orgânica ao andamento)
  - `Sidechain HPF`: 105 Hz (Evita bombeamento de graves)
  - `Makeup Gain`: +2.0 dB
  - `Mix (Dry/Wet)`: 100% Wet
- **Resultado Sonoro**: A guitarra estéreo soa instantaneamente como um disco comercial finalizado.

### Cena B: Modern Rock Wall Punch (Paredão Pesado e Encorpado)
- **Objetivo**: Para Rock pesado, Hard Rock e Metal moderno. Une guitarras dobradas em um bloco monolítico com impacto percussivo devastador.
- **Parâmetros do Master Compressor**:
  - `Model`: `VCA MODERN IMPACT`
  - `Threshold`: Ajustado para -3.5 dB a -4.5 dB de GR
  - `Ratio`: 4:1 (Aperto mais firme)
  - `Attack Time`: 10 ms (Pega o topo da dinâmica sem matar o ataque)
  - `Release Time`: 100 ms (Recuperação rápida para acentuar o ritmo de palhetadas rápidas)
  - `Sidechain HPF`: 120 Hz
  - `Makeup Gain`: +3.0 dB
- **Resultado Sonoro**: Palm-mutes estalam no peito com sustentação pesada e foco central imbatível.

### Cena C: Dynamic Acoustic Cohesion (Violões Estéreo e Ambiências)
- **Objetivo**: Para violões acústicos de aço/nylon, dedilhados e arranjos delicados com delays e reverbs densos. Mantém a dinâmica sutil sem achatamento.
- **Parâmetros do Master Compressor**:
  - `Model`: `NEVE 33609 BUS GLUE`
  - `Ratio`: 1.5:1 ou 2:1
  - `Attack Time`: 40 ms
  - `Release Time`: 400 ms (Recuperação lenta e graciosa)
  - `Sidechain HPF`: 85 Hz
  - `Parallel Blend (Mix)`: 75% Wet / 25% Dry (Compressão paralela natural)
- **Resultado Sonoro**: Os sobretons amadeirados e as caudas de ambiência respiram sem esforço.

### Cena D: Transparent Clean Peak Leveler (Proteção de PA e Fones)
- **Objetivo**: Nivelador estéreo com tolerância zero para picos descontrolados, garantindo consistência absoluta de volume entre diferentes presets sem alterar o timbre.
- **Parâmetros do Master Compressor**:
  - `Ratio`: 3:1
  - `Attack Time`: 20 ms
  - `Release Time`: Auto
  - `Sidechain HPF`: 90 Hz
  - `Target Integrated Loudness`: -16 LUFS
  - `Peak Limiter Ceiling`: -0.5 dBFS (Proteção absoluta contra distorção no PA)

---

## 5. Dicas de Ouro para Calibração de Saída no UltraRig

1. **Monitore o Medidor de Redução de Ganho (GR)**:
   - Se o medidor passar de $-6\text{ dB}$ de atenuação constante, o compressor está sendo forçado em excesso, o que tirará a dinâmica da música e deixará o som abafado. Recue o limiar (*Threshold*) até que a redução fique entre $-2\text{ dB}$ e $-4\text{ dB}$ nos momentos mais fortes da apresentação.
2. **A Regra do Bypass de Verificação**:
   - Ao ajustar o ganho de compensação (*Makeup Gain*), faça comparações ativando e desativando o bypass do bloco. O volume percebido com o compressor ativado deve ser exatamente idêntico ao volume com o compressor desativado. Isso garante que a mixagem soe melhor pela coesão física do som, e não simplesmente por estar mais alta.
