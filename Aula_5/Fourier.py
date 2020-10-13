import numpy as np
import matplotlib.pyplot as plt

a = 0.5
w = np.arange(-1*np.pi, 1*np.pi, np.pi/100)

num = 1
den = 1 - a * np.exp(-1j*w) # 1-a^(-j*w) 
x = num/den

mod_x = np.absolute(x)
fase_x = np.angle(den)

plt.figure("Transformada de Fourier",figsize=(15,8))
plt.subplot(211)
plt.plot(mod_x)
plt.title('Modulo')
plt.grid(True)

plt.subplot(212)
plt.plot(fase_x)
plt.title('Fase')
plt.grid(True)


plt.tight_layout()
plt.savefig("tfd.png", format="png")
plt.show()