a=int(input("Enter the value of first number:"))
b=int(input("Enter the value of second number:"))
c=int(input("Enter the value of third number:"))
x=0
y=0
if(a>b and a>c):
    print("A is the greatest element.");
    x=a*a;
    y=b*b+c*c
    if(x==y):
        print("This is a right angle triangle.")
    else:
        print("It is not a right angle triangle")
elif(b>a and b>c):
    print ("B is greater than A & C");
    x=b*b
    y=a*a+c*c
    if(x==y):
        print("This is a right angle triangle.")
    else:
        print("It is not a right angle triangle")
else:
    print("C is greater")
    x=c*c
    y=a*a+b*b
    if(x==y):
        print("This is a right angle triangle.")
    else:
        print("It is not a right angle triangle")
        