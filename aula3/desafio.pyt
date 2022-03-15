# Faça um programa em Python para resolver o seguinte problema:
# O programa deve receber um número inteiro, digitado pelo usuário, e apresentar uma mensagem:
# Se o número que o usuário digitou for divisível por 3 e por 5 ao mesmo tempo, a mensagem será:
# O número é divisível por 3 e por 5.
# Se o número que o usuario digitou não for divisivel por 3 e 5 ao mesmo tempo, a mensagem será:
# O número não é divisível por 3 e 5.
print("Insira um número inteiro: ")
num = int(input())
if num %3==0 and num %5 ==0:
    print("O número é divisível por 3 e 5")
else:
    print("O número não é divisível por 3 e 5")


