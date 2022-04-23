# Faça um programa que leia um número entre 30 e 70.
# Repetir a entrada de dados até o usuário digitar um valor válido.
num = float (input("Digite um número entre 30 e 70:"))
while num <= 30 or num>= 70:
    if num <= 30 or num>= 70:
        print("valor inválido, digite novamente")
    num = float (input("Digite um número entre 30 e 70:"))
print ("Valor válido")