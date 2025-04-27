a=int(input("Enter Number a:"))
b=int(input("Enter Number b:"))
c=int(input("Enter Number c:"))
if(a>b and a>c):
    print("a number is Greater:",a)
elif(b>c):
    print("b number is greater:",b)
elif(c>a and c>b):
    print("c number is greater:",c)  
else:
   print("Number are Equal")          