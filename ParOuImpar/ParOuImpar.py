numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print(f"O número {numero} é par", end=" ")
else:
    print(f"O número {numero} é ímpar", end=" ")

if numero >= 0:
    print("e é positivo.")
else:
    print("e é negativo.")