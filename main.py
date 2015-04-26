# Main Python File

# Using a import and function
from hello import hello, goodbye
# Saying Hello
jake = "Jake The Snake" 
print hello(jake) #One way
print hello("Jake The Rabbit")# Another way
# Saying Goodbye
print goodbye(jake)


# ==================================
# Import a class and functions
from class_student import Student

# initialize 3 Different studnets
bob = Student("Bob Hope",60, "M")
dave = Student("David Letterman", 50, "M")
frank = Student("Frank Miller", 30, "M")

# Say hello to a student
print Student.hello(frank)




