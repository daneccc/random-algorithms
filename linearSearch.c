#include <stdio.h>
#include <stdlib.h>

int main() {
    int vet[] = {2, 4, 1, 6, 4, 3, 7, 9, 4, 1};
    int n = 10;
    int buscar;
    int resp[n];
    int p = 0; // variável indicadora da posição no vetor resp.

    printf("Informe o número que deseja buscar: ");
    scanf("%d", &buscar);

    for(int i = 0; i <= n - 1; i++) {
        if(vet[i] == buscar) {
            resp[p] = i;
            p = p + 1; 
        }   
    }

    if(p > 0) {
        for(int i = 0; i <= p - 1; i++)
            printf("Posição no Vetor: %d\n", resp[i]);
    } else {
        printf("Número não encontrado!");
    }
}