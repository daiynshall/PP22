"""Using super() (simple)."""

class Employee:
    def __init__(self, name):
        self.name = name

class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name)  # call parent constructor
        self.language = language

if __name__ == "__main__":
    dev = Developer("Dana", "Python")
    print("name =", dev.name)
    print("language =", dev.language)
