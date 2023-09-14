#idade_completo.py

#carrega da biblioteca datetime a classe date
from datetime import date

#armazena na variável hoje o valor da função today da classe date
hoje = date.today()

#acessando o atributo ano dentro da função today
atual = int(hoje.strftime("%Y"))
teste_year = int(hoje.strftime("%y"))


nome = input("qual o seu nome?\n")
ano = int(input("qual ano você nasceu?\n"))
#Pergunta o ano atual
#atual = int(input("em qual ano estamos?\n"))

idade = atual - ano
print("Valor %y", teste_year)
print("olá", nome, "! você tem", idade, "anos")

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")
