import numpy as np
from numpy import pi, cos, sin, log10
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, subplot, xlabel, ylabel, title, grid, axis, figure, show
from scipy.signal import freqz


def gera_coef(M, fc):
    # 0 to M
    i1 = np.arange(10 ** -9, M, 1.)

    # Eq diretamente 16-4
    h1 = (sin(2 * pi * fc * (i1 - M / 2)) / (i1 - M / 2)) * (
                0.42 - 0.5 * cos(2 * pi * i1 / M) + 0.08 * cos(4 * pi * i1 / M))

    # normalize
    h1 = h1 / np.sum(h1)

    return h1

sample_rate = 8000

# definindo a frequencia de corte
# tem que estar entre 0 e 0.5
fc1 = float(input("frequencia de corte PB: "))/sample_rate
fc2 = float(input("frequencia de corte PA: "))/sample_rate

# definindo o roll-off
# BW é a largura em samples da banda de transição
# Tem que estar em 0 e 0.5
BW = 100/sample_rate
M = 4 / BW
print(M)


# filtro PA
h_pa = gera_coef(M, fc1)
h_pa = -h_pa
h_pa[int(M/2)] += 1

# filtro PB
h_pb = gera_coef(M, fc2)

# filtro PF
h_pf = np.convolve(h_pa, h_pb, mode="same")

# salva coeficientes
coefs_name = "coefs_pf.dat"
with open(coefs_name, 'w') as f:
    for d in h_pf:
        f.write(str(d.astype(np.float16))+",\n")

read_path = "swip.pcm"
with open(read_path, 'rb') as f:
    buf = f.read()
    data_i = np.frombuffer(buf, dtype='int16')
    data_len = len(data_i)

    # replica do arquivo lido para salvar o resultado
    data_o = np.convolve(h_pf, data_i)
    data_o = data_o.astype(dtype='int16')


# amostra de 100 ms
t = np.arange(0, data_len/sample_rate, 1 / sample_rate)

###############
#   plot
subplot(2, 1, 1)
plt.plot(t, data_i[: len(t)], label="Input")
plt.plot(t, data_o[: len(t)], label="Output")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

# grafico em frequencia
[w1, h1] = freqz(h_pa, worN=sample_rate, fs=sample_rate)
[w2, h2] = freqz(h_pb, worN=sample_rate, fs=sample_rate)

subplot(2, 1, 2)
# Se plotar em dB, descomentar a seguir
# plot(w1, 20 * log10(abs(h1)), label="freqz1")
# plot(w2, 20 * log10(abs(h2)), label="freqz2")
plot(w1, abs(h1), label="PA")
plot(w2, abs(h2), label="PB")
plt.legend()
plt.xlabel("Freq")
plt.ylabel("Amplitude")

file_name = "filtro_pf.pcm"
with open(file_name, 'wb') as f:
    for d in data_o:
        f.write(d)
        
plt.tight_layout()
grid()
show()

