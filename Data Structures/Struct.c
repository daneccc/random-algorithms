#include <stdio.h>
#include <stdlib.h>

struct Estudante {
    char nome[80];
    int mat, idade;
    float media;
};

int main() {
    struct Estudante aluno;

    printf("Informe o primeiro nome do aluno: ");
    scanf("%s", aluno.nome);
    printf("Informe a matrícula: ");
    scanf("%d", &aluno.mat);
    printf("Informe a idade: ");
    scanf("%d", &aluno.idade);
    printf("Informe a média: ");
    scanf("%f", &aluno.media);

    printf("\n\nPrimeiro Nome: %s\n", aluno.nome);
    printf("Matrícula: %d\n", aluno.mat);
    printf("Idade: %d anos\n", aluno.idade);
    printf("Média: %f\n", aluno.media);
}