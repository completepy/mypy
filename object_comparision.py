class User:
    def __init__(self, name, age, mobile):
        self.name = name
        self.age = age
        self.mobile = mobile

    def __str__(self):
        return f"name={self.name}, age={self.age}, mobile={self.mobile}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age and self.mobile == other.mobile

    def __gt__(self, other):
        return self.age > other.age

    def __lt__(self, other):
        return self.age < other.age


if __name__ == '__main__':
    jack = User(name='Jack', age=12, mobile=1321323)
    rose = User(name="Rose", age=13, mobile=123)
    jack_jon = User(name='Jack', age=12, mobile=1321323)
    print(jack == jack_jon)
    2 + 3
    5 + 2
