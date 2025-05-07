import sys
input=sys.stdin.readline

s=input().rstrip()
tag_stack=[]
word_stack=[]
answer=[]
for i in range(len(s)):
    if(s[i]=='>'):
        tag_stack.append(s[i])
        for word in tag_stack:
            answer.append(word)
        tag_stack=[]
        continue
    if(s[i]=='<'):
        if word_stack:
            word_stack=word_stack[::-1]
            for word in word_stack:
                answer.append(word)
            word_stack=[]
        tag_stack.append(s[i])
        continue
    if('<' in tag_stack):
        tag_stack.append(s[i])
        continue

    if(s[i]!=' '):
        word_stack.append(s[i])
        continue
    if(s[i]==' '):
        word_stack=word_stack[::-1]
        for word in word_stack:
            answer.append(word)
        answer.append(' ')
        word_stack=[]

if word_stack:
    word_stack=word_stack[::-1]
    for word in word_stack:
        answer.append(word)

print(''.join(answer))