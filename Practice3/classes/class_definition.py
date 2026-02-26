"""Class definition: simplest Person class."""

class Person: #We create a Person template (class)
    def __init__(self, name, age):  #We initialize the object using a constructor (init)
        self.name = name   #We store data as attributes (name, age)
        self.age = age

if __name__ == "__main__":  #This part runs only when we run the file directly
    p1 = Person("Amina", 18)   #We create (instantiate) an object from the class
    print("name =", p1.name) #We access the name using dot notation (p1.name) and print it
    print("age =", p1.age)

#A class defines what an object should look like, and an object is created based on that class.