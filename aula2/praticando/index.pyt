
result = int(2**4)
print(result)

result2 = float(2*5**1.9)
print(result2)

a = 5
b = 2
c = a+b
print(f'soma = {c}')

import math
x = 3.954
print(f'o valor de x é:{x}')
y = math.ceil(x)
print(f'o valor de x para cima é:{y}')

# Escreva um programa que receba o raio de uma esfera, calcule e apresente o seu volume.

import math
print("Cálculo do colume da esfera")
raio = float(input("Raio:"))
vol = 3/4 * math.pi * math.pow(raio, 3)
print(f"volume = {vol}")

#Três amigos: Carlos, André e Felipe, decidiram rachar igualmente a conta em um bar.
# Faça um programa para ler o valor total da conta e imprimir quando cada um deve pagar,
# mas faça com que Carlos e André não paguem centavos.
# Por exemplo: uma conta de R$101,53 resulta em R$33,00 para Carlos e Andre e R$35,53 para Felipe
 
valor = float(input('Valor da conta:'))
divisao = valor/3
cada = int(divisao)
sobra = valor - 2 * cada
print("Carlos irá pagar R$ %.2f" % cada)
print("Andre irá pagar R$ %.2f" % cada)
print("Carlos irá pagar R$ %.2f" % sobra)

# Desenvolva um programa para converter a temperatura Celcius para Fahrenheit.
#  A fórmula de conversão é: f = (c*9/5) +32

import math
c = int (input("Temperatura em Celsius:"))
f = (c*9/5) +32
print('Temperatura em F', int(f),"°")
