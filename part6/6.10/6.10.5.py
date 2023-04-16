class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattr__(self, name):
        if name == "description":
            return "{} is {} years old.".format(self.name, self.age)
        else:
            return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        if name == "age" and value < 0:
            raise ValueError("Age cannot be negative.")
        else:
            object.__setattr__(self, name, value)


if __name__ == "__main__":
    person = Person("Alex", 18)
    print(person.description)  # Alex is 18 years old.

    person.age = -10  # Raises ValueError: Age cannot be negative.
