# Guia Avançado de Calibração de Noise Gate com Detecção Sidechain no UltraRig

Este guia técnico aborda a física de atenuação de ruído, a topologia de chaveamento com detector lateral (*Sidechain / Key Input*) e a calibração de parâmetros no bloco de **Noise Gate** do firmware **UltraRig** (família M-VAVE Tank-G v1/v2, Tank-B e Black Box).

Em timbres modernos de alto ganho (*high-gain* metal, djent, solos com overdrives empilhados e amplificadores NAM valvulados), o uso convencional de um noise gate simples gera um dilema acústico: **ou o ruído de fundo permanece audível, ou as caudas dos solos são estranguladas abruptamente**. A detecção via *sidechain* resolve esse problema de forma definitiva.

---

## 1. O Dilema Clássico do Noise Gate em Rigs High-Gain

Em cadeias de guitarra com alto ganho, amplificadores valvulados e pedais de saturação aplicam entre **+40 dB e +65 dB de ganho**, comprimindo drasticamente a dinâmica natural do instrumento:

```
Posicionamento Convencional 1: Gate no Início da Cadeia (Pré-Drive)
Guitarra ---> [ Noise Gate ] ---> [ Overdrive ] ---> [ NAM High-Gain Amp ] ---> Saída
  * Problema: Silencia o ruído dos captadores, mas o chiado (hiss) gerado pelo pré-amp
              continua ruidoso no PA e nos fones!

Posicionamento Convencional 2: Gate no Fim da Cadeia / Loop de Efeitos (Pós-Amp)
Guitarra ---> [ Overdrive ] ---> [ NAM High-Gain Amp ] ---> [ Noise Gate ] ---> Saída
  * Problema: O pré-amp comprimiu tanto o sinal que a nota que está morrendo tem quase
              a mesma amplitude do chiado de fundo. O gate "gagueja" (chatter) e corta
              as notas com estalos abruptos.
```

---

## 2. A Arquitetura de Detecção Sidechain (4-Cable Digital Method)

Inspirado em pedais analógicos de referência como o *Boss NS-2* e o *ISP Decimator II G-String*, o UltraRig implementa uma rota de áudio desacoplada:

```
+-------------------------------------------------------------------------------+
|             TOPOLOGIA DE NOISE GATE COM SIDECHAIN NO ULTRARIG                 |
|                                                                               |
|   [ Sinal Limpo da Guitarra ] ----------------------------+ (Key / Detector)  |
|               | (Sinal de Áudio)                          |                   |
|               v                                           v                   |
|   [ Bloco Overdrive / Boost ]                    [ Detector de Envelope ]     |
|               |                                           |                   |
|               v                                           |                   |
|   [ Bloco NAM Amp (High Gain) ]                           | Curva VCA         |
|               |                                           | (Abre / Fecha)    |
|               v                                           v                   |
|   [ Atenuador do Gate (VCA) ] <---------------------------+                   |
|               |                                                               |
|               v                                                               |
|   [ Delays e Reverbs Espaciais ] ---> Saída de Áudio                          |
+-------------------------------------------------------------------------------+
```

### Como Funciona:
1. **Ouvido (Detector / Sidechain):** Fica posicionado logo na entrada digital (`Raw Input`), ouvindo a dinâmica 100% limpa e pura das cordas da guitarra antes de qualquer saturação.
2. **Ação (Atenuador VCA):** Fica posicionado imediatamente após o amplificador NAM de alto ganho (e antes dos delays/reverbs).
3. **Resultado Perfeito:** O detector percebe o decaimento linear e natural da vibração mecânica da corda. No momento em que você abafa as cordas com a mão, o detector fecha o atenuador instantaneamente, eliminando todo o chiado do pré-amp sem nunca engasgar o som!

---

## 3. Parâmetros Essenciais e Calibração Fina

### 3.1 Threshold (Limiar de Disparo)
- No modo *Sidechain Raw Input*, o limiar responde aos decibéis crus da guitarra.
- **Faixa típica:** Entre **-52 dBFS e -42 dBFS**.
- **Ajuste Prático:** Com o volume da guitarra aberto em 10 e as mãos apoiadas levemente nas cordas (sem tocar), suba o *Threshold* lentamente até que o chiado suma completamente. Em seguida, aumente mais **1.5 dB a 2.0 dB** para margem de segurança contra variações de rede elétrica.

