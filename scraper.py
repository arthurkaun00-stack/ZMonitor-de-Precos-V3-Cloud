from datetime import datetime
import requests
from bs4 import BeautifulSoup
import re

def procurar_produtos(url,nome1_url,nome2_url,preco1_url,preco2_url):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    try:
        resposta = requests.get(url, headers=headers, timeout = 10)
        
        if resposta.status_code == 200:
            soup = BeautifulSoup(resposta.text, 'html.parser')

            '''NOME'''

            nome_tag = soup.find(nome1_url, class_=nome2_url)
            nome_produto = nome_tag.text.strip() if nome_tag else 'Nada encontrado'

            '''PREÇO'''

            preco_tag = soup.find(preco1_url, class_=preco2_url)
            preco_produto = preco_tag.text.strip() if preco_tag else 'Nada encontrado'

            '''Trasformado Texto em Real'''

            if preco_produto != 'Nada encontrado':
                preco_produto = preco_produto.replace('.', '').replace(',', '.')
                preco_produto = float(re.sub(r'[^0-9.]','', preco_produto))
                

            data_atual = datetime.now().strftime('%d/%m/%y')

            return nome_produto,preco_produto,data_atual,url

            
    except requests.exceptions.RequestException as e:
        print(f'ERRO de conexao: {e}')
        return 'Nada encontrado', 'Nada encontrado', datetime.now().strftime('%d/%m/%y'), 'Nada encontrado'
    
    except Exception as e:
        print(f'Erro no codigo: {e}')
        return 'Nada encontrado', 'Nada encontrado', datetime.now().strftime('%d/%m/%y'), 'Nada encontrado'