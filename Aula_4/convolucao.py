import numpy as np
import matplotlib.pyplot as plt




h = [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125]

# Impulso
xUnitario = [1, 0, 0, 0, 0, 0]
impulso = np.zeros(6)
impulso[0] = 1

plt.figure("Convoluções",figsize=(15,6))

plt.subplot(311)
plt.title("Impulso unitário")
plt.grid(True)
plt.stem(np.convolve(impulso, h))
#plt.xticks(np.arange(-1, 12.1, 1))
#plt.yticks(np.arange(0, 0.2, 0.05))

# Degrau unitário
xDegrau = [1, 1, 1, 1, 1, 1]
degrau = np.ones(6)

plt.subplot(312)
plt.title("Degrau unitário")
plt.grid(True)
plt.stem(np.convolve(degrau, h))
#plt.xticks(np.arange(-1, 12.1, 1))
#plt.yticks(np.arange(0, 1.1, 0.2))

# Seno
#seno = [1, 0.5, 0.25, 0.125]
seno = np.array([1, 0.5, 0.25, 0.125])

plt.subplot(313)
plt.title("Seno")
plt.grid(True)
plt.stem(np.convolve(seno, h))
#plt.xticks(np.arange(-1, 10.1, 1))
#plt.yticks(np.arange(0, 0.5, 0.1))


plt.tight_layout()


# Salvando os gráficos
plt.savefig("Convolucoes.png", format="png")

plt.show()