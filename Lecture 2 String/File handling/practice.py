#with open("practice 2.py","a") as f:
 #   f.write("Hi everyone \n we are learning file I/O") 
  #  f.write("\n using java\n i like programming in java")

#--------------------------------------------------------
# repalce in java into python

#with open("practice 2.py","r") as f:
 #   data=f.read()
  #  new_data=data.replace("java","Python")
 #   print(new_data)

#with open("practice 2.py","w") as f:
  #  data=f.write(new_data)
#--------------------------------------------------

#check the exist value or word
 #is sary procedure ko function my b likh skty ha   
 # for example:
def check_for_word():
    word="learning"
    with open("practice.py","r") as f:
        data=f.read()
        if(word in data):
            print("Found")
        else:
            print("Not found") 


check_for_word()             