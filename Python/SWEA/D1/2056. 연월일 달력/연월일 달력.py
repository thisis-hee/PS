T=int(input())

for i in range(1,T+1):
    date=list(str((input())))

    if(((date[4]+date[5]) in ['01','03','05','07','08','10','12']) and int(date[6]+date[7])<=31):
        print(f"#{i} {''.join(date[0:4])}/{''.join(date[4:6])}/{''.join(date[6:8])}")
    elif(((date[4]+date[5]) in ['04','06','09','11']) and int(date[6]+date[7])<=30):
        print(f"#{i} {''.join(date[0:4])}/{''.join(date[4:6])}/{''.join(date[6:8])}")
    elif((date[4]+date[5])=='02' and int(date[6]+date[7])<=28):
        print(f"#{i} {''.join(date[0:4])}/{''.join(date[4:6])}/{''.join(date[6:8])}")
    else:
        print(f"#{i} {-1}")
        