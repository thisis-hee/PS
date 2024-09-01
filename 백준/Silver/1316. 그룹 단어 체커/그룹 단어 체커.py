# 슬라이싱이랑 checker_count를 N에서 줄여가는 방식을 떠올려야 함
N=int(input())

checker_count=N
for _ in range(N):
    word=input()
    for i in range(len(word)-1):
        if(word[i]==word[i+1]):
            pass
        elif(word[i] in word[i+1:]):
            checker_count-=1
            break
    
print(checker_count)
