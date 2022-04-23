# Faça um programa em python que calcule e apresenta o fatorial de um número
# inteiro e natural pelo usuário.

fat = 1
print("Digite um número inteiro e natural")
num = int(input())
while num < 0:
    num = int(input())
for i in range(1, num+1):
    fat = fat * i
print(f'{num}!= {fat}')
