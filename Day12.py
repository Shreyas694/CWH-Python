# Recursion in Python 
def factorial (n):
    if n == 1: return 1 
    return n  * factorial (n-1)

print(factorial(6))

# The Josephus Permutation 
def solution(array,k):
    permutation = []
    index = 0 
    while array :
        index = (index + k-1) % len(array)
        item = array.pop(index)
        permutation.append(item)
    return permutation

soldiers = 7 
arr = [s+1 for s in range(soldiers)]  # List Comphrehension 
k = 3 
perm = solution(arr,k)
print(perm)

import time 
soldiers = 1_000_000
arr = [s+1 for s in range(soldiers)]  # List Comphrehension 
k = 3 
start = time.perf_counter()
perm = solution(arr,k)
stop = time.perf_counter()
print(stop-start)           # The code took 233sec to execute 

# Unlike "array" where the elements are stored neighbouring memory locations,In "deque" the elements are not stored adjacent memory locations instead they are connected by pointers.

# deque
from collections import deque  
def solution(array,k):
    d = deque(array)
    permutation = []
    while d:
        d.rotate(1-k)
        item = d.popleft()
        permutation.append(item)
    return permutation
