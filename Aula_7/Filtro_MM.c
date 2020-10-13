#include <stdio.h>
#include <fcntl.h>
#include <io.h>


#define NSAMPLES  16	

int main()
{
	FILE *in_file, *out_file;
	int i, n, n_amost;

	short entrada, saida;
	short sample[NSAMPLES] = {0x0};

	float y=0;

	//Carregando os coeficientes 
	float coef[NSAMPLES]={
				
	#if NSAMPLES == 4
	#include "coefs_mm_4.dat"
	#elif NSAMPLES == 8
	#include "coefs_mm_8.dat"
	#elif NSAMPLES == 16
	#include "coefs_mm_16.dat"
	#else
	#include "coefs_mm_32.dat"
	#endif

	};


	// abre os arquivos de entrada e saida 
	if ((in_file = fopen("sweep_100_2k.pcm","rb"))==NULL){
		printf("\nErro: Nao abriu o arquivo de entrada\n");
		return 0;
	}
	if ((out_file = fopen("sweep_out_mm.pcm","wb"))==NULL){
		printf("\nErro: Nao abriu o arquivo de saida\n");
		return 0;
	}

    //Inicializa o vetor com zeros
	for (i=0; i<NSAMPLES; i++){
		sample[i]=0;
	}

   
	do {
			
		y=0;

	    //Retira um valor do arquivo
		n_amost = fread(&entrada,sizeof(short),1,in_file);
				sample[0] = entrada;

	 
		for (n=0; n<NSAMPLES; n++){
			y += coef[n]*sample[n];
		}

	   
		for (n=NSAMPLES-1; n>0; n--){
			sample[n]=sample[n-1];
		}

		saida = (short) y;

		fwrite(&saida,sizeof(short),1,out_file);

	} while (n_amost);//Enquanto tiver valores para ler, executa o filtro

   //Fecha os arquivos p/ liberar memoria
   fclose(out_file);
   fclose(in_file);
   return 0;
}