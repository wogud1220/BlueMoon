# 집합 자료형 사용하기

s1 = set([1, 2, 3, 3, 2, 'a'])    # s1={1, 2, 3}
s2 = {2, 3, 4, 'a'}

print("s1 =",s1)
print("s2 =",s2)
print("2 in s1 = ", 2 in s1)
print("5 in s2 = ", 5 in s2)
print("s1 | s2 =", s1 | s2)
print("s1 & s2 =", s1 & s2)
print("s1 - s2 =", s1 - s2)
print("s2 - s1 =", s2 - s1)

s2.add(9)
s1.update({4, 5, 6})
s1.remove(3)

print("s1 =", s1)
print("s2 =", s2)