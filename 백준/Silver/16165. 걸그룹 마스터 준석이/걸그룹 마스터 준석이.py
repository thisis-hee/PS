import sys
input=sys.stdin.readline

N,M=map(int,input().split())

team_name=[]
member_cnt=[]
member_name=[]

for _ in range(N):
    name=input().rstrip()
    team_name.append(name)
    cnt=int(input().rstrip())
    member_cnt.append(cnt)
    member_list=[]
    for _ in range(cnt):
        member_list.append(input().rstrip())
    member_name.append(member_list)

for i in range(len(member_name)):
    member_name[i].sort()

answer=[]

for i in range(M):
    question=input().rstrip()
    quiz_num=int(input())
    if(quiz_num==1):
        check_team=0
        for member in member_name:
            if(question in member):
                print(team_name[check_team])
            else:
                check_team+=1
    else:
        check_member=0
        for team in team_name:
            if(question==team):
                for i in range(len(member_name[check_member])):
                    print(member_name[check_member][i])
            else:
                check_member+=1