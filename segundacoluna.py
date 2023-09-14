import pandas as pd

dados = pd.read_excel('tabela.xlsx')

dados.set_index(keys="Produto", inplace=True)

num_teste = input("qual teste deseja salvar?")
teste = 'teste' + num_teste


coluna_teste1 = tuple(dados[teste])

print(coluna_teste1)