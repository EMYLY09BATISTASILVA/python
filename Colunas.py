import pandas as pd

dados = pd.read_excel('tabela.xlsx')

minha_coluna = []

for indice, linha in dados.iterrows():
    valor = linha['Área de Cultivo (mil hectares)']
    minha_coluna.append(valor)

# print(minha_coluna)

index = int(input(f"digite o numero do índice da lista:\n"))
print(minha_coluna[index])