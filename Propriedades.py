import tkinter as tk
import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

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
  )
  label.grid(column=0, row=(2 * (i + 1)))

  props[i]["Label"] = label




def slider_changed(value):
  print("Valor selecionado:", value)
  # Converte o valor do slider para um número
  slider_value = float(value)
  
  # Atualiza os dados do gráfico com base no valor do slider
  y1 = np.sin(x1 * slider_value)
  line1.set_ydata(y1)
  y2 = np.sin(x2 * slider_value)
  line2.set_ydata(y2)

  canvas.draw()



# Cria um slider
slider = tk.Scale(
  janela, 
  from_=0, to=100, 
  orient=tk.HORIZONTAL, 
  command=slider_changed
)
slider.grid(column=0, row=7)



# Cria uma figura do Matplotlib
fig = Figure(figsize=(6, 6), dpi=100)

# Cria o primeiro subplot
ax1 = fig.add_subplot(211)
x1 = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x1)

line1, = ax1.plot(x1, y1)
ax1.set_title("Gráfico 1")

# Cria o segundo subplot
ax2 = fig.add_subplot(212)
x2 = np.linspace(0, 2 * np.pi, 100)
y2 = np.cos(x2)

line2, = ax2.plot(x2, y2)
ax2.set_title("Gráfico 2")

# Cria um widget do Matplotlib para exibir a figura na interface
canvas = FigureCanvasTkAgg(fig, master=janela)
canvas.get_tk_widget().grid(column=1, row=1, rowspan=len(props * 2))




# Inicia o loop principal da aplicação
janela.mainloop()
