populacao_A = int(input("Digite o número da população A: "))
taxa_crescimento_A = float(input("Digite a taxa de crescimento da população A: "))

populacao_B = int(input("Digite o número da população B: "))
taxa_crescimento_B = float(input("Digite a taxa de crescimento da população B: "))

anos = 0

while populacao_A < populacao_B:
    anos += 1
    populacao_A += populacao_A * taxa_crescimento_A
    populacao_B += populacao_B * taxa_crescimento_B

print(f"São necessários {anos} anos para que a população do país A ultrapasse ou iguale a população do país B.")