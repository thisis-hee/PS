N=int(input())
books={}

for _ in range(N):
    title=input()
    if title not in books:
        books[title]=1
    else:
        books[title]+=1


max_value=max(books.values())
best=[]
for key, value in books.items():
    if(value==max_value):
        best.append(key)

best.sort()

print(best[0])