class Lesson:

    def __init__(self,teacher,time,):
        self.teacher = teacher
        self.time = time

    def summary(self):
        print("This Lesson is thought by {} on {} ".format(self.teacher,self.time))
    @classmethod
    def math(cls):
        return cls("Emma","Monday")
    @classmethod
    def english(cls):
        return cls("Peter","Thursday")
    
math_1 = Lesson.math()
english_1 = Lesson.english()
math_1.summary()
english_1.summary()




