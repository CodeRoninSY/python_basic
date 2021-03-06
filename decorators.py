#!/usr/bin/env python
''' decorators.py

Decorators example
# Decorators wrap a function, modifying its behavior.

'''

import math
from decorlib import decorator, timer, debug, slow_down, do_twice
from decorlib import repeat


#  # Decorators
#  def decor(func):
#      def wrapper():
#          print("qualcosa sta arrivando!")
#          func()
#          print("ecco e' qui")
#      return wrapper
#
#  def say_ohr():
#      print("Ohharraaa!")
#
#
#  say_ohr = decor(say_ohr)
#
#  say_ohr()

#  # with a 'pie' syntax - syntactic sugar for Decorators
#  def decorator(func):
#      def wrapper():
#          print("qcosa arrivando..")
#          func()
#          print("eccolo")
#      return wrapper
#
#
#  @decorator
#  def sayit():
#      print("Hobarraaa!")
#
#
#  sayit()
#
#
#
#  @do_twice
#  def say():
#      print("hoppalaaaaaa!")
#
#
#  say()
#
#
#  # decorating funcs with args
#  @do_twice
#  def selam(nome):
#      print(f"Ciao {nome}")
#
#
#  selam("Mondo")


#  # @decorator
#  @decorator
#  def r_selam(nome):
#      print("Costruire il saluto".rjust(40, u'\u00b7'))
#      return f"Ciao {nome}"
#
#
#  s_sy= r_selam("Sener")
#  print(s_sy.rjust(18, u'\u2219'))
#
#
#  # @timer decorator
#  @timer
#  def waste_some_time(num_times):
#      for _ in range(num_times):
#          sum([i**2 for i in range(10000)])
#
#
#  waste_some_time(1)
#  waste_some_time(51)


# Historic Person Data
DH = {
    'p1': {
        'name': "Halid ibn al-Walid",
        'nick': "The Great General",
        'predecessor': "",
        'successor': "",
        'father': "Mughirah",
        'mother': "",
        'title': {
            "Commander-in-Chief",
            "Military governor of Iraq",
            "Governor of Chalcis" },
        'born': 585,
        'died': 642,
        'burial': "Khalid ibn al-Walid mosque, Homs, Syria",
        'allegiance': "Rashidun Caliphate",
        'service': "Rashidun Islamic Army",
        'service_year': "632-638",
        'rank': "Commander-in-chief",
        'ref': "https://en.wikipedia.org/wiki/Khalid_ibn_al-Walid",
    },
    'p2': {
        'name': "Sultan Mehmed Han bin Murad Han",
        'nick': "The Conqueror",
        'predecessor': "Murad 2",
        'successor': "Bayezid 2",
        'father': "Murad 2",
        'mother': "Huma Hatun",
        'title': {
            "Sultan of the Ottoman Empire",
            "Kayser-i Rûm",
            "The Lord of the Two Lands and the Two Seas",
            "Padishah" },
        'born': 1432,
        'died': 1481,
        'burial': "Fatih Mosque, Istanbul",
        'allegiance': "Imperial House of Osman",
        'service': "Ottoman Empire",
        'service_year': "1451-1481",
        'rank': "Emperor / Padishah"
    },
    'p3': {
        'name': "Alp Arslan",
        'nick': "Sultan of the Seljuk Empire",
        'predecessor': "Tughril",
        'successor': "Malik-Shah 1",
        'father': "Chaghri Bey",
        'mother': "",
        'title': {
            "Sultan Alp Arslan",
            "Seljuk Emperor",
        },
        'born': 1030,
        'died': 1072,
        'burial': "",
        'allegiance': "House of Seljuk",
        'service': "Seljuk Empire",
        'service_year': "1063-1072",
        'rank': "Sultan"
    },
    'p4': {
        'name': "Abu Ali Hasan ibn Ali Tusi",
        'nick': "Nizam al-Mulk",
        'predecessor': "Al-Kunduri",
        'successor': "Taj al-Mulk Abu'l Ghana'im",
        'father': "Ali Tusi",
        'mother': "",
        'title': {
            "Vizier of the Seljuk Empire",
        },
        'born': 1018,
        'died': 1092,
        'burial': "",
        'allegiance': "Seljuk Empire",
        'service': "Seljuk Empire",
        'service_year': "1064-1092",
        'rank': "Grand Vizier"
    },
    'p5': {
        'name': "Kanuni Sultan Suleyman",
        'nick': "Muhtesem Suleyman",
        'predecessor': "Selim I",
        'successor': "Selim II",
        'father': "Selim I",
        'mother': "Hafsa Sultan",
        'title': {
            "Sultan of the Ottoman Empire",
            "Custodian of the Two Holy Mosques",
            "Ottoman Caliph"
        },
        'born': 1494,
        'died': 1566,
        'burial': "Suleymaniye Mosque, Istanbul",
        'allegiance': "Imperial House of Osman",
        'service': "Ottoman Empire",
        'service_year': "1520-1566",
        'rank': "Emperor"
    },
}

