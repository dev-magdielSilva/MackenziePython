# Faça um programa que leia vários números, encerrando a entrada e dados quando o usuário digitar
# um número negativo. Calcule e mostre a quantidade de números digitados. 
# O número que encerra não deve ser contado.

print = ("Digite vários números:")
ct = 0
num = int(input(""))
while num >=0:
    ct += 1
    num = int(input(""))
print ("Quantidade de números digitados:", ct)