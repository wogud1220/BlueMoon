import time

def prime1():
    global upper
    t1= time.time()
    num=[]
    for i in range(2,upper+1):
        prime = True
        if i ==2:
            prime = True
        else:
            for j in range (2, i):
                if i % j ==0:
                    prime = False
                    break
        if prime == True:            
            num.append(i)
    print ()
    t2 = time.time()
    print ("elapsed time = ", t2-t1)
    print ("# of primes = ",len(num))
    print (num[-100:])
    
def prime2():
    global upper
    t1 = time.time()
    num = []
    for i in range(2,upper+1):
        num.append(i)

    for i in num:
        for j in range (2,upper+1):
            s = i*j
            if s >upper:
                break
            if s in num:
                num.remove(s)
    
    t2 = time.time()
    print ("elapsed time = ", t2-t1)
    print ("# of primes = ",len(num))
    print (num[-100:])

upper = 1000
print("Method 1")
prime1()
print ()
print("Method 2")
prime2()