#!/usr/bin/env python
"""
employee.py

<2017-10-15>

@author: CodeRoninSY

"""

# OOP in python
import datetime
# import numpy as np


class Employee:
    ''' Employee class '''

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        """fullname"""
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        """apply_raise"""
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        """set_raise_amt"""
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        """from_string"""
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        """is_workday"""
        if (day.weekday() == 5 or day.weekday() == 6):
            return False
        return True


def main():
    """main"""
    print("Number of employees 'before instantiate'= {}".format(
        Employee.num_of_emps))
    emp1 = Employee("john", "doe", 50000)
    emp2 = Employee("jane", "doe", 48000)

    Employee.set_raise_amt(1.05)

    print("Number of employees 'after instantiate'= {}".format(
        Employee.num_of_emps))

    print("First:{}, Last:{}".format(emp1.first, emp1.last))
    print("Employee email: {}".format(emp1.email))
    print("Employee fullname: {}".format(emp1.fullname()))

    print(emp1.pay)
    emp1.apply_raise()
    print(emp1.pay)

    print(Employee.raise_amt)
    print(emp1.raise_amt)
    print(emp2.raise_amt)

    emp_str_1 = 'John-Doe-70000'
    emp_str_2 = 'Steve-Smith-30000'
    emp_str_3 = 'Jane-Doe-90000'

    new_emp_1 = Employee.from_string(emp_str_1)
    new_emp_2 = Employee.from_string(emp_str_2)
    new_emp_3 = Employee.from_string(emp_str_3)

    print("Employee fullname: {}".format(new_emp_1.fullname()))
    print("Employee fullname: {}".format(new_emp_2.fullname()))
    print("Employee fullname: {}".format(new_emp_3.fullname()))
    print("new_emp_1.email= {}".format(new_emp_1.email))
    print("new_emp_1.pay= {}".format(new_emp_1.pay))

    print("Number of employees 'after instantiate'= {}".format(
        Employee.num_of_emps))

    my_date = datetime.date(2017, 10, 19)

    print("Is {} work day? => {}".format(datetime.date(2017, 10, 19),
                                         Employee.is_workday(my_date)))

    #  print(Employee.__dict__)


if __name__ == "__main__":
    main()
