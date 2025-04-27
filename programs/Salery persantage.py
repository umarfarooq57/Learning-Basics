 # Grading Scheme in student
print("Check the persantage income tax")
inc=int(input("Please Enter the Income:"))
if(inc>=10000 and inc<=20000):
    print("No Tax")
elif(inc>=20001 and inc<=30000):
    print("5 % Tax:",5/100*inc)
elif(inc>=30001 and inc<=40000):
    print("10 % Tax:",10/100*inc)
elif(inc>=40001 and inc<=50000):
    print("15 % Tax:",15/100*inc)

      