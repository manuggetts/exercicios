def fatorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def main():
    N = int(input())
    numeros = list(map(int, input().split()))

    somaFatoriais = sum(fatorial(num) for num in numeros)

    print(somaFatoriais)

if __name__ == "__main__":
    main();

''' Soma de fatoriais
Dado um número inteiro N (1 ≤ N ≤ 10) e N números F (0 ≤ F ≤ 10), determine a
soma do fatorial desses N números.
 
Entrada
A entrada consiste em uma linha contendo um número inteiro N (1 ≤ N ≤ 10) e a
segunda linha com N números F (0 ≤ F ≤ 10)

Saida
Imprima um único número, a soma do fatorial de cada N números F.

Exemplo 1
Entrada: 1 4
 
Saida: 24

Exemplo 2
Entrada: 2 4 10
 
Saida: 3628824
 
Exemplo 3
Entrada: 3 0 1 2
 
Saida: 4'''