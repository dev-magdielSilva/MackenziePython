# EXEMPLOS
# EXERCÍCIO 3

# Faça um programa em Python que resolva o seguinte problema: 
# Um concurso possui um prêmio no montante de R$ 780.000,00 para dividir entre três ganhadores da seguinte forma: 
# o primeiro ganhador receberá 46% do prêmio; 
# o segundo ganhador receberá 32% do prêmio;  
# o terceiro ganhador receberá o restante do prêmio. 

montante = float (780.000)
primeiroGanhador = float(montante * (46/100))
segundoGanhador = float(montante * (32/100))
terceiroGanhador = float(montante - primeiroGanhador - segundoGanhador)
print(f"Primeiro Ganhador = {primeiroGanhador}")
print(f"Segundo Ganhador = {segundoGanhador}")
print(f"Terceiro Ganhador = {terceiroGanhador}")
