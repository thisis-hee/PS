import sys
input=sys.stdin.readline

word=[]

for _ in range(3):
    word.append(input().rstrip())

try:
    if(type(int(word[0]))==int):
        ans=int(word[0])+3
except:
    pass
try:
    if(type(int(word[1]))==int):
        ans=int(word[1])+2
except:
    pass
try:
    if(type(int(word[2]))==int):
        ans=int(word[2])+1
except:
    pass


if(ans%3==0 and ans%5==0):
    print("FizzBuzz")
elif(ans%3==0 and ans%5!=0):
    print("Fizz")
elif(ans%3!=0 and ans%5==0):
    print("Buzz")
else:
    print(ans)