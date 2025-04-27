student={
    "name":"Musa",
    "subjects":{
        "chem":53,
        "phy":55,
        "math":71
     }
    }

# items method formula : dict.items()  output = outer,inner  in tuple forms 
print(student.items())
# items method formula : dict.items()  output = outer,inner  in list forms but list ky ander tuple hi ho ga
print(list(student.items()))
# index  of list
pairs=(list(student.items()))
print("Index 0 is: ",pairs[0])
print("Index 1 is: ",pairs[1])