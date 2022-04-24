# Elabore um programa em Python que leia um número inteiro e positivo
# calcule e apresente os divisores deste número, separados por um
# espaço em branco.
divisor = 1
num = int(input())
while num <= 0:
    print("VALOR INVÁLIDO")
    num = int(input())
for divisor in range (1, num+1):
    if num % divisor == 0:
        print(divisor,end = " ")