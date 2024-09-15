N=int(input())

password=[]

for _ in range(N):
    password.append(input())


reverse_password=[]

for i in range(len(password)):
    reverse_password.append(password[i][::-1])

for word in reverse_password:
    if(word in password):
        real_password=word

print(len(real_password), real_password[len(real_password)//2])