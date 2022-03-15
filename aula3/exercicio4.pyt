# Um comerciante comprou um produto e quer vendê-lo com um
# lucro de 45% se o valor da compra for menor que R$ 20,00; caso contrário,
# o lucro será de 30%.
# Escreva um programa em Python que recebe o valor do produto e exiba o valor da venda!"

valor = float(input("Insira o valor da compra:"))
if valor<20.00:
    valorVenda = valor*1.45
else:
    valorVenda = valor*1.30
print("Valor da venda: %.2f" %valorVenda)