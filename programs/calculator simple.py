print("1 - Addition")
print("2 - subtraction")
print("3 - multiplication")
print("4 - dividion")
option=int(input("choose an operation:"))

if(option in [1,2,3,4]):
    num1= int(input("enter first number:"))
    num2= int(input("enter second number:"))

    if(option==1):
        result=num1+num2
    elif(option==2):
        result=num1-num2
    elif(option==3):
        result=num1*num2
    elif(option==4):
        if(num2==0):
            print("division by zero is not allowed")
        else:
            result=num1/num2 
    print("result:",result)            
else:
    print("invalid option")

