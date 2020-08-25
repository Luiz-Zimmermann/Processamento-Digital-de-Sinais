import numpy as np
import matplotlib.pyplot as matp

# Ganho que será aplicado ao áudio
gain = 0.5

# Taxa de amostragem do áudio
rate = 8000

# Arquivo (na mesma pasta que o arquivo .py) que se deseja manipular
path = "alo.pcm"

try:
    # Abrindo o arquivo que será manipulado
    with open (path, "rb") as file:
        buffer = file.read()
        file.close()
except:
    print("Erro ao abrir arquivo!! Verifique se ele existe no mesmo local que este programa!!")
    exit(0)

# Criando uma variável que receberá o conteúdo formatado, do arquivo que está sendo manipulado
original_data = np.frombuffer(buffer, dtype = "int16")
len_data = len(original_data)

# Executa o filtro, aplicando um ganho de 0.5 ao áudio original
final_data = np.ones_like(original_data)
for i in range(len_data):
    final_data[i] = original_data[i] * gain

# Calcula o tempo do áudio divindo o tamanho da amostra pela taxa de amostragem,
# com passo de 1/taxa de amostragem, para ser utilizado no gráfico
time = np.arange(0, len_data/rate, 1/rate)

# Nome e tamanho da janela a ser aberta
matp.figure(u"Gráfico do audio: "+path,figsize=(15,8))

# Plota os gráficos
matp.subplot(311)
matp.title(u"Gráfico Áudio original")
matp.xlabel("Time [s]")
matp.ylabel("Amplitude")
matp.grid(1)
matp.plot(time,original_data)

matp.subplot(312)
matp.title(u"Gráfico Áudio pós filtro")
matp.xlabel("Time [s]")
matp.ylabel("Amplitude")
matp.grid(1)
matp.plot(time,final_data,color='orange')

matp.subplot(313)
matp.title(u"Gráficos transpostos")
matp.xlabel("Time [s]")
matp.ylabel("Amplitude")
matp.grid(1)
matp.plot(time,original_data)
matp.plot(time,final_data)

# Ajusta as posições dos gráficos 
matp.tight_layout()

path = path.split(".")

# Salva o áudio alterado

with open(path[0]+"-after_filter."+path[1], "wb") as new_file:
    for data in final_data:
        new_file.write(data)
    new_file.close()

# Salva os gráficos
matp.savefig(path[0]+"-Graficos.png", format="png")

# Mostra os gráficos
matp.show()