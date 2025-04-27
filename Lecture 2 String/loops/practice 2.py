# number 1 to 100
for i in range(1,101):
    print(i)
print("------------------100 to 1-----------------")
# number 100 to 1
for i in range(100,0,-1):
    print(i)


print("------------------table of multiplication-----------------")
num=int(input("Enter table number:"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)