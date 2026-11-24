# Guia de Modelagem, Eletro-Óptica e Roteamento de Compressor Ótico Estilo Teletronix LA-2A no UltraRig

Este documento estabelece as diretrizes de modelagem analógica, histerese fotoquímica da célula T4B, dinâmica de liberação em dois estágios (*two-stage release*) e técnicas de performance para a emulação do clássico **Compressor Ótico Valvulado Teletronix LA-2A** no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

Projetado originalmente na década de 1960 por Jim Lawrence na Califórnia, o Teletronix LA-2A tornou-se o processador dinâmico mais aclamado e universalmente utilizado em estúdios de gravação de todo o planeta (*The Beatles, Led Zeppelin, Steely Dan, Pink Floyd, Eric Clapton, Marcus Miller*). Ao contrário de compressores baseados em transistores rápidos que podem soar mecânicos e agressivos, o LA-2A oferece uma musicalidade aveludada, transparente e sedosa, onde a compressão nivela a dinâmica e eleva a sustentação sem que o ouvinte perceba que o compressor está atuando.

---

## 1. A Física da Célula Eletro-Óptica T4B

O segredo inimitável da resposta dinâmica do LA-2A reside na cápsula selada **T4B Optical Attenuator**, que combina um painel eletroluminescente (EL) com fotoresistores de sulfeto de cádmio (CdS):

```
+---------------------------------------------------------------------------------------+
|                    DIAGRAMA DA CÁPSULA OPTO-ELETRÔNICA T4B                            |
|                                                                                       |
|   [ SINAL DE ÁUDIO DE ENTRADA ]                                                       |
|                 │                                                                     |
|                 ▼                                                                     |
|   [ PAINEL ELETROLUMINESCENTE (EL) ]                                                  |
|   (Emite luz fria proporcional à voltagem do sinal)                                   |
|                 │                                                                     |
|                 ▼ (Fótons de Luz)                                                     |
|   [ FOTORRESISTORES DE SULFETO DE CÁDMIO (CdS) ]                                      |
|   (A resistência cai quando a luz incide, atenuando o áudio suavemente para o terra)  |
|                 │                                                                     |
|                 ▼                                                                     |
|   [ ESTÁGIO DE GANHO VALVULADO: 12AX7 + 12BH7 + TRANSFORMADOR UTC A-24 ]             |
|   (Restaura o ganho e introduz harmônicos pares de 2ª ordem calorosos)                |
+---------------------------------------------------------------------------------------+
```

---

## 2. A Liberação em Dois Estágios (Two-Stage Release)

A assinatura auditiva única do LA-2A nasce da memória fotoquímica dos fotoresistores de CdS. Enquanto compressores digitais e VCA possuem tempos de release matematicamente lineares, o LA-2A comporta-se como um organismo biológico:

```
+---------------------------------------------------------------------------------------+
|                 A CURVA DE LIBERAÇÃO EM DOIS ESTÁGIOS DA CÉLULA T4B                   |
|                                                                                       |
|  1º ESTÁGIO (Recuperação Rápida):                                                     |
|  - Os primeiros 50% da redução de ganho são liberados muito rapidamente, em cerca de  |
|    60 ms após a palhetada. Isso permite que a próxima nota mantenha sua articulação!  |
|                                                                                       |
|  2º ESTÁGIO (Recuperação Gradual e Aveludada):                                        |
|  - Os 50% restantes de atenuação são liberados de forma ultra-lenta e exponencial     |
|    ao longo de 1 a 5 segundos, dependendo da densidade do sinal prévio.               |
|                                                                                       |
|  ──► Efeito Psicoacústico: Ausência total de bombeamento audível (Zero Pumping).      |
|      O instrumento ganha um corpo espesso, aveludado e com sustain cantante infinito! |
+---------------------------------------------------------------------------------------+
```

---

## 3. Aplicações Tímbricas na Guitarra e no Contrabaixo

```
+---------------------------------------------------------------------------------------+
|                    APLICAÇÕES PRINCIPAIS DO LA-2A NO ULTRARIG                         |
+---------------------+-------------------+---------------------------------------------+
| Instrumento         | Ajuste Típico     | Resultado Acústico                          |
+---------------------+-------------------+---------------------------------------------+
| Contrabaixo         | Peak Reduction:   | Ancora o baixo na mixagem com peso          |
| Elétrico e Acústico | 4 a 6 dB de GR    | monolítico, unindo notas graves e agudas    |
|                     | Modo Compress     | com consistência perfeita de estúdio.       |
+---------------------+-------------------+---------------------------------------------+
| Guitarra Limpa      | Peak Reduction:   | Som límpido aveludado, acabando com a       |
| (Strat / Tele)      | 3 a 4 dB de GR    | estridência de palhetadas fortes nos agudos.|
+---------------------+-------------------+---------------------------------------------+
| Jazz & Hollowbody   | Peak Reduction:   | Médios encorpados e redondos estilo Wes     |
| (Captador Braço)    | 2 a 3 dB de GR    | Montgomery com sustentação aveludada.       |
+---------------------+-------------------+---------------------------------------------+
| Violão Acústico     | Peak Reduction:   | Toque sedoso que nivela dedilhados suaves e |
| (Nylon e Aço)       | 3 a 5 dB de GR    | acordes cheios sem achatamento mecânico.    |
+---------------------+-------------------+---------------------------------------------+
```

