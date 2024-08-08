# 13.8 배열의 합 구하기

import numpy as np
x = np.random.randint(10, size=5)
y = np.random.randint(10, size=(3, 4))
print(x)
print(y)
x_sum = np.sum(x)
y_sum = np.sum(y)
col_mean = np.mean(y, axis = 0)
row_mean = np.mean(y, axis = 1)
print(x_sum)
print(y_sum)
print(col_mean)
print(row_mean)
