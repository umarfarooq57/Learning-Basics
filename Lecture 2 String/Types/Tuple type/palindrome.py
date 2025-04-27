list1=[1,2,3]                    # palindrome us ko khty ha jis ki dono side yani start or reverse  
list2=[1,2,3]                       # side dono sy pra jay jasy 'ma''am' agr hm is ko reverse b prhy to maam hi bny ga 
copy_list1=list1.copy()
copy_list1.reverse()
if (copy_list1==list1):
    print("Palindrome")
else:
    print("Not palindrome")    