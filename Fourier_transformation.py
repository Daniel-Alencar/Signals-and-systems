import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
fig.suptitle('FFT', fontsize=16)
ax.remove()

# Função x(t)
t = np.linspace(0, 0.5, 500)
f_t = np.sin(t * 100)

plt.subplot(3, 1, 1)
plt.xlabel('t')
plt.ylabel('x(t)')
plt.plot(t, f_t)
plt.title('Função f(x)')

# Transformada de Fourier em x(t)
fft = np.fft.fft(f_t)
T = t[1] - t[0]
N = f_t.size

f = np.fft.fftfreq(len(f_t), T)
frequencias = f[0 : N // 2]
amplitudes = np.abs(fft)[0 : N // 2] * 1 / N

plt.subplot(3, 1, 2)
plt.xlabel("Frequência (Hz)")
plt.ylabel("Amplitude")
plt.bar(frequencias, amplitudes, width=1.5)
plt.title('FFT (Fast Fourier Transformation)')

# Espectro:
# - Eixo x: tempo
# - Eixo y: frequência
# - Escala de cores: amplitude

plt.subplot(3, 1, 3)
plt.ylabel('Frequência (Hz)')
plt.xlabel('Tempo (s)')
plt.specgram(f_t, NFFT=N-1, Fs=1/T, scale='linear', scale_by_freq=False)
plt.colorbar()
plt.title('Espectro: Tempo, frequência e amplitude')

# Ajustar espaçamento entre subplots
plt.tight_layout()
# Mostrar os gráficos
plt.show()