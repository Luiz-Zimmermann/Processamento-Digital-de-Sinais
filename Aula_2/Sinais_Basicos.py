import numpy as np
import matplotlib.pyplot as plt

def impulso():

    imp = np.zeros(10)
    imp[0] = 1

    plt.subplot(2, 3, 1)
    plt.title(u'Impulso unitario')
    plt.grid(True)
    plt.ylabel('Amplitude')
    plt.xlabel('tempo')
    plt.stem(imp)

def degrau():

    deg = np.ones(10)

    plt.subplot(2, 3, 2)
    plt.title(u'Degrau unitario')
    plt.grid(True)
    plt.ylabel('Amplitude')
    plt.xlabel('tempo')
    plt.stem(deg)

def sinusoidal():
    A = 1
    n = np.arange(-30,30,1)
    f = 200
    Fs = 8000

    sin = A * np.sin(2*np.pi*n*(f/Fs))

    plt.subplot(2, 3, 3)
    plt.title(u'Sinusoidal')
    plt.grid(True)
    plt.ylabel('Amplitude')
    plt.xlabel('tempo')
    plt.stem(n,sin)

def exponencial():

    n = np.arange(0, 10, 0.2)

    exp = 1 * 0.5 ** n

    plt.subplot(2, 3, 4)
    plt.title(u'Exponencial a = 0,5')
    plt.grid(True)
    plt.ylabel('Amplitude')
    plt.xlabel('tempo')
    plt.stem(exp)
    
    exp = 1 * -0.5 ** n

    plt.subplot(2, 3, 5)
    plt.title(u'Exponencial a = -0,5')
    plt.grid(True)
    plt.ylabel('Amplitude')
    plt.xlabel('tempo')
    plt.stem(exp)
    
    exp = 1 * 2 ** n

    plt.subplot(2, 3, 6)
    plt.title(u'Exponencial a = 2')
    plt.grid(True)
    plt.ylabel('Amplitude')
    plt.xlabel('tempo')
    plt.stem(exp)
    
    



if __name__ == "__main__":
    plt.figure(u'Sinais Basicos', figsize=(10, 6))
    impulso()
    degrau()
    sinusoidal()
    exponencial()
    plt.tight_layout()
    plt.savefig("Sinais basicos.png", format="png")
    plt.show()
