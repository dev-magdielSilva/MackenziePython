# Escreva um programa em python que leia um número inteiro, entre 0 e 10,
# e mostre a tabuada deste número multiplicado de 1 até 10.

num = int(input())
while num < 0 or num > 10:
    print("VALOR INVÁLIDO")
    num = int(input())
for i in range(1,11):
    result=num*i
    print(f"{num}x{i}={result}")
