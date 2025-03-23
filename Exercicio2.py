import numpy as np
import matplotlib.pyplot as plt

# Equação: 2x² + 2x - 6 = 0
a = 2
b = 2
c = -6

# Cálculo do discriminante
delta = b**2 - 4*a*c
print(f"Discriminante (Δ) = {delta}")

# Cálculo das raízes usando a fórmula de Bhaskara
if delta < 0:
    print("A equação não possui raízes reais.")
elif delta == 0:
    x = -b / (2*a)
    print(f"A equação possui uma raiz real: x = {x}")
else:
    x1 = (-b + np.sqrt(delta)) / (2*a)
    x2 = (-b - np.sqrt(delta)) / (2*a)
    print(f"A equação possui duas raízes reais:")
    print(f"x₁ = {x1}")
    print(f"x₂ = {x2}")

# Plotagem da função
x_valores = np.linspace(-5, 5, 1000)
y_valores = a * x_valores**2 + b * x_valores + c

plt.figure(figsize=(10, 6))
plt.plot(x_valores, y_valores, label=f'{a}x² + {b}x + {c}')
plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='black', linestyle='-', alpha=0.3)

# Marcação das raízes se existirem
if delta >= 0:
    if delta > 0:
        plt.scatter([x1, x2], [0, 0], color='red', s=100, label=f'Raízes: x₁={x1:.2f}, x₂={x2:.2f}')
    else:
        plt.scatter([x], [0], color='red', s=100, label=f'Raiz: x={x:.2f}')

plt.grid(True, alpha=0.3)
plt.legend()
plt.title('Equação do Segundo Grau: 2x² + 2x - 6 = 0')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.ylim(-10, 30)
plt.show()