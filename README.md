# 🛒 ZMonitorDePreço V3 Cloud

Um monitor de preços automatizado desenvolvido em Python. O sistema realiza o *scraping* de produtos na web, salva o histórico em banco de dados **SQLite** e envia notificações diretas via **Telegram** quando detecta promoções ou alterações nos preços.

---

## 📌 Funcionalidades

- **Web Scraping Flexível:** Extração de nome e preço utilizando `BeautifulSoup4` e expressões regulares.
- **Notificações via Telegram:** Alertas instantâneos no seu telemóvel/dispositivo quando o preço baixa.
- **Banco de Dados SQLite:** Registo e armazenamento do histórico de preços monitorizados (`banco.db`).
- **Tratamento Interativo de Erros:** Prompt via terminal para correção imediata caso uma URL ou seletor mude.
- **Segurança:** Configuração de credenciais e tokens através de variáveis de ambiente (`.env`).

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Web Scraping:** `BeautifulSoup4`, `requests`, `re`
- **Banco de Dados:** `sqlite3`
- **Notificações:** API de Bots do Telegram
- **Gerenciamento de Ambiente:** `python-dotenv`

---

## 📁 Estrutura do Projeto

```text
ZMonitorDePreço V3 Cloud/
├── 01_main.py         # Arquivo principal e loop de execução
├── collect_data.py    # Lógica de verificação dos preços e alertas
├── database.py        # Conexão e queries com o banco de dados SQLite
├── models.py          # Painéis do terminal e tratamento de exceções
├── scraper.py         # Lógica de extração de dados HTML/CSS
├── Telegrambot.py     # Envio de mensagens via API do Telegram
├── .env               # Variáveis de ambiente (Chaves e Tokens)
└── banco.db           # Banco de dados (gerado automaticamente)
🚀 Como Configurar e Executar
1. Clonar o repositório e instalar as dependências
Bash
pip install requests beautifulsoup4 python-dotenv
2. Configurar o ficheiro .env
Crie um ficheiro chamado .env na raiz do projeto com as suas credenciais do Telegram:

Snippet de código
TOKEN=seu_token_aqui
CHAT_ID=seu_chat_id_aqui
3. Executar o projeto
Bash
python 01_main.py