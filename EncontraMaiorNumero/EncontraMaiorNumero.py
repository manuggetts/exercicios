# Criando a lista com os números
lista = [1, 3, 5, 7, 2, 8, 4, 9, 6, 10]

# Iniciando a variável para guardar o número maior
maior = lista[0]

# Percorrendo a lista para encontrar o número maior
for num in lista[1:]:
    if num > maior:
        maior = num

print(f"O maior número é: {maior}")

''' Sintaxe do Loop for em Python
Em Python, o loop for é usado para iterar sobre uma sequência (como uma lista, uma string ou um intervalo numérico)
A sintaxe básica é a seguinte:

for elemento in sequencia:
    # Código a ser executado

Inicialização (ausente em Python):
Diferentemente do Java, em Python, não precisamos especificar uma inicialização separada. O loop for automaticamente itera sobre os elementos da sequência.

Condição (ausente em Python):
Também não especificamos explicitamente uma condição. O for percorre todos os elementos da sequência até que não haja mais elementos.

Incremento (ausente em Python):
Não precisamos incrementar manualmente o índice ou contador. O for cuida disso automaticamente.

Execução do “código a ser executado”:
O bloco de código dentro do for é executado para cada elemento da sequência.
O elemento representa cada item da sequência.

Exemplo em Python
Suponha que temos a seguinte lista:
numeros = [1, 2, 3, 4, 5]

Podemos usar o for para percorrer essa lista:
for num in numeros:
    print(num)

Nesse exemplo, o código dentro do for será executado 5 vezes (uma vez para cada número na lista), e cada número será impresso no console.
O Python simplifica a sintaxe do for, tornando-o mais legível e conciso.
'''