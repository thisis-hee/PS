import sys
input=sys.stdin.readline

word=input()

partial=[]

for i in range(len(word)):
    for j in range(len(word)-i):
        if(word[j:j+i]!=''):
            partial.append(word[j:j+i])

print(len(set(partial)))