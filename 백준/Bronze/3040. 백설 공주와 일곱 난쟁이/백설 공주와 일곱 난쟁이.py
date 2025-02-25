import sys
input=sys.stdin.readline

people=[]

for _ in range(9):
    people.append(int(input()))

from itertools import combinations

for i in combinations(people,7):
    if(sum(i)==100):
        for j in i:
            print(j)
        break