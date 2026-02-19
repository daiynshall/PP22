"""Function arguments: default, *args, **kwargs (simple)."""

def power(base, exponent=2):
    # Default exponent is 2
    return base ** exponent

def total(*nums):
    # *nums collects any number of values into a tuple
    return sum(nums)

def show_profile(**info):
    # **info collects named arguments into a dictionary
    for k, v in info.items():
        print(k, "=", v)

if __name__ == "__main__":
    print("power(5) =", power(5))
    print("power(5, 3) =", power(5, 3))

    print("total(1, 2, 3) =", total(1, 2, 3))

    show_profile(name="Ali", age=18, city="Almaty")
