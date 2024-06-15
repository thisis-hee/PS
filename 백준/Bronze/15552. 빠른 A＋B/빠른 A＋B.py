# input 대신 sys.stdin.readline()으로 빠르게 읽어오기
import sys
count=int(input())
for i in range(count):
    A,B=map(int,sys.stdin.readline().split(' '))
    print(A+B)
