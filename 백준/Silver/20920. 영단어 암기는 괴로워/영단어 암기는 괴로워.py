# 딕셔너리 + lambda를 활용한 조건 정렬
import sys

N,M=map(int,input().split())

word_list=list()

for _ in range(N):
    a=sys.stdin.readline().rstrip()
    if(len(a)>=M):
        word_list.append(a)

word_dict={}

for word in word_list:
    if(word not in word_dict.keys()):
        word_dict[word]=1
    else:
        word_dict[word]+=1

word_dict = sorted(word_dict.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for i in range(len(word_dict)):
    print(word_dict[i][0])
