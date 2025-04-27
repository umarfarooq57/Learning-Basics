# nested dict
student={
    "name":"Musa",
    "subjects":{
        "chem":53,
        "phy":55,
        "math":71
     }
    }
# only keys check use in dict
print(student.values())

# conver dict keys into list
print(list(student.values()))

# conver dict keys into tuple
print(tuple(student.values()))

# conver dict keys into string
print(str(student.values()))

# check the length dict,list,tuple,string

print(len(student.values()))
print(len(list(student.values())))