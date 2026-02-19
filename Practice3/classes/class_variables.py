"""Class variable vs instance variable (simple)."""

class Car:  # Create a Car class (template)
    wheels = 4  # Class variable (shared: same for all cars)

    def __init__(self, brand):  # Constructor (runs when object is created)
        self.brand = brand  # Instance variable (unique: different for each car)

if __name__ == "__main__":  # Runs only when file is executed directly
    c1 = Car("Toyota")  # Create first car object
    c2 = Car("BMW")  # Create second car object

    print("c1 wheels =", c1.wheels)  # Access class variable through object
    print("c2 wheels =", c2.wheels)

    Car.wheels = 6  # Change class variable (affects all cars)
    print("after Car.wheels=6 -> c1 wheels =", c1.wheels, ", c2 wheels =", c2.wheels)

    c1.wheels = 3  # Create an instance variable wheels ONLY for c1 (overrides class value)
    print("after c1.wheels=3 -> c1 wheels =", c1.wheels, ", c2 wheels =", c2.wheels)
