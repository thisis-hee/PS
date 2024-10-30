lecture_list=[]

score_dict={
    'A+':4.5,
    'A0':4.0,
    'B+':3.5,
    'B0':3.0,
    'C+':2.5,
    'C0':2.0,
    'D+':1.5,
    'D0':1.0,
    'F':0.0
}

for _ in range(20):
    lecture_list.append(list(input().split()))


grade_count=0
grade=0
for i in range(len(lecture_list)):
    if(lecture_list[i][2]!='P'):
        grade_count+=int(float(lecture_list[i][1]))
        grade+=float(lecture_list[i][1])*score_dict[lecture_list[i][2]]

print(round(grade/grade_count,6))