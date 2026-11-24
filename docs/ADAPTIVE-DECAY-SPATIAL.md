# Guia de Roteamento Espacial com Decaimento Adaptativo e Reverb Dinâmico no UltraRig

Este documento estabelece os princípios de processamento digital de sinais (DSP), algoritmos de rastreamento de densidade de palhetada, controle dinâmico de tempo de reverberação ($T_{60}$) e roteamento de efeitos espaciais com **Decaimento Adaptativo (Adaptive Decay Spatial Routing)** no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

O grande dilema acústico de guitarristas e baixistas em performances ao vivo reside no equilíbrio entre clareza de articulação e grandiosidade espacial. Em frases rápidas (*shredding, arpejos de semicolcheias, riffs sincopados ou dedilhados percussivos*), caudas longas de reverb (decay $> 3.5\text{ s}$) transformam a mixagem em uma "lama harmônica" embolada que destrói a definição rítmica. Por outro lado, se o reverb for encurtado para acomodar a velocidade, as notas longas, paradas dramáticas e vibratos sustentados soam secos, finos e sem corpo.

---

## 1. O Dilema Espacial: Ducking Convencional vs. Decaimento Adaptativo

Para contornar o embolamento de reverberação, sistemas tradicionais costumam empregar *Sidechain Ducking*:

```
+---------------------------------------------------------------------------------------+
|                    DUCKING TRADICIONAL vs. DECAIMENTO ADAPTATIVO DSP                  |
+---------------------+-----------------------------+-----------------------------------+
| Abordagem           | O que acontece durante notas| Limitações Acústicas Reais        |
|                     | rápidas e staccatos         |                                   |
+---------------------+-----------------------------+-----------------------------------+
| Sidechain Ducking   | Atenua o volume de saída    | O tempo de decaimento (T60)       |
| Convencional        | (Wet Mix) do reverb durante | continua longo internamente no    |
|                     | a presença do sinal direto. | buffer (e.g. 5.0s). Quando o      |
|                     |                             | guitarrista para de tocar, o "mar |
|                     |                             | de notas emboladas acumuladas"    |
|                     |                             | sobe de volume abruptamente!      |
+---------------------+-----------------------------+-----------------------------------+
| Adaptive Decay      | O algoritmo contrai         | O tanque de reverberação nunca    |
| Modulation          | fisicamente o tempo de      | acumula ressonâncias indesejadas; |
| (UltraRig DSP)      | reverberação (T60: 0.8s)    | cada nota rápida desaparece com   |
|                     | e expande para 5.5s apenas  | clareza cirúrgica; notas longas   |
|                     | em notas longas ou pausas.  | florescem em nuvens limpas.       |
+---------------------+-----------------------------+-----------------------------------+
```

Enquanto o ducking comum apenas "esconde a sujeira debaixo do tapete" atuando no ganho de saída (*VCA/fader*), o **Decaimento Adaptativo (*Adaptive Decay*)** do UltraRig atua diretamente nos coeficientes de retroalimentação interna da rede de linhas de atraso com realimentação (*Feedback Delay Network - FDN*), limpando ativamente a memória do reverb em passagens velozes.

---

## 2. A Arquitetura DSP de Modulação Adaptativa no UltraRig

O sistema opera através de dois blocos interligados: o **Estimador de Densidade de Transientes (TDE)** e o **Interpolador de Coeficientes de Decaimento**:

```
                       [ ENTRADA DIRETA DA GUITARRA ]
                                      │
            ┌─────────────────────────┴─────────────────────────┐
            │                                                   │
            ▼                                                   ▼
   [ ESTIMADOR DE DENSIDADE ]                          [ CADEIA PRINCIPAL ]
   (Envelope + Transientes/seg)                        (Comp / Preamp / Cab)
            │                                                   │
            ▼                                                   ▼
   [ MAPA DE CURVA INVERSA ]                          [ ENTRADA DO REVERB FDN ]
   (Rápido/Forte ──► Contrai T60)                               │
   (Lento/Sustain ─► Expande T60)                               │
            │                                                   │
            └─────────────────────────┬─────────────────────────┘
                                      │
                                      ▼
                        [ INTERPOLADOR COEFICIENTE T60 ]
                        (Variação Contínua 0.8s <──► 5.5s)
                                      │
                                      ▼
                             [ BUFFER DO REVERB ]
                         (Absorção Variável em Tempo Real)
                                      │
                                      ▼
                           [ SAÍDA ESPACIAL ESTÉREO ]
```

