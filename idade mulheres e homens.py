num = str(input(f"digite um numero 1: "))
maior = num
menor = num
soma = 0
i = 1
for i in range(9):
    num = int(input(f"digite um numero {i+1}: "))
    soma = soma + num
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print("a media é: ", soma / 10)
print(f"o maior numero foi: {maior}")
print(f"o menor numero foi: {menor}")

