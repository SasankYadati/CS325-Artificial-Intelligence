import numpy as np
import random

a = [[_, 0] for _ in np.random.normal(0, 0.1, 950)]
b = [[_, 1] for _ in np.random.laplace(0, 1., 50)]
x = np.concatenate([a, b])

np.random.shuffle(x)

for i in x:
    print(i[0], i[1], sep='    ')
