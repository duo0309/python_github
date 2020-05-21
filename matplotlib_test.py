import numpy as np
import matplotlib.pyplot as plt
plt.style.use('classic')


# ------------------------------------------
# 0 dimension plot
# ------------------------------------------
r = np.random.randn(100)

plt.plot(r, 'o')
plt.show()


# ------------------------------------------
# 1 dimension plot
# ------------------------------------------
x = np.arange(0, 100, 2)
y = np.log(x)

[plt.plot(x, y+i, 'o') for i in range(10)]
plt.show()

# ------------------------------------------
# 2 dimension plot
# ------------------------------------------


def f(x, y):
    return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)


x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.contourf(X, Y, Z, 20, cmap='RdGy')
plt.colorbar()
plt.show()
