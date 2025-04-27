f=open("demo.txt","r")             # 'r' open for reading(default
data=f.read()
print(data)
print(type(data))
f.close()