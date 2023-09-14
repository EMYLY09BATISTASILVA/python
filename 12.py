numero = int(input("Digite um número para treinar a tabuada: "))
acertos = 0
erros = 0

 

for multiplicador in range(1, 11):
    resposta = int(input(f"Quanto é {numero} x {multiplicador}? "))
    resultado_correto = numero * multiplicador

 

    if resposta == resultado_correto:
        print("CORRETO")
        acertos += 1
    else:
        print(f"QUE PENA, VOCÊ ERROU. O VALOR CORRETO É {resultado_correto}")
        erros += 1

 

print("Total de acertos:", acertos)
print("Total de erros:", erros)
