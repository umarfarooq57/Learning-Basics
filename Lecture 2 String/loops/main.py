import random
computer=random.choice([-1,0,1])
youstr=input("Enter you Choice: ")
youDict={"w":-1,"s":1,"g":0}
reverseDict={-1:"water",1:"snake",0:"gun"}
you=youDict[youstr]
print(f"You choice {reverseDict[you]}\ncomputer choice {reverseDict[computer]}")

if computer==you:
    print("Its draw..!")
else:
    if(computer==-1 and you==1):
        print("you win.!")
    elif(computer==-1 and you==0):
        print("you lose.!")
    elif(computer==1 and you==-1):
        print("you lose.!")
    elif(computer==1 and you==0):
        print("you win.!")
    elif(computer==0 and you==1):
        print("you lose.!")
    elif(computer==0 and you==-1):
        print("you win.!")
