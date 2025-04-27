# choose the number
print("select the number")
number=(input("choose the number is (between 0 and 100):"))
# check the number is between 0 and 100
if number.isdigit():
    number=int(number)
    if number>=0 and number<=100:
        print("number is in range")
    else:
        print("number is not in range")
else:
    print("number is not valid")