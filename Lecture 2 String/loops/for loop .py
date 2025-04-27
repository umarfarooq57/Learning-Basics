num=[1,2,3,4,5]
for i in num:
    print(i)
print("---------------list type------------")
# list type
vagetable=["potato","onion","clumber","collyflower"]
for i in vagetable:
    print(i)  
print("---------------tuple type------------")
# tuple type
num=(1,2,3,4,5,6) 
for val in num:
    print(val)
print("---------------string type------------")
# string type 
name="codecraft"
for char in name:
    print(char)   
else:
    print("End")     # else ki zarort is liya prti ha asa kam jis my hm complete loop use krty ha un ko end krwana hon us ko else my likhty ha 

name="codecraft"
for char in name:
    print(char)
    if(char=='a'):
        print("found a")
        break
   