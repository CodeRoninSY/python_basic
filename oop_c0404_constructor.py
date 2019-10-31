#!/usr/bin/env python
"""
#**********************************************************
# oop_constructor_c0404.py
# polymorphism : many shapes
# * two classes with same interface (i.e., method name)
# * the methods are often different, but conceptually similar
#
# <2018-01-07> CodeRoninSY
#**********************************************************
"""
from __future__ import print_function

__author__ = 'CodeRoninSY'
__date__ = '<2019-10-29>'
__version__ = 1.0
# print(__doc__)
# print(__author__)
# print(__date__)
# print(__version__)
# print('*' * 72)
# print('\n')

# chap 0404 - inheriting constructor
import random
import os.path
import requests
import pandas as pd

DOGNAMESF = "dognames.txt"
CATNAMESF = "catnames.txt"
DOGBREEDFILE = "dog_breed.csv"
CATBREEDFILE = "cat_breed.csv"


class WriteFile(object):
    """ WriteFile """
    def __init__(self, writer, deftxt=""):
        self.writer = writer
        self.deftxt = deftxt

    def write(self, text=""):
        self.writer.write(text)


class Animal(object):
    """ Animal """
    count = 0

    def __init__(self, name):
        self.name = name
        Animal.count += 1

    def eat(self, food):
        print('{0} eats {1}'.format(self.name, food))

    @classmethod
    def get_count(cls):
        return cls.count


class Dog(Animal):
    """ Dog """
    count = 0

    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.breed = [random.choice(get_breed(DOGBREEDFILE))]
        Dog.count += 1

    def fetch(self, thing):
        print('{0} goes after the {1]!'.format(self.name, thing))

    def show_affection(self):
        print('{0} wags tail'.format(self.name))


class Cat(Animal):
    """ Cat """
    count = 0
    def __init__(self, name):
        super(Cat, self).__init__(name)
        self.breed = [random.choice(get_breed(CATBREEDFILE))]
        Cat.count += 1

    def swatstring(self):
        print('{0} shreds the string!'.format(self.name))

    def show_affection(self):
        print('{0} purrs'.format(self.name))


def save_breed_from_web(url, file=CATBREEDFILE, table='cat'):
    """ save breed names from wiki page tables """
    html = requests.get(url).content
    df_list = pd.read_html(html)

    if table == 'dog':
        df = df_list[0]
    elif table == 'cat':
        df = df_list[1]
    else:
        df = df_list[-1]
    # save breed table to csv
    if table == 'dog':
        print(df[:-1])
        df[:-1].to_csv(file)
    elif table == 'cat':
        print(df[:])
        df[:].to_csv(file)


def get_breed(breedfile=CATBREEDFILE):
    """ get_breed from generated 'BREEDFILE' """
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(cur_dir, breedfile)) as data:
        breed = [br.rstrip() for br in data]
    return list(breed)


def main():
    """ main """
    wrt = open('Dog_cat_random_names.txt', 'w+')
    w = WriteFile(wrt)

    # download Breed names from wiki pages
    # save_breed_from_web(
    #     'https://en.wikipedia.org/wiki/List_of_dog_breeds',
    #     DOGBREEDFILE, 'dog')
    # save_breed_from_web(
    #     'https://en.wikipedia.org/wiki/List_of_cat_breeds',
    #     CATBREEDFILE, 'cat')

    cur_dir = os.path.dirname(os.path.abspath(__file__))
    # print("cur_dir: {}, __file__: {}".format(cur_dir, __file__))
    # read dog & cat names from files
    with open(os.path.join(cur_dir, DOGNAMESF)) as data:
        dogname = [d.rstrip() for d in data]
    with open(os.path.join(cur_dir, CATNAMESF)) as data:
        catname = [c.rstrip() for c in data]

    # populate Dog instances
    for i in range(int(len(dogname)/19)):
        d = Dog(random.choice(dogname))
        print(
            "Dog name: {},\tBreed: {}".format(
                d.name, d.breed[0].split(',')[1:3]),file=w)

    # populate Cat instances
    for i in range(int(len(catname)/19)):
        c = Cat(random.choice(catname))
        print(
            "Cat name: {},\tBreed: {}".format(
                c.name, c.breed[0].split(',')[1:3]),file=w)
    # Dog & Cat counts
    print("Dog count: {}".format(d.get_count()))
    print("Cat count: {}".format(c.get_count()))

    w.write("Dog count: {}\n".format(d.get_count()))
    w.write("Cat count: {}\n".format(c.get_count()))
    wrt.close()


if __name__ == "__main__":
    main()