### 3.2 Attack Time (Tempo de Abertura)
- O tempo necessário para o portão se abrir após a palheta atingir a corda.
- **Para Metal / Riffs Rápidos / Djent:** **0.5 ms a 1.5 ms**. Abertura imediata sem corte do clique transitório inicial.
- **Atenção:** Ataques menores que 0.2 ms sem filtro de passagem por zero (*zero-crossing*) podem produzir cliques digitais perceptíveis.

### 3.3 Hold Time (Tempo de Sustentação do Portão)
- O tempo que o gate permanece 100% aberto após o sinal cru cair abaixo do *Threshold*.
- **Valor Recomendado:** **15 ms a 35 ms**.
- **Função Crítica:** Evita o efeito "gaguejo" (*chattering*) durante notas abafadas com a palma da mão (*palm-mutes*), onde a amplitude oscila violentamente entre as batidas.

### 3.4 Release / Decay Time (Tempo de Fechamento)
- A velocidade com que o sinal é atenuado quando o portão decide fechar.
- **Para Metal Moderno e Riffs Estacatos:** **30 ms a 60 ms** (corte seco e preciso, pausas entre riffs com silêncio cirúrgico).
- **Para Solos, Rock Clássico e Blues:** **150 ms a 300 ms** (decaimento aveludado e musical, permitindo que a sustentação da nota se dissipe suavemente).

### 3.5 Sidechain Key Filter (Filtros de Detecção HPF / LPF)
O UltraRig permite filtrar o sinal que alimenta o circuito detector:
- **Key HPF (Filtro Passa-Altas do Detector):** Ajustado em **80 Hz a 100 Hz**. Evita que batidas percussivas da mão na ponte ou vibrações subgraves abram o gate acidentalmente.
- **Key LPF (Filtro Passa-Baixas do Detector):** Ajustado em **4 kHz a 5 kHz**. Impede que ruídos de alta frequência induzidos por iluminação de palco ou telas de computador enganem o detector.

---

## 4. Presets Práticos de Noise Gate no UltraRig

### Preset 1: "Djent & Modern Metal Tightness" (Riffs Estacatos Extremos)
- **Sidechain Source:** `Raw Input (Pre-Drive)`
- **Threshold:** -44 dBFS
- **Attack:** 0.8 ms
- **Hold:** 15 ms
- **Release:** 35 ms
- **Key HPF:** 90 Hz
- *Efeito no Áudio:* Silêncio absoluto milissegundos após cada parada de palheta; perfeito para sincronismo com bumbo de pedal duplo.

### Preset 2: "Singing High-Gain Lead" (Solos Fluidos com Sustentação)
- **Sidechain Source:** `Raw Input (Pre-Drive)`
- **Threshold:** -48 dBFS
- **Attack:** 1.2 ms
- **Hold:** 30 ms
- **Release:** 220 ms
- **Key HPF:** 70 Hz
- *Efeito no Áudio:* Sustentação infinita de notas com vibrato; quando as cordas são silenciadas, o chiado desaparece suavemente sem cortes bruscos.

### Preset 3: "Single-Coil 60-Hz Hum Defense" (Stratocaster / Telecaster Vintage)
- **Sidechain Source:** `Raw Input (Pre-Drive)`
- **Threshold:** -41 dBFS (levemente mais alto para vencer o zumbido de bobina simples)
- **Attack:** 1.0 ms
- **Hold:** 25 ms
- **Release:** 120 ms
- *Efeito no Áudio:* Elimina o ronco de 60 Hz em repouso sem matar o brilho característico dos captadores vintage.

---

## 5. Resolução de Problemas (Troubleshooting)

- **O som apresenta pequenos cliques ou "estalos" ao palhetar:**
  - *Causa:* O tempo de *Attack* está excessivamente rápido (< 0.3 ms) cortando a forma de onda fora do ponto zero.
  - *Solução:* Aumente o *Attack* para **0.8 ms ou 1.0 ms**.
- **As caudas dos bends e notas longas somem de repente:**
  - *Causa:* O *Threshold* está muito elevado ou o *Release* está curto demais.
  - *Solução:* Reduza o *Threshold* em 3 dB e aumente o *Release* para **180–250 ms**.
- **O gate reabre sozinho quando tiro a mão da ponte:**
  - *Causa:* Ruído elétrico estático do corpo ou captadores não blindados gerando picos que ultrapassam o limiar.
  - *Solução:* Ative o *Key HPF* em 100 Hz e verifique o aterramento da guitarra.
