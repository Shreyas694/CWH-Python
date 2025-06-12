import time
from collections import deque


def solution(array, k):
    d = deque(array)
    permutation = []
    while d:
        d.rotate(1-k)
        item = d.popleft()
        permutation.append(item)
    return permutation


soldiers = 1_000_000
arr = [s+1 for s in range(soldiers)]  # List Comphrehension
k = 3
start = time.perf_counter()
perm = solution(arr, k)
stop = time.perf_counter()
print(stop-start)           # Here the code took only 0.33 sec to execute
