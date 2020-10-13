#include <stdio.h>
#include <fcntl.h>
#include <io.h>

int main() {
    FILE * input_file, * output_file;
    int i, n, n_amost;

    float y = 0;

    int Fs = 8000;   
    float T1 = 1;       
    float T2 =  1.5;     
    int N1 = (T1*Fs);     
    int N2 = (T2*Fs);     
    float A0 = 0.5;
    float A1 = 0.3;
    float A2 = 0.2;

    int entrada, saida;
    int sample[N2];

    /* abre os arquivos de entrada e saida */
    if ((input_file = fopen("alo.pcm", "rb")) == NULL) {
        printf("Erro ao abrir arquivo de entrada\n");
        return 0;
    }
    if ((output_file = fopen("alo_eco.pcm", "wb")) == NULL) {
        printf("Erro ao abrir arquivo de saida\n");
        return 0;
    }

    // zera vetor
    for (i = 0; i < N2; i++) {
        sample[i] = 0;
    }

    // executa filtro
    do {

        //zera saída
        y = 0;

       
        n_amost = fread( & entrada, sizeof(short), 1, input_file);
        sample[0] = entrada;

        // atraso
        y = A0 * sample[0] + A1 * sample[N1-1] + A2 * sample[N2-1];

        //deslocamento
        for (n = N2 - 1; n > 0; n--) {
        sample[n] = sample[n - 1];
        }

        saida = (short) y;

        //escreve no arquivo de saída
        fwrite(&saida, sizeof(short), 1, output_file);

    } while (n_amost);// Enquanto houver dados, execute

    //fecha os arquivos para liberar memoria
    fclose(input_file);
    fclose(output_file);

    return 0;
}