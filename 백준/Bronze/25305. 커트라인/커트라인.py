N, k = map(int, input().split(' '))
# 리스트에 띄어쓰기로 숫자 넣기
score=list(map(int,input().split(' ')))
score.sort()
print(score[len(score)-k])
