a=int(input("Enter the first side:"))
b=int(input("Enter the second side:"))
c=int(input("Enter the third side:"))

# If a,b,c are: 3,4,5 and 5,12,13 this code tells that it is a Pythogoreas traingle.
if(a>b and a>c):
    print("a is the largest side")
    p=a*a
    q=b*b+c*c
    if(p==q):
        print("It is a Pythogoreas  Triangle")
    else:
        print("It is not a Pythogoreas  triangle")
elif(b>a and b>c):
    print("b is the largest side")
    p=b*b
    q=a*a+c*c
    if(p==q):
        print("It is a Pythogoreas  triange")
    else:
        print("It is not a Pythogoreas triangle")
else:
    print("c is the largest side")
    p=c*c
    q=a*a+b*b
    if(p==q):
        print("It is a Pythogoreas traingle")
    else:
        print("It is not a Pythogoreas traingle")