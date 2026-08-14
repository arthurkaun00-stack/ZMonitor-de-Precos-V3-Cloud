from models import Painel_save
import requests
from dotenv import load_dotenv
import os

def telebot(mensagem):
    url ,nome ,preco, data = mensagem
    texto_mensagem = f'''
Preço Baixo 🔥

Produto: {nome}

Preço: {preco}
Data: {data}
Url: {url}'''
    
    '''Adicionando Senhas'''

    load_dotenv()
    
    TOKEN = os.getenv("TOKEN")
    CHAT_ID = os.getenv("CHAT_ID")

    url_telegram = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    dados = {"chat_id": CHAT_ID, "text": texto_mensagem}

    '''Indo ate o Telegram'''

    res = requests.post(url_telegram, json=dados)
    status = res.status_code

    Painel_save(nome, preco, data, url, status).iniciar()