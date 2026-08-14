from database import criar_banco_de_dados
from time import sleep
from models import Cadastrar_produto, Quer_continuar
from collect_data import vereficar_produto

def main():
    criar_banco_de_dados('banco')
    lista = []

    while True:
        produtos = Cadastrar_produto().iniciar()
        if produtos == False:
            break
        lista.append(produtos)
        res = Quer_continuar().iniciar()
        if res:
            break

    if produtos:
        while True:
            for prod in lista:
                vereficar_produto(prod)
            sleep(86)
if __name__ == '__main__':
    main()