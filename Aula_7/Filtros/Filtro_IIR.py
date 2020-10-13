import numpy as np
import matplotlib.pyplot as matp
from matplotlib import patches
from matplotlib.pyplot import axvline, axhline
from collections import defaultdict

# Copyright (c) 2011 Christopher Felton
def zplane(z, p):
    """Plot the complex z-plane given zeros and poles.
    """

    # get a figure/plot
    ax = matp.subplot(4, 1, 4)

    # Add unit circle and zero axes
    unit_circle = patches.Circle((0, 0), radius=1, fill=False,
                                 color='black', ls='solid', alpha=0.1)
    ax.add_patch(unit_circle)
    axvline(0, color='0.7')
    # Plot the poles and set marker properties
    poles = matp.plot(p.real, p.imag, 'x', markersize=9, alpha=0.5)

    # Plot the zeros and set marker properties
    zeros = matp.plot(z.real, z.imag, 'o', markersize=9,
                     color='none', alpha=0.5,
                     # same color as poles
                     markeredgecolor=poles[0].get_color(),
                     )

    # Scale axes to fit
    r = 1.5 * np.amax(np.concatenate((abs(z), abs(p), [1])))
    matp.axis('scaled')
    matp.axis([-r, r, -r, r])

    matp.savefig("planoZ.png", format="png")


    print("Zeros: ", z)
    print("Polos: ", p)
    
    matp.show()





Fs = float(input("Fs: "))
fc = float(input("Fc: "))

wc = 2*np.pi*fc
Fl = 2*Fs

a = wc/(Fl+wc)
b = (wc-Fl)/(Fl+wc)

print("a: ",a)
print("b: ",b)

prev_entrada = 0
prev_saida = 0

# Le o arquivo
with open ("Sweep10_3600.pcm", "rb") as input_f:   
    buf = input_f.read ()
    data = np.frombuffer (buf, dtype = 'int16') 

# Cria o vetor de saida zerado
output_data = np.zeros_like(data, dtype="int16")

# Aplica o filtro
for i in range(len(data)):

    y = 0
    input = data[i]
    # Calcula o valor na saida
    y = a*input + a*prev_entrada - b*prev_saida

    # Deslocamento
    prev_saida = y
    prev_entrada = input
    output_data[i] = y

# Escreve no arquivo
with open ("sai_sweep_mm_4.pcm", "wb") as output:    
    for x in output_data:
        output.write(x)
output.close()

#Zero = wcz + wc
#Polo = Flz + wcz + wc - Fl
zero = [0, wc, wc]
polo = [0,(Fl+wc),(wc-Fl)]

z = np.roots(zero)
p = np.roots(polo)
print(z,p)
#zplane(z,p)

# Nome e tamanho da janela a ser aberta
matp.figure(u"Gráfico da transformada Z",figsize=(15,8))

# Plota os gráficos
matp.subplot(411)
matp.title(u"Gráfico input")
matp.xlabel("amostra")
matp.ylabel("Amplitude")
matp.grid(1)
matp.plot(data)

matp.subplot(412)
matp.title(u"Gráfico output")
matp.xlabel("amostra")
matp.ylabel("Amplitude")
matp.grid(1)
matp.plot(output_data)

matp.subplot(413)
matp.title(u"Gráfico input e output")
matp.xlabel("amostra")
matp.ylabel("Amplitude")
matp.grid(1)
matp.plot(data)
matp.plot(output_data)

# Ajusta as posições dos gráficos 
matp.tight_layout()

# Mostra os gráficos
matp.show()