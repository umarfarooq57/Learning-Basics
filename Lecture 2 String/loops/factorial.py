num=int(input("Ente the factorial number is:"))

fact=1
i=1
for i in range(1,num+1):
    fact*=i
    i+=1
print("fact is:",fact)