# printout DH dictionary
for DH_id, DH_info in DH.items():
    print(f"\nPersonId: {DH_id}")
    for key in DH_info:
        print(f"\t\t{key}: {DH_info[key]}")


# @debug
@debug
def make_greeting(*name, age=None):
    if age is None:
        return f"As-salam {name}! Unknown age.."
    else:
        return f"As-salamu-alaykum {name}; {age}!"


make_greeting(DH['p1']['name'], DH['p1']['nick'],
              DH['p1']['father'], DH['p1']['title'],
              age=DH['p1']['died'] - DH['p1']['born'])

make_greeting(DH['p2']['name'], DH['p2']['nick'],
              DH['p2']['father'], DH['p2']['title'],
              age=DH['p2']['died'] - DH['p2']['born'])

make_greeting(DH['p3']['name'], DH['p3']['nick'],
              DH['p3']['father'], DH['p3']['title'],
              age=DH['p3']['died'] - DH['p3']['born'])

make_greeting(DH['p4']['name'], DH['p4']['nick'],
              DH['p4']['father'], DH['p4']['title'],
              age=DH['p4']['died'] - DH['p4']['born'])

make_greeting(DH['p5']['name'], DH['p5']['nick'],
              DH['p5']['father'], DH['p5']['title'],
              age=DH['p5']['died'] - DH['p5']['born'])

# math library example
math.factorial = debug(math.factorial)

def appr_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))

# approximate e(n)
appr_e(5)


# slow-down example
@slow_down
def countdown(from_num):
    if from_num < 1:
        print("Liftoff!")
    else:
        print(from_num)
        countdown(from_num - 1)


countdown(5)


# Decorating Classes
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        ''' get value of radius '''
        return self._radius

    @radius.setter
    def radius(self, value):
        ''' set radius '''
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    @property
    def area(self):
        ''' calculate area '''
        return self.pi() * self.radius**2

    def cylinder_volume(self, height):
        ''' calculate volume of cylinder '''
        return self.area * height

    @classmethod
    def unit_circle(cls):
        ''' factory method creating a circle with radius 1 '''
        return cls(1)

    @staticmethod
    def pi():
        ''' value of pi '''
        return 3.141592654


c = Circle(5)
print(f"c.radius: {c.radius}")
print(f"c.area: {c.area}")


class TimeWaster:
    @debug
    def __init__(self, max_num):
        self.max_num = max_num

    @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])


tw = TimeWaster(1000)
tw.waste_time(999)


# nesting decorators
@debug
@do_twice
def greet(name):
    print(f"Hello {name}")


greet("Oguz Kaan")


# decorators with arguments
@repeat(num_times=4)
def greetn(name):
    print(f"Hello {name}")


greetn("Viva El Mundo")
