import sympy as smp
import numpy as np
import matplotlib.pyplot as plt

from sympy import Piecewise
from sympy import I

# Definindo algumas funções conhecidas
t = smp.symbols('t', real=True)
T_variable = smp.symbols('T', real=True)

u_t = Piecewise((0, t < 0), (1, t >= 0))

# Definindo variáveis e constantes
a = smp.symbols('a', real=True)
a = 5

# Definindo função x(t)
x_t = smp.exp(a*(-t)) * u_t
x_t = x_t.simplify()

# Transformando em uma função Lambda
try:
  # Tenta avaliar a função em um ponto específico
  x_t_function = smp.lambdify(t, x_t.args[1][0], 'numpy')
  y = x_t_function(1)
  print("Prossiga normalmente!")
    
except Exception as error:
  print(f"Erro: {error}")

  # Defina a função explicitamente
  print("Você deve definir a função explicitamente!")
  def x_t_function(t):
    return t


# Transformada de Fourier
w = smp.symbols('w', real=True)

function_t = x_t * smp.exp(-I*w*t)
function_t = function_t.simplify()

# Definição de intervalos da integral
intervals = (0, +smp.oo)

function_to_integrate = function_t.args[1][0]
all_result = smp.integrate(function_to_integrate, (t, intervals[0], intervals[1]))

# Função que será avaliada pela transformada de Fourier
result = all_result.args[0][0]

# Plotagem
# Separação módulo e fase da função
f_abs = smp.Abs(result)
f_phase = smp.arg(result)

try:
  # Tenta avaliar a função em um ponto específico
  abs_function = smp.lambdify(w, f_abs, 'numpy')
  y = abs_function(1)
  print("Prossiga normalmente!")
    
except Exception as error:
  print(f"Erro: {error}")

  # Defina a função explicitamente
  print("Você deve definir a função explicitamente!")
  def abs_function(w):
    return w

try:
  # Tenta avaliar a função em um ponto específico
  phase_function = smp.lambdify(w, f_phase, 'numpy')
  y = phase_function(1)
  print("Prossiga normalmente!")
    
except Exception as error:
  print(f"Erro: {error}")

  # Defina a função explicitamente
  print("Você deve definir a função explicitamente!")
  def phase_function(w):
    return w

# Avaliando valores das funções
for i in range(1, 10):
  value1 = abs_function(i)
  value2 = phase_function(i)
  print(f"{value1} e {value2}")

# Geração de valores
w_values = np.linspace(-2*2*np.pi, 2*2*np.pi, 100)

# Gerar valores para o módulo e fase do sinal
X_w_abs = abs_function(w_values)
X_w_phase = phase_function(w_values)

# Plotar os gráficos
# plt.plot(w_values, X_w_abs, label='Módulo')
# plt.plot(w_values, X_w_phase, label='Fase')
# plt.xlabel('w')
# plt.ylabel('X(w)')
# plt.title('Transformada de Fourier')
# plt.legend()
# plt.grid(True)
# plt.show()