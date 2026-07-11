import customtkinter as ctk
from time import sleep

def cadastrar_produto_com_interface():
    ctk.set_appearance_mode('dark')

    janela = ctk.CTk()
    janela.title('Interface')
    janela.geometry('400x450')

    titulo = ctk.CTkLabel(janela, text='Sistema de Monitoramento', font=('Roboto',15,'bold'))#,anchor="w")
    titulo.pack(pady=30)#pady=10 fill=10)

    '''Inserir Dados'''

    menor = 9999

    titulo = ctk.CTkLabel(
                        janela, 
                        text='Url Site:', 
                        font=('Roboto',10,'bold'),
                        text_color='snow',
                        wraplength=390,
                        justify="left"
                        )
    titulo.pack(padx=25,anchor='w')
    url = ctk.CTkEntry(janela, placeholder_text='Url_Site', width=350, height=10)
    url.pack(pady=10)

    titulo = ctk.CTkLabel(
                        janela, 
                        text='Url Nome 1:', 
                        font=('Roboto',10,'bold'),
                        text_color='snow',
                        wraplength=390,
                        justify="left"
                        )
    url_nome1 = ctk.CTkEntry(janela, placeholder_text='Url_Nome1', width=350, height=10)
    url_nome1.pack(pady=10)

    titulo = ctk.CTkLabel(
                        janela, 
                        text='Url Nome 2:', 
                        font=('Roboto',10,'bold'),
                        text_color='snow',
                        wraplength=390,
                        justify="left"
                        )
    url_nome2 = ctk.CTkEntry(janela, placeholder_text='Url_Nome2', width=350, height=10)
    url_nome2.pack(pady=10)

    titulo = ctk.CTkLabel(
                        janela, 
                        text='Url Preço 1:', 
                        font=('Roboto',10,'bold'),
                        text_color='snow',
                        wraplength=390,
                        justify="left"
                        )
    url_preco1 = ctk.CTkEntry(janela, placeholder_text='Url_Preço1', width=350, height=10)
    url_preco1.pack(pady=10)

    titulo = ctk.CTkLabel(
                        janela, 
                        text='Url Preço 2:', 
                        font=('Roboto',10,'bold'),
                        text_color='snow',
                        wraplength=390,
                        justify="left"
                        )
    url_preco2 = ctk.CTkEntry(janela, placeholder_text='Url_Preço2', width=350, height=10)
    url_preco2.pack(pady=10)

    '''Enviar Dados'''

    resultado = {}

    def enviar_dados():
        resultado.update ({
                'menor' :menor,
                'url'   :url.get(), 
                'nome1' :url_nome1.get(), 
                'nome2' :url_nome2.get(),
                'preco1':url_preco1.get(), 
                'preco2':url_preco2.get()
                })
        janela.destroy()

    butao = ctk.CTkButton(janela, text='Enviar Informaçoes',command=enviar_dados)
    butao.pack(pady=50)

    janela.mainloop()
    return resultado

def Quer_continuar():
    resposta = ''

    def clique_sim():
        nonlocal resposta
        resposta = 'S'
        janela.destroy()

    def clique_nao():
        nonlocal resposta
        resposta = 'N'
        janela.destroy()

    ctk.set_appearance_mode('dark')

    janela = ctk.CTk()
    janela.title('Interface')
    janela.geometry('400x450')

    titulo = ctk.CTkLabel(janela, text='Quer continuar?', font=('Roboto',30,'bold'))
    titulo.pack(pady=100)

    butao = ctk.CTkButton(
        janela, 
        text='Sim', 
        command=clique_sim,
        fg_color='green',       
        hover_color='darkgreen' 
    )
    butao.pack(pady=10)

    butao = ctk.CTkButton(
        janela, 
        text='Não', 
        command=clique_nao,
        fg_color='red',       
        hover_color='darkred' 
    )
    butao.pack(pady=10)

    janela.mainloop()
    return resposta

