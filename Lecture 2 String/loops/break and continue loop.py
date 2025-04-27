i=1
while(i<=5):
    print(i)       # break loop
    if(i == 3):
        break
    i+=1
print("End of loop")



print("--------------continue loop-----------------")
i=0
while(i<=5):
    if(i == 3):
        i+=1            # continue loop my jo condition equal ha wo print nhi ho gi us ky bad jo b hon print ho ga or continue ky nichy b increse value nhi ho gi
        continue
    print(i)
    i+=1
print("End of loop")