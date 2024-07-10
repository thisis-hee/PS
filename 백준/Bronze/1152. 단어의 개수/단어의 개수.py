# split(' ')랑 split() 차이 있음
# split(' ')는 공백 하나하나를 셈.
# split()은 공백이 연속으로 있어도 하나로 셈.
# 이거 알면 간단히 풀 수 있음

word=list(map(str, input().split()))
print(len(word))
