x,y=map(int,input().split())

date_dict={
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}

day=0
for i in range(1,x):
    day+=date_dict[i]
day+=y-1

if(day%7==0):
    print('MON')
elif(day%7==1):
    print('TUE')
elif(day%7==2):
    print('WED')
elif(day%7==3):
    print('THU')
elif(day%7==4):
    print('FRI')
elif(day%7==5):
    print('SAT')
elif(day%7==6):
    print('SUN')