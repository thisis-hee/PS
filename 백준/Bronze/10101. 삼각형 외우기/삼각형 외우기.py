a=int(input())
b=int(input())
c=int(input())
if(a+b+c!=180):
    print("Error")
else:
    if(a==60 and b==60 and c==60):
        print("Equilateral")
    elif(a==b and c!=a):
        print("Isosceles")
    elif(a==c and b!=a):
        print("Isosceles")
    elif(b==c and a!=b):
        print("Isosceles")
    elif(a!=b and b!=c and a!=c):
        print("Scalene")
