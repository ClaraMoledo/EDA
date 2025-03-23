import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1, -0.5], [1, 1]])
b = np.array([0.5, 2])

solucao = np.linalg.solve(A, b)
x, y = solucao

print(f"Solução do sistema:")
print(f"x = {x}")
print(f"y = {y}")

# Plotagem das equações
x_valores = np.linspace(-1, 3, 100)

# Primeira equação: y = 0.5x + 0.5
y1 = 0.5 * x_valores + 0.5

# Segunda equação: y = -x + 2
y2 = -x_valores + 2

plt.figure(figsize=(10, 6))
plt.plot(x_valores, y1, color='blue',label='y = 0.5x + 0.5')
plt.plot(x_valores, y2,color='green', label='y = -x + 2')
plt.scatter(x, y, color='red', s=100, label=f'Solução ({x}, {y})')
plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='black', linestyle='-', alpha=0.3)
plt.grid(True, alpha=0.3)
plt.legend()
plt.title('Sistema de Equações Lineares')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.show()