class Int:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __mul__(self, other):
        return self.value * other.value

    def __sub__(self, other):
        return self.value - other.value

    def __eq__(self, other):
        return self.value == other.value

    def __float__(self):
        return float(self.value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"Int({self.value})"


a = Int(3)
b = Int(3)

print(a + b)
print(a * b)
print(a == b)
print(str(a))
print(float(a))
print(repr(a))


class User:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age and self.phone == other.phone

    def __gt__(self, other):
        return self.age > other.age

    def __lt__(self, other):
        return self.age < other.age

    def __str__(self):
        return f"name={self.name}, age={self.age}, phone={self.phone}"


user1 = User("Jhon", 26, 1234)
user2 = User("Jhon", 26, 1234)
user3 = User("Jhon", 27, 1234)

print(user1 == user2)
print(user3 > user2)
print(str(user1))
