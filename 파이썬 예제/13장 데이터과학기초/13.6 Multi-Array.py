# 다양한 차원의 행렬 생성하기
import numpy as np
x = np.full(2, 5)  
y = np.full((3, 4), fill_value = 1)
z = np.full((3, 4, 5), fill_value = 3)
print(x, end='\n\n')
print(y, end='\n\n')
print(z, end='\n\n')
print("ndim ", x.ndim, y.ndim, z.ndim)
print("shape ", x.shape, y.shape, z.shape)
print("size ", x.size, y.size, z.size)
