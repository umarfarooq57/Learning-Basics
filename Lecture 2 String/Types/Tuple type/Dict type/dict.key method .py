# nested dict
student={
    "name":"Musa",
    "subjects":{
        "chem":53,
        "phy":55,
        "math":71
     }
    }
print(student)
# inner dict
print(student["subjects"])

# inner dict keys and values
print(student["subjects"]["chem"])

# only keys check use in dict
print(student.keys())

# conver dict keys into list
print(list(student.keys()))

# conver dict keys into tuple
print(tuple(student.keys()))

# conver dict keys into string
print(str(student.keys()))

# check the length dict,list,tuple,string

print(len(student.keys()))
print(len(list(student.keys())))