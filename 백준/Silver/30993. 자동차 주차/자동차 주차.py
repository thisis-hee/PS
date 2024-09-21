import math

N,A,B,C=map(int,input().split())

print(int((math.factorial(N)/(math.factorial(N-A)*math.factorial(A)))*(math.factorial(N-A)/(math.factorial(N-A-C)*math.factorial(C)))))