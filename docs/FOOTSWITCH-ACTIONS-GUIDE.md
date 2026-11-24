# Guia Avançado de Programação e Atribuição de Funções dos Footswitches Físicos no UltraRig

Este documento orienta sobre a programação, personalização de eventos e mapeamento de footswitches físicos nos dispositivos da família M-VAVE (**Tank-G v1/v2, Tank-B e Black Box**) executando o firmware **UltraRig**.

Enquanto o firmware original de fábrica impõe uma navegação rígida e predefinida (bancos fixos de presets ou modos "Live" limitados), o UltraRig oferece controle total sobre eventos de toque, modos de operação flexíveis e atribuição de ações por cena ou globais.

---

## 1. Arquitetura de Eventos dos Footswitches no UltraRig

Cada footswitch físico da pedaleira pode interceptar e responder a diferentes tipos de gestos mecânicos:

```
                  +----------------------------------------------+
                  |           EVENTO DE PRESSÃO MECÂNICA         |
                  +----------------------------------------------+
                                         |
                       +-----------------+-----------------+
                       |                                   |
             [ Toque Rápido (Tap) ]               [ Toque Mantido (Hold) ]
             (Duração < Hold Threshold)           (Duração >= Hold Threshold)
                       |                                   |
           Disparo: On Release ou Instant        Disparo: No limiar do tempo
                       |                                   |
          Ex: Alternar Cena / Bypass Bloco       Ex: Afinador / Tap Tempo
```

### 1.1 Tipos de Eventos Suportados

1. **Short Press (Tap):** Toque rápido convencional com liberação imediata.
2. **Long Press (Hold):** Manter o footswitch pressionado continuamente além do limiar configurado (ex: 500 ms).
3. **Double-Tap (Toque Duplo):** Dois toques rápidos consecutivos em uma janela de tempo definida (ex: 300 ms).
4. **Combination Press (Toque Simultâneo):** Pressionar simultaneamente dois footswitches adjacentes (ex: `FS A + FS B` ou `FS B + FS C`).

---

## 2. Modos de Operação dos Footswitches

O UltraRig permite configurar a interface física da pedaleira em quatro paradigmas operacionais principais:

| Modo de Operação | Comportamento Primário do Toque | Ideal Para |
| :--- | :--- | :--- |
| **Preset Navigation Mode** | Alterna entre os 32 presets da memória interna (Patch 1 a 32). | Repertórios com timbres completamente distintos por música. |
| **Scene Mode (Recomendado)** | Alterna entre as 4 Cenas (A, B, C, D) do preset ativo sem cortes de áudio. | Dinâmica de palco com transições suaves (Verso, Refrão, Solo). |
| **Stompbox / Live Mode** | Liga/desliga blocos de efeitos individuais (Drive, Mod, Delay, Reverb). | Músicos que operam a pedaleira como um pedalboard analógico tradicional. |
| **Hybrid Smart Mode** | Toque rápido comuta Cena; Toque longo ativa Boost/Solo ou Afinador. | Máxima versatilidade com número reduzido de footswitches. |

---

## 3. Calibração de Tempo e Latência de Acionamento (Timing & Debounce)

A percepção de responsividade de um pedal de efeitos é crítica durante apresentações ao vivo.

### 3.1 Limiar de Detecção de Toque Mantido (`Hold Threshold`)

- **Padrão de Fábrica no UltraRig:** `500 ms`
- **Ajuste Recomendado para Palco:**
  - `400 ms a 450 ms`: Ideal para guitarristas experientes que desejam acionamento ágil de funções secundárias (afinador, tap tempo).
  - `600 ms a 750 ms`: Recomendado para evitar disparos acidentais de *Hold* durante pisadas mais pesadas ou desajeitadas no palco.

### 3.2 Gatilho: `On Press` vs `On Release`

- **Ação `On Press` (No Pressionamento):** Ação imediata (latência mecânica zero). Disponível **apenas** quando o footswitch **não** possui uma ação secundária de *Hold* configurada.
- **Ação `On Release` (Na Liberação):** O UltraRig precisa aguardar até que o botão seja solto (para confirmar se o toque foi curto ou longo). Se você precisa de sincronismo rítmico perfeito em uma virada de compasso com acionamento de cena, configure o footswitch como ação única sem *Hold*, permitindo resposta instantânea `On Press`.

---

## 4. Ações Especiais de Utilidade

### 4.1 Tap-Tempo Dedicado e Compartilhado

- **Função:** Sincroniza o tempo de atraso de Delays e a frequência de Modulações (Tremolo, Phaser, Chorus).
- **Feedback Visual:** O anel ou indicador LED do footswitch passa a piscar no andamento exato (BPM) das batidas detectadas.
- **Dica de Programação:** Se não houver footswitch sobrando, atribua o *Tap-Tempo* ao evento de *Double-Tap* do footswitch do Delay.

### 4.2 Afinador Cromático com Silenciamento de Palco (Mute Tuner)

