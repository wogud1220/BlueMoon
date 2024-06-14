# 13.10 로그함수, 1차함수, 2차함수, 지수함수 그리기

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(1,10)
y0 = np.log(x)
y1 = x
y2 = x**2
y3 = 2**x
plt.plot(x, y0, x, y1, x, y2, x, y3)
plt.show()
