import json

import pandas as pd

dados = pd.read_excel('tabela.xlsx')

dados.set_index('Produto', inplace=True)


input("Qual teste deseja salvar?")
teste = 'Área de Cultivo (mil hectares)'

dicionario = {}

for indice, linha in dados.iterrows():
    chave = indice
    valor = linha[teste]
    dicionario[chave] = valor

print(dicionario)

dados_json = json.dumps(dicionario)

print(dados_json)
