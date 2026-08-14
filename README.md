<div align="center">

# 🛒 ZMonitorDePreço V2 (POO)

**Um monitor automático e inteligente de preços desenvolvido em Python com Orientação a Objetos.**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57.svg?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Telegram](https://img.shields.io/badge/Telegram-Bot_API-26A5E4.svg?style=for-the-badge&logo=telegram&logoColor=white)](https://core.telegram.org/bots/api)
[![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-blueviolet.svg?style=for-the-badge)](https://github.com/TomSchimansky/CustomTkinter)

*Receba alertas no Telegram em tempo real assim que seus produtos favoritos atingirem o menor preço!*

</div>

---

## 📌 Sobre o Projeto

O **ZMonitorDePreço** é uma aplicação completa para monitoramento contínuo de produtos em lojas online. O sistema raspa informações de preços, armazena o histórico em um banco de dados local SQLite e notifica o usuário via Telegram sempre que um novo menor preço for detectado.

A versão 2.0 foi reformulada utilizando **Programação Orientada a Objetos (POO)** na interface gráfica e conta com uma arquitetura modularizada para facilitar a manutenção e expansão.

---

## ✨ Funcionalidades

- 🔄 **Monitoramento Automatizado:** Checagem periódica dos preços cadastrados.
- 🎨 **Interface Gráfica em POO:** Telas interativas para cadastro, validação e busca com CustomTkinter.
- 📊 **Banco de Dados SQLite:** Armazenamento automático do histórico de preços.
- 📲 **Notificações no Telegram:** Alertas diretos no celular com suporte a mensagens formatadas.
- 🛠️ **Tratamento Dinâmico de Erros:** Telas de correção para URLs, nomes ou preços não encontrados.
- 🔒 **Segurança:** Configurações sensíveis (Tokens e Chat IDs) protegidas via `.env`.

---

## 📂 Estrutura do Projeto

```text
ZMonitorDePreço V2 com POO/
│
├── 📄 01_main.py         # Script principal e loop de execução
├── 🖥️ interface.py       # Classes da interface gráfica (CustomTkinter)
├── 🕵️ scraper.py         # Extração e raspagem de dados web (BeautifulSoup4)
├── 📊 collect_data.py    # Lógica de verificação e comparação de preços
├── 🗄️ database.py        # Gerenciamento do banco de dados SQLite3
├── 💬 Telegrambot.py     # Integração e envio de alertas via Telegram
├── 🔒 .env               # Variáveis de ambiente
├── 📋 requirements.txt   # Dependências do projeto
└── 📘 README.md          # Documentação do projeto
🛠️ Tecnologias Utilizadas
Linguagem: Python 3

Interface Gráfica: CustomTkinter

Web Scraping: Requests, BeautifulSoup4

Banco de Dados: SQLite3

Notificações: Telegram Bot API

Variáveis de Ambiente: python-dotenv

⚙️ Como Instalar e Executar
1. Clonar o repositório
Bash
git clone [https://github.com/arthurkaun00-stack/ZMonitorDePreco.git](https://github.com/arthurkaun00-stack/ZMonitorDePreco.git)
cd ZMonitorDePreco
2. Instalar dependências
Bash
pip install -r requirements.txt
3. Configurar variáveis de ambiente
Crie um arquivo .env na raiz do projeto com as suas credenciais do Telegram:

Snippet de código
TOKEN=SEU_TOKEN_DO_TELEGRAM
CHAT_ID=SEU_CHAT_ID
4. Executar a aplicação
Bash
python 01_main.py