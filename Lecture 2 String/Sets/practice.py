# store following word meaning in a python dictionary:

dict={
    "table":["a piece furniture","list of facts & figures"],
    "cat":"a small animal"
}
print(dict)


# you are given a list of subjects for students.Assume one
# classroom is required for 1 subject. how many classroom
# are needed by all students.

subjects={
    "python","java","C++","python","javascript","java","python","java","C++","C"
      }
print(len(subjects))

# wap to enter marks of 3 subjects from the user and store them in a dictionary
# start with an empty dictionary & add one by one.Use subject name as key & marks as value
marks={}

x=int(input("Enter the phy marks:"))
marks.update({"phy":x})
x=int(input("Enter the chem marks:"))
marks.update({"chem":x})
x=int(input("Enter the math marks:"))
marks.update({"math":x}) 
print(marks) 

# figure out a way to store 9 & 9.0 as saparate values in the set.
# (you can take hepl of built in data type)
value={9,9.0}
print(value)
value={9,9.25}
print(value)
value={9,9.25,8,8.0} # is process my koi b millti valus print nhi hoti  
print(value)
value={9,"9.0"}
print(value)

print("***********built in data type**************")
value={
    ("float",9.0),
    ("int",9)
       }
print(value)