# Class_Student.py

# Student Class
class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def hello(self): #Saying Hello
        var = ('Hello %s! Welcome...' % (self.name))
        return var



