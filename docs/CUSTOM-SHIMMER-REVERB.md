# Guia de Construção e Roteamento de Shimmer Reverb com Pitch Shifter em Ramo Paralelo no UltraRig

Este documento ensina a projetar, equalizar e calibrar manualmente um efeito de **Shimmer Reverb** de alta fidelidade no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box), utilizando a combinação modular de **Pitch Shifter Polifônico** e **Reverb de Placa/Hall** em ramos paralelos (*Parallel DSP Branching*).

O efeito *Shimmer* (pioneirizado por Brian Eno e Daniel Lanois em produções com o U2 nos anos 80, combinando harmonizadores *Eventide* com reverbs *Lexicon*) cria uma cauda etérea semelhante a um teclado sintetizador de cordas (*pad*) que floresce atrás da guitarra. Em pedaleiras digitais compactas, algoritmos de shimmer embutidos de fábrica frequentemente soam metálicos, estridentes e artificiais. A construção modular paralela no UltraRig entrega um som quente, aveludado e com total controle de harmônicos.

---

## 1. A Anatomia do Efeito Shimmer Autêntico

Diferente de um simples reverb com filtro brilhante, o Shimmer genuíno envolve transposição de frequência na malha de reverberação:

```
+-------------------------------------------------------------------------------+
|                       ARQUITETURA DE SHIMMER PARALELO NO ULTRARIG             |
|                                                                               |
|                             +---> [ RAMO A: GUITARRA PRINCIPAL ] ---+         |
|                             |     - Timbre Direto (Clean ou Lead)   |         |
|                             |     - Pan Central / Punch Firme       |         |
| [ Sinal da Guitarra ] ----->+                                       +>[ Merge]|
|                             |                                       | (Master)|
|                             +---> [ RAMO B: MALHA SHIMMER ] --------+         |
|                                   - Pré-LPF (Corta estalo @ 5 kHz)  |         |
|                                   - Pitch Shifter (+1 Oitava / +12) |         |
|                                   - Plate/Hall Reverb (Decay 4.0s)  |         |
|                                   - Dynamic Ducking / Compressor    |         |
|                                   - Stereo Detune (+/- 4 cents)     |         |
+-------------------------------------------------------------------------------+
```

### Por Que Algoritmos Fixos de Fábrica Soam Metálicos?
1. **Transientes de Palheta Transpostos:** Quando o estalo pontiagudo da palheta atinge um oitavador direto, os harmônicos de alta frequência são multiplicados para 8 kHz a 14 kHz, gerando um "tilintar" agudo e metálico (*digital glassiness*).
2. **Realimentação Sem Amortecimento (Runaway Highs):** Se o sinal transposto for devolvido ao reverb sem filtragem, as frequências agudas entram em ciclo de feedback ressonante estridente.

---

## 2. Passo a Passo de Construção no Ramo Paralelo

### Passo 1: O Pré-Filtro Amortecedor (Pre-LPF)
- No início do Ramo B (antes do Pitch Shifter), insira um filtro passa-baixas:
  - **Frequência de Corte (LPF):** **4.5 kHz a 5.5 kHz (12 dB/oitava)**.
  - *Função:* Remove o atrito da palheta nas cordas e ruídos de manuseio antes que o algoritmo de pitch tente transpô-los para a oitava superior.

### Passo 2: O Pitch Shifter Polifônico
- **Modo:** Polifônico (capaz de transpor acordes cheios sem desafinação ou tremulação).
- **Intervalo:** **+12 semitons (+1 Oitava)**.
- **Mix no Bloco de Pitch:** **100% Wet** (o Ramo B deve conter exclusivamente o sinal transposto; o som original já é preservado no Ramo A).
- **Fine Tune / Detune:** Aplique uma sutil desafinação de **+3 a +5 centésimos**. Isso impede que o sinal oitavado dispute fase com os harmônicos naturais da guitarra, gerando um efeito de coro angelical (*chorused shimmer*).

### Passo 3: O Bloco de Reverb Espacial
- **Tipo de Reverb:** *Studio Plate* ou *Large Hall*.
- **Decay Time:** **3.5 segundos a 5.0 segundos** (longa duração para criar a sustentação de teclado).
- **High Damping / Hi-Cut:** Ajustado em **4.0 kHz**. As repetições da cauda perdem agudos suavemente com o tempo, imitando a absorção acústica do ar em uma catedral.
- **Pre-Delay:** **40 ms a 70 ms**. Deixa um pequeno espaço de respiro após a nota palhetada antes que a nuvem de shimmer comece a subir.

