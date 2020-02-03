class Employee:

    num_of_emps = 0
    raise_amount = 1.04 # Class Variable

    def __init__(self, first, last, pay): # Constructor Method with Class Attributes
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullName(self): 
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod # Class methods automatically take the class as the first argument
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod # Static methods don't take anything as the first argument - behave like a normal function
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee): # Class inherits from Employee class
    raise_amt = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # Super handles init method for first, last, and pay by utilizing the init from Employee
        self.prog_lang = prog_lang

#print(help(Developer)) # Help functions shows method resolution order (places Python searches for attributes and methods)

emp_1 = Employee('Corey', 'Schafer', 50000)
dev_1 = Developer('Test', 'User', 60000, 'Python')


# Testing Employee Class Method
emp_str_1 = 'John-Doe-70000'
print (Employee.from_string(emp_str_1).__dict__)


# Testing Employee Static Method
import datetime
my_date = datetime.date(2020, 2, 2)
print(Employee.is_workday(my_date))

# Testing Developer Class 
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

