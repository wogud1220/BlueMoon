import numpy as np

first = np.arange(2, 10)
second = np.arange(1, 10)

for i in range (0, first.size):
    print(second*first[i])
