#!/usr/bin/env python
# -*- coding: windows-1252 -*-
'''
elegant_solutions_alias.py

= Alias methods =
From Nina Zakharenko - Elegant solutions for everyday python problems
PyCon 2018

Dev: CodeRoninSY
Date: <2019-05-11>

'''


class Word:
    ''' Word '''
    def __init__(self, word):
        self.word = word

    def __repr__(self):
        return self.word

    def __add__(self, other_word):
        return Word('%s %s' % (self.word, other_word))

    # Add an alias from method __add__
    concat = __add__


first_name = Word('Atra')
last_name = Word('Punio')

fullname = first_name + last_name
print(f"{fullname}")


class Dog(object):
    ''' Dog '''
    sound = 'Bark'
    def speak(self):
        print(self.sound + '!', self.sound + '!')


my_dog = Dog()
my_dog.speak()
print(getattr(my_dog, 'speak'))
speak_method = getattr(my_dog, 'speak')
speak_method()