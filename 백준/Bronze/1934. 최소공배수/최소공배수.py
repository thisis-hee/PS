# 내장함수 math를 활용해 최대공약수, 최소공배수를 쉽게 구할 수 있음
import math
from math import gcd

T=int(input())

for _ in range(T):
    A,B=map(int,input().split())
    print((A*B)//gcd(A,B))
