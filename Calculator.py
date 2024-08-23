import numpy as np # import Numpy library to generate

z = (0.5)*0.55+(-0.35)*0.45+0.15
sigmoid = 1.0 / (1.0 + np.exp(-z))
print(z)
print(sigmoid)