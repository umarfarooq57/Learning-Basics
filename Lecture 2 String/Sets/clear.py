collection=set()
collection.add(1)  #for int
collection.add(2)   
collection.add(3.6)  # for float
collection.add("Hello")   # for string
collection.add("word")      
collection.add((10,20,30,40,"hello","word"))   # tuple
print(collection)     # hm list or dict ko add nhi kr skty
print(len(collection))
collection.clear()
print(collection)
print(len(collection))