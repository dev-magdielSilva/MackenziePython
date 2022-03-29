# Fala um programa em Python que leia a quantidade em Km e a quantidade de litros de gasolina 
# consumidos por um carro em um percurso, calcule o consumo em km/litros e escreva uma mensagem 
#  de acordo com a tabela abaixo:

# consumo menor que 8 - mensagem venda o carro!
# consumo entre 8 e 12 - mensagem Econômico!
# consumo maior 12 - mensagem Super econômico!

km = float(input("Insira o valor em Km: "))
l = float(input("Insira o valor em Litros: "))
consumo = km / l
print(f"Consumo = {consumo}")
if consumo <8:
    print("Venda o carro!")
elif consumo <=12:
    print("Economico!")
else:
    print("Super Economico!")
    