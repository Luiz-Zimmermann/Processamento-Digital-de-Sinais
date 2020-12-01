
#include <stdio.h>
#include <fcntl.h>
#include <io.h>

#define NSAMPLES 320
#define taxa 0.000000000005

int main() {
  //Manipuladores de arquivo
  FILE *in_file, *out_file;
  int i, n, n_amost;

  short entrada, saida;
  short sample[NSAMPLES];

  //Saida do sistema desconhecido
  double dn = 0.0;
  //Saida do filtro FIR
  double yn = 0.0;
  //Diferença entre o desejado e o obtido
  double erro = 0.0;

  //Carregando os coeficientes de um filtro
  float coef[NSAMPLES] = {
        #include "coefs_pb.dat" // NSAMPLES
  };

  //Coeficientes para descobrir sinal
  double coef_adpt [NSAMPLES];


  //Abre os arquivos de entrada e saida
  if ((in_file = fopen("ruido_branco.pcm", "rb")) == NULL) {
    printf("\nErro: Nao abriu o arquivo de entrada\n");
    return 0;
  }
  if ((out_file = fopen("resultado_filtro_c.pcm", "wb")) == NULL) {
    printf("\nErro: Nao abriu o arquivo de saida\n");
    return 0;
  }

  //Zera vetor de amostras
  for (i = 0; i < NSAMPLES; i++) {
    sample[i] = 0;
    coef_adpt[i] = 0.0;
  }


  //Execução do filtro
  do {

    //Zera saída do filtro
    dn = 0;
    yn = 0;

    //Lê dado do arquivo
    n_amost = fread( & entrada, sizeof(short), 1, in_file);
    sample[0] = entrada;

    //Convolução e acumulação DN
    for (n = 0; n < NSAMPLES; n++) {
      dn += coef[n] * sample[n];
    }

    //Convolução e acumulação YN
    for (n = 0; n < NSAMPLES; n++) {
      yn += coef_adpt[n] * sample[n];
    }

    //Calculo do erro
    erro = dn - yn;

    printf("erro %f\n", erro);
	
	//Atualiza coeficientes
    for (n = 0; n < NSAMPLES; n++) { 
        coef_adpt[n] = coef_adpt[n] + 2.0 * taxa * erro * sample[n];
    }

    //Desloca amostra
    for (n = NSAMPLES - 1; n > 0; n--) {
      sample[n] = sample[n - 1];
    }

    //Cast para escrita
    saida = (short) erro;

    //Escreve no arquivo de saída
    fwrite( & saida, sizeof(short), 1, out_file);

  } while (n_amost);

  //Fecha os arquivos de entrada de saída
  fclose(out_file);
  fclose(in_file);
  return 0;
}
