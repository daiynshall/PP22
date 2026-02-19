"""Method overriding: same method name, different behavior."""

class Parent:
    def hello(self):
        print("Мен ата-анамын")

class Child(Parent):
    def hello(self):
        print("Мен баламын")

if __name__ == "__main__":
    p = Parent()
    c = Child()
    p.hello()
    c.hello()
