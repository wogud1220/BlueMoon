# 13.15 판다스 배열에서 최대값, 최소값 출력하기

import pandas as pd
pop = pd.read_csv("population.csv")
print("population max", pop["population"].max())
print("population min", pop["population"].min())
print("area max", pop["area"].max())
print("area min", pop["area"].min())
print("density max", pop["density"].max())
print("density min", pop["density"].min())
