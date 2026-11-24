# Guia de Roteamento, Dinâmica e Modelagem para Violão de 12 Cordas no UltraRig

Este documento estabelece as diretrizes de engenharia eletroacústica, compressão de transientes duplos, equalização corretiva e ambiência espacial para **Violão e Guitarra Acústica de 12 Cordas** (modelos estilo *Guild F-512, Taylor 856ce, Martin D12-28 e Takamine*) no firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

O violão de 12 cordas é um dos instrumentos mais majestosos e complexos da música acústica (*Folk, Rock Clássico dos anos 60/70 como The Byrds, Led Zeppelin, Pink Floyd, Genesis e MPB*). Suas quatro ordens mais graves são afinadas em oitavas paralelas (Mi, Lá, Ré, Sol) e as duas mais agudas em uníssono (Si e Mi). Quando amplificado por captadores piezoelétricos comuns de rastilho, o instrumento sofre com transientes percussivos dobrados, estridência metálica cortante e acúmulo de médios embolados.

---

## 1. A Física Eletroacústica do Violão de 12 Cordas

```
+-------------------------------------------------------------------------------+
|                       ESTRUTURA DE ORDENS DO VIOLÃO DE 12 CORDAS              |
|                                                                               |
|  Ordem 6 (Mi): Corda Fundamental (E2) + Corda Oitavada Fina (E3)              |
|  Ordem 5 (Lá): Corda Fundamental (A2) + Corda Oitavada Fina (A3)              |
|  Ordem 4 (Ré): Corda Fundamental (D3) + Corda Oitavada Fina (D4)              |
|  Ordem 3 (Sol):Corda Fundamental (G3) + Corda Oitavada Fina (G4)              |
|  Ordem 2 (Si): Corda Uníssono (B3)    + Corda Uníssono (B3)                   |
|  Ordem 1 (Mi): Corda Uníssono (E4)    + Corda Uníssono (E4)                   |
|                                                                               |
|  * O Fenômeno de Transiente Duplo: Cada palhetada atinge duas cordas com      |
|    micro-defasagem de milissegundos, gerando picos duplos no conversor A/D!   |
+-------------------------------------------------------------------------------+
```

### Principais Desafios de Processamento:
1. **O "Quack" Piezo Multiplicado:** As cordas oitavadas agudas possuem diâmetro muito fino sob tensão elevada (~250 a 300 libras no tampo), transferindo picos de estalo mecânico extremamente ásperos em **3.5 kHz a 6 kHz**.
2. **Acúmulo de Médios Graves (Mud Build-Up em 150–250 Hz):** A presença de 12 cordas vibrando simultaneamente gera um acúmulo de ressonância na madeira que rouba clareza e definição em acordes cheios.
3. **Conflito com Modulações Convencionais:** Adicionar pedais comuns de Chorus ou Flanger ao violão de 12 cordas frequentemente gera um som embolado e difuso, pois o instrumento já possui um efeito acústico natural de desafinação em micro-centésimos (*natural chorus*).

---

## 2. Ganho de Entrada e Proteção de Headroom

Como o choque da palheta atinge duas cordas em cada movimento:
- **Risco Iminente de Clipping Digital:** No painel web do UltraRig, configure o `Input Trim` com atenuação de **-4 dB a -8 dB**.
- O ataque de palhetada aberta mais forte em um acorde de Mi Maior (E) não deve ultrapassar **-3 dBFS**. Manter esse *headroom* evita que os transientes duplos das cordas oitavadas sofram corte digital achatado.

---

## 3. Compressão Óptica: O Segredo do "Jingle-Jangle"

Para obter a lendária sonoridade brilhante e uniforme de Roger McGuinn (*The Byrds*) e David Gilmour (*Pink Floyd*):
1. **Compressor Óptico / Studio VCA no Início da Cadeia:**
   - **Attack Time:** Lento a moderado (**20 ms a 35 ms**). Permite que o estalo natural do par de cordas passe, preservando o brilho percussivo inicial.
   - **Release Time:** Moderado a longo (**200 ms a 350 ms**). Nivela as cordas finas e as cordas grossas, fazendo com que o sustain de todas as 12 cordas decaia de forma uniforme.
   - **Ratio:** **3:1 a 4:1** com redução de ganho moderada (**3 dB a 5 dB**).
2. **Resultado Sonoro:** O violão soa encorpado, com harmônicos sustentados e equilíbrio dinâmico perfeito entre as notas graves e as cordas oitavadas.

---

## 4. Equalização Cirúrgica para 12 Cordas

