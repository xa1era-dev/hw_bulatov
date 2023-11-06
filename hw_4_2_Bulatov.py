import matplotlib.pyplot as plt
import numpy as np

def func(x : float):
    return np.cos(x) + np.log(x)

r = np.arange(0, 50, 0.1)

plt.plot(r, [func(i) for i in r])
plt.show()