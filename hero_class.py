#!/usr/bin/env python
'''
hero_class.py

Hero -> Hero class definition
Synopsis: Hero class definition
To learn & understand the "class" feature and methods
Author: CodeRoninSY @2019
Date: <2019-04-21>

'''


class Hero():
    ''' Hero Class '''
    # class defaults
    ID = 0
    name = "Sunny"
    health = 100
    alive = 1
    level = 1
    wins = 0
    kills = 0
    clan = "Clippers"
    country = "Badlands"
    inventory = ['Sword']
    # total number of heros
    numHeros = 0

    def __init__(self, ID=ID, name=name, health=health, inventory=inventory,
                 level=level, wins=wins, kills=kills, clan=clan, country=country):
        self.ID = ID
        self.name = name
        self.inventory = inventory
        self.health = health
        self.level = level
        self.wins = wins
        self.kills = kills
        self.clan = clan
        self.country = country
        # add1 to total number of heros
        Hero.numHeros += 1

    def __str__(self):
        return f"--> ID: {self.ID}, name: {self.name}, alive: {self.alive},\
            health: {self.health}, level: {self.level}, wins: {self.wins},\
            kills: {self.kills}, clan: {self.clan}, country: {self.country},\
            inventory: {self.inventory}"

    def __repr__(self):
        return str({'ID': self.ID, 'name': self.name, 'health': self.health, \
                'level': self.level, 'wins': self.wins, 'kills': self.kills, \
                    'clan': self.clan, 'country': self.country, \
                    'inventory': self.inventory})

    @property
    def items(self):
        return self.inventory

    def additem(self, item):
        return self.inventory.append(item)

    def dropItem(self, item):
        return self.inventory.remove(item)

    @property
    def kill(self):
        return f"{self.name}: {self.kills} kills total"

    @kill.setter
    def kill(self, kill):
        self.kills = kill

    @kill.getter
    def kill(self):
        return self.kill

    def addKill(self, killno):
        self.kills += killno

    @property
    def healthstat(self):
        return self.health

    def incHealth(self, h):
        if self.health + h >= 100:
            print(f"Healthy enough now!: 100")
            self.health = 100
        else:
            self.health += h

    def decHealth(self, h):
        if self.health - h <= 0:
            print(f"Need health to be alive!: 0!")
            self.alive = 0
            self.health = 0
        else:
            self.health -= h

    @staticmethod
    def set_level(self, amount):
        self.level = amount

    def addWin(self, win):
        self.wins += win


## Hero class default
hero0 = Hero()

print(f"Hero : {hero0!s}")
print(f"Hero name: {hero0.name}")
print(f"Hero items: {hero0.items}")
print(f"Hero stat: {hero0.healthstat}")
print(f"Hero wins: {hero0.wins}")

# generate a Hero object
hero = Hero(name='Thor', ID=1, health=85, level=2,
            inventory=['Mjolnir', 'Chariot', 'Bilskirnir'], wins=2, kills=10,
            clan="Asgardian", country='Asgard')

print(f"Hero name: {hero.name}")
print(f"Hero items: {hero.items}")
print(f"Hero stat: {hero.healthstat}")

hero.additem('Bifrost')
Hero.set_level(hero, 5)
print(f"Hero {hero.name} items: {hero.items}")
print(f"Hero {hero.name} level: {hero.level}")
print(f"Hero {hero.name} wins: {hero.wins}")

hero.dropItem('Bifrost')
hero.addWin(4)
print(f"Hero {hero.name}, items: {hero.items}")
print(f"Hero {hero.name} wins: {hero.wins}")
print(f"Hero {hero.name}, kill #: {hero.kills}")
print(f"Hero {hero.name}, kill total #: {hero.kills}")
hero.kill = 12
print(f"Hero {hero.name}, kill #: {hero.kills}")
hero.addKill(5)
print(f"Hero {hero.name}, kill #: {hero.kills}")
print(f"Hero {hero.name}, health: {hero.health}")
hero.incHealth(10)
print(f"Hero {hero.name}, health: {hero.health}")
hero.incHealth(10)
print(f"Hero {hero.name}, health: {hero.health}")
print(f"Hero {hero.name}, alive: {hero.alive}")

print(f"Hero {hero!s}")
print(f"Hero {hero!r}")

print(f"Number of heros {Hero.numHeros}")
