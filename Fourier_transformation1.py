import numpy as np
import sympy as smp
import matplotlib.pyplot as plt

# Definindo variáveis e constantes
from sympy import I
t, a = smp.symbols('t a', real=True)
a = 5

# Função
x_t = smp.exp(-a*t)

# Transformada de Fourier
w = smp.symbols('w', real=True)
function_t = x_t * smp.exp(-I*w*t)
result = smp.integrate(function_t, (t, 0, smp.oo))

f_abs = smp.Abs(result)
f_phase = smp.arg(result)

print("Módulo:")
smp.pprint(f_abs)

print("Fase:")
smp.pprint(f_phase)

# Plotagem
w_values = np.linspace(1, 2, 10)

X_w_values = []
for value in w_values:
  value_response = result.subs(w, value)
  print(value_response)
  X_w_values.append(value_response)
