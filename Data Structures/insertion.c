#include <stdio.h>
#include <stdlib.h>

int main() {
    int A[] = {80, 20, 7, 47, 33, 4};

    printf("Vetor desordenado:\n");
    for(int i = 0; i < 6; i++) {
        printf("%dª Posição do vetor: %d\n", i + 1, A[i]);
    }

    int i, chave;
    for(int j = 1; j < 6; j++) {
        chave = A[j];
        i = j - 1;
        while((i >= 0) && (A[i] > chave)) {
            A[i + 1] = A[i];
            i = i - 1;
        }
        A[i + 1] = chave;
    }

    printf("\nVetor ordenado:\n");
    for(int i = 0; i < 6; i++) {
        printf("%dª Posição do vetor: %d\n", i + 1, A[i]);
    }
}