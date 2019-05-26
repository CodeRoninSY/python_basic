#!/usr/bin/env python
"""
employee_template.py

Class tutorials

CodeRoninSY @2019
<2019-05-04>

Note:
1. fullname() is changed to "@property"

"""


class Employee:
    """Employee"""
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    @property
    def fullname(self):
        """ fullname """
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        """ apply_raise """
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    """Developer(Employee)"""
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super(Developer, self).__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    """Manager(Employee)"""
    num_emp = 0

    def __init__(self, first, last, pay, employees=None):
        super(Manager, self).__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        """ add_emp """
        if emp not in self.employees:
            self.employees.append(emp)
            Manager.num_emp += 1

    def remove_emp(self, emp):
        """ remove_emp """
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        """ print_emps """
        for emp in self.employees:
            print('-->', emp.fullname)


dev_1 = Developer('Abdulhamid', 'Osmanoglu', 90000, 'Python')
dev_2 = Developer('Osman', 'Ertugrul', 100000, 'Perl')
mngr_1 = Manager('Ertugrul', 'Gündüzalpoglu', 100000, 'C')
emp_1 = Employee('Bilal', 'Habeşi', 50000)

#  mngr_1.add_emp(dev_1)
#  mngr_1.add_emp(dev_2)
#  print(f"Employees of mngr_1> {mngr_1.print_emps()}")

print(mngr_1.fullname)
#  print(mngr_1.print_emps())
print(dev_1.fullname)
print(dev_2.fullname)
print(emp_1.fullname)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print(dev_2.pay)
dev_2.apply_raise()
print(dev_2.pay)

# print(help(Developer))

print(dev_1.email)
print(dev_1.prog_lang)
print(dev_2.email)
print(dev_2.prog_lang)