- Atribuir a ação de afinador ao evento **Long Press (Hold) por 800 ms** em qualquer footswitch.
- Ao entrar em modo afinador:
  - O sinal de saída de áudio principal é instantaneamente mutado (*Stage Silence*).
  - O display e os LEDs indicam a afinação com precisão estroboscópica de 0.1 centésimo.
  - Um toque simples em qualquer footswitch cancela o afinador e restaura o som original.

### 4.3 Navegação por Combinações (`Bank Up` / `Bank Down`)

Em pedaleiras compactas com 3 ou 4 footswitches:
- Pressionar **`FS A + FS B`** simultaneamente: `Bank Down / Preset Anterior`.
- Pressionar **`FS B + FS C`** (ou `FS C + FS D`): `Bank Up / Próximo Preset`.
- Essa configuração libera os toques individuais exclusivamente para controle de cenas e efeitos.

---

## 5. Exemplos de Mapeamento para Apresentações ao Vivo

### 5.1 Cenário 1: Tank-G (4 Footswitches) — Setup "Scene Master + Solo Boost"

Configuração definitiva para quem toca repertório variado com transições perfeitas:

```
+-------------------------------------------------------------------------------+
|                      TANK-G (4 FOOTSWITCHES): SCENE MASTER                    |
|                                                                               |
|  [ FS A ]              [ FS B ]              [ FS C ]            [ FS D ]     |
|  Tap: Scene A (Clean)  Tap: Scene B (Crunch) Tap: Scene C (Lead) Tap: Tap-Tem |
|  Hold: Mute            Hold: Rotary Fast     Hold: Solo +4dB     Hold: Tuner  |
+-------------------------------------------------------------------------------+
```

- **FS A:** Toque = Cena A (Limpo cristalino); Hold (1s) = Mudo Geral para trocar de guitarra.
- **FS B:** Toque = Cena B (Overdrive de base/ritmo); Hold = Acelera rotação do Chorus/Rotary.
- **FS C:** Toque = Cena C (Lead/Solo com delay estéreo); Hold = Boost pós-amp de +4 dB imediato.
- **FS D:** Toque sucessivo = Sincronismo de Tap-Tempo; Hold (600 ms) = Abre o Afinador Silencioso.

### 5.2 Cenário 2: Tank-B ou Tank-G (3 Footswitches Ativos) — Setup "Stompbox Clássico"

Para quem prefere a sensação de pedalboard tradicional com pedais soltos:

```
+-------------------------------------------------------------------------------+
|                       SETUP STOMPBOX TRADICIONAL (3 FS)                       |
|                                                                               |
|       [ FS 1 ]                     [ FS 2 ]                     [ FS 3 ]      |
|  Tap: Overdrive Bypass        Tap: Delay On/Off            Tap: Reverb Boost  |
|  Hold: Pré-Amp Crunch/Clean   Hold: Tap-Tempo              Hold: Afinador Mute|
+-------------------------------------------------------------------------------+
```

- **FS 1:** Liga/Desliga pedal de Overdrive/Booster. Hold comuta o canal do amplificador virtual.
- **FS 2:** Liga/Desliga Delay (com preservação de cauda/*spillover*). Hold entra em modo Tap-Tempo.
- **FS 3:** Toque adiciona Reverb longo de ambiência. Hold ativa o Afinador.

---

## 6. Configuração no Painel Web do UltraRig

Para personalizar as funções dos footswitches:
1. Abra o painel de controle do UltraRig no navegador (Chrome ou Edge) ou aplicativo Android.
2. Acesse a aba **`Footswitches / Controller Mapping`**.
3. Selecione o footswitch desejado (`FS 1` a `FS 4`).
4. Escolha o gatilho (`Tap`, `Hold`, `Double-Tap` ou `Combo`).
5. Defina a ação desejada:
   - `Scene: Select 1 / 2 / 3 / 4`
   - `Block Toggle: [Nome do Bloco DSP]`
   - `Utility: Tuner / Tap-Tempo / Master Mute`
   - `Preset: Next / Previous / Select Patch`
6. Clique em **`Save to Pedal`** para gravar a configuração na memória permanente do dispositivo.

---

## 7. Solução de Problemas Comuns (Troubleshooting)

- **Sensação de atraso ao trocar de cena com o footswitch:**
  - *Causa:* O footswitch possui uma ação de *Hold* configurada, forçando o firmware a esperar pelo término da janela de tempo.
  - *Solução:* Remova a ação de *Hold* atribuída àquele footswitch específico. A ação `Tap` passará a disparar instantaneamente `On Press`.
- **Disparo duplo acidental (Double-Triggering / Bouncing):**
  - *Causa:* Chave mecânica do footswitch com desgaste ou contato ruidoso.
  - *Solução:* No menu de configurações globais de hardware, aumente o `Debounce Filter` de 15 ms para 35 ms.
- **Toques simultâneos de combo não disparam com precisão:**
  - *Causa:* Pressionar os dois botões com descompasso superior a 50 ms.
  - *Solução:* Ajuste o parâmetro `Combo Detection Window` para 80–100 ms para tolerar pisadas levemente desalinhadas.
