n = int(input())

for i in range(n):
  s = list(input().split())
  for j in s:
    # slicing 이용해 거꾸로 출력하기
    print(j[::-1], end=' ')
print()
