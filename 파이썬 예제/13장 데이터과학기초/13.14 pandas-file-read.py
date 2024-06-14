# 13.14 판다스로 파일 읽기

import pandas as pd
pop = pd.read_csv("population.csv")
print(pop)
print(pop["gu"])
print(pop["population"])
