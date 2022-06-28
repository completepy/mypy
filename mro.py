class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def greet(self):
        print(f"Hi user:{self.username}")


class Customer(User):
    def greet(self):
        print(f"Hi Customer, {self.username}")


class Employee(User):
    def greet(self):
        print(f"Hi Employee, {self.username}")


class Chef(Employee):
    def greet(self):
        print(f"Hi Chef, {self.username}")


class Receptionist(Employee):
    def greet(self):
        print(f"Hi Receptionist, {self.username}")


class Waiter(Employee):
    def greet(self):
        print(f"Hi Waiter, {self.username}")


class FrontWaiter(Waiter):
    def greet(self):
        print(f"Hi FrontWaiter, {self.username}")


class HeadWaiter(Waiter, Receptionist, Customer):
    def greet(self):
        print(f"Hi Head Waiter, {self.username}")


print(HeadWaiter.__mro__)
