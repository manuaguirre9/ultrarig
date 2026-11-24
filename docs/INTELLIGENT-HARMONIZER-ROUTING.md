# Guia de Modelagem, Teoria Musical Diatônica e Roteamento de Harmonizador Inteligente no UltraRig

Este documento estabelece as diretrizes de processamento digital de sinais (DSP), detecção de pitch em tempo real (*pitch tracking*), regras de quantização tonal diatônica e técnicas de roteamento estéreo para **Harmonizadores Inteligentes em Escala (*Intelligent Diatonic Scale Harmonizers*)** no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

O harmonizador inteligente é uma das ferramentas mais sofisticadas e impactantes da guitarra moderna (*Thin Lizzy - The Boys Are Back in Town, Iron Maiden - The Trooper / Hallowed Be Thy Name, The Allman Brothers Band - Jessica, Queen / Brian May - Bohemian Rhapsody / Killer Queen, Boston, Avenged Sevenfold*). Ao contrário de pedais pitch-shifters convencionais que aplicam transposições estáticas em semitons (gerando notas desafinadas fora do campo harmônico), o harmonizador diatônico calcula em frações de milissegundo a nota exata correspondente à tonalidade e escala configuradas na música.

---

## 1. Pitch Shifter Cromático vs. Harmonizador Diatônico Inteligente

```
+---------------------------------------------------------------------------------------+
|                 PITCH SHIFTER CROMÁTICO vs. HARMONIZADOR DIATÔNICO                    |
+---------------------+-----------------------------+-----------------------------------+
| Abordagem           | Lógica de Transposição      | Resultado Musical na Prática      |
+---------------------+-----------------------------+-----------------------------------+
| Pitch Shifter       | Transposição fixa em        | Em C Maior, se tocar Dó (C), a    |
| Cromático Fixo      | semitons constantes         | terça é Mi (E) = +4 semitons (OK).|
| (Ex: +4 semitons)   | (ex: sempre 3ª Maior).      | Mas se tocar Ré (D), a terça vira |
|                     | Não conhece a escala.       | Fá# (F#) (+4 semitons), gerando   |
|                     |                             | uma nota FORA da escala (erro)!   |
+---------------------+-----------------------------+-----------------------------------+
| Harmonizador        | Analisa a tônica (Key) e a  | Em C Maior:                       |
| Inteligente         | escala (Scale) em tempo real| - Toca C (Dó) ──► Gera E (+4 st)  |
| Diatônico (UltraRig)| e varia dinamicamente entre | - Toca D (Ré) ──► Gera F (+3 st)  |
|                     | 3ª Maior e 3ª Menor.        | - Toca E (Mi) ──► Gera G (+3 st)  |
|                     |                             | 100% afinado com o campo harmônico|
+---------------------+-----------------------------+-----------------------------------+
```

---

## 2. A Arquitetura DSP: Pitch Tracking, Formantes e Humanização

Para que a harmonia soe como um segundo guitarrista real tocando no palco ao lado do músico:

```
                            [ SINAL DA GUITARRA ]
                                      │
            ┌─────────────────────────┴─────────────────────────┐
            │                                                   │
            ▼                                                   ▼
   [ SINAL DIRETO (DRY) ]                             [ DETECTOR DE PITCH ]
   (Voz Central Principal)                            (Algoritmo YIN / Wavelet)
            │                                                   │
            │                                                   ▼
            │                                         [ TABELA DE ESCALAS ]
            │                                         (Key + Mode Configurados)
            │                                                   │
            │                                                   ▼
            │                                         [ SHIFTER COM FORMANTES ]
            │                                         (Gera Voz Harmônica)
            │                                                   │
            │                                                   ▼
            │                                         [ HUMANIZAÇÃO / DELAY ]
            │                                         (Atraso intencional 12ms)
            │                                                   │
            └─────────────────────────┬─────────────────────────┘
                                      │
                                      ▼
                           [ MATRIZ ESTÉREO L/C/R ]
                    (Voz Dry no Centro | Harmonia nos Lados)
```

### Componentes Tecnológicos Essenciais:
1. **Algoritmo de Rastreamento de Pitch de Baixa Latência (YIN Wavelet)**:
   - Rastreia o período fundamental ($F_0$) em menos de $8\text{ ms}$ a $12\text{ ms}$, permitindo solos ultra-rápidos sem atraso perceptível no toque.
2. **Correção e Preservação de Formantes (Formant Preservation)**:
   - Sem correção de formantes, subir uma terça ou quinta aguda faz a guitarra soar como um "esquilo" (*chipmunk effect*), perdendo a ressonância do corpo do instrumento. O UltraRig mantém a resposta acústica natural das madeiras na voz sintetizada.
3. **Parâmetro de Humanização (Micro-Timing e Micro-Detune)**:
   - Guitarristas humanos nunca tocam com sincronia mecânica de zero milissegundos. Adicionar um atraso intencional de **$10\text{ ms}$ a $16\text{ ms}$** e uma leve variação aleatória de afinação ($\pm 4\text{ cents}$) na voz harmônica cria a sensação autêntica de dois músicos de carne e osso tocando juntos.

---

## 3. Modos e Escalas Suportados no UltraRig

