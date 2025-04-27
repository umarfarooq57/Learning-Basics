# agr koi asa concept jis ko hm class ky ander rkhna chty ha us ko hm private bna skty ha 

class account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass    # 2 underscore function ko private kr deta ha agr class ky ky ander private krna hon

    def reset_pass(self):
        print(self.__acc_pass)


acc1=account("12345","abcde")   
print(acc1.acc_no)
# print(acc1.acc_pass)

print(acc1.reset_pass())                
print(acc1.__acc_pass)


# hm simple word my kh skty ha ky private funtion agr apply krna ha to attributes or method ky sath 2 
#  underscore use krny pry gy 