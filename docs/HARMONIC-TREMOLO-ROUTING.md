# Guia de Modelagem e Roteamento de Tremolo Harmônico Vintage vs. Tremolo Óptico no UltraRig

Este documento ensina a projetar, equalizar e calibrar o lendário **Tremolo Harmônico (Brownface Harmonic Vibrato)** e compará-lo ao **Tremolo Óptico / Bias** tradicional no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

No início da década de 1960, Leo Fender desenvolveu nos amplificadores *Fender Brownface / Blonde (Super, Concert, Pro, Twin e Bandmaster)* um dos circuitos de modulação analógica mais fascinantes da história da guitarra: o **Harmonic Vibrato**. Ao contrário do tremolo óptico comum (que apenas corta e sobe o volume geral), o tremolo harmônico divide o espectro em duas faixas de frequência moduladas em oposição de fase, criando um movimento tridimensional pulsante, aveludado e que lembra um híbrido entre Phaser, Uni-Vibe e Rotary Speaker.

---

## 1. Tremolo Óptico / Bias vs. Tremolo Harmônico

| Característica | Tremolo Óptico / Bias (Blackface / Vox) | Tremolo Harmônico (Brownface 1960–1963) |
| :--- | :--- | :--- |
| **Princípio de Funcionamento** | Modulação de amplitude direta (VCA / fotocélula LDR). | **Divisão em bandas de frequência (Split Crossover).** |
| **Comportamento das Frequências** | Todo o espectro de frequências sobe e desce de volume junto. | Graves e agudos são modulados **em oposição de fase (180°)**. |
| **Sensação de Volume Geral** | Perda perceptiva de volume de até 3 dB nos vales da onda. | **Volume constante e estável:** enquanto o grave sobe, o agudo desce. |
| **Caráter Sonoro** | Seco, cortante, percussivo (*chop* de onda quadrada). | Quente, aquático, hipnótico e com textura tridimensional de fase. |

---

## 2. A Arquitetura do Tremolo Harmônico no UltraRig

Para recriar a topologia original do amplificador Brownface no UltraRig, utilizamos dois ramos paralelos com filtros passa-baixas e passa-altas operando em fases invertidas:

```
+-------------------------------------------------------------------------------+
|         TOPOLOGIA DO TREMOLO HARMÔNICO PARALELO NO ULTRARIG                   |
|                                                                               |
|                             +---> [ RAMO A: BANDA DE GRAVES ] ---------------+ |
|                             |     - LPF em 750 Hz (12 dB/oitava)             | |
|                             |     - Tremolo de Volume (LFO Fase 0°)          | |
| [ Sinal da Guitarra ] ----->+                                                +>[Merge]
|                             |                                                | (Master)
|                             +---> [ RAMO B: BANDA DE AGUDOS ] ---------------+ |
|                                   - HPF em 750 Hz (12 dB/oitava)             |
|                                   - Tremolo de Volume (LFO Fase 180° Invert) |
+-------------------------------------------------------------------------------+
```

### O Que Acontece no Áudio:
1. **Momento 1 do Ciclo do LFO:** A banda grave (Ramo A) atinge o pico máximo de volume, enquanto a banda aguda (Ramo B) é atenuada ao mínimo. O som fica escuro, encorpado e aveludado.
2. **Momento 2 do Ciclo do LFO:** A banda grave é atenuada, enquanto a banda aguda abre com brilho máximo. O som fica cristalino, aéreo e estalado.
3. **Resultado:** A energia total do sinal permanece constante no ar, mas a guitarra pulsa organicamente entre calor e brilho, gerando uma onda sonora quase física sem nenhuma perda de peso ou presença.

---

## 3. Calibração Prática de Parâmetros Passo a Passo

### 3.1 Ponto de Cruzamento do Crossover (Crossover Frequency)
- O ponto onde as duas bandas se encontram define o centro tonal do efeito:
  - **650 Hz a 750 Hz (Padrão Brownface Clássico):** Equilibra o corpo das cordas graves com o brilho percussivo das agudas.
  - **450 Hz (Dark Swirl):** Deixa a oscilação mais focada nos médios-agudos, lembrando um Uni-Vibe estilo Hendrix.
  - **900 Hz (Bright Throb):** Dá maior peso à modulação nos bordões da guitarra.

