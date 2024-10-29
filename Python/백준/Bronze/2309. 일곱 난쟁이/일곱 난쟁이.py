from itertools import combinations

height=[]
for _ in range(9):
    height.append(int(input()))

for j in combinations(height,7):
    if(sum(j)==100):
        j=sorted(list(j))
        for k in range(len(j)):
            print(j[k])
        break
    else:
        continue