import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
fig.suptitle('FFT', fontsize=16)
ax.remove()

# Função x(t)
amplitudes_f_t = [2, 0.5]
frequencias_f_t = [1, 10]

t = np.linspace(0, 10, 500)
f_t = amplitudes_f_t[0] * np.cos(frequencias_f_t[0]*2*np.pi*t)
f_t += amplitudes_f_t[1] * np.cos(frequencias_f_t[1]*2*np.pi*t)
f_t += np.exp(t * 0.2)

plt.subplot(2, 1, 1)
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

plt.subplot(2, 1, 2)
plt.xlabel("Frequência (Hz)")
plt.ylabel("Amplitude")
plt.bar(frequencias, amplitudes, width=1.5)
plt.title('FFT (Fast Fourier Transformation)')

# Ajustar espaçamento entre subplots
plt.tight_layout()
# Mostrar os gráficos
plt.show()