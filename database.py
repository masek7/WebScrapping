import pandas as pd
import os
from scrapper import captura_preco
from datetime import date


def anota_preco():
    """Função que anota o preço recolhido pela captura_preco()"""

    #Cria variável que armazena a data do dia em que o script é executado, e depois a formata para o formato BR
    data = date.today()
    dataFormatada = data.strftime('%d/%m/%Y')

    #Arquivo onde ficarão armazenados os preços e as datas
    arquivo = 'dados.csv'

    #Verifica se o arquivo já existe, e caso não exista, ele o cria.
    if os.path.exists(arquivo):
        df = pd.read_csv(arquivo)
    else:
        #Cria as colunas do dataframe
        df = pd.DataFrame(columns=['Preco', 'Data'])

    #Guarda o preço do produto, na variável preco_novo, para que toda vez que o script seja rodado, ele seja atualizado
    preco_novo = captura_preco()

    #adiciona o preço e a data ao dataframe criado, e o salva.
    df = df._append({'Preco':preco_novo,'Data':dataFormatada}, ignore_index = True)
    df.to_csv(arquivo, index=False)
    print(df)


anota_preco()