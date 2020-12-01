import numpy as np
import matplotlib.pyplot as matp
from matplotlib import patches
from matplotlib.pyplot import axvline, axhline
from collections import defaultdict
from zplane import zplane

def passa_baixa(input_data, output_data, Fs, fc):

    wc = 2*np.pi*fc
    Fl = 2*Fs

    a = wc/(Fl+wc)
    b = (wc-Fl)/(Fl+wc)

    print("a: ",a)
    print("b: ",b)

    xm1 = 0
    ym1 = 0

    # Aplica o filtro
    for i in range(len(input_data)):

        y = 0
        input = input_data[i]
        # Calcula o valor na saida
        y = a*input + a*xm1 - b*ym1

        # Deslocamento
        ym1 = y
        xm1 = input
        output_data[i] = y
    
    return output_data 
    
# Filtro passa alta usando um filtro passa baixa
def passa_alta(input_data, output_data, Fs, fc):   
    output_data = input_data - passa_baixa(input_data, output_data, Fs, fc)
    return output_data

def passa_faixa(input_data, output_data, Fs, fc1, fc2):
    
    pb = passa_baixa(input_data, output_data, Fs, fc1)
    pa = passa_alta(input_data, output_data, Fs, fc2)
    output_data = np.convolve(pb, pa)

    matp.subplot(211)
    matp.title(u"Gráfico passa baixa")
    matp.xlabel("amostra")
    matp.ylabel("Amplitude")
    matp.grid(1)
    matp.plot(pb)

    matp.subplot(212)
    matp.title(u"Gráfico passa alta")
    matp.xlabel("amostra")
    matp.ylabel("Amplitude")
    matp.grid(1)
    matp.plot(pa)
    matp.tight_layout()
    
    return output_data

def rejeita_faixa(input_data, output_data, Fs, fc1, fc2):
    output_data = passa_alta(input_data, output_data, Fs, fc2) + passa_baixa(input_data, output_data, Fs, fc1)
    return output_data
    


if __name__ == "__main__":

    # Pega valores do usuario
    print("Escolha uma opção de filtro:")
    print("1 - Passa baixa. 2 - Passa alta. 3 - Passa faixa. 4 - Rejeita faixa.")
    opcao = int(input("Opção: "))
    Fs = float(input("Fs: "))
    
    # Le o arquivo
    with open ("Sweep10_3600.pcm", "rb") as input_f:   
        buf = input_f.read ()
        data = np.frombuffer (buf, dtype = 'int16') 

    # Cria o vetor de saida zerado
    output_data = np.zeros_like(data, dtype="int16")

    if opcao == 1:
        fc = float(input("Fc: "))
        output_data = passa_baixa(data, output_data, Fs, fc)
    elif opcao == 2:
        fc = float(input("Fc: "))
        output_data = passa_alta(data, output_data, Fs, fc)
    elif opcao == 3:
        fc = float(input("Fc baixa: "))
        fc2 = float(input("Fc alta: "))
        output_data = passa_faixa(data, output_data, Fs, fc, fc2)
    else:
        fc = float(input("Fc baixa: "))
        fc2 = float(input("Fc alta: "))
        output_data = rejeita_faixa(data, output_data, Fs, fc, fc2)


    # Escreve no arquivo
    with open ("sweep_out.pcm", "wb") as output:    
        for x in output_data:
            output.write(x)
    output.close()


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