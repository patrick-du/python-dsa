import datetime


class Employee:

    num_of_emps = 0
    raise_amount = 1.04  # Class Variable

    def __init__(self, first, last, pay):  # Constructor Method with Class Attributes
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod  # Class methods automatically take the class as the first argument
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod  # Static methods don't take anything as the first argument - behave like a normal function
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):  # Subclass that inherits from Employee
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # Super handles init method by utilizing the Employee init
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullName())


# Instance of Employee, Developer, Manager
emp_1 = Employee('Corey', 'Schafer', 50000)
dev_1 = Developer('Test', 'User', 60000, 'Python')
dev_2 = Developer('Test2', 'User2', 60000, 'Python')
mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])


# Testing Employee Class Method
emp_str_1 = 'John-Doe-70000'
print(Employee.from_string(emp_str_1).__dict__)


# Testing Employee Static Method
my_date = datetime.date(2020, 2, 2)
print(Employee.is_workday(my_date))


# Testing Developer Class
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)


# Help functions shows method resolution order (places Python searches for attributes and methods)
# print(help(Developer))


# Testing Manager Class
print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()


# isInstance() tells us whether an object is an instance of a class
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

# issubclass() tells us whether a class is a subclass of another
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))
