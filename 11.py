altura_cm = float(input("Digite a altura do reservatório (cm): "))
largura_cm = float(input("Digite a largura do reservatório (cm): "))
comprimento_cm = float(input("Digite o comprimento do reservatório (cm): "))
consumo_medio_litros_por_dia = float(input("Digite o consumo médio diário (litros/dia): "))

 

volume_cm3 = altura_cm * largura_cm * comprimento_cm
volume_litros = volume_cm3 / 1000
autonomia_dias = volume_litros / consumo_medio_litros_por_dia

 

print(f"A capacidade total do reservatório é de {volume_litros:.2f} litros.")
print(f"A autonomia do reservatório é de {autonomia_dias:.2f} dias.")

 

classificacao = ""
if autonomia_dias < 2:
    classificacao = "Consumo elevado"
elif autonomia_dias >= 2 and autonomia_dias <= 7:
    classificacao = "Consumo moderado"
else:
    classificacao = "Consumo reduzido"

 

print(f"A classificação do consumo é: {classificacao}.")
