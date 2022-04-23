# Este programa em Python solicita ao usuário um número
# e mostra os próximos 5 números a partir do número digitado.

num = int(input("Numero:"))
for ct in range(5):
    num = num +1
    print(num)

    # ct é a variável de controle do for
