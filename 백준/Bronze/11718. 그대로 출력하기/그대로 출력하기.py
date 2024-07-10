# 1번 풀이 예외 처리
'''
while True:
    try:
        print(input())
    except EOFError:
        break
'''
# 2번 풀이 sys.stdin.readlines()로 받기

import sys

s = sys.stdin.readlines() # 각 줄이 원소로 된 리스트를 생성함
for i in s:
    # readlines는 개행문자까지 포함하므로 rstrip()으로 개행 문자를 없애줘야 함
    print(i.rstrip())
    