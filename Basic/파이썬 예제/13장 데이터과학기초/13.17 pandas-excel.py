# 13.17 엑셀 파일에 데이터 프레임 저장하기

import pandas as pd
import openpyxl
item = {'City' : ['Seoul', 'Tokyo', 'Paris', 'New York'],
       'Nation' : ['Korea', 'Japan', 'France', 'USA']}
city = pd.DataFrame(item, index=['KR', 'JP', 'FR', 'US'])
city.to_excel('city.xlsx', sheet_name='city')
