# list + set 동시 활용 / sort 함수의 key를 활용해 길이로 정렬하기
N=int(input())

word_list=[]

for _ in range(N):
    word_list.append(input())

word_list=list(set(word_list))
word_list.sort()
word_list.sort(key=len)

for i in word_list:
    print(i)