def painel_salve(nome,preco,data,url,reposta):
    ctk.set_appearance_mode('dark')

    janela = ctk.CTk()
    janela.title('Interface')
    janela.geometry('700x600')

    titulo = ctk.CTkLabel(
        janela, 
        text='''
    ║                      ╔═════════════════════════╗
    ═════════════════╝                             
    ║    🔥🔥🔥🔥 O Preço Baixo 🔥🔥🔥🔥      ║
                            ╔══════════════════
    ╚════════════════════════╝                  ║
    ''', 
        font=('Roboto', 23, 'bold'),
        text_color='lime'
    )
    titulo.pack(pady=20)

    titulo = ctk.CTkLabel(
        janela, 
        text=f'''
    Produto:
    {nome}

    Preço: {preco}

    Data: {data}
    Url: {url}''', 
        font=('Roboto', 15, 'bold'),
        text_color='gray',
        justify="left",
        wraplength=360
    )
    titulo.pack(pady=10,padx=10,anchor='w')

    if reposta == 200:
        titulo = ctk.CTkLabel(janela, text='A uma mesagem no seu Telegram!',text_color='darkgreen')
        titulo.pack(pady=20)
    else:
        titulo = ctk.CTkLabel(janela, text='Houve um erro ao tentar enviar uma mesagem no seu Telegram!',text_color='darkred')
        titulo.pack(pady=20)
        print(reposta)

    '''Fechar Janela'''
    def fechar_janela():
        janela.destroy()

    butao = ctk.CTkButton(janela, text='Fechar', command=fechar_janela,fg_color='green',hover_color="darkgreen", width=150, height=50)
    butao.pack(pady=0)

    janela.after(30000,janela.destroy)

    janela.mainloop()

def interface_erro_preco(p1='Nada encontrado',p2='Nada encontrado',url='Nada encontrado'):
    ctk.set_appearance_mode('dark')

    janela = ctk.CTk()
    janela.title('Interface')
    janela.geometry('400x420')

    '' '--- Titulo --- '''

    titulo = ctk.CTkLabel(
                        janela, 
                        text='Houve algum ERRO no "URL PREÇO" por favor atualize as informações abaixo!', 
                        font=('Roboto',19,'bold'),
                        text_color='red',
                        wraplength=390
                        )
    titulo.pack(pady=20)

    '''Informações passadas'''

    titulo = ctk.CTkLabel(janela, text='Informações passadas',text_color='snow')
    titulo.pack(pady=0)
    titulo = ctk.CTkLabel(
                        janela, 
                        text=p1, 
                        font=('Roboto',10,'bold'),
                        text_color='snow',
                        wraplength=390,
                        justify="left"
                        )
    titulo.pack(padx=25,anchor='w')

    titulo = ctk.CTkLabel(
                        janela, 
                        text=p2, 
                        font=('Roboto',10,'bold'),
                        text_color='snow',
                        wraplength=390,
                        justify="left"
                        )
    titulo.pack(padx=25,anchor='w')

    '''Transfirir informações'''

    titulo = ctk.CTkLabel(
                        janela, 
                        text='Novo Url Preço 1:', 
                        font=('Roboto',10,'bold'),
                        text_color='snow',
                        wraplength=390,
                        justify="left"
                        )
    titulo.pack(padx=25,anchor='w')
    novo_url_preco1 = ctk.CTkEntry(janela, placeholder_text='Novo_Url_preço1', width=350, height=10)
    novo_url_preco1.pack(pady=0)

    titulo = ctk.CTkLabel(
                        janela, 
                        text='Novo Url Preço 2:', 
                        font=('Roboto',10,'bold'),
                        text_color='snow',
                        wraplength=390,
                        justify="left"
                        )
    titulo.pack(padx=25,anchor='w')
    novo_url_preco2 = ctk.CTkEntry(janela, placeholder_text='Novo_Url_preço2', width=350, height=10)
    novo_url_preco2.pack(pady=0)

    '''Enviar Dados'''

    resultado = []

    def enviar_dados():
        resultado.append(novo_url_preco1.get())
        resultado.append(novo_url_preco2.get())
        janela.destroy()
    butao = ctk.CTkButton(janela, text='Enviar Informaçoes Atualizadas',command=enviar_dados)
    butao.pack(pady=30)

    '''Copiar URL do Produto'''

    def copiar_URL():
        janela.clipboard_clear()
        janela.clipboard_append(url)

    butao = ctk.CTkButton(janela, text='Copiar URL', command=copiar_URL,fg_color='green',hover_color="darkgreen", width=50, height=10)
    butao.pack(pady=0)

    janela.mainloop()
    return resultado

