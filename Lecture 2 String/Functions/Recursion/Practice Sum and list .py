def sum(n):
    if(n==0):
        return 0
    return sum(n-1) + n


print(sum(5))  



# print all element in the list 
print("-------------------------------------------------")
def print_list(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

fruit=["Mango","Orange","Banana","Litchi","Apple"]

print_list(fruit) 

   
    
    