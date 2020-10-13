import numpy as np
import matplotlib.pyplot as matp
from matplotlib import patches
from matplotlib.pyplot import axvline, axhline
from collections import defaultdict
from zplane import zplane

# Pega valores do usuario
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
zero = np.array([0, wc, wc])
polo = np.array([0,(Fl+wc),(wc-Fl)])

z = np.roots(zero)
p = np.roots(polo)
print(z,p)
zplane(zero,polo)

# Nome e tamanho da janela a ser aberta
matp.figure(u"Gráfico da transformada Z",figsize=(15,8))

# Plota os gráficos
matp.subplot(311)
matp.title(u"Gráfico input")
matp.xlabel("amostra")
matp.ylabel("Amplitude")
matp.grid(1)
matp.plot(data)

matp.subplot(312)
matp.title(u"Gráfico output")
matp.xlabel("amostra")
matp.ylabel("Amplitude")
matp.grid(1)
matp.plot(output_data)

matp.subplot(313)
matp.title(u"Gráfico input e output")
matp.xlabel("amostra")
matp.ylabel("Amplitude")
matp.grid(1)
matp.plot(data)
matp.plot(output_data)

# Ajusta as posições dos gráficos 
matp.tight_layout()

# Salva os graficos
matp.savefig("Filtro_PB.png", format="png")

# Mostra os gráficos
matp.show()