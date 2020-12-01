import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz


"""
        sin(2*pi*fc*(i-M/2))
sinc = -----------------------
               i - M/2
"""
def windowed_sinc(M, fc):


    h = np.zeros(M, dtype=float)

    for i in range(M):

        if i - (M/2) == 0:
            h[i] = 2*np.pi*fc
        if i - (M/2) != 0:

            h[i] = (np.sin(2*np.pi*fc*(i - M/2))/(i - M/2))

        h[i] = h[i] * (0.42 - 0.5 * np.cos(2*np.pi*i/M) + 0.08 * np.cos(4*np.pi*i/M))

    return h


if __name__ == "__main__":

    # tamanho do filtro, deve ser um numero par
    M = int(input("Tamanho do filtro: "))
    # frequencia de corte
    # para windowed_sinc, fc tem que ser um valor entre 0 e 0.5
    fc = float(input("Frequencia de corte: "))

    h = windowed_sinc(M, fc)

    # plota

    # Nome e tamanho da janela a ser aberta
    plt.figure(u"Gráficos",figsize=(15,8))
    plt.subplot(2, 1, 1)
    plt.title(u"Gráfico windowed_sinc tempo")
    plt.xlabel("amostra")
    plt.ylabel("Amplitude")
    plt.grid(1)
    plt.plot(h)

    # resposta em frequencia
    [i, h] = freqz(h, fs=1)

    plt.subplot(2, 1, 2)
    plt.title(u"Gráfico windowed_sinc frequencia")
    plt.plot(i, abs(h))
    plt.ylabel("Magnitude")

    plt.tight_layout()
    plt.savefig("windowed_sinc.png", format="png")

    plt.show()
