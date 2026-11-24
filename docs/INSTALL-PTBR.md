# Guia de Instalação e Segurança do UltraRig (Português - Brasil)

Este guia foi elaborado para ajudar os usuários do **M-VAVE Tank-G (v1 e v2)**, **Tank-B** e marcas equivalentes (*rebrands* como **Ziron Station G / Station B**, **Lekato**, etc.) a instalar, configurar e atualizar o firmware alternativo **UltraRig** com total segurança.

---

> [!CAUTION]
> ### AVISO CRÍTICO: NUNCA FORMATE O DISCO NO WINDOWS
> Ao conectar o pedal em modo de gravação, o Windows poderá exibir uma caixa de diálogo alertando:
> **"Você precisa formatar o disco na unidade X: antes de poder usá-lo."**
> **CLIQUE SEMPRE EM CANCELAR!**
> Essa unidade de disco não é um pendrive comum; ela corresponde à memória flash do seu pedal. Clicar em "Formatar" corromperá as partições internas e inutilizará o aparelho.

---

## 1. Antes de Começar (Requisitos)

1. **Versão do Firmware de Fábrica:**
   - **Recomendado:** Versão **97** ou **98** (ou **99** exclusivamente no Tank-G v2).
   - Se seu pedal estiver na versão **96, 53 ou anterior**, você deve primeiro atualizá-lo para a 98 usando o utilitário oficial `M-UPGRADE` baixado em [m-vave.com/download](https://m-vave.com/download).
   - *Atenção:* O `M-UPGRADE` restaura os presets e IRs de fábrica. Faça o backup dos seus timbres antes no `M-EFCS`.
   - Pedais Tank-G v1 com firmware 99 ainda **não** são compatíveis com o instalador.

2. **Cabo e Conexão USB:**
   - Utilize um cabo USB que transmita **dados e energia** de boa qualidade.
   - Conecte o cabo diretamente em uma porta USB do computador (placa-mãe ou notebook). **Evite hubs USB não alimentados**.

3. **Softwares Conflitantes:**
   - Antes de abrir o instalador, feche completamente os programas:
     - `M-EFCS`
     - `M-UPGRADE`
     - DAWs (Reaper, Cubase, Ableton, FL Studio, etc.)
     - Qualquer programa que utilize a interface MIDI ou de áudio USB do pedal.

---

## 2. Passo a Passo da Instalação

### Passo 1: Baixar o pacote correto
Acesse a página de [Releases oficiais](../../releases/latest) e baixe o arquivo correspondente ao seu modelo:
- `UltraRig-<versao>-v2-win.zip`: Para Tank-G **v2** (Windows)
- `UltraRig-<versao>-v1-win.zip`: Para Tank-G **v1** (Windows)
- `UltraRig-<versao>-android.apk`: (Opcional) Aplicativo de controle para celular Android

> [!TIP]
> Não tem certeza se seu pedal é v1 ou v2? O próprio instalador detecta a versão da placa e impede a instalação se o arquivo baixado for incorreto.

### Passo 2: Extrair os arquivos
- Descompacte o arquivo `.zip` completamente em uma pasta no seu computador (por exemplo, na Área de Trabalho ou em Documentos).
- **Mantenha todos os arquivos da pasta juntos.** Não execute o instalador de dentro do arquivo compactado.

### Passo 3: Executar o Instalador
1. Ligue o pedal e conecte-o ao computador via cabo USB.
2. Abra o arquivo `UltraRig-Installer.exe`.
   - *Nota:* No modelo v1, clique com o botão direito e selecione **"Executar como Administrador"**.
3. Se o Windows exibir o alerta de formatação de disco, clique em **Cancelar**.
4. Clique no botão **"Install UltraRig"**.

### Passo 4: Backup Automático e Gravação
- O instalador realizará primeiramente uma cópia completa de segurança (backup) de toda a memória flash do pedal.
- Em seguida, gravará o novo firmware UltraRig e reiniciará o pedal automaticamente.
- **NÃO desconecte o cabo USB nem desligue o pedal** até que a janela confirme a mensagem de conclusão com sucesso.

---

## 3. Seu Arquivo de Backup (Muito Importante!)

Durante o processo, seu backup será salvo no seguinte diretório:
`Documentos\tankg_installer\backup_<data>`

> [!IMPORTANT]
> - Esse arquivo é o **único método** para restaurar seu pedal de volta ao firmware de fábrica original da M-VAVE.
> - Guarde essa pasta em um local seguro (por exemplo, no Google Drive ou em um pendrive).
> - **NUNCA compartilhe esse backup com outras pessoas nem anexe em issues do GitHub**, pois ele contém chaves e identificadores criptográficos exclusivos do seu aparelho.

---

## 4. Como Usar o Editor e Configurar os Timbres

Após a instalação, você pode editar todos os efeitos, capturas NAM e impulsos de caixa (IRs):

### Pelo Computador (Web Editor)
1. Abra a pasta do UltraRig descompactada.
2. Dê dois cliques em `web\index.html` para abrir no **Google Chrome** ou **Microsoft Edge** (navegadores com suporte a Web MIDI).
3. Na página que abrir, clique em **"Connect"** e selecione o pedal.

### Pelo Celular (Android)
1. Instale o arquivo `UltraRig-<versao>-android.apk` no seu smartphone Android.
2. Ative o Bluetooth e a Localização (necessária para emparelhamento BLE no Android).
3. Abra o aplicativo e conecte-se ao seu pedal sem fios.

---

## 5. Como Atualizar no Futuro

Para atualizar para uma nova versão do UltraRig:
1. Baixe o novo pacote na página de Releases.
2. Execute o `UltraRig-Installer.exe`.
3. Clique em **"Update UltraRig"**.
   - Seus presets, modelos de amplificadores NAM e IRs de caixa gravados no pedal serão **preservados intactos**.

---

## 6. Como Retornar ao Firmware de Fábrica

Se desejar remover o UltraRig e voltar para o sistema oficial:
1. Abra o `UltraRig-Installer.exe`.
2. Clique na opção **"Go back to the factory firmware"**.
3. O instalador usará o backup salvo em `Documentos\tankg_installer` para restaurar o estado original de fábrica.

---

## 7. Solução de Problemas (FAQ)

* **O antivírus acusou ameaça no executável:**
  * O instalador do UltraRig acessa a memória flash de baixo nível via comandos SCSI/USB brutos. Isso pode disparar falsos positivos em antivírus como o Windows Defender. Adicione uma exceção temporária para a pasta do instalador.
* **O pedal não foi reconhecido pelo instalador:**
  * Verifique se o cabo é realmente de dados (muitos cabos servem apenas para carregamento).
  * Certifique-se de que o programa oficial `M-EFCS` ou `M-UPGRADE` está fechado.
  * Tente mudar de porta USB (dê preferência para portas traseiras do PC).
* **O afinador não emite som em presets com NAM:**
  * Modelos de amplificador NAM e IRs de alta resolução utilizam bastante processamento. Na versão **Alpha 13.1**, o gerenciamento de recursos para o afinador foi aprimorado. Certifique-se de estar na versão mais recente.
