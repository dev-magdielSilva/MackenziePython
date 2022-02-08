# faça um programa que receba três notas e seus respectivos pesos, 
# calcule e mostre a média ponderada dessas notas.
print("Digite as três notas:")
n1 = float(input())
n2 = float(input())
n3 = float(input())
print("Digite o peso de cada nota:")
p1 = int(input())
p2 = int(input())
p3 = int(input())
media = (n1*p1+n2*p2+n3*p3) / (p1+p2+p3)
print("Média ponderada = ", media)