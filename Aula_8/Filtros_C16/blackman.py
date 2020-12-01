import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz


"""
h[i] = 0,42 - 0,5 * cos(2pi*i/M) + 0.08 * cos(4pi*i/M)
"""
def blackman(rate, M):
    # indice
    i = np.arange(0, M, 1/rate)
    # função hamming window
    w = 0.42 - 0.5 * np.cos(2*np.pi*i/M) + 0.08 * np.cos(4*np.pi*i/M)
    return i, w


if __name__ == "__main__":

    # taxa de amostragem
    sample_rate = int(input("Sample rate: "))
    # limite, deve ser um numero par
    M = int(input("Tamanho do filtro: "))

    i, w = blackman(sample_rate, M)

    # plota
    plt.figure(u"Gráficos", figsize=(15, 8))
    plt.subplot(2, 1, 1)
    plt.title(u"Gráfico Blackman tempo")
    plt.xlabel("amostra")
    plt.ylabel("Amplitude")
    plt.grid(1)
    plt.plot(i, w)
    plt.savefig("Blackman.png", format="png")

    # resposta em frequencia
    [w, h] = freqz(w, worN=sample_rate, fs=1)

    plt.subplot(2, 1, 2)
    #dB
    plt.title(u"Gráfico Blackman frequencia (dB)")
    plt.plot(w, 20 * np.log10(abs(h)), 'b')
    #Normal
    #plt.title(u"Gráfico Blackman frequencia")
    #plt.plot(w, abs(h), 'b')
    plt.ylabel("Magnitude")

    plt.tight_layout()
    plt.savefig("Blackman.png", format="png")

    plt.show()
