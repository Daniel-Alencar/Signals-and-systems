import tkinter as tk
import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.style as style

from Fourier_signal import w_values, X_w_abs, X_w_phase
from Fourier_signal import abs_function, phase_function

props = [
  {
    "title": "Linearidade"
  },
  {
    "title": "Dualidade Tempo-Frequência"
  },
  {
    "title": "Escalonamento"
  },
  {
    "title": "Deslocamento no tempo"
  },
  {
    "title": "Deslocamento na frequência"
  },
]

# Cria a janela principal
janela = tk.Tk()
janela.title("Propriedades da transformada de Fourier")

# Define as cores do tema escuro
# cor de fundo
cor_background = "#000000"
# cor do texto
cor_texto = "#FFFFFF"
# cor das bordas  
cor_borda = "#333333"

# Configura as cores do tema escuro
janela.configure(bg=cor_background)
janela.option_add("*Background", cor_background)
janela.option_add("*Foreground", cor_texto)
janela.option_add("*Font", "Arial 10")
janela.option_add("*Button.relief", "raised")
janela.option_add("*Button.activeBackground", cor_borda)
janela.option_add("*Button.activeForeground", cor_texto)


subtitle = tk.Label(
  janela, 
  text="Propriedades", 
  font=("Arial", 14, "bold"),
  padx=10,
  pady=10
)
subtitle.grid(column=0, row=0)




for i in range(5):
  label = tk.Label(
    janela,
    text=props[i]["title"],
    padx=20
  )
  label.grid(column=0, row=(2 * (i + 1)))

  props[i]["Label"] = label




def slider_changed(value):
  # Converte o valor do slider para um número
  slider_value = float(value)
  
  # Atualiza os dados do gráfico com base no valor do slider
  X_w_abs = abs_function(w_values * slider_value)
  line1.set_ydata(X_w_abs)
  X_w_phase = phase_function(w_values * slider_value)
  line2.set_ydata(X_w_phase)

  canvas.draw()



# Cria um slider
slider = tk.Scale(
  janela, 
  from_=-50, to=50, 
  orient=tk.HORIZONTAL, 
  command=slider_changed
)
slider.grid(column=0, row=7)





# Define o estilo escuro
style.use('dark_background')

# Cria uma figura do Matplotlib
fig = Figure(figsize=(6, 6), dpi=100)

# Cria o primeiro subplot
ax1 = fig.add_subplot(211)

line1, = ax1.plot(w_values, X_w_abs, label="Módulo")
ax1.legend()
ax1.grid()
ax1.set_title("Gráfico 1")

# Cria o segundo subplot
ax2 = fig.add_subplot(212)

line2, = ax2.plot(w_values, X_w_phase, label="Fase")
ax2.legend()
ax2.grid()
ax2.set_title("Gráfico 2")

# Cria um widget do Matplotlib para exibir a figura na interface
canvas = FigureCanvasTkAgg(fig, master=janela)
canvas.get_tk_widget().grid(column=1, row=1, rowspan=len(props * 2))




# Inicia o loop principal da aplicação
janela.mainloop()
