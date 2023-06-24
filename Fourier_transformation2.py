import numpy as np
import matplotlib.pyplot as plt

# Criando uma função de exemplo
def minha_funcao(x):
    return np.sin(2 * np.pi * x) + 0.5 * np.sin(10 * np.pi * x)

# Criando os pontos no eixo x
x = np.linspace(0, 1, 5000)

# Calculando a transformada de Fourier da função
transformada = np.fft.fft(minha_funcao(x))

# Frequências correspondentes à transformada
frequencias = np.fft.fftfreq(len(x))

# Plotando a função original
plt.subplot(2, 1, 1)
plt.plot(x, minha_funcao(x))
plt.title('Função Original')

# Plotando a transformada de Fourier
plt.subplot(2, 1, 2)
plt.plot(frequencias, np.abs(transformada))
plt.title('Transformada de Fourier')
plt.xlabel('Frequência')
plt.ylabel('Amplitude')

# Exibindo o gráfico
plt.tight_layout()
plt.show()
