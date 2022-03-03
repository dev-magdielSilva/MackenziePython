# Faça um programa em Python que receba o custo (valor em reais) de um espetáculo teatral 
# e o preço do convite (valor em reais) desse espetáculo. 
# Esse programa deve calcular e mostrar:  

# a) A quantidade de convites que devem ser vendidos para que, pelo menos, o custo do espetáculo seja alcançado.  

import math
print("Digite o preço do custo")
custo = int(input())
print("custo =", custo)
print("Digite o preço do ingresso")
ingresso = int(input())
print("ingresso =", ingresso)
quantidadeDeConvitesParaBancarOCusto = math.ceil(custo/ingresso) 
print("Quantidade mínima de convites =", quantidadeDeConvitesParaBancarOCusto )


# b) A quantidade de convites que devem ser vendidos para que se tenha um lucro de 23%. 

custoLucro = float(custo * (23/100))
quantidadeDeConvitesParaBancarOCustoMaisLucro = math.ceil((custo + custoLucro)/ingresso) 
print("Quantidade mínima de convites para ter um lucro de 23% =", quantidadeDeConvitesParaBancarOCustoMaisLucro )

# Observe que as quantidades calculadas devem ser um número inteiro, portanto, 
# o resultado da quantidade de convites deve ser arredondada para cima, usando a 
# função matemática apropriada em Python. 

