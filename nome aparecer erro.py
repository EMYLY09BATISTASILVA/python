nome = input("Digite um nome: ")
codigo = input("Digite um código pessoal: ")

 

while nome == codigo:
    print("Erro: O código não pode ser igual ao nome. Tente novamente.")
    codigo = input("Digite um código pessoal: ")

 

print("Nome:", nome)
print("Código pessoal:", codigo)
