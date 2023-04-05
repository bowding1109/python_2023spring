# class Person:
# #屬性
#     def __init__(self,name,age,favoriteFood):
#         self.name = name
#         self.age = age
#         self.favoriteFood = favoriteFood
# #方法
#     def introduce(self):
#         print("我是"+self.name+"我今年"+str(self.age)+"歲，嘴喜歡吃"+self.favoriteFood+"。")
#     def shout(self,content):
#         print("我大喊：「"+content+"」")


# amy = Person("Amy",15,"Apple")
# amy.introduce()
# amy.shout("我討厭看牙醫")

class Person:
    state = "heathy"

    def getCold(self):
        self.__class__.state = "sick"

print("Origin: I'm "+Person.state+".")
any = Person()
any.getCold()
print("After: I'm "+Person.state+".")


