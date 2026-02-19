"""*args and **kwargs: super simple examples."""

def sum_all(*args):
    return sum(args)

def build_profile(username, **details):
    profile = {"username": username}
    profile.update(details)
    return profile

if __name__ == "__main__":
    print("sum_all(1,2,3,4) =", sum_all(1, 2, 3, 4))

    user = build_profile("amir", age=19, city="Almaty")
    print("profile =", user)
