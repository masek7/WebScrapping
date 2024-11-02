import pandas as pd
import os
from scrapper import captura_preco, captura_id, armazena_link
from datetime import date
from winotify import Notification, audio


def anota_preco():
    """Função que anota o preço recolhido pela captura_preco()"""

    #Cria variável que armazena a data do dia em que o script é executado, e depois a formata para o formato BR
    data = date.today()
    data_formatada = data.strftime('%d/%m/%Y')

    #Arquivo onde ficarão armazenados os preços e as datas
    arquivo = 'dados.csv'

    #Verifica se o arquivo já existe, e caso não exista, ele o cria.
    if os.path.exists(arquivo):
        global df
        df = pd.read_csv(arquivo)
    else:
        #Cria as colunas do dataframe
        df = pd.DataFrame(columns=['ID','Preco','Variacao', 'Data'])

    #Guarda o preço e o ID do produto, na variável preco_novo, para que toda vez que o script seja rodado, ele seja atualizado
    preco_novo = captura_preco()
    id_novo = captura_id()

    #adiciona o preço e a data ao dataframe criado, e o salva.
    df=df._append({'ID':id_novo,'Preco':preco_novo,'Data':data_formatada}, ignore_index = True)
    # calcula a variação do preço
    df['Variacao'] = df['Preco'].pct_change() * 100
    # substitui o valor NaN por um 0.
    df['Variacao'] = df['Variacao'].fillna(0)
    df.to_csv(arquivo, index=False)
    print(df)

def notify():
    """Configura Notificações"""

    #Faz a verificação dos valores
    last_price = df['Preco'].iloc[-1]
    last_but_one = df['Preco'].iloc[-2]
    atl_price = df['Preco'].min()

    print(atl_price)

    #configuração da notificação caso o preço SUBA
    notify_high = Notification(app_id="Monitorador de Preço",
                               title="O PREÇO DO PRODUTO SUBIU",
                               msg=f'O preço atual é:{last_price} reais',
                               duration="short")
    notify_high.set_audio(audio.Reminder, loop=False)
    notify_high.add_actions(label="Link para o produto",
                            launch=armazena_link())

    if last_price > last_but_one:
        notify_high.show()

    #configuração da notificação caso o preço CAIA
    notify_low = Notification(app_id="Monitorador de Preço",
                               title="O PREÇO DO PRODUTO CAIU",
                               msg=f'O preço atual é:{last_price} reais',
                               duration="short")
    notify_low.set_audio(audio.Reminder, loop=False)
    notify_low.add_actions(label="Link para o produto",
                            launch=armazena_link())

    if last_price < last_but_one:
        notify_low.show()

    #configuração da notificação do preço mais baixo de todos os tempos
    notify_atl = Notification(app_id="Monitorador de Preço",
                              title="O PREÇO DO PRODUTO CAIU",
                              msg=f'O preço atual é:{last_price} reais',
                              duration="short")
    notify_atl.set_audio(audio.Reminder, loop=False)
    notify_atl.add_actions(label="Link para o produto",
                           launch=armazena_link())

    if last_price > atl_price:
        notify_low.show()







anota_preco()
notify()