def interface_erro_nome(p1='Nada encontrado',p2='Nada encontrado',url='Nada encontrado'):
    ctk.set_appearance_mode('dark')

    janela = ctk.CTk()
    janela.title('Interface')
    janela.geometry('400x420')

    '' '--- Titulo --- '''

    titulo = ctk.CTkLabel(
                        janela, 
                        text='Houve algum ERRO no "URL NOME" por favor atualize as informações abaixo!', 
                        font=('Roboto',19,'bold'),
                        text_color='red',
                        wraplength=390
                        )
    titulo.pack(pady=20)

    '''Informações passadas'''

    titulo = ctk.CTkLabel(janela, text='Informações passadas',text_color='snow')
    titulo.pack(pady=0)
    titulo = ctk.CTkLabel(
                        janela, 
                        text=p1, 
                        font=('Roboto',10,'bold'),
                        text_color='snow',
                        wraplength=390,
                        justify="left"
                        )
    titulo.pack(padx=25,anchor='w')
    
    titulo = ctk.CTkLabel(
                        janela, 
                        text=p2, 
                        font=('Roboto',10,'bold'),
                        text_color='snow',
                        wraplength=390,
                        justify="left"
                        )
    titulo.pack(padx=25,anchor='w')

    '''Transfirir informações'''

    titulo = ctk.CTkLabel(
                        janela, 
                        text='Novo Url Nome 1:', 
                        font=('Roboto',10,'bold'),
                        text_color='snow',
                        wraplength=390,
                        justify="left"
                        )
    titulo.pack(padx=25,anchor='w')
    novo_url_nome1 = ctk.CTkEntry(janela, placeholder_text='Novo_Url_nome1', width=350, height=10)
    novo_url_nome1.pack(pady=0)

    titulo = ctk.CTkLabel(
                        janela, 
                        text='Novo Url Nome 2:', 
                        font=('Roboto',10,'bold'),
                        text_color='snow',
                        wraplength=390,
                        justify="left"
                        )
    titulo.pack(padx=25,anchor='w')
    novo_url_nome2 = ctk.CTkEntry(janela, placeholder_text='Novo_Url_nome2', width=350, height=10)
    novo_url_nome2.pack(pady=0)

    '''Enviar Dados'''

    resultado = []

    def enviar_dados():
        resultado.append(novo_url_nome1.get())
        resultado.append(novo_url_nome2.get())
        janela.destroy()
    butao = ctk.CTkButton(janela, text='Enviar Informaçoes Atualizadas',command=enviar_dados)
    butao.pack(pady=30)

    '''Copiar URL do Produto'''

    def copiar_URL():
        janela.clipboard_clear()
        janela.clipboard_append(url)

    butao = ctk.CTkButton(janela, text='Copiar URL', command=copiar_URL,fg_color='green',hover_color="darkgreen", width=50, height=10)
    butao.pack(pady=0)

    janela.mainloop()
    return resultado

def interface_erro_url(url='Nada encontrado'):

    ctk.set_appearance_mode('dark')

    janela = ctk.CTk()
    janela.title('Interface')
    janela.geometry('400x330')

    '' '--- Titulo --- '''

    titulo = ctk.CTkLabel(
                        janela, 
                        text='Houve algum ERRO no "URL" por favor atualize as informações abaixo!', 
                        font=('Roboto',19,'bold'),
                        text_color='red',
                        wraplength=390
                        )
    titulo.pack(pady=20)

    '''Informações passadas'''

    titulo = ctk.CTkLabel(janela, text='Informações passadas',text_color='snow')
    titulo.pack(pady=0)
    titulo = ctk.CTkLabel(
                        janela, 
                        text=url, 
                        font=('Roboto',10,'bold'),
                        text_color='snow',
                        wraplength=390,
                        justify="left"
                        )
    titulo.pack(padx=25,anchor='w')

    '''Transfirir informações'''

    titulo = ctk.CTkLabel(
                        janela, 
                        text='URL:', 
                        font=('Roboto',10,'bold'),
                        text_color='snow',
                        wraplength=390,
                        justify="left"
                        )
    titulo.pack(padx=25,anchor='w')
    novo_url = ctk.CTkEntry(janela, placeholder_text='URL', width=350, height=10)
    novo_url.pack(pady=0)
    
    '''Enviar Dados'''

    reposta = ''

    def enviar_dados():
        nonlocal reposta
        reposta = novo_url.get().strip()
        janela.destroy()
    butao = ctk.CTkButton(janela, text='Enviar Informações Atualizadas',command=enviar_dados)
    butao.pack(pady=30)

    '''Copiar URL do Produto'''

    def copiar_URL():
        janela.clipboard_clear()
        janela.clipboard_append(url)

    butao = ctk.CTkButton(janela, text='Copiar URL', command=copiar_URL,fg_color='green',hover_color="darkgreen", width=50, height=10)
    butao.pack(pady=0)

    janela.mainloop()
    return reposta
