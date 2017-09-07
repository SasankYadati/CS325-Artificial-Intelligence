import numpy as np
import random

a = np.random.normal(0, 0.1, 750)
b = np.random.laplace(0, 1., 250)
x = np.concatenate([a, b])

np.random.seed(42)
random.shuffle(x)

for _ in x:
    print(_)

