# EXEMPLOS
# EXERCÍCIO 1

# Escreva um programa em Python que permita ao usuário digitar dois números inteiros
# e exibir o resultado para cada uma das seguintes operações: soma, subtração, multiplicação,
# divisão, divisão truncada, resto e exponenciação.

print("Digite dois números inteiros:")
number1 = int(input())
number2 = int(input())
soma = number1 + number2
subtração = number1 - number2
multiplicação = number1 * number2
divisão = number1 / number2
divisãoTruncada = number1 // number2
resto = number1 % number2
exponenciação = number1 ** number2

print(f"Soma dos números = {soma}")
print(f"Subtração dos números = {subtração}")
print(f"Multiplicação dos números = {multiplicação}")
print(f"Divisão dos números = {divisão}")
print(f"Divisão Truncada dos números = {divisãoTruncada}")
print(f"Resto dos números = {resto}")
print(f"Exponenciação dos números = {exponenciação}")

