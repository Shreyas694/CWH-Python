# Creating funtion for shifting all 0 to the end of the list 
# Idea: Iterate over each element of the list if 0 appear append it to the end of the list 
def func(array):
    for i in array :
        if i == 0:
            array.remove(i)
            array.append(0)
    return array 

arr = [1,2,9,0,9,5,0,0,4,5,6,7,9]
print(func(arr))

# Put our Function to the test for checking its efficiency 
import random 
import time 
n = 200000
arr = [random.randint(0,9) for _ in range(n)]
start = time.time()
x = func(arr)
stop = time.time()
print(stop-start) # To get the total time 

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
            
       
