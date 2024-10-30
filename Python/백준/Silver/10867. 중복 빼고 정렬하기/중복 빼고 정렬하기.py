N=int(input())

word_set=set(map(int,input().split()))
print(*sorted(list(word_set)))