---

## 4. Modos Operacionais: Compress vs. Limit

O UltraRig permite comutar entre os dois modos clássicos do seletor original:
- **Modo Compress (Ratio ~3:1 dependente de nível)**:
  A curva de joelho (*soft-knee*) é suave e musical. É a escolha primária para nivelamento transparente de instrumentos melódicos, violões e contrabaixo.
- **Modo Limit (Ratio ~8:1 a 10:1)**:
  Apresenta uma inclinação mais íngreme para segurar picos percussivos e proteger contra ceifamento digital, preservando ainda assim a doçura analógica da célula T4B.

---

## 5. Presets de Performance em 4 Cenas (Scenes A/B/C/D)

```
+---------------------------------------------------------------------------------------+
|                    BANCO DE PRESET ULTRA-LA2A: 4 CENAS AVELUDADAS                     |
+---------------------+-------------------+---------------------+-----------------------+
| Cena A: Velvet Vocal| Cena B: Smooth    | Cena C: Vintage     | Cena D: Acoustic      |
| Clean Guitar        | Singing Jazz      | Bass Foundation     | Fingerstyle Silk      |
+---------------------+-------------------+---------------------+-----------------------+
```

### Cena A: Velvet Vocal Clean Guitar (Estúdio Clássico / Steely Dan)
- **Objetivo**: O som de guitarra limpa aveludada, refinada e sem picos agressivos, com sustentação cremosa (*estilo Larry Carlton, Mark Knopfler, Steely Dan*).
- **Módulo LA-2A**:
  - `Model`: `OPTICAL LA-2A TUBE T4B`
  - `Mode`: `COMPRESS (Soft-Knee)`
  - `Peak Reduction`: 55% (Atingindo -3 dB a -4 dB de atenuação nos acordes fortes)
  - `Gain (Makeup)`: +3.5 dB
  - `Tube Saturation (12AX7 Warmth)`: 25% (Ricas harmônicas de 2ª ordem)
- **Amp / Cab**: Fender Blackface Twin Reverb limpo com IR de caixa 2x12 Jensen.
- **Ambiência**: Warm Plate Reverb (Decay 1.8s, Mix 18%).

### Cena B: Smooth Singing Jazz Warmth (Wes Montgomery / George Benson)
- **Objetivo**: Timbre de guitarra semi-acústica (*hollowbody*) com captador de braço humbucker, graves redondos e médios aveludados para linhas de oitava e arpejos jazzísticos.
- **Módulo LA-2A**:
  - `Mode`: `COMPRESS`
  - `Peak Reduction`: 45% (Atenuação suave de -2.5 dB)
  - `High-Frequency Emphasis`: Suave roll-off acima de 5 kHz
  - `Gain`: +2.5 dB
- **Amp**: Roland JC-120 limpo ou Fender Tweed Deluxe no ponto limpo.

### Cena C: Vintage Bass Thick Foundation (Marcus Miller / James Jamerson)
- **Objetivo**: A fundação definitiva para contrabaixo elétrico. Graves profundos inabaláveis que grudam no bumbo da bateria sem oscilar de volume.
- **Módulo LA-2A**:
  - `Mode`: `COMPRESS`
  - `Peak Reduction`: 68% (Atingindo -5 dB de redução de ganho firme)
  - `Gain`: +4.5 dB
  - `Low-End Tube Weight`: Ativo (Reforço sutil de calor em 80 Hz)
- **Amp / Cab**: Ampeg B-15 Portaflex valvulado clássico com falante de 15".
- **Saída**: XLR balanceada para PA e fones.

### Cena D: Acoustic Fingerstyle Silk (Violão de Seda Sem Picos)
- **Objetivo**: Dedilhado de violão de aço ou nylon perfeitamente equilibrado, onde cada nota dedilhada soa com volume uniforme e sustentação doce.
- **Módulo LA-2A**:
  - `Mode`: `COMPRESS`
  - `Peak Reduction`: 50% (Redução de ganho de -3 dB)
  - `Gain`: +3.0 dB
  - `Body IR Acoustic`: 2048 pts Dreadnought Spruce/Rosewood
  - `Ambiência`: Lush Hall Reverb (Decay 2.4s, Mix 22%)

---

## 6. Dicas de Otimização e Calibração no UltraRig

1. **Ajuste Exclusivo com os Olhos e Ouvidos**:
   - No LA-2A real, não existem controles manuais de Attack, Release ou Ratio: o circuito faz tudo sozinho de forma musical. Ajuste simplesmente o botão `Peak Reduction` até que o medidor de ganho oscile suavemente entre $-2\text{ dB}$ e $-4\text{ dB}$ nas partes mais fortes da música.
2. **Posição na Cadeia de Efeitos**:
   - Posicione o LA-2A **como primeiro elemento** após a entrada se o objetivo for nivelar o sinal antes dos amplificadores; posicione **após o bloco de simulação de amplificador/IR** se o objetivo for emular a compressão de estúdio de pós-gravação de uma faixa finalizada.
