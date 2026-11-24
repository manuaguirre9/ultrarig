# Guia de Diagnóstico, Otimização de Buffers e Prevenção de Latência USB Audio no UltraRig

Este documento estabelece os padrões técnicos de calibração de buffers, cálculo de latência de ida e volta (*Round-Trip Latency - RTL*), mitigação de picos de DPC no sistema operacional e configuração de monitoração com latência zero para gravação e performances ao vivo utilizando as pedaleiras M-VAVE (**Tank-G v1/v2, Tank-B e Black Box**) executando o firmware **UltraRig** como interface de áudio USB 24-bit / 48 kHz.

---

## 1. Latência do Hardware (Standalone) vs. Latência USB (DAW Round-Trip)

É fundamental diferenciar o tempo que o áudio leva para ser processado internamente na pedaleira daquele decorrente da passagem pelo computador:

```
+-------------------------------------------------------------------------------+
|                       COMPARAÇÃO DE CAMINHOS DE LATÊNCIA                      |
|                                                                               |
|  1. MONITORAMENTO DIRETO NO HARDWARE (STANDALONE / PALCO):                    |
|  Guitarra ---> [ ADC 24-bit ] ---> [ DSP UltraRig ] ---> [ DAC ] ---> Fone/PA |
|                (0.8 ms)            (1.5 ms)              (0.8 ms)             |
|                * LATÊNCIA TOTAL: ~3.1 ms (Imperceptível ao ouvido humano!)    |
|                                                                               |
|  2. MONITORAMENTO VIA SOFTWARE NO COMPUTADOR (DAW ROUND-TRIP):                |
|  Guitarra ---> [ UltraRig ] ---> Cabo USB ---> [ Buffer Entrada DAW ]         |
|                                                       |                       |
|                                           [ CPU / Plugins VST ]               |
|                                                       |                       |
|  Fone <------- [ UltraRig ] <--- Cabo USB <--- [ Buffer Saída DAW ]           |
|                * LATÊNCIA TOTAL: 8.5 ms a 25.0 ms (Sensação de tocar atrasado)|
+-------------------------------------------------------------------------------+
```

- **Limiar Auditivo Crítico:** O cérebro humano começa a perceber atraso como um incômodo físico ou "som oco" (*comb filtering*) a partir de **7 ms a 10 ms**. Em 15 ms, palhetadas rápidas parecem desacopladas dos dedos.

---

## 2. A Fórmula dos Buffers: Tamanho em Amostras vs. Estabilidade

No áudio digital operando a **48 kHz** (48.000 amostras por segundo), o tamanho do buffer define quantos dados a CPU do computador processa em cada ciclo antes de enviar para os conversores:

$$\text{Latência Unidirecional (ms)} = \left( \frac{\text{Tamanho do Buffer (amostras)}}{\text{Taxa de Amostragem (48.000 Hz)}} \right) \times 1000$$

A Latência Total de Ida e Volta (*Round-Trip Latency - RTL*) soma o buffer de entrada, o buffer de saída e o overhead de comunicação do barramento USB (*Safety Margin*):

| Tamanho do Buffer | Latência de Áudio Pura (Ida e Volta) | Latência RTL Típica com Overhead USB | Estabilidade e Carga na CPU | Uso Recomendado |
| :---: | :---: | :---: | :--- | :--- |
| **32 amostras** | 1.33 ms | ~3.8 ms a 4.5 ms | **Extrema carga de CPU.** Risco de cliques (*dropouts*). | Apenas computadores topo de linha dedicados. |
| **64 amostras** | 2.66 ms | ~5.8 ms a 6.8 ms | **Carga moderada/alta.** Resposta muito ágil. | Gravação de solos velozes e palhetadas rápidas. |
| **128 amostras** | 5.33 ms | ~8.5 ms a 9.5 ms | **Equilíbrio ideal (Ponto Ideal).** Alta estabilidade. | **Padrão recomendado para shows e ensaios.** |
| **256 amostras** | 10.66 ms | ~14.0 ms a 15.5 ms | **Baixa carga de CPU.** Seguro para notebooks antigos. | Tracking com monitoramento direto do pedal. |
| **512+ amostras** | 21.33 ms+ | 25.0 ms a 45.0 ms | **Carga mínima de CPU.** Inviável para tocar ao vivo. | Mixagem e Masterização com dezenas de plugins. |

---

## 3. Ecossistema de Drivers por Sistema Operacional

### 3.1 Windows (ASIO Obrigatório)
- **O Erro Comum:** Utilizar drivers genéricos do Windows (*DirectSound, MME ou WASAPI compartilhado*). O mixer do Windows introduz reamostragem interna e adiciona de 30 ms a 60 ms de latência imprevisível.
- **A Solução:** Use sempre drivers com arquitetura **ASIO (Audio Stream Input/Output)**, que comunicam a DAW diretamente com a porta USB do hardware sem passar pelo sistema operacional:
  - Utilize o driver ASIO dedicado de baixa latência do fabricante ou o *ASIO4ALL v2 / FL Studio ASIO*.
  - No painel da DAW (Reaper, Cubase, Ableton, FL Studio), selecione `Driver Type: ASIO` e configure o buffer para **128 amostras**.

