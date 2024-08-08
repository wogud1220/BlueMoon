# 재귀를 이용한 값 검색 함수

def search(lst, key):
    if not lst:         	# 빈 리스트인 경우 
        return False
    elif lst[0] == key: 	# 찾고자 하는 원소를 찾은 경우
        return True
    else:               	# 리스트 나머지 부분에 대해서 검색 
        return search(lst[1:], key)


print(search([35, 28, 30, 29, 33, 31, 30], 30))

# 리스트 내의 값의 위치 검색 함수
def searchn(lst, key):
    if lst == []:
        return False
    elif lst[0] == key:
        n = searchn(lst[1:], key) 
        return n+1
    else:
        n = searchn(lst[1:], key)
        return n

print(searchn([35, 28, 30, 29, 33, 31, 30], 30))
