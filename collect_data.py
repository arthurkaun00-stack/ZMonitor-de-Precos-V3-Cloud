from scraper import procurar_produtos
from database import salvar_produtos
from Telegrambot import telebot
from models import preco_erro, nome_erro, url_erro



def vereficar_produto(p):
    nome_produto, preco_produto, data_atual, url = procurar_produtos(p["url"], p["nome1"], p["nome2"], p["preco1"], p["preco2"])        

    while nome_produto == 'Nada encontrado' or preco_produto == 'Nada encontrado' or url == 'Nada encontrado':
        if url == 'Nada encontrado' or url == '':
            url = url_erro(url=p['url']).strip()
            print(url)
        if url != 'Nada encontrado' and url != '':
            if nome_produto == 'Nada encontrado':
                p["nome1"], p["nome2"] = nome_erro(p["nome1"], p["nome2"], url)
            if preco_produto == 'Nada encontrado':
                p["preco1"], p["preco2"] = preco_erro(p["preco1"], p["preco2"], url)

        nome_produto, preco_produto, data_atual, url = procurar_produtos(url, p["nome1"], p["nome2"], p["preco1"], p["preco2"])

    salvar_produtos(nome_produto, preco_produto ,data_atual)
    
    if preco_produto < p["menor"]:
        p["menor"] = preco_produto
        mensagem = (url, nome_produto, preco_produto ,data_atual)
        telebot(mensagem)