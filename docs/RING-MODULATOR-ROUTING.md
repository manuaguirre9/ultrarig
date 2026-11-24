# Guia de Modelagem, Matemática de Bandas Laterais e Roteamento de Ring Modulator no UltraRig

Este documento estabelece as diretrizes de processamento analógico-digital, equações trigonométricas de multiplicação de sinais, supressão de portadora (*Suppressed-Carrier*) e técnicas de afinação harmônica para **Moduladores em Anel (*Ring Modulators*, estilo Maestro RM-1B e Moog Moogerfooger MF-102)** no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

O Ring Modulator é um dos efeitos mais exóticos, radicais e instantaneamente reconhecíveis da história da música elétrica e experimental (*Jonny Greenwood / Radiohead - "Paranoid Android", Jeff Beck, Devo, Black Sabbath - "Paranoid", Jan Hammer / Mahavishnu Orchestra e as vozes originais dos Daleks na série Doctor Who*). Em vez de adicionar harmônicos múltiplos ou defasar o sinal, o modulador em anel realiza a multiplicação matemática pura entre a guitarra e uma onda senoidal interna, transformando o instrumento em sinos metálicos, sintetizadores robóticos e texturas alienígenas inarmônicas.

---

## 1. A Física e Matemática da Modulação em Anel

O circuito analógico original utiliza uma ponte de quatro diodos em anel acoplados a dois transformadores de áudio balanceados com tomada central (*center-tap*):

```
+---------------------------------------------------------------------------------------+
|                    DIAGRAMA DA PONTE DE DIODOS DO RING MODULATOR                      |
|                                                                                       |
|                               ┌──►|─── D1 ───►|───┐                                   |
|                               │                   │                                   |
|   [ SINAL DA GUITARRA ] ──────┼───►|── D2 ───►|───┼──────► [ SAÍDA SOMA & DIFERENÇA ]  |
|      (Modulador f_m)          │                   │          (f_c + f_m e f_c - f_m)  |
|                               │                   │                                   |
|                               └──►|─── D3 ───►|───┘                                   |
|                                         ▲                                             |
|                                         │                                             |
|                          [ OSCILADOR DE PORTADORA (CARRIER) ]                         |
|                                  (Onda Senoidal f_c)                                  |
+---------------------------------------------------------------------------------------+
```

### A Equação de Multiplicação e Supressão de Portadora:
Quando multiplicamos a onda da guitarra ($f_m$) pela portadora interna ($f_c$):
$$\cos(2\pi f_c t) \times \cos(2\pi f_m t) = \frac{1}{2} \cos(2\pi (f_c + f_m) t) + \frac{1}{2} \cos(2\pi (f_c - f_m) t)$$

1. **Supressão Total da Fundamental (Double-Sideband Suppressed-Carrier)**:
   - Em um modulador em anel balanceado ideal, **nem a frequência original da guitarra ($f_m$) nem a frequência da portadora ($f_c$) aparecem na saída**.
   - Apenas duas novas frequências são geradas: a **soma ($f_c + f_m$)** e a **diferença ($f_c - f_m$)**.
2. **Por Que o Som é Inarmônico e Metálico?**:
   - Instrumentos tradicionais geram harmônicos em proporções inteiras ($1f, 2f, 3f, 4f$).
   - Se tocarmos a nota Lá ($A_2 = 110\text{ Hz}$) e a portadora estiver em $150\text{ Hz}$, as bandas de saída serão:
     - Banda de Soma: $150 + 110 = 260\text{ Hz}$
     - Banda de Diferença: $150 - 110 = 40\text{ Hz}$
   - Essas frequências resultantes não possuem relação harmônica natural com a escala musical, gerando timbres ressonantes metálicos que lembram chapas de aço, gongos e sinos de igreja.

---

## 2. A Fronteira entre Tremolo e Modulação em Anel

O comportamento perceptivo depende estritamente da frequência da portadora ($f_c$):

```
+---------------------------------------------------------------------------------------+
|                    A TRANSIÇÃO PERCEPTIVA DE FREQUÊNCIA DA PORTADORA                  |
+---------------------+-------------------+---------------------------------------------+
| Faixa de Frequência | Comportamento DSP | Percepção Auditiva Humana                   |
+---------------------+-------------------+---------------------------------------------+
| Sub-Áudio           | 0.5 Hz a 18 Hz    | O ouvido não distingue novas frequências. O |
| (LFO Lento)         |                   | resultado é um tremolo de onda senoidal     |
|                     |                   | pura, transparente e aveludado.             |
+---------------------+-------------------+---------------------------------------------+
| Zona de Transição   | 18 Hz a 35 Hz     | O tremolo começa a vibrar tão rápido que se |
| (Flutter / Buzz)    |                   | transforma em um zumbido áspero motorizado. |
+---------------------+-------------------+---------------------------------------------+
| Faixa Audível       | 40 Hz a 4.000 Hz  | Modulação em anel plena. Surgem os tons     |
| (Ring Mod Pleno)    |                   | metálicos, sinos cósmicos e vozes robóticas.|
+---------------------+-------------------+---------------------------------------------+
```

---

## 3. Roteamento de Sinal e Afinação Diatônica no UltraRig

Para que o efeito não soe apenas como ruído caótico e possa ser utilizado melodicamente em canções reais:

```
[ GUITARRA ] ──► [ RASTREADOR DE NOTA ] ──► [ OSCILADOR DE PORTADORA ]
                       │                               │
                       ▼                               ▼
                 [ AFINAÇÃO EM C ] ────────► [ MULTIPLICADOR EM ANEL ]
                                                       │
                                                       ▼
[ SAÍDAS MASTER ] ◄── [ DELAY / REVERB ] ◄── [ MIXER PARALELO (WET/DRY) ] ◄── [ GUITARRA DRY ]
```

### Recursos Avançados no UltraRig:
1. **Afinação Diatônica da Portadora (Tuned Carrier Mode)**:
   - Permite fixar a portadora em notas musicais exatas (ex: Dó, Ré, Mi ou Lá em 440 Hz). Ao tocar melodias na tonalidade correta, as bandas laterais de soma e diferença geram intervalos consonantes harmonizados com timbre de carrilhão ou sino tibetano afinado.
2. **Modulação Dinâmica por Envelope (Envelope-to-Carrier)**:
   - A intensidade com que a palheta golpeia a corda dispara um desvio dinâmico de frequência na portadora: palhetadas fortes disparam a portadora em agudos metálicos brilhantes que escorregam para graves aveludados conforme a nota sustenta.
3. **Controle Manual via Pedal de Expressão**:
   - O pedal de expressão varre continuamente a frequência da portadora de $2\text{ Hz}$ (tremolo lento) até $2.5\text{ kHz}$ (apito de laser metálico) em tempo real.

---

## 4. Presets de Performance em 4 Cenas (Scenes A/B/C/D)

```
+---------------------------------------------------------------------------------------+
|                 BANCO DE PRESET ULTRA-RING MOD: 4 CENAS EXPERIMENTAIS                 |
+---------------------+-------------------+---------------------+-----------------------+
| Cena A: Paranoid    | Cena B: Tuned     | Cena C: Tremolo-to- | Cena D: Space Bells   |
| Android Metallic    | Robot Synth       | Ring Speed Ramp     | Ambient Drone         |
+---------------------+-------------------+---------------------+-----------------------+
```

### Cena A: 1971 Paranoid Android Metallic Lead (Jonny Greenwood / Radiohead)
- **Objetivo**: O agressivo, distorcido e rasgado solo metálico do final de *Paranoid Android*.
- **Módulo Ring Modulator**:
  - `Carrier Frequency`: 360 Hz (Frequência fixa inarmônica agressiva)
  - `Carrier Waveform`: Sine puro analógico
  - `Mix (Dry/Wet)`: 60% Wet / 40% Dry (Preserva a nota direta da guitarra no centro)
  - `Drive Pós-Ring Mod`: Fuzz de silício de alto ganho com corte de agudos em 4.5 kHz
- **Amp**: Fender Twin Reverb saturado com booster limpo.

### Cena B: Tuned Robot Synth (Melodia Diatônica Robótica)
- **Objetivo**: Transforma melodias de guitarra em solos de sintetizador futurista afinados com a música (*estilo Daft Punk, Kraftwerk e Devo*).
- **Módulo Ring Modulator**:
  - `Carrier Tuning`: Travado em A4 (440 Hz)
  - `Key Tracking`: Ativo (A portadora acompanha a fundamental da escala)
  - `Mix`: 85% Wet / 15% Dry
  - `Envelope Depth`: +120 Hz (Leve desvio dinâmico percussivo no ataque da palheta)
  - `Attack Time`: 5 ms
- **Ambiência**: Analog Slapback Delay (Tempo 120 ms, Mix 25%).

### Cena C: Tremolo-to-Ring Speed Ramp (Controle Contínuo por Pedal)
- **Objetivo**: Controle total pelo **Pedal de Expressão**: com o calcanhar (0%), funciona como um tremolo quente e suave de 4 Hz; ao empurrar para a ponta (100%), a portadora acelera até 1.8 kHz, cruzando a barreira audível em um uivo alienígena.
- **Mapeamento de Expressão**:
  - `Exp Heel (0%)`: Carrier 4.5 Hz (Modo Tremolo)
  - `Exp Toe (100%)`: Carrier 1.850 Hz (Modo Ring Mod Espacial)
  - `Curve`: Logarítmica suave
  - `Mix`: 50% Wet / 50% Dry

### Cena D: Space Bells Ambient Drone (Sinos Espaciais Cósmicos)
- **Objetivo**: Texturas cinematográficas e trilhas atmosféricas de ficção científica com ressonâncias de carrilhão e sino de bronze.
- **Módulo Ring Modulator**:
  - `Carrier Frequency`: 880 Hz (Oitava alta cristalina)
  - `Mix`: 40% Wet
  - `Tape Delay`: Tempo 520 ms pontilhado com Wow & Flutter
  - `Shimmer Reverb`: Cauda imensa de 7.0s com oitava aguda (+12 semitons)

---

## 5. Dicas de Otimização e Execução Musical

1. **Equilíbrio de Mix (Dry/Wet Blend)**:
   - Para solos em músicas de banda, evite usar `Mix: 100% Wet`, pois o desaparecimento total da nota fundamental pode desorientar os outros músicos no palco. Manter entre 35% e 50% de sinal Dry preserva a afinação central enquanto as bandas laterais metálicas decoram o som.
2. **Posição em Relação ao Ganho**:
   - **Antes da Distorção**: As frequências somadas e subtraídas são esmagadas juntas pelo amplificador valvulado, gerando um timbre lo-fi rasgado e agressivo.
   - **Depois da Distorção (Recomendado)**: Cada nota distorcida é multiplicada com clareza cristalina, gerando sinos limpos e espaciais.
