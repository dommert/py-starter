# Student Example

class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


# declare a student
bob = Student("Bob Hope", 60, "M")
dave = Student("David Letterman", 50, "M")

# Using a student
print "Hello " + bob.name