### Passo 4: Dynamic Ducking (Controle de Clareza)
- Para evitar que a nuvem de shimmer embole passagens rápidas ou dedilhados complexos:
  - Configure o detector de envelope no bloco de delay/reverb para **atenuar o Ramo B em -6 dB a -8 dB enquanto houver palhetada ativa**.
  - No momento em que você sustenta uma nota ou acorde e para de palhetar, o shimmer sobe suavemente (*bloom*), preenchendo o silêncio.

---

## 3. Variações Harmônicas: Shimmer de 5ª e Dark Shimmer

Além da clássica oitava superior (+12), o UltraRig permite explorar outras atmosferas musicais:

| Tipo de Shimmer | Intervalo de Pitch | Efeito Sonoro | Ideal Para |
| :--- | :--- | :--- | :--- |
| **Classic Angelic** | +12 semitons (+1 Oct) | Brilho cristalino de cordas etéreas e luz. | Worship, Dream Pop, Post-Rock. |
| **Ethereal Synth Pad** | +7 semitons (+ Quinta Justa) | Adiciona a 5ª harmônica, transformando qualquer acorde simples em um pad orquestral rico. | Ambient, Trilhas Sonoras, Sci-Fi. |
| **Dark / Sub-Shimmer** | -12 semitons (-1 Oct) | Oitava grave reverberada, criando um manto sombrio, pesado e cinematográfico. | Doom Metal, Shoegaze, Darkwave. |

---

## 4. Arquitetura de 4 Cenas para Shows ao Vivo

```
+-------------------------------------------------------------------------------+
|             PRESET: "CUSTOM-SHIMMER-PRO" (4 CENAS PROGRAMADAS)                |
|                                                                               |
|  [Scene A] CORE STUDIO CLEAN (Seco e Definido)                                |
|   - Ramo A: 100% Ativo (Amp limpo + Compressor sutil)                         |
|   - Ramo B (Shimmer): BYPASS                                                  |
|   - Tonalidade pura para ritmo funk, pop e estrofes com banda completa        |
|                                                                               |
|  [Scene B] SUBTLE ANGELIC SHIMMER (Baladas e Dedilhados)                      |
|   - Ramo A: 100% Ativo                                                        |
|   - Ramo B (Shimmer +12): 22% Mix em paralelo                                 |
|   - Nuvem suave flutuando atrás da melodia sem disputar espaço                |
|                                                                               |
|  [Scene C] ETHEREAL SWELL PAD (Volume Swell / Teclado)                        |
|   - Ramo A: 40% Mix (Ataque arredondado)                                      |
|   - Ramo B (Shimmer +12 / +7 Detuned): 60% Mix                                |
|   - Pedal de expressão controlando swell de volume (0% a 100%)                |
|   - Camadas sonoras monumentais estilo orquestra sinfônica                    |
|                                                                               |
|  [Scene D] DARK CINEMATIC SUB-SHIMMER (Pós-Rock e Temas Sombrios)             |
|   - Ramo B configurado em -12 semitons (-1 Oitava)                            |
|   - Plate Reverb longo (Decay 5.2s) + Cauda escura filtrada em 2.5 kHz        |
|   - Peso colossal de graves flutuantes para solos melancólicos                |
+-------------------------------------------------------------------------------+
```

---

## 5. Resolução de Problemas (Troubleshooting)

- **O shimmer fica apitando em microfonia digital contínua:**
  - *Causa:* Realimentação descontrolada no bloco de pitch ou agudos excessivos acima de 6 kHz.
  - *Solução:* Reduza o parâmetro *Feedback* da malha e feche o *Pre-LPF* para **4.2 kHz**.
- **O som fica embolado e perde o ritmo da música:**
  - *Causa:* Ramo de shimmer alto demais (mix > 45%) competindo com a guitarra base.
  - *Solução:* Ative o *Dynamic Ducking* para abaixar o shimmer enquanto toca e diminua o mix do Ramo B para **20%**.
- **A afinação do shimmer parece oscilar de forma desafinada:**
  - *Causa:* O pitch shifter está operando em modo monofônico tentando rastrear acordes.
  - *Solução:* Certifique-se de selecionar o algoritmo **Polyphonic Pitch Tracking** nas configurações do bloco.
