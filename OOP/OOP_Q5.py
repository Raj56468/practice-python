class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    
class Employee(Person):

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    
emp = Employee("Alice", 30, 50000)


print(f"Name: {emp.name}")
print(f"Age: {emp.age}")
print(f"Salary: {emp.salary}")