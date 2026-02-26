"""Instance method vs classmethod vs staticmethod (simple)."""

class Student:                               # Create a Student class (template)
    school = "School #1"                     # Class variable (same for all students)
    count = 0                                # Class variable to count students

    def __init__(self, name):                # Constructor (runs when object is created)
        self.name = name                     # Store name in the object
        Student.count += 1                   # Increase student count

    def say_hi(self):                        # Instance method (works with one student)
        print("Hi! I'm", self.name)

    @classmethod
    def how_many(cls):                       # Class method (works with the class)
        return cls.count

    @staticmethod
    def is_honors(gpa):                      # Static method (simple helper)
        return gpa >= 3.5

if __name__ == "__main__":                   # Runs only when file is executed directly
    s1 = Student("Ali")                      # Create first student
    s2 = Student("Dana")                     # Create second student

    s1.say_hi()                              # Call instance method
    s2.say_hi()

    print("students =", Student.how_many())  # Call class method
    print("3.8 honors? =", Student.is_honors(3.8))  # Call static method
