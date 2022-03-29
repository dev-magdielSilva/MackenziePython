# Um banco concederá um crédito especial a seus clientes de acordo com o saldo médio
# no último ano. Faça um pseudocódigo que receba o saldo médio de um cliente e calcule o valor
# do crédito, de acordo com a tabela a seguir. Mostre o saldo médio e o valor do credito.

#  SALDO MÉDIO Até R$200,00 - PERCENTUAL 10%  do saldo médio
#  SALDO MÉDIO Entre R$200,01 e R$300,00 - PERCENTUAL 20% do saldo médio
#  SALDO MÉDIO entre R$300,01 e R$400,00 - PERCENTUAL 25% do saldo médio
#  ACIMA DE R$400,00 - PERCENTUAL 30% do saldo médio.

saldo = float (input("Saldo médio: "))
if saldo <= 200:
    credito = saldo*0.1
elif saldo <=300:
    credito = saldo*0.2
elif saldo <= 400:
    credito = saldo*0.25
else:
    credito = saldo *0.3
print (f"Valor do crédito é {credito}")