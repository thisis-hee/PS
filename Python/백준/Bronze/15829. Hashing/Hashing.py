L = int(input())
word = input()
num_word=[]
for i in word:
    num_word.append(ord(i)-96)

r=31
M=1234567891
ans=0

for j in range(len(num_word)):
    ans+=num_word[j]*(r**j)

print(ans%M)