```
+-------------------------------------------------------------------------------+
|                       CURVA DE EQUALIZAÇÃO CORRETIVA NO ULTRARIG              |
|                                                                               |
|  [ HPF 55 Hz ]      [ Notch 200 Hz ]       [ De-Quack 3.8 kHz ]  [ Air Shelf ]|
|  (Corta Rumble)     (Limpa Embolamento)    (Amortece Aspereza)   (10 kHz)     |
|  -18 dB/oct         -3.5 dB (Q=2.5)        -4.5 dB (Q=3.5)       +2.0 dB      |
+-------------------------------------------------------------------------------+
```

1. **Filtro Passa-Altas (HPF em 55 Hz):** Protege subwoofers contra batidas no tampo sem esvaziar o peso da sexta corda Mi grave (82 Hz).
2. **Limpeza de Cavidade (Corte em 180 Hz a 220 Hz):** Remove o som "abafado de caixa oca" que costuma mascarar a voz do violão.
3. **Neutralização do "Quack" de Oitavas (Corte em 3.8 kHz a 4.5 kHz):** Amortece o estalo metálico cortante das cordas oitavadas finas de aço.
4. **Realce de Ar Acústico (High-Shelf em 10 kHz a 12 kHz):** Aplica um ganho suave de **+2 dB** para restaurar a respiração e brilho nobre de estúdio.

---

## 5. Convolução de Acoustic Body IR (1024 Pontos)

O bloco de convolução de IR no UltraRig transforma o sinal elétrico e seco do captador piezo no timbre ressonante de um violão *Jumbo* de luthier:
- **Desative totalmente caixas elétricas (`CAB IR Bypass`).**
- Carregue uma resposta de impulso acústica de violão de grande volume (**Jumbo ou Dreadnought 1024 pontos** gravada com microfones condensadores Neumann KM184 ou Royer R-121).
- **Ajuste de Blend (Mix):** Configure entre **45% e 60% Wet**. Isso injeta o ar e a madeira maciça do instrumento acústico sem atrasar a resposta rítmica.

---

## 6. Arquitetura de 4 Cenas para Shows ao Vivo

```
+-------------------------------------------------------------------------------+
|             PRESET: "ACOUSTIC-12-STRING-PRO" (4 CENAS PROGRAMADAS)           |
|                                                                               |
|  [Scene A] JUMBO STUDIO NATURAL                                               |
|   - Body IR Jumbo (Mix 55%) + Compressor Óptico suave                         |
|   - EQ Corretivo ativado (HPF 55 Hz, Notch 200 Hz, De-Quack 3.8 kHz)          |
|   - Room Reverb curto e discreto (12% mix) para ambiência de sala             |
|   - Timbre equilibrado, encorpado e orgânico para ritmo e dedilhados          |
|                                                                               |
|  [Scene B] 60s JINGLE-JANGLE (The Byrds & Roger McGuinn)                      |
|   - Compressor com sustain aumentado (Attack 15ms, Release 350ms)             |
|   - Realce de presença em 2.8 kHz e agudos em 10 kHz                          |
|   - Som brilhante, estridente e percussivo que corta qualquer mixagem de rock |
|                                                                               |
|  [Scene C] WISH YOU WERE HERE (Pink Floyd & Led Zeppelin Acústico)            |
|   - Analog Tape Delay sincronizado (340ms, mix 20% com cauda quente)          |
|   - Plate Reverb aveludado e amplo (Decay 2.4s)                               |
|   - Espacialidade tridimensional profunda para intros acústicas lendárias     |
|                                                                               |
|  [Scene D] HIGH-STAGE ANTI-FEEDBACK (Modo Emergência Palco Alto)              |
|   - HPF elevado para 70 Hz + Duplo Notch ativo em 180 Hz e 2.2 kHz            |
|   - Limitador de pico atuando em -2 dBFS                                      |
|   - Imunidade total a retorno de bateria e monitores de chão                  |
+-------------------------------------------------------------------------------+
```

---

## 7. Solução de Problemas Comuns (Troubleshooting)

- **O som soa desafinado quando uso efeitos de modulação:**
  - *Causa:* O uso de chorus comum adiciona uma segunda camada de modulação LFO sobre o batimento acústico natural das 12 cordas.
  - *Solução:* Desative pedais de Chorus e Flanger. Utilize apenas **Stereo Detune microtonal (+/- 2 cents)** ou reverbs de placa estéreo para espacialização.
- **As cordas graves soam muito mais baixas do que as cordas oitavadas:**
  - *Causa:* Pressão desigual sobre o rastilho do piezo ou falta de compressão prévia.
  - *Solução:* Aumente a taxa de compressão no bloco óptico para **4:1** e verifique se o rastilho de osso está perfeitamente nivelado sobre o cristal piezoelétrico.
