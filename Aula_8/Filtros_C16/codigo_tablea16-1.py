import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

if __name__ == "__main__":

    vetor_X = np.ones(4999)  # Guarda o input
    vetor_Y = np.zeros(4999)  # Guarda o output


    # tamanho do filtro, deve ser um numero par
    M = int(input("Tamanho do filtro: "))
    # frequencia de corte
    # para windowed_sinc, fc tem que ser um valor entre 0 e 0.5
    fc = float(input("Frequencia de corte: "))

    kernel = np.zeros(M)
    # Calculo do kernel
    for i in range(M):
        if i - (M / 2) == 0:
            kernel[i] = 2 * np.pi * fc
        if i - (M / 2) != 0:
            kernel[i] = (np.sin(2 * np.pi * fc * (i - M / 2)) / (i - M / 2))

        kernel[i] = kernel[i] * (0.54 - 0.46 * np.cos(2 * np.pi * i / M))

    # Normalizar o kernel
    soma = 0
    for i in range(M):
        soma = soma + kernel[i]

    for i in range(M):
        kernel = kernel/soma

    # Executa a convolução do input com o filtro
    for j in range(100, 4999):
        vetor_Y[j] = 0
        for i in range(M):
            vetor_Y[j] = vetor_Y[j] + vetor_X[j - i] * kernel[i]

    # Nome e tamanho da janela a ser aberta
    plt.figure(u"Gráficos", figsize=(15, 8))
    plt.subplot(2, 1, 1)
    plt.title(u"Gráfico windowed_sinc tempo")
    plt.xlabel("amostra")
    plt.ylabel("Amplitude")
    plt.grid(1)
    plt.plot(vetor_Y)

    # resposta em frequencia
    [i, h] = freqz(vetor_Y, fs=1)

    plt.subplot(2, 1, 2)
    plt.title(u"Gráfico windowed_sinc frequencia")
    plt.plot(i, abs(h))
    plt.ylabel("Magnitude")

    plt.tight_layout()
    plt.savefig("table16-1.png", format="png")

    plt.show()