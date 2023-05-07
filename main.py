class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

class Manager(Employee):
    def __init__(self):
        self.name = "Bob"
        self.age = 46
        self.salary = 100000
        self.subordinates = 15

class Developer(Employee):
    def __init__(self):
        self.name = "John"
        self.age = 27
        self.salary = 25000
        self.program = "Phyton"

a1 = Manager
b1 = Developer

print(a1)
print(b1)