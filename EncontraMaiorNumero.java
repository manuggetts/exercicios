public class EncontraMaiorNumero {
    public static void main(String[] args) {
        // criando a array com os números
        int[] lista = { 1, 3, 5, 7, 2, 8, 4, 9, 6, 10 };

        // iniciando a variavel pra guardar o numero maior
        int maior = lista[0];

        // percorrendo a lista pra encontrar o numero maior
        for (int i = 1; i < lista.length; i++) {
            if (lista[i] > maior) {
                maior = lista[i]
            }
        }
        System.out.println("O maior número é:" + maior);
    }
}

/*
 * Sintaxe do loop for em java:
 * 
 * for (inicialização; condição; incremento) {
 * código a ser executado
 * }
 * 
 * 1. Inicialização:
 * 
 * A parte de inicialização é executada só uma vez, antes do início do loop
 * No código a inicialização é: int i = 1;
 * Isso cria uma variável i e inicia ela com o valor 1
 * 
 * 2. Condição:
 * 
 * A condição é verificada antes de cada iteração do loop
 * Se a condição for verdadeira, o bloco de código dentro do loop é executado;
 * caso contrário, o loop é encerrado.
 * No código, a condição é: i < lista.length;
 * Isso verifica se o valor de i é menor que o tamanho da lista
 * 
 * 3. Incremento:
 * 
 * A parte de incremento é executada após cada iteração do loop
 * No código, o incremento é: i++
 * Isso aumenta o valor de i em 1 a cada iteração
 * 
 * 4. Execução do "código a ser executado":
 * 
 * O código dentro do loop é executado enquanto a condição for verdadeira.
 * No código fornecido, o código a ser executado é:
 * 
 * if (lista[i] > maior) {
 * maior = lista[i];
 * }
 * 
 * Isso verifica se o número atual (na posição i da lista) é maior que o valor
 * atual de "maior"
 * Se for, atualiza o valor de maior para o número atual
 */