from scipy.signal import freqz
import scipy.signal as signal
import numpy as np

import matplotlib.pyplot as plt


# Exercicio a
num = [3, -1.2]
den = [1, -1.4, 0.45]
w, h = freqz(num, den)
plt.subplot(3, 1, 1)
plt.grid(True)
plt.title("Questão A")
plt.plot(w, 20 * np.log10(abs(h)))

# Exercicio b
num = [1, 0]
den = [1, -2.1, 1.08]
w, h = freqz(num, den)
plt.subplot(3, 1, 2)
plt.grid(True)
plt.title("Questão B")
plt.plot(w, 20 * np.log10(abs(h)))

# Exercicio c
num = [1, 0.9]
den = [1, 1, 0.41]
w, h = freqz(num, den)
plt.subplot(3, 1, 3)
plt.grid(True)
plt.title("Questão C")
plt.plot(w, 20 * np.log10(abs(h)))

plt.tight_layout()

plt.show()