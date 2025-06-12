def func(array):
    t = []
    z = 0 
    for i in array :
        if i != 0 : 
           t.append(i)
        else:
            z += 1
    t.extend(z * [0]) 
    return t 


# Lets put our function to the test for checking its efficiency 
import random 
import time 
n = 200000
arr = [random.randint(0,9) for _ in range(n)]
start = time.time()
x = func(arr)
stop = time.time()
print(stop-start) # To get the total time TWQ