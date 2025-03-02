import sys
input=sys.stdin.readline

N=int(input())

word_list=[]

for _ in range(N):
    word_list.append(input().rstrip())

expansion_list=[]

for word in word_list:
    a=word.split('.')
    expansion_list.append(a[1])

expansion_list=list(set(expansion_list))

word_dict={key : 0 for key in sorted(expansion_list)}

for word in word_list:
    a=word.split('.')
    word_dict[a[1]]+=1

for key, value in word_dict.items():
    print(key, value)