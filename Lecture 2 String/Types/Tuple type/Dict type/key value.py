
#  Note: Key ky ander hm dictionary or list ko use nhi kr skty hm key ko string bna skty ha ya koi number bna skty ha 
#   Hum tuple ko key bna skty ha lakin hm ya use nhi krty kuky tuple immutable type ha  
print("-------------------Key value-------------------------------")

# Hum Dictionary ky ander hr kism ki data type store krwa skty ha jis ka formula 
# dict={
# key:value 
#  } ha dict ky variable ki jaga koi b name rkh skty ha 
info={
    "name":"codecraft",    # string
    "subjects":["Python","Java","PhP","C++"],   # for list
    "Topics":("Dict","Sets","Codebooks"),    # for tuple
    "age":20,   # integer
    "is_adult":True,   # Boolean
    12:"point",
    13.23:"Float",    # Key ko integer b bna skty ha or float b but no use dict and list
    "marks":98.4   #Floating
}
print(info)
print("----------------type------------------")
print(type(info))
print("**************check the key value**************")
print(info["name"])
print(info["subjects"])
print(info["is_adult"])
print(info[13.23])
print(info)

 # re assign mean value change
print("*************change****************")
info["name"]="Umar"   
info["age"]=20.7
info["subjects"]=["Numpy","AI","ML","PHP","Python"]
info["Topics"]=("Sets","W3shool","cs201","codebooks")
print(info)
print("----------see the replace value-------------")
# replace value check
print(info["name"])
print(info["subjects"])
print(info["Topics"])
# ADD mean insert value
print("---------------Add new value--------------")
info["Full_Name"]="Umar farooq"
print(info)


# They are unorderd(no sequence), mutable(chaneable) & dont't allows dupplicate keys  