### 3.2 macOS (CoreAudio Nativo)
- O hardware M-VAVE é compatível com a norma **UAC2 (USB Audio Class 2.0)** sem necessidade de instalação de drivers manuais.
- O subsistema *CoreAudio* da Apple opera com latência nativa ultrabaixa e jitter mínimo. Basta conectar o cabo USB e selecionar o hardware no menu de áudio da DAW.

### 3.3 Linux (ALSA / JACK / PipeWire)
- Reconhecido nativamente como interface de áudio ALSA classe 2. Para baixa latência em distros de áudio (*Ubuntu Studio, Arch*), utilize o servidor *PipeWire* ou *JACK* configurado com períodos de 2 ou 3 e buffer de 128 amostras.

---

## 4. Diagnóstico de Cliques, Estalos e Buffer Underruns (DPC Latency)

Se você ouvir pequenos estalos secos (*pops / clicks*) ou engasgos intermitentes no áudio mesmo com o uso de CPU abaixo de 30%:
- **A Causa Principal (DPC Latency no Windows):** *Deferred Procedure Calls* são interrupções prioritárias do sistema operacional. Se o driver da placa Wi-Fi (`ndis.sys`), drivers gráficos da GPU (*Nvidia/AMD*) ou esquemas de economia de bateria de notebooks demorarem mais de 1 milissegundo para responder, a CPU do computador perde o prazo de entregar o bloco de áudio a tempo (*Buffer Underrun*).
- **Como Diagnosticar:** Baixe e execute o utilitário gratuito **Latencymon** (*Resplendence*). Ele identificará qual driver de dispositivo está causando picos de latência no sistema.

### 4.1 Otimizações Críticas para Windows em Gravação ao Vivo:
1. **Desative o Wi-Fi e Bluetooth do Computador:** A varredura constante de redes sem fio é a principal causadora de estalos em notebooks no palco.
2. **Plano de Energia de Alto Desempenho:** Configure o Windows em `Desempenho Máximo (High Performance)` para impedir que o processador reduza o clock dinâmico durante a execução musical.
3. **Porta USB Direta (Sem Hubs):** Conecte a pedaleira diretamente a uma porta USB traseira da placa-mãe (ou porta dedicada do notebook). **Nunca utilize hubs USB não alimentados**, pois a largura de banda é dividida com mouses, teclados e discos rígidos externos.

---

## 5. A Regra de Ouro: Monitoração Direta de Latência Zero (Direct Monitoring)

A maneira mais profissional e confiável de gravar guitarras e baixos no estúdio sem nenhum tipo de atraso nos ouvidos é utilizar a **Monitoração Direta do Hardware**:

```
+-------------------------------------------------------------------------------+
|         MONITORAÇÃO DIRETA COM LATÊNCIA ZERO NO ULTRARIG                      |
|                                                                               |
|  [ Fones P2 / IEM ] <----- Sinal do Pedal em Tempo Real (3.0 ms) <-----+       |
|                                                                        |       |
|  Guitarra ---> [ Hardware UltraRig com Efeitos / IR ] -----------------+       |
|                             |                                                  |
|                             v (Cabo USB)                                       |
|                    [ DAW de Gravação ]                                         |
|                    * MONITORING: OFF (Mudo o canal armado na DAW!)            |
|                    * Ouça apenas o playback das faixas antigas da bateria     |
+-------------------------------------------------------------------------------+
```

- **Por que isso é Superior:** Você ouve o seu timbre completo (com amplificador NAM, efeitos e gabinete IR) diretamente pelo circuito analógico da pedaleira com latência de **apenas 3.0 ms**.
- **A Armadilha do Eco (Comb Filtering):** Certifique-se de **desativar o monitoramento de software na pista armada da DAW (`Record Monitor: OFF`)**. Se deixar ambos ligados, você ouvirá o sinal direto e o sinal atrasado do computador simultaneamente, soando como um eco oco com perda total de graves.

---

## 6. Checklist Rápido Pré-Gravação (Pre-Session Checklist)

- [ ] **Taxa de Amostragem Casada:** DAW e driver do UltraRig configurados ambos em **48.000 Hz (48 kHz) / 24-bit**.
- [ ] **Tamanho do Buffer:** Ajustado para **128 amostras** para gravação ou **64 amostras** para execuções ultrarrápidas.
- [ ] **Cabo USB Direto:** Conectado diretamente a uma porta USB sem extensões longas ou hubs compartilhados.
- [ ] **Wi-Fi e Antivírus em Pausa:** Recursos em segundo plano desativados durante a gravação ao vivo.
- [ ] **Direct Monitoring Ativado:** Monitoramento de software da DAW mutado na pista de gravação para latência zero nos fones.
