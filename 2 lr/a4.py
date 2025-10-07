import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 200)
y = x ** 2

plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$y = x^2$')
plt.title('График функции y = x²')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()