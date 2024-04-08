#version 1
'''
ans = []
n = 0

def searchn(lst, key):
    global n
    
    if lst == []:
        return
    
    elif lst[0] == key:
        ans.append(n)
        n += 1
        searchn(lst[1:], key)
        
    else:
        n += 1
        searchn(lst[1:], key)

    return ans
'''

#version 2

def searchn(lst, key, ans=[], i=0):
    if i == len(lst):
        return ans
    
    elif lst[i] == key:
        ans.append(i)
        return searchn(lst, key, ans, i+1)
        
    else:
        return searchn(lst, key, ans, i+1)
        

#print(searchn([2,4,6,8,0,2,4,6,8,0],0))
print(searchn([35,28,30,29,33,31,30],30))
