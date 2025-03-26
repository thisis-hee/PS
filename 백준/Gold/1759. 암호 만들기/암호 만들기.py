import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque
from itertools import combinations, permutations

L,C=map(int,input().split())
str_list=list(map(str,input().split()))
a_list=[]
b_list=[]

for word in str_list:
    if word in ('a','e','i','o','u'):
        a_list.append(word)
    else:
        b_list.append(word)

word_list=[]

for i in range(1, len(a_list)+1):
    for a in combinations(a_list,i):
        if(L-i>=2):
            for j in combinations(b_list,L-i):
                add_list=[]
                for word_a in a:
                    add_list.append(word_a)
                for word_b in j:
                    add_list.append(word_b)
                word_list.append(add_list)

sorted_word_list=[]
for i in range(len(word_list)):
    word=''.join(sorted(word_list[i]))
    sorted_word_list.append(word)

sorted_word_list=sorted(sorted_word_list)
for word in sorted_word_list:
    print(word)