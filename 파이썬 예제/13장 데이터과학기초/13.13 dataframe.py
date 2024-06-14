# 13.13 데이터 프레임 생성하기

import pandas as pd
item = {'City' : ['Seoul', 'Tokyo', 'Paris', 'New York'],
        'Nation' : ['Korea', 'Japan', 'France', 'USA']}
city = pd.DataFrame(item)
city2 = pd.DataFrame(item, index=['KR', 'JP', 'FR', 'US'])
print(city)
print(city2)
