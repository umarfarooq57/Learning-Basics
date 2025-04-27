student={
    "name":"Musa",
    "subjects":{
        "chem":53,
        "phy":55,
        "math":71
     }
    }
#print(student["name2"])   get ka function is liya use hota agr glti sy hm sy key name change ho jay to ya error
print(student.get("name"))   # nhi deta blky none print kr ky det aha lakin simple key method error dy ga
print(student.get("name2"))   # simple key my error ky bad koi b code run nhi ho ga lakin get ky function ky bad run ho ga
print("After")
print(student.get("name"))