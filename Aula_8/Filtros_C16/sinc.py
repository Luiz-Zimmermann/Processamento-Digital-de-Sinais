import numpy as np
import matplotlib.pyplot as plt


def sinc(rate, fc): 

    # indice
    i = np.arange(-0.1, 0.1, 1/sample_rate)

    # função sinc 
    """
        sin(2pi*fc*i)
    h[i] = -------------
            i*pi
    """
    # não precisa fazer o laço for, ele já calcula para todas as posições
    h = np.sin(2*np.pi*fc*i)/(i*np.pi)
    return i, h

if __name__ == "__main__":
    # taxa de amostragem
    sample_rate = int(input("Sample rate: "))
    # frequencia de corte
    fc = int(input("Frequencia de corte: "))

    i, h = sinc(sample_rate, fc)

    # plota
    plt.title(u"Gráfico Função Sinc")
    plt.xlabel("amostra")
    plt.ylabel("Amplitude")
    plt.grid(1)
    plt.plot(i, h)
    plt.savefig("Função Sinc.png", format="png")
    plt.show()