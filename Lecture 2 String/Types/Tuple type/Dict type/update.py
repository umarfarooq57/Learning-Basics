student={
    "name":"Musa",
    "subjects":{
        "chem":53,
        "phy":55,
        "math":71
     }
    }
new_dict={"city":"Lahore","code":85643}
student.update(new_dict)     # no duplicate keys
print(student)