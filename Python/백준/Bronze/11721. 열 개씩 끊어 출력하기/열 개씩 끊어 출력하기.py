word=input()
for i in range(len(word)//10):
    print(word[10*i:10*i+10])
print(word[10*(len(word)//10):len(word)])