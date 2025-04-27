operator=input("enter the number (+,-,*,/):")
num1=float(input("enter thr first number:"))
num2=float(input("enter thr second number:"))

if operator=='+':
     result=(num1+num2)
     print(round(result,3))
elif operator=='-':
     result=(num1-num2)
     print(round(result,3))
elif operator=='*':
     result=(num1*num2)
     print(round(result,3))
elif operator=='/':
     if num2==0:
         print("division by zero is not allowed")
     else:
          result=(num1/num2)
          print(round(result,3))


else:
    print(f"{operator} is not valid operator")
