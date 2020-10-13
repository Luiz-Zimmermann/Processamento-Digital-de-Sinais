#include <stdio.h>
#include <stdlib.h>
#define k 4  // tamanho da media

int somaVetor(int *vet)
{
    int soma =0;
    for (int i = 0; i < k; i++)
    {
        soma += vet[i];
    }
    return soma;
}

void deslocaVetor(int *vet)
{
    for (int i = k-1; i > k; i--)
    {
        vet[i] = vet[i-1];
    }
}

int main()
{
    //Abrindo o arquivo
    FILE *input;
    input = fopen("alo.pcm", "rb");
    if (input == NULL)
    {
        printf("Nao foi possivel encontrar o arquivo\n");
    }
    else
    {
        //Cria arquivo de saida
        FILE *output;
        output = fopen("alo_media.pcm", "wb");

        int vet[k];
        //Inicializnado vetor com zeros
        for (int i = 0; i < k; i++)
        {
            vet[i] = 0;
        }

        short dado = 0;
        while(fread(&dado, 2, 1, input) != 0)
        {
            vet[0] = dado;
            short soma = somaVetor(vet)/k;
            fwrite(&soma, 2, 1, output);
            deslocaVetor(vet);
        }
        //Descarta variaveis para liberar memoria
        fclose(input);
        fclose(output);
    }
    return 0;
}