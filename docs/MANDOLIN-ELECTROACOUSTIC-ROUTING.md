# Guia de Engenharia Eletroacústica, Dinâmica de Chop e Convolução de IR para Bandolim no UltraRig

Este documento estabelece as diretrizes de processamento eletroacústico, controle de transientes percussivos de batida de acorde (*mandolin chop*), nivelamento dinâmico de trêmolo rápido de palheta e convolução de respostas de impulsos (IR) de corpos entalhados em Spruce/Maple (*F-Style e A-Style*) para **Bandolins Eletroacústicos (*Acoustic Mandolin*)** no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

O bandolim de 8 cordas é o motor rítmico e melódico fundamental do *Bluegrass, Choro brasileiro, Música Celta, Folk e Country acústico* (*Bill Monroe, Chris Thile / Punch Brothers, Sam Bush, David Grisman, Hamilton de Holanda, Jacob do Bandolim*). Composto por 4 pares de cordas de aço duplas afinadas em quintas (*G3-D4-A4-E5*), o instrumento possui uma escala ultra-curta (~13.8 polegadas) submetida a uma tensão mecânica formidável. Quando amplificado ao vivo por captadores piezoelétricos sob a ponte flutuante (*Fishman M-200, K&K Mandolin Twin, Schertler*), o bandolim sofre com estridência metálica excessiva, falta de graves e picos dinâmicos violentos no acompanhamento rítmico.

---

## 1. A Física Acústica das 8 Cordas e as Formas F-Style vs. A-Style

```
+---------------------------------------------------------------------------------------+
|                    COMPARAÇÃO: BANDOLIM F-STYLE vs. BANDOLIM A-STYLE                  |
+---------------------+-----------------------------+-----------------------------------+
| Modelo              | Características Físicas     | Resposta Sonora & Aplicação       |
+---------------------+-----------------------------+-----------------------------------+
| F-Style             | Tampo entalhado em abeto    | Timbre cortante, focado, percussivo|
| (Florentine)        | (Spruce) com volutas de bico| com graves rápidos. O padrão      |
|                     | e f-holes (estilo violino). | absoluto do Bluegrass (*Bill      |
|                     | Corpo de bordo (Maple).     | Monroe, Sam Bush, Chris Thile*).  |
+---------------------+-----------------------------+-----------------------------------+
| A-Style             | Corpo oval em formato de    | Som mais doce, aberto, ressonante |
| (Teardrop / Gota)   | gota, boca oval ou f-holes. | e aveludado com maior sustentação.|
|                     | Construção clássica.        | Ideal para Choro, Celta e Folk.   |
+---------------------+-----------------------------+-----------------------------------+
```

### O Desafio dos Picos do "Chop" e do Trêmolo Rápido:
1. **O Chop Rítmico de Bluegrass**:
   - O bandolinista golpeia acordes abafando as cordas imediatamente com a mão esquerda, funcionando como a "caixa da bateria" na banda acústica. Esse golpe gera transientes percussivos com picos de até $+16\text{ dB}$ em relação ao solo melódico.
2. **A Estridência Piezo no Cavalete**:
   - Os pares duplos de cordas agudas de aço puro (Mi a $659.3\text{ Hz}$ e Lá a $440\text{ Hz}$) transmitem picos agressivos concentrados entre **$3.2\text{ kHz}$ e $4.2\text{ kHz}$**, gerando um estalo cortante e estridente.
3. **Ausência de Subgraves**:
   - O par de cordas mais grave do bandolim é o Sol ($G_3 \approx 196.0\text{ Hz}$). Qualquer energia abaixo de $140\text{ Hz}$ é ruído mecânico inútil (batidas da palma da mão na ponte ou vibrações de pedestal).

---

## 2. Roteamento de Sinal e Cadeia DSP no UltraRig

Para domar a estridência e restaurar a reverberação amadeirada da cavidade entalhada:

```
[ BANDOLIM COM PIEZO ]
          │
          ▼
 [ HPF CIRÚRGICO 140 Hz ] ──► [ NOTCH ANTI-QUACK 3.6 kHz ] ──► [ COMPRESSOR ÓTICO ]
 (Elimina batidas na ponte)    (Remove aspereza do piezo)       (Nivela o chop e o trêmolo)
                                                                       │
                                                                       ▼
 [ SAÍDAS XLR / FONES ] ◄── [ AMBIÊNCIA SALA / PLATE ] ◄── [ F-STYLE MANDOLIN IR ] ◄─┘
  (Sinal doce e percussivo)  (Decay 1.3s, madeira rica)     (Convolução 2048 pts)
```

### Blocos Críticos da Modelagem:
1. **Filtro Passa-Altas Cirúrgico (HPF)**:
   - Configurado entre **$135\text{ Hz}$ e $150\text{ Hz}$** ($18\text{ dB/octave}$). Isola o som das cordas e elimina 100% de baques de mão na ponte flutuante.
2. **Filtro Notch Anti-Quack de Médios-Agudos**:
   - Atenuação cirúrgica de $-4.5\text{ dB}$ em **$3.6\text{ kHz}$** ($Q: 2.2$). Devolve a nobreza ao ataque sem tirar o brilho harmônico das cordas de aço.
