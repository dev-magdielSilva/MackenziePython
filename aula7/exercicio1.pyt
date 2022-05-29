# Escreva uma função para cada operação da calculadora
# Uma função para apresentar o menu de opções para o usuário
# Uma função para a entrada dos 2 números
# Uma função para a escolha da operação a ser realizada
# Uma função principal que definirá a ordem em que as funções pré-definidas
# serão processadas, ou seja, faremos a chamada das funções. 


def soma (n1,n2):
    return n1+n2 

def subtracao (n1, n2):
    return n1-n2

def multiplicacao (n1, n2):
    return n1*n2

def divisao (n1, n2):
    return n1/n2

def menu():
    print ('1- soma \n 2- Subtrai \n 3-Multiplica \n 4- Divide \n 5- Sair')
    op = int(input())
    while (op<1 or op>5):
        print('Opção inválida')
        op = int (input())
    return op

def entrada():
    return int (input())

def escolha(op, n1, n2):
    if op == 1:
        result = soma(n1, n2)
    elif op == 2:
        result = subtracao(n1, n2)
    elif op == 3:
        result = multiplicacao(n1, n2)
    elif op == 4:
        if n2 != 0:
            result = divisao(n1, n2)
        else:
            result = None
    return result

def main():
    while True:
        op = menu()
        if op == 5:
            break
        print('Digite dois números')
        n1 = entrada()
        n2 = entrada()
        if escolha(op, n1, n2) == None:
            print("Não há divisão por zero")
        else:
            print(escolha(op, n1, n2))

main()