### Equações do Decaimento Dinâmico:
1. **Seguidor de Transientes**: O sinal direto é derivado em tempo real ($d|x(t)|/dt$) para isolar os picos de ataque da palheta, gerando um valor de densidade $D(t) \in [0, 1]$.
2. **Tempo de Reverberação Adaptado**:
   $$T_{60}(t) = T_{\text{max}} - D(t) \cdot (T_{\text{max}} - T_{\text{min}})$$
   - Durante frases rápidas de solo ($D \approx 1.0$):
     $$T_{60} = T_{\text{min}} \approx 0.8\text{ s}$$
   - Ao sustentar uma nota ou fazer uma pausa ($D \approx 0.0$):
     $$T_{60} = T_{\text{max}} \approx 5.0\text{ s}$$
3. **Interpolação Livre de Artefatos (*Slew Limiting*)**: Os filtros passa-tudo e delays da rede FDN são modulados através de suavizadores exponenciais, garantindo que a transição de tempo não gere desafinações harmônicas (*pitch fluttering*) ou ruído digital de degrau (*zipper noise*).

---

## 3. Roteamento e Modulação Cruzada com Delay Adaptativo

Para potencializar o efeito, o UltraRig permite estender a modulação adaptativa para o bloco de **Delay**:

```
[ DRIVE / AMP ] ──► [ ADAPTIVE DELAY ] ──► [ ADAPTIVE REVERB ] ──► [ SAÍDAS L / R ]
                          ▲                        ▲
                          │                        │
                          └───────[ MODULADOR ]────┘
                                  (Envelope TDE)
```

- **Comportamento no Delay**:
  - Em palhetadas rápidas: O feedback do delay é automaticamente reduzido para `12%` (apenas 1 repetição limpa por nota) e o mix wet é contido em `15%`.
  - Em notas sustentadas: O feedback se expande para `55%` e o mix sobe para `35%`, criando ecos espaciais luxuriantes sem embolar os solos.

---

## 4. Presets de Performance em 4 Cenas (Scenes A/B/C/D)

```
+---------------------------------------------------------------------------------------+
|                 BANCO DE PRESET ADAPTIVE SPATIAL: 4 CENAS DE PERFORMANCE              |
+---------------------+-------------------+---------------------+-----------------------+
| Cena A: Dynamic     | Cena B: Finger-   | Cena C: Rhythmic    | Cena D: Ambient       |
| Lead Bloom          | style Cloud       | Staccato Clamp      | Infinite Swell        |
+---------------------+-------------------+---------------------+-----------------------+
```

### Cena A: Dynamic Lead Bloom (Solo Virtuoso de Alta Definição)
- **Objetivo**: Clareza absoluta em licks rápidos de semicolcheias e tappings virtuosos; cauda expansiva com florescimento etéreo assim que a nota final repousa.
- **Parâmetros de Reverb Adaptativo**:
  - `Algorithm`: `PLATE/HALL HYBRID`
  - `T60 Min (Fast/Hard Attacks)`: 0.9 s
  - `T60 Max (Sustain/Rest)`: 4.8 s
  - `Sensitivity / Threshold`: -24 dB
  - `Attack Time (Contração)`: 15 ms (resposta imediata à palheta)
  - `Release Time (Florescimento)`: 280 ms (expansão suave e musical)
  - `High-Frequency Damping`: 4.5 kHz
  - `Reverb Wet Level`: 28%
- **Delay Integrado**:
  - `Tempo`: 480 ms (Semínima pontuada sincronizada)
  - `Adaptive Feedback`: Varia de 15% (rápido) a 48% (sustentado)
