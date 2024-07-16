N=int(input())

# 666부터 숫자를 하나씩 늘려감.
number=666
count=0

while(True):
    # 그리고 숫자에 666이 포함되면 count를 1 늘림
    if('666' in str(number)):
        count+=1
    # count와 입력한 N이 동일해지면 그 숫자를 출력함.
    if(count==N):
        print(number)
        break
    number+=1
