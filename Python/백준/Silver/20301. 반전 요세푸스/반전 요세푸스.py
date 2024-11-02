import sys 
from collections import deque
input = sys.stdin.readline

n, k, m = map(int, input().split())
q = deque(range(1, n+1))
pop_list = []
removal_number = 0
rotate_content = -(k - 1)

while q:
    if removal_number == m:
        if rotate_content == k:
            rotate_content = -(k - 1)
        else: rotate_content = k
        removal_number = 0
    q.rotate(rotate_content)
    pop_num = q.popleft()
    pop_list.append(pop_num)
    removal_number += 1

for ans in pop_list:
    print(ans)