primeiro = float(input('Primeiro numero: '))
segundo  = float(input('Segundo numero : '))


    # Achando o maior número
maior = primeiro

if (segundo > maior):
    maior = segundo

if (primeiro > segundo):
    maior = primeiro


print('Maior:  ', maior)
