# Pedindo e lendo os valores de A, B e C
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

# somando A + B
soma = a + b

# Verificando se a soma (A + B) é menor que C
if soma < c:
    print(f"A soma de A e B ({soma}) é menor que C ({c}).")
else:
    print(f"A soma de A e B ({soma}) não é menor que C ({c}).")