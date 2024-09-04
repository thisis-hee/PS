score_list=[]
for _ in range(8):
    score_list.append(int(input()))

sorted_score_list=sorted(score_list,reverse=True)
print(sum(sorted_score_list[:5]))
index_list=[]

for i in range(5):
    index_list.append(score_list.index(sorted_score_list[i])+1)

print(*sorted(index_list))