import sqlite3

def criar_banco_de_dados(nome='banco'):
    conexao = sqlite3.connect(f'{nome}.db')
    cursor = conexao.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS monitoramento_produto (
                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                   produto TEXT NOT NULL,
                   preco FLOAT NOT NULL,
                   data TEXT NOT NULL
                   )''')
    conexao.commit()
    conexao.close()
 
def salvar_produtos(nome_produto,preco_produto,data_produto,nome='banco'):
    conexao = sqlite3.connect(f'{nome}.db')
    cursor = conexao.cursor()

    commando = '''INSERT INTO monitoramento_produto
                  (produto,preco,data) VALUES
                  (?,?,?)'''
    dados = (nome_produto,preco_produto,data_produto)
    cursor.execute(commando, dados)

    conexao.commit()
    conexao.close()