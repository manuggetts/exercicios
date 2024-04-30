import java.util.Scanner;

public class SomaFatoriais {
    public static long fatorial(int n) {
        if (n == 0) {
            return 1;
        } else {
            long result = 1;
            for (int i = 1; i <= n; i++) {
                result *= i;
            }
            return result;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o número de elementos (N): ");
        int N = scanner.nextInt();

        int[] numeros = new int[N];
        System.out.println("Digite os " + N + " números:");
        for (int i = 0; i < N; i++) {
            numeros[i] = scanner.nextInt();
        }

        long somaFatoriais = 0;
        for (int num : numeros) {
            somaFatoriais += fatorial(num);
        }

        System.out.println("A soma dos fatoriais é: " + somaFatoriais);

        scanner.close();
    }
}

/*
 * Soma de fatoriais
 * Dado um número inteiro N (1 ≤ N ≤ 10) e N números F (0 ≤ F ≤ 10), determine a
 * soma do fatorial desses N números.
 * 
 * Entrada
 * A entrada consiste em uma linha contendo um número inteiro N (1 ≤ N ≤ 10) e a
 * segunda linha com N números F (0 ≤ F ≤ 10)
 * 
 * Saida
 * Imprima um único número, a soma do fatorial de cada N números F.
 * 
 * Exemplo 1
 * Entrada: 1 4
 * 
 * Saida: 24
 * 
 * Exemplo 2
 * Entrada: 2 4 10
 * 
 * Saida: 3628824
 * 
 * Exemplo 3
 * Entrada: 3 0 1 2
 * 
 * Saida: 4
 */