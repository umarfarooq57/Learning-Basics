# hm simple word my kh skty ha ky private funtion agr apply krna ha to attributes or method ky sath 2 
#  underscore use krny pry gy 
# for example 
class person:
    __name="hamid"
    def __hello(self):
        print("hello person")

    def welcome(self):
        self.__hello()
p1=person()
print(p1.welcome())
print(p1.__hello())