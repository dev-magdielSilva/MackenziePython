# Faça um programa modularizado em Python com as seguintes funções:
# A atualiza_preco(): a função deve receber como parâmetro o valor de um produto, calcular e retornar este valor com aumento de 10%
# B taxa(valor): a função calcula e retorna o valor da taxa de 2,5 % sobre o valor do produto atualizado (após a chamada da função atualiza_preco).
#  C main(): terá o programa principal que deve, nesta ordem, fazer a entrada via teclado do valor do produto. Depois chamar as funções atualiza_preco()
# e taxa e apresentar os calores calculados do vvalor atualizado com duas casas decimais e do valor da taxa também com duas casas decimais.
# Ao final, chame a função main() para qe o programa seja executado.

def atualiza_preco(valor):
    valor = valor *1.10
    return valor

def taxa (valor):
    tax = valor *0.025
    return tax

def main():
    valor = float(input())
    valor = atualiza_preco(valor)
    tax = taxa(valor)
    print('%.2f'%valor)
    print('%.2f'%tax)

main()

