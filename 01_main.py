from collect_data import criartabela, vereficar_produto, sleep, cadastrar_produto_com_interface, Quer_continuar, system

criartabela()
lista = []
a = 0

while True:
    produto = cadastrar_produto_com_interface()
    if not produto:
        a = 1
        break
        
    lista.append(produto)
    res = Quer_continuar()
    if res == "N":
        break
system('cls')
if a == 0:
    while True:
        for prod in lista:
            vereficar_produto(prod)
        system('cls')
        sleep(86400)   