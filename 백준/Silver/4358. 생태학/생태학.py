import sys
input=sys.stdin.readline

tree_dict={}

while True:
    s=input().rstrip()
    if(s==''):
        break
    else:
        if(s in tree_dict):
            tree_dict[s]+=1
        else:
            tree_dict[s]=1

sum=0
for v in tree_dict.values():
    sum+=v

for i in range(len(tree_dict)):
    print(sorted(tree_dict)[i], "{:.4f}".format(tree_dict[sorted(tree_dict)[i]]/sum*100))