3. **Compressor Ótico com Tempo de Ataque Calibrado**:
   - `Attack Time`: $20\text{ ms}$ a $30\text{ ms}$ (Permite que o "estalo" percussivo do chop seja ouvido, mas intervém rapidamente para evitar sobrecarga no PA).
   - `Release Time`: $110\text{ ms}$ (Recuperação rápida para não embolar notas rápidas de trêmolo).
4. **Convolução de Resposta de Impulso de Bandolim (Mandolin IR)**:
   - Carrega um IR de 2048 amostras capturado com par casado de microfones condensadores de estúdio (*Neumann KM184*) em um Gibson Lloyd Loar F-5 de 1923, restaurando a ressonância de madeira nobre.

---

## 3. Presets de Performance em 4 Cenas (Scenes A/B/C/D)

```
+---------------------------------------------------------------------------------------+
|                 BANCO DE PRESET ULTRA-MANDOLIN: 4 CENAS DE PALCO                      |
+---------------------+-------------------+---------------------+-----------------------+
| Cena A: Bluegrass   | Cena B: Fast      | Cena C: Brazilian   | Cena D: Stage Clean   |
| Chop Foundation     | Tremolo Solo      | Choro / Celtic Mellow| Feedback-Proof DI    |
+---------------------+-------------------+---------------------+-----------------------+
```

### Cena A: Bluegrass Chop Foundation (Bill Monroe / Sam Bush)
- **Objetivo**: A base rítmica clássica de Bluegrass, com corte seco, grave percussivo firme e estalo seco sem estridência no PA.
- **Módulos DSP**:
  - `HPF`: 145 Hz
  - `Fast Peak Limiter`: Teto em -2 dBFS para segurar os golpes mais fortes do chop
  - `Optical Compressor`: Ratio 3.5:1, Attack 22 ms, Release 95 ms
  - `Parametric EQ`: Low-Mid +2.5 dB @ 380 Hz (corpo de madeira), Notch -5 dB @ 3.6 kHz
  - `Body IR`: F-Style Lloyd Loar Master Model (Mix 55%)
  - `Room Reverb`: Mix 10%, Decay 0.8s
- **Saída**: XLR balanceada para PA e fones in-ear.

### Cena B: Fast Tremolo Solo Chime (Chris Thile / Virtuoso)
- **Objetivo**: Solos virtuosos e palhetada alternada rápida contínua (*tremolo picking*), com sustentação cantante e textura sedosa.
- **Módulos DSP**:
  - `HPF`: 135 Hz
  - `Compressor Suave`: Ratio 2.5:1, Attack 35 ms, Release 140 ms
  - `EQ`: High-Shelf +2.0 dB @ 8 kHz (brilho aéreo cristalino)
  - `Stereo Dimension Chorus`: Mix 12% (Largura estéreo sutil)
  - `Warm Plate Reverb`: Decay 1.8s, Mix 20%, Pre-delay 20 ms
  - `Body IR`: F-5 Custom Spruce/Maple (Mix 60%)

### Cena C: Brazilian Choro / Celtic Mellow (Jacob do Bandolim / Hamilton)
- **Objetivo**: Timbre doce, redondo e aveludado característico do Choro brasileiro e da música celta irlandesa, com corpo de boca redonda A-Style.
- **Módulos DSP**:
  - `HPF`: 125 Hz
  - `High-Cut Filter`: 6.5 kHz (Roll-off suave para eliminar ruído de atrito de palheta de celuloide)
  - `Parametric EQ`: +3.0 dB em 500 Hz (Médios quentes amadeirados)
  - `Body IR`: Vintage A-Style Oval Hole Mandolin (Mix 65%)
  - `Ambiência`: Wooden Hall Reverb (Decay 1.6s, Mix 18%)

### Cena D: Stage Clean Feedback-Proof DI (Festivais com Volume Alto)
- **Objetivo**: Tolerância zero para microfonia em palcos barulhentos com monitores de chão e baterias próximas.
- **Módulos DSP**:
  - `HPF`: 160 Hz (Elimina qualquer risco de ressonância de baixa frequência)
  - `Dual Notches`: -6 dB @ 3.6 kHz e -4 dB @ 850 Hz (ressonância do tampo)
  - `Inversor de Fase (180°)`: Ativo para cancelamento acústico de palco
  - `IR & Reverb`: Bypass para sinal direto cirúrgico na mesa de som

---

## 4. Dicas de Otimização e Execução no Palco

1. **Escolha da Palheta**:
   - Bandolins exigem palhetas pesadas e rígidas (1.2 mm a 1.5 mm, com bordas arredondadas e polidas, como as clássicas *BlueChip ou Dunlop Primetone*). Palhetas finas geram um som estaladiço e agudo que nenhum equalizador consegue consertar.
2. **Afinação Precisa dos Pares de Cordas**:
   - Como o bandolim possui cordas duplas, um desvio de apenas 2 cents entre os dois fios de um mesmo par gera um batimento de desafinação indesejado. Utilize o afinador cromático estroboscópico de alta precisão do UltraRig para calibrar cada corda individualmente, abafando a corda vizinha com a mão durante a afinação.