O motor suporta todas as escalas e modos essenciais da música ocidental:
- **Major (Jônio)**: Rock clássico, Pop, Country, Hinos e Baladas (*Allman Brothers, Boston*).
- **Natural Minor (Eólio)**: Heavy Metal tradicional, Hard Rock (*Iron Maiden, Judas Priest*).
- **Harmonic Minor (Menor Harmônica)**: Metal Neoclássico, solos barrocos (*Yngwie Malmsteen, Symphony X*).
- **Dorian (Dórico)**: Fusion, Funk-Rock instrumental (*Carlos Santana, Pink Floyd*).
- **Mixolydian (Mixolídio)**: Blues-Rock, Southern Rock, solos modais com 7ª menor.
- **Pentatônica Maior e Menor**: Linhas melódicas bluesy rápidas.

---

## 4. Presets de Performance em 4 Cenas (Scenes A/B/C/D)

```
+---------------------------------------------------------------------------------------+
|                 BANCO DE PRESET ULTRA-HARMONIZER: 4 CENAS DE PALCO                    |
+---------------------+-------------------+---------------------+-----------------------+
| Cena A: Allman Dual | Cena B: Iron      | Cena C: Brian May   | Cena D: Neoclassical  |
| Southern Lead       | Maiden Heavy 3rds | Queen Orchestration | Harmonic Minor Run    |
+---------------------+-------------------+---------------------+-----------------------+
```

### Cena A: Allman Brothers Dual Southern Lead (Rock Clássico Sulista)
- **Objetivo**: O doce dueto harmônico de Dickey Betts e Duane Allman (*Jessica, Ramblin' Man*).
- **Configuração do Harmonizador**:
  - `Key`: A (Lá)
  - `Scale`: `MAJOR / MIXOLYDIAN`
  - `Voice 1 Interval`: `+3rd Diatonic Above` (Terça diatônica acima)
  - `Voice 1 Pan`: 75% Left
  - `Dry Voice Pan`: 0% Center
  - `Humanize Delay`: 14 ms
  - `Detune`: +3 cents
  - `Voice Balance`: 50% Dry / 50% Voice 1
- **Amp**: Marshall Plexi limpo-quente com overdrive suave.

### Cena B: Iron Maiden Heavy Metal 3rds (The Trooper / Hallowed Be Thy Name)
- **Objetivo**: Duas guitarras gêmeas cortantes em menor natural, perfeitas para riffs de cavalgada e solos em palhetada alternada rápida.
- **Configuração do Harmonizador**:
  - `Key`: E (Mi)
  - `Scale`: `NATURAL MINOR (AEOLIAN)`
  - `Voice 1 Interval`: `+3rd Diatonic Above`
  - `Voice 1 Pan`: 100% Right
  - `Dry Voice Pan`: 100% Left (Separação estéreo radical estilo Dave Murray e Adrian Smith)
  - `Humanize Delay`: 10 ms
  - `Amp Model`: British High-Gain JCM800 com booster Tube Screamer
  - `Cab IR`: 4x12 Celestion G12-75

### Cena C: Brian May Queen Orchestration (Coral de Guitarras a 3 Vozes)
- **Objetivo**: Orquestração épica a 3 vozes simultâneas (*Killer Queen, Bohemian Rhapsody*), transformando uma única guitarra em uma sinfonia.
- **Configuração do Harmonizador**:
  - `Key`: F (Fá) / Bb (Si bemol)
  - `Scale`: `MAJOR`
  - `Voice 1`: `+3rd Diatonic` (Pan 80% Left, Nível 80%)
  - `Voice 2`: `+5th Diatonic` (Pan 80% Right, Nível 75%)
  - `Dry Voice`: Centro (Nível 100%)
  - `Humanize Delay`: Voice 1: 12 ms / Voice 2: 20 ms
- **Amp**: Vox AC30 Top Boost com treble booster no input.

### Cena D: Neoclassical Harmonic Minor Run (Shredding Barroco)
- **Objetivo**: Escala menor harmônica com 7ª maior para solos rápidos de arpejos diminutos e escalas neoclássicas.
- **Configuração do Harmonizador**:
  - `Key`: A (Lá)
  - `Scale`: `HARMONIC MINOR` (Inclui o Sol# característico)
  - `Voice 1 Interval`: `-3rd Diatonic Below` (Terça abaixo para peso extra)
  - `Voice Balance`: 60% Dry / 40% Wet
  - `Pitch Tracking Sensitivity`: Ultra-Fast (Otimizado para palhetada rápida staccato)
- **Ambiência**: Hall Reverb catedral de 2.5s.

---

## 5. Dicas de Ouro para Execução Perfeita com Harmonizador

1. **Toque Monofônico Limpo nas Passagens Harmonizadas**:
   - Para melodias de solo com harmonizador inteligente ativado, palhete uma nota de cada vez com clareza. Evite deixar cordas vizinhas soarem soltas (faça abafamento cuidadoso com a mão esquerda), pois notas simultâneas podem confundir o detector monofônico de pitch fundamental.
2. **Ajuste de Tonalidade Pré-Música**:
   - Configure a tônica (*Key*) e a escala da música no preset antes de iniciar a faixa no show. Você pode criar cenas dedicadas (Ex: Cena A para solo em E Menor, Cena B para solo em G Maior).
3. **Posicionamento Antes do Delay/Reverb**:
   - Posicione o bloco do Harmonizador **antes** dos blocos de delay e reverb. Harmonizar um sinal já cheio de repetições e caudas de reverb causará erros de rastreamento de pitch.
