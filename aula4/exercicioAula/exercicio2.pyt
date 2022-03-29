# Elabora um programa que calcule e mostre o valor que deve ser pago por um produto,
# considerando que o usuário fornecerá o preço normal de atiqueta e o código de pagamento.
# Utilize os códigos da tabela seguinte para ler qual é a condição de pagamento escolhida e efetuar o
# calculo adequado.

# CÓDIGO 1 - A vista em dinheiro ou débito, recebe 10 % de desconto.
# CÓDIGO 2 - A vista no cartão de crédito, recebe 5 % de desconto.
# CÓDIGO 3 - Em 2 vezes, preço normal de etiqueta sem juros.
# CÓDIGO 4 - Em 3 vezes, preço normal de etiqueta mais juros de 10 %.

preco = float(input("Preço normal da etiqueta:"))
cod = int(input("Insira o código de desconto:"))
if cod == 1:
    valor = preco*0.90
    print("À vista em dinheiro ou débito, recebe 10 % de desconto: R$ %.2f" %valor)
elif cod ==2:
    valor = preco*0.95
    print("A vista no cartão de crédito, recebe 5 % de desconto. R$ %.2f" %valor)
elif cod ==3:
    valor = preco/2
    print("Em 2 vezes, preço normal de etiqueta sem juros. Valor da parcela: R$ %.2f" %valor)
elif cod ==4:
    valor = preco*1.10/3
    print("Em 3 vezes, preço normal de etiqueta mais juros de 10 %.alor da parcela: R$ %.2f" %valor)
else:
    print("Código inválido")