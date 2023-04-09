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

# #建立方法
# amy = Person("Amy",15,"Apple")
# amy.introduce()
# #呼叫行為
# amy.shout("我討厭看牙醫")

class Person:
    state = "heathy"#類別屬性:屬性類別的屬性，而不是物件
#實體方法
    def getCold(self):
        self.__class__.state = "sick"

print("Origin: I'm "+Person.state+".")
any = Person()
any.getCold()
print("After: I'm "+Person.state+".")

# class Person:
#     # 築構式
#     def __init__(self, eyesColor, hairColor):
#         self.eyesColor = eyesColor
#         self.hairColor = hairColor

#     @classmethod
#     def american(cls):
#         return cls("blue","brown")
#     @classmethod
#     def american(cls):
#         return cls("black","black")
#     def introduce(self):
#         print("My eyes is {} and my hair is {}.".format(self.eyesColor,self.hairColor))

# class Person:
# #速率靜態方法
#     @staticmethod
#     def work(work_hour):
#         print("Working hours :", work_hour)
# #透過物件呼叫
# amy = Person()
# amy.work(8)