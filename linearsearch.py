a=int(input("Enter the number of elements in a list:"))
b=[]
for i in range(a):
    b.append(int(input("Value of element:")))
print("The values given by user are :",b)

data=int(input("Enter the element to search :"))

for i in range(a):
    if(b[i]==data):
        print("The element:",data,"is found at the index number:",i)
        print("The element is at the position:",i+1)
        break
    else:
        print("Sorry data not found")
    