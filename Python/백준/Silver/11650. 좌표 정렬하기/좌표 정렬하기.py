import sys
input=sys.stdin.readline

N=int(input())
data = []

for i in range(N):
	x, y = map(int,input().split())
	data.append((x,y))

data.sort(key = lambda x : (x[0], x[1]))

for d in data:
	print(d[0], d[1])