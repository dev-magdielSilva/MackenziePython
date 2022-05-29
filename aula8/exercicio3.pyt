# A agenda irá permitir, através de um menu:
# Cadastrar um amigo, no final da lista
# Mostrar os nomes de todos os amigos
# Cadastrar um amigo, no início da lista
# Remover um nome
# Substituir um nome
# Mostrar o número total de amigos cadastrados
# Colocar os nomes dos amigos em ordem alfabética
# Sair do programa

def menu():
    print("(1) Cadastrar um amigo, no final da lista")
    print("(2) Mostrar os nomes de todos os amigos")
    print("(3) Cadastrar um amigo, no inicio da lista")
    print("(4) Remover um nome")
    print("(5) Substituir um nome")
    print("(6) Mostrar o número total de amigos cadastrados")
    print("(7) Colocar os nomes dos amigos em ordem alfabética")
    print("(8) Sair do programa")
    op = int(input("Opção selecidada:"))
    while op <1 or op > 8:
        op = int(input("Opção selecionada:"))
    return op

def inserir_amigo(amigo):
    nome = input("Nome:")
    amigo.append(nome)

def mostrar_nomes(amigo):
    print(amigo)

def inserir_amigo_final(amigo):
    nome = input("Digite um nome:")
    amigo.insert(0,nome)

def remover_amigo (amigo):
    nome = input("Qual é o nome a ser removido:")
    for i in range (0, len(amigo)):
        if amigo[i] == nome:
            pos = i
            break
    del amigo[pos]

def substituir_nome(amigo):
    nome = input("Qualo nome a ser substituído:")
    nomenovo = input('Qual é o novo nome:')
    for i in range (0,len(amigo)):
        if amigo[i] == nome:
            amigo[i] = nomenovo

def total_cadastro(amigo):
    print("Total de amigos = %d" %len(amigo))

def ordenar_amigos(amigo):
    amigo.sort()
    mostrar_nomes(amigo)

def main():
    amigo = []
    while True:
        op = menu()
        if op == 1:
            inserir_amigo(amigo)
        elif op == 2:
            mostrar_nomes(amigo)
        elif op == 3:
            inserir_amigo_final(amigo)
        elif op == 4:
            remover_amigo(amigo)
        elif op == 5:
            substituir_nome(amigo)
        
main()
