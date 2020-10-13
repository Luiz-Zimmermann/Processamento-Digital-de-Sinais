import numpy as np
import matplotlib.pyplot as matp

#Exemplo sistema discreto
#equaçao diferença: y[n] + 0,25y[n-1] + 0,125y[n-2] = x[n]

# Tamanho das amostras do sinal degrau.
tam_amostras = 10 # (0 a 9 no grafico)

# Cria os vetores de entrada e saida
x = np.ones(tam_amostras)
output = np.zeros_like(x)

# Definindo [y-1] e [y-2]
ynm1 = 0
ynm2 = 0

for i in range(tam_amostras):

    input = x[i]
    # Calcula o valor na saida
    y = input - 0.25*ynm1 - 0.125*ynm2

    # Deslocamento
    ynm2 = ynm1
    ynm1 = input
    output[i] = y

# Nome e tamanho da janela a ser aberta
matp.figure(u"Gráfico da transformada Z",figsize=(15,8))

# Plota os gráficos
matp.subplot(211)
matp.title(u"Gráfico input")
matp.xlabel("amostra")
matp.ylabel("Amplitude")
matp.grid(1)
matp.stem(x)

matp.subplot(212)
matp.title(u"Gráfico output")
matp.xlabel("amostra")
matp.ylabel("Amplitude")
matp.grid(1)
matp.stem(output)


# Ajusta as posições dos gráficos 
matp.tight_layout()

# Salav a figura
matp.savefig("Sistema_discreto.png",format="png")

# Mostra os gráficos
matp.show()