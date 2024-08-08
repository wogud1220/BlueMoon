# 13.7 난수로 배열 생성하기
import numpy as np
x = np.random.randint(10, size=(3, 4))
print(x)
col_max = np.amax(x, axis=0)  # 각 열의 최대값
print("col_max", col_max)
row_max = np.amax(x, axis=1)  # 각 행의 최대값
print("row_max", row_max)
col_min = np.amin(x, axis=0)  # 각 열의 최소값
print("col_min", col_min)
row_min = np.amin(x, axis=1)  # 각 행의 최소값
print("row_min", row_min)
max_pos = np.argmax(x)         # 배열의 최대값의 위치
min_pos = np.argmin(x)         # 배열의 최소값의 위치
col_max_pos = np.argmax(x, axis=0)  # 배열의 열에서 최대값의 위치
row_min_pos = np.argmin(x, axis=1)  # 배열의 행에서 최소값의 위치
print("max_pos", max_pos)
print("min_pos", min_pos)
print("col_max_pos", col_max_pos)
print("row_min_pos", row_min_pos)
