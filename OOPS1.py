class Employee:
    increment = 2
    no_of_employees = 0
    def __init__(self, name, salary, ID):
        self.name = name
        self.salary = salary
        self.ID = ID
        self.increment = 1.5
        Employee.no_of_employees += 1

    def increase(self):
        # self.salary = int(self.salary * Employee.increment)
        self.salary = int(self.salary * self.increment)

    @classmethod
    def change_in_increment(cls,amount):
      cls.increment = amount


E1= Employee('Rohan', 12000, 234)
E2 = Employee('Ajay', 16000, 426)

print(Employee.no_of_employees)

E1.increment = 2.6

E1.increase()
E2.increase()

print(E1.__dict__)
print(E2.__dict__)

# Employee.change_in_increment(3)
# print(E1.salary)