- **Uso Recomendado**: Solos de Hard Rock, Metal Melódico, Fusion e Blues contemporâneo.

### Cena B: Fingerstyle Adaptive Cloud (Violão e Guitarra Limpa)
- **Objetivo**: Preservar o ataque percussivo de unhas/palhetas no dedilhado de acordes complexos, enquanto notas finais e harmonias ecoam como em uma catedral de pedra.
- **Parâmetros de Reverb Adaptativo**:
  - `Algorithm`: `LUSH WOOD CATHEDRAL`
  - `T60 Min`: 1.2 s
  - `T60 Max`: 6.5 s
  - `Sensitivity`: -30 dB (captura dinâmica sutil de dedos)
  - `Attack Time`: 25 ms
  - `Release Time`: 400 ms
  - `Predelay`: 35 ms (mantém o ataque primário separado da cauda)
  - `Reverb Wet Level`: 35%
- **Uso Recomendado**: Violão folk de aço, violão clássico de nylon, ambient jazz e neo-soul.

### Cena C: Rhythmic Staccato Clamp (Riffs Cortantes Funk / Metal Moderno)
- **Objetivo**: Tolerância zero para embolamento. Reverb e delays são energicamente "grampeados" (*clamped*) a cada golpe de palheta para máxima pegada percussiva.
- **Parâmetros de Reverb Adaptativo**:
  - `Algorithm`: `TIGHT STUDIO ROOM`
  - `T60 Min`: 0.3 s (Praticamente seco em palm-mutes)
  - `T60 Max`: 1.8 s (Apenas uma cauda moderada em quebras de compasso)
  - `Sensitivity`: -18 dB
  - `Attack Time`: 5 ms
  - `Release Time`: 120 ms
  - `Reverb Wet Level`: 20%
- **Uso Recomendado**: Funk de palhetada 16th, Djent/Metalcore com paradas secas e Pop rítmico.

### Cena D: Ambient Infinite Swell (Swell Dinâmico com Auto-Freeze)
- **Objetivo**: Ao tocar com o potenciômetro de volume fechado e abrir suavemente (ou usando o envelope do UltraRig), a cauda entra em modo infinito (*near-infinite feedback freeze*), criando colchões de sintetizador (*pads*) contínuos.
- **Parâmetros de Reverb Adaptativo**:
  - `Algorithm`: `SHIMMER AMBIENT CLOUD`
  - `T60 Min`: 2.5 s
  - `T60 Max`: 18.0 s (Sustentação infinita tipo freeze)
  - `Sensitivity`: -35 dB
  - `Release Time`: 850 ms (Florescimento atmosférico lento)
  - `Shimmer Octave Pitch`: +12 semitons (+1 oitava cristalina)
  - `Wet Level`: 60%
- **Uso Recomendado**: Post-Rock, trilhas sonoras atmosféricas, introduções lentas e adoração moderna (*Worship ambient pads*).

---

## 5. Dicas de Otimização e Prevenção de Problemas

1. **Ajuste de Limiar (*Threshold/Sensitivity*) de Acordo com o Ganho**:
   - Se você estiver utilizando muito overdrive ou distorção de alto ganho, a compressão do amp aumenta o nível de sinal médio e sustém o envelope por mais tempo. Nesses casos, aumente o limiar de sensibilidade para `-18 dB` para evitar que o algoritmo interprete o ruído de fundo da guitarra como notas sendo tocadas.
2. **Filtragem de Frequências Graves (*Low-Frequency Damping*)**:
   - Caudas longas de reverb (especialmente acima de 4 segundos) tendem a acumular energia em torno de 150 Hz a 250 Hz, competindo diretamente com o contrabaixo e o bumbo da bateria. Mantenha sempre ativo o filtro passa-altas (*Low-Cut*) do bloco de reverb ajustado entre `120 Hz` e `160 Hz`.
3. **Casamento com Footswitches**:
   - No UltraRig, configure um dos footswitches físicos para congelamento manual instantâneo (*Hold / Freeze*) ou para alternar dinamicamente a taxa de Release do envelope entre rápida e lenta.
