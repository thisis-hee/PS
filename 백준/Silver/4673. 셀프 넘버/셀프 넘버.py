import sys

input = sys.stdin.readline

natural_num = set([i for i in range(1,10001)])
generated_num = set()

for i in range(1, 10001):
    for j in str(i):
        i+=int(j)
    generated_num.add(i)

answer = list(natural_num-generated_num)
answer.sort()

for i in answer:
    print(i)