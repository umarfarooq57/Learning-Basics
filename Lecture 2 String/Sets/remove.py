collection={1,3,5.4,7,8,4,"hello","umar",("umar","Farooq",34),(1.3,4,'G',"Hi")}
collection.remove(3) # for int remove
collection.remove(7)
collection.remove(5.4)   # for flaot
collection.remove("umar")   # for string   
collection.remove((1.3,4,'G',"Hi"))   # for tuple
print(collection)