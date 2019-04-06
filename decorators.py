#!/usr/bin/env python
''' decorators.py

Decorators example
# Decorators wrap a function, modifying its behavior.

'''

from decorlib import decorator, timer

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


@decorator
def r_selam(nome):
    print("Costruire il saluto")
    return f"Ciao {nome}"


s_julia = r_selam("Julia")
print(s_julia)


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])


waste_some_time(1)
waste_some_time(9999)
