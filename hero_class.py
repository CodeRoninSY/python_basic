#!/usr/bin/env python
'''
hero_class.py

Synopsis: Hero class definition
To learn & understand the "class" feature and methods
Author: CodeRoninSY @2019
Date: <2019-04-21>

'''
import json
from pprint import pprint


class Hero():
    ''' Hero Class '''
    # class defaults
    ID = 0
    name = "Sunny"
    health = 100
    alive = 1
    level = 1
    wins = 0
    losses = 0
    kills = 0
    clan = "Clippers"
    country = "Badlands"
    inventory = ['Sword']
    archenemy = ['Baron Quinn']
    # total number of heros
    numHeros = 0

    def __init__(self, ID=ID, name=name, health=health, alive=alive,
                 inventory=inventory,
                 level=level, wins=wins, losses=losses, kills=kills,
                 clan=clan, country=country, archenemy=archenemy):
        self.ID = ID
        self.name = name
        self.inventory = inventory
        self.health = health
        self.level = level
        self.wins = wins
        self.alive = alive
        self.losses = losses
        self.kills = kills
        self.clan = clan
        self.country = country
        self.archenemy = archenemy
        # add1 to total number of heros
        Hero.numHeros += 1

    def __str__(self):
        return f"--> ID: {self.ID}, name: {self.name}, alive: {self.alive},\
            health: {self.health}, level: {self.level}, wins: {self.wins},\
            losses: {self.losses}, kills: {self.kills}, clan: {self.clan},\
            country: {self.country}, inventory: {self.inventory}, \
            archenemy: {self.archenemy}"

    def __repr__(self):
        return str({'ID': self.ID, 'name': self.name, 'health': self.health, \
                    'alive': self.alive, 'level': self.level, 'wins': self.wins, \
                    'losses': self.losses, 'kills': self.kills, \
                    'clan': self.clan, 'country': self.country, \
                    'inventory': self.inventory, 'archenemy': self.archenemy})

    @property
    def enemy(self):
        return self.archenemy

    @enemy.setter
    def enemy(self, rival):
        self.archenemy.additem(rival)

    @property
    def items(self):
        return self.inventory

    @items.setter
    def items(self, item):
        self.inventory = self.inventory.append(item)

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
            print(f"{self.name} -> Healthy enough now!: 100")
            self.health = 100
        else:
            self.health += h

    def decHealth(self, h):
        if self.health - h <= 0:
            print(f"{self.name} -> Need health to be alive!: 0!")
            self.alive = 0
            self.health = 0
        else:
            self.health -= h

    @staticmethod
    def set_level(self, amount):
        self.level = amount

    def addWin(self, win):
        self.wins += win

    def addLoss(self, loss):
        self.losses += loss


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
            clan="Asgardian", country='Asgard',
            archenemy=['Thanos', 'Hella', 'Malekith'])

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

hero.addLoss(2)
print(f"Hero {hero.name}, losses: {hero.losses}")

# full object
print(f"Hero {hero!s}")
print(f"Hero {hero!r}")

print(f"Number of heros {Hero.numHeros}")


DATAHERO = {
    "heros": [ {
            'ID': 2,
            'name': "DareDevil",
            'health': 100,
            'alive': 1,
            'level': 3,
            'wins': 19,
            'losses': 1,
            'kills': 0,
            'clan': "Defenders",
            'country': "US",
            'inventory': ['Armor', 'Sticks', 'Horned mask'],
            'archenemy': ['Wilson Fisk'],
        },

    {
            'ID': 3,
            'name': "Superman",
            'health': 100,
            'alive': 1,
            'level': 100,
            'wins': 20,
            'losses': 2,
            'kills': 5,
            'clan': 'El family',
            'country': "US",
            'inventory': ['Body suit'],
            'archenemy': ["General Zod", "Lex Luthor"],
        },
    ]
    }


# json data
data = DATAHERO
pprint(data)


def get_entity(data, entity):
    return data['entity']

#  # printout data dictionary
#  for data_id, data_info in data.items():
#      print(f"\nPersonId: {data_id}")
#      for key in data_info:
#          print(f"\t\t{key}: {data_info[key]}")
