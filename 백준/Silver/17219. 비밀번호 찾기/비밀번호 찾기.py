import sys

N,M=map(int,sys.stdin.readline().rstrip().split())

site_dict={}

for _ in range(N):
    a,b=sys.stdin.readline().split()
    site_dict[a]=b

for _ in range(M):
    site=sys.stdin.readline().rstrip()
    print(site_dict[site])
