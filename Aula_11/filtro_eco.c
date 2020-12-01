#include <stdio.h>
#include <fcntl.h>
#include <io.h>

#define NSAMPLES 320 

int main() {
  FILE *far, *near, *out_file;
  int i, n, n_amost, n_amost_near;

  short entrada_far, entrada_near, saida;
  short sample_far[NSAMPLES];
  short sample_near[NSAMPLES];

  double erro = 0.0;

  // auxiliar convolução
  double y = 0;

  // vetor de coeficientes
  double coef[NSAMPLES];

  /* abre os arquivos far e near*/
  if ((far = fopen("far_apcm.pcm", "rb")) == NULL) {
    printf("\nErro: Nao abriu o arquivo de entrada\n");
    return 0;
  }
  if ((near = fopen("near_apcm.pcm", "rb")) == NULL) {
    printf("\nErro: Nao abriu o arquivo de entrada\n");
    return 0;
  }

  /* arquivo de saida*/
  if ((out_file = fopen("resultado_filtro_eco.pcm", "wb")) == NULL) {
    printf("\nErro: Nao abriu o arquivo de saida\n");
    return 0;
  }

  // zera vetor de amostras e coeficientes
  for (i = 0; i < NSAMPLES; i++) {
    sample_far[i] = 0.0;
    sample_near[i] = 0.0;
    coef[i] = 0.0;
  }
	printf("\nPressione qualquer tecla para aplicar o filtro!!\n");
	getchar();


  // execução do filtro
  do {

    //zera saída do filtro
    y = 0;

    //lê dado dos arquivos
    n_amost = fread( &entrada_far, sizeof(short), 1, far);
    sample_far[0] = entrada_far;
    n_amost_near = fread( &entrada_near, sizeof(short), 1, near);


    for (n = 0; n < NSAMPLES; n++) { // Convolução far * filtro
        y += coef[n] * sample_far[n];
    }

    erro = entrada_near - y;         // calculo do erro
	//printf("\nErro: %f", erro);
	// atualiza coeficientes
	//taxa de aprendizado
    for (n = 0; n < NSAMPLES; n++) { 
        coef[n] = coef[n] + 2.0 * 0.000000000005 * erro * sample_far[n];
    }

    //desloca amostra
    for (n = NSAMPLES - 1; n > 0; n--) {
      sample_far[n] = sample_far[n - 1];
    }

    saida = (short) erro;
    fwrite( & saida, sizeof(short), 1, out_file);


  } while (n_amost);

  printf("\nTerminou de aplicar o filtro\n");

  //fecha os arquivos de entrada de saída
  fclose(out_file);
  fclose(far);
  fclose(near);

  return 0;
}
