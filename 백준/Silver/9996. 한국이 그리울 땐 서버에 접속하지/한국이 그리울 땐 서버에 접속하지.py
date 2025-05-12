import sys
input=sys.stdin.readline

N=int(input())

pattern=input().rstrip()
pattern_list=pattern.split('*')
word_list=[]

for _ in range(N):
    word_list.append(input().rstrip())

for word in word_list:
    if(len(pattern_list[0])+len(pattern_list[1])>len(word)):
        print("NE")
    elif(word[:len(pattern_list[0])]==pattern_list[0] and word[-len(pattern_list[1]):]==pattern_list[1]):
        print("DA")
    else:
        print("NE")
