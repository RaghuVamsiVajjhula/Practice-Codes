a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n")
choice=int(input("Enter your choice:"))
if (choice==1):
    print("The sum of 2 numbers is:",(a+b))
elif(choice==2):
    print("The difference of 2 numbers is:",(a-b))
elif(choice==3):
    print("The product of 2 numbers is:",(a*b))
else:
    print("The division of 2 numbers is:",(a/b))
    