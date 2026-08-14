class Cadastrar_produto:
    def __init__(self):
        print(f'{'Url Site':^100}')
        terabyte = input('Site Terabyte[S/N]?: ').upper()
        url   = input('Url: ')
        if terabyte == 'S':
            nome1, nome2, preco1, preco2 = 'h1', 'tit-prod', 'p', 'valVista'
        else:
            nome1 = input('Url Nome 1: ')
            nome2 = input('Url Nome 2: ')
            preco1 = input('Url Preço 1: ')
            preco2 = input('Url Preço 2: ')
        menor = 999
        self.Resposta = {
                    'menor': menor,
                    'url'  : url,
                    'nome1': nome1,
                    'nome2': nome2,
                    'preco1': preco1,
                    'preco2': preco2
                   }
    def iniciar(self):
        res = self.Resposta
        return res if res else False

#a = Cadastrar_produto()

class Quer_continuar:
    def __init__(self):
        self.Resposta = 0
        while self.Resposta not in ('S', 'N'):
            self.Resposta = input('Quer continuar?[S/N]: ').upper()
    def iniciar(self):
        return self.Resposta

#a = Quer_continuar()

class Painel_save:
    def __init__(self, nome, preco, data, url, http_ok):

        if http_ok == 200:
            print(f'''Produto: {nome}
Preço: {preco}
Data: {data}
Url: {url} 
                   ''')
        else:
            print(f'Houve um erro Http atual:{http_ok}')

class Erro:
    def __init__(self, v1='', v2='', url= '', tipo_erro = ''):
        self.tipo_erro = tipo_erro
        print(f'Houve algum ERRO no {tipo_erro} por favor atualize as informações abaixo!')
        if tipo_erro != 'URL':
            print(f'{'Informações passadas:':^100} \n\n{v1}\n{v2}\n')
            self.n1 = input(f'Novo {tipo_erro} 1: ')
            self.n2 = input(f'Novo {tipo_erro} 2: ')
        else:
            print(f'{'Informações passadas:':^80} \n\n{url}\n')
            self.nu = input(f'Novo {tipo_erro}')
        print(f'URL: {url}')

    def iniciar(self):
        if self.tipo_erro != 'URL':
            return self.n1, self.n2
        else:
            return self.nu
a = Erro()

def preco_erro(p1='', p2='', url=''):
    janela = Erro(v1=p1, v2=p2, url=url, tipo_erro='URL PREÇO')
    return janela.iniciar()

def nome_erro(n1='', n2='', url=''):
    janela = Erro(v1=n1, v2=n2, url=url, tipo_erro='URL NOME')
    return janela.iniciar()

def url_erro(n1='', n2='', url=''):
    janela =  Erro(v1=n1, v2=n2, url=url, tipo_erro='URL')
    return janela.iniciar()