# Kitne subjects ka input lena hai
num_subjects = int(input("Kitne subjects ka input lena hai? "))

# Khali list banayein subjects store karne ke liye
subjects = []

# Loop ke zariye har subject ka input lein
for i in range(num_subjects):
    subject = input(f"Subject {i+1} ka naam enter karein: ")
    subjects.append(subject)  # Subject ko list mein add karein

# Sab subjects ko print karein
print("Aapke subjects hain:")
for subject in subjects:
    print(subject)

for num in range(num_subjects):
    subject = input(f"Subject {num_subjects} ka number enter karein: ")
    subjects.append(num)



student={
    "name":"Musa",
    subject:{
        num_subjects:num,
        num_subjects:num,
        num_subjects:num
     }
    }
print(student)
#print(student["subjects"])
#print(student["subjects"]["chem"])
