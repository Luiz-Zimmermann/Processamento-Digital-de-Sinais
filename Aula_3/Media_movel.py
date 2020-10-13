
import numpy as np
import matplotlib.pyplot as plt

# Função que realiza a média movel
def media_movel(a, n) : 
    ret = np.cumsum(a, dtype='int16') 
    ret[n:] = ret[n:] - ret[:-n] 
    return ret[n - 1:] / n



file = "sweep.pcm"

# Abre o arquivo 
with open (file, 'rb') as f:   
    buf = f.read ()
    data = np.frombuffer (buf, dtype = 'int16') 
  
k = int(input("Digite o tamanho de média Ex.(4, 8, 16, 32, 64):"))

new_data = media_movel(data, k)

plt.figure(figsize=[10, 5])
#Plota o original
plt.subplot(211)
plt.title("Entrada")
plt.grid(True)
plt.plot(data)



#Plota a media
plt.subplot(212)
plt.title("Saida")
plt.grid(True)
plt.plot(new_data)
plt.tight_layout()

plt.savefig("Media_movel.png", format="png")

plt.show()

with open("media_movel.pcm", "wb") as new_file:
    for x in new_data:
        new_file.write(x)
new_file.close()