from os import system
from scraper import procurar_produtos
from database import salvar_produtos,criartabela
from time import sleep
from Telegrambot import telebot
from interface import cadastrar_produto_com_interface,Quer_continuar,painel_salve,interface_erro_preco,interface_erro_nome,interface_erro_url

def vereficar_produto(p):

    #adicionar uma proteçao de url na pasta scraper

    nome_produto, preco_produto ,data_atual,url = procurar_produtos(p["url"], p["nome1"], p["nome2"], p["preco1"], p["preco2"])        

    while nome_produto == 'Nada encontrado' or preco_produto == 'Nada encontrado' or url == 'Nada encontrado':
        if url == 'Nada encontrado' or url == '':
            url = interface_erro_url(p['url']).strip()
            print(url)
        if url != 'Nada encontrado' and url != '':
            if nome_produto == 'Nada encontrado':
                p["nome1"], p["nome2"] = interface_erro_nome(p["nome1"], p["nome2"], url)
            if preco_produto == 'Nada encontrado':
                p["preco1"], p["preco2"] = interface_erro_preco(p["preco1"], p["preco2"], url)

        nome_produto, preco_produto ,data_atual,url = procurar_produtos(url, p["nome1"], p["nome2"], p["preco1"], p["preco2"])

    salvar_produtos(nome_produto, preco_produto ,data_atual)
    
    if preco_produto < p["menor"]:
        p["menor"] = preco_produto
        mensagem = (url, nome_produto, preco_produto ,data_atual)
        telebot(mensagem)
    system('cls')