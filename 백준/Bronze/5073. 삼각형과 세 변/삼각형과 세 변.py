while(True):
    a,b,c=map(int,input().split(' '))
    A=[a,b,c]
    A.sort()
    if(a==0 and b==0 and c==0):
        break
    else:
        if(A[2]>=A[0]+A[1]):
            print("Invalid")
        else:
            if(a==b==c):
                print("Equilateral")
            elif(a==b and c!=a):
                print("Isosceles")
            elif(a==c and b!=a):
                print("Isosceles")
            elif(b==c and a!=b):
                print("Isosceles")
            elif(a!=b and b!=c and a!=c):
                print("Scalene")    