### 3.2 Sincronismo e Inversão de Fase dos LFOs (180° Phase Offset)
- Certifique-se de que os osciladores dos dois blocos estejam com a **mesma velocidade (Rate em Hz ou BPM sincronizado)**.
- O Tremolo do Ramo B deve ter o parâmetro **Phase ajustado em 180°**. Se ambos estiverem em 0°, o efeito se tornará um tremolo de volume comum.

### 3.3 Profundidade de Modulação (Depth)
- **Depth em 40% a 55%:** Efeito sutil e orgânico, ideal para bases de blues, soul e baladas sem cansar o ouvinte.
- **Depth em 75% a 90%:** Modulação profunda e psicodélica com varredura quase aquática para temas instrumentais e surf music.

---

## 4. Tremolo Harmônico Estéreo com Espalhamento Espacial

No UltraRig, você pode levar a ideia de Leo Fender para uma dimensão impossível nos amplificadores analógicos da década de 60:

```
Ramo A (Graves modulados) ----> Pan L 40% (Levemente à Esquerda)
Ramo B (Agudos modulados) ----> Pan R 40% (Levemente à Direita)
```

- Nos fones de ouvido ou no sistema de PA estéreo, a transição entre grave e agudo viaja diagonalmente no espaço, criando um vórtice tridimensional envolvente sem causar problemas de cancelamento quando somado em mono.

---

## 5. Arquitetura de 4 Cenas para Shows ao Vivo

```
+-------------------------------------------------------------------------------+
|             PRESET: "VINTAGE-TREMOLO-PRO" (4 CENAS PROGRAMADAS)               |
|                                                                               |
|  [Scene A] 1962 BROWNFACE HARMONIC PULSE                                      |
|   - Tremolo Harmônico Paralelo (Crossover 720 Hz, Fase 180°)                 |
|   - Rate: 1.8 Hz (Semínima suave), Depth 60%                                  |
|   - Saturação leve de pré-amp valvulado vintage                               |
|   - Timbre aveludado e orgânico estilo Dan Auerbach / Black Keys              |
|                                                                               |
|  [Scene B] 1965 BLACKFACE OPTO CHOP                                           |
|   - Tremolo de volume único (Modo Óptico tradicional)                         |
|   - Onda senoidal pura com corte de volume perceptivo                         |
|   - Spring Reverb vintage integrado para surf music e trilhas cinematográficas|
|                                                                               |
|  [Scene C] PSYCHEDELIC UNIVIBE SWIRL                                          |
|   - Crossover ajustado em 550 Hz com espalhamento estéreo L/R                 |
|   - LFO com leve assimetria de onda                                           |
|   - Saturação de Fuzz suave em série gerando o clássico som de Jimi Hendrix   |
|                                                                               |
|  [Scene D] DYNAMIC TOUCH TREMOLO (Acelerador Dinâmico)                        |
|   - O envelope da palhetada acelera a velocidade de 1.2 Hz para 5.5 Hz        |
|   - Ataques pesados de palheta fazem o efeito vibrar rapidamente               |
|   - Conforme a nota sustenta, o tremolo desacelera suavemente                 |
+-------------------------------------------------------------------------------+
```

---

## 6. Solução de Dúvidas e Problemas (Troubleshooting)

- **O som apresenta pequenos cancelamentos de volume no centro:**
  - *Causa:* As inclinações dos filtros do crossover estão com inclinações diferentes ou há um pequeno atraso de delay entre os ramos.
  - *Solução:* Certifique-se de que tanto o filtro LPF quanto o HPF estejam configurados com a mesma inclinação (**12 dB/oitava**) e sem blocos adicionais de delay em apenas um dos ramos.
- **O efeito soa como um tremolo comum sem o movimento harmônico:**
  - *Causa:* O parâmetro de fase do LFO não está defasado em 180°.
  - *Solução:* Verifique no bloco de modulação do Ramo B se a fase está configurada em exatos 180°.
