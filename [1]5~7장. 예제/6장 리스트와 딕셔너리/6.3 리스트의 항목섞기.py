# 리스트 항목의 순서를 바꾼다

import random
menu = ['apple', 'banana','pineapple','grape','strawberry']
print(menu)
print()
random.shuffle(menu)
print(menu)
random.shuffle(menu)
print(menu)
for i in range(10):
    print(random.choice(menu))