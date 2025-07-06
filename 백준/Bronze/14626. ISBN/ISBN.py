import sys

input = sys.stdin.readline

isbn = input().rstrip()
weight = [1 if i % 2 == 0 else 3 for i in range(12)]
ast_index = isbn.index('*')
total = 0

for i in range(12):
    if i == ast_index:
        continue
    total += int(isbn[i]) * weight[i]

for j in range(10):
    tmp = total + weight[ast_index] * j
    check = int(isbn[-1])

    if (tmp + check) % 10 == 0:
        print(j)
        break
