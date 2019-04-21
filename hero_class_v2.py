#!/usr/bin/env python
'''
hero_class.py

Synopsis: Hero class definition
To learn & understand the "class" feature and methods
Author: CodeRoninSY @2019
Date: <2019-04-21>

'''
import json
#  from pprint import pprint
#  from functools import reduce
#  from operator import attrgetter, itemgetter


class Hero():
    ''' Hero Class '''
    # class properties
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
    superpower = ['Martial arts']
    # total number of heros
    numHeros = 0

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        # add1 to total number of heros
        Hero.numHeros += 1

    def __str__(self):
        return f"--> ID: {self.ID}, name: {self.name}, alive: {self.alive},\
            health: {self.health}, level: {self.level}, wins: {self.wins},\
            losses: {self.losses}, kills: {self.kills}, clan: {self.clan},\
            country: {self.country}, inventory: {self.inventory}, \
            archenemy: {self.archenemy}, superpower: {self.superpower}"

    def __repr__(self):
        return str({'ID': self.ID, 'name': self.name, 'health': self.health,
                    'alive': self.alive, 'level': self.level,
                    'wins': self.wins, 'losses': self.losses,
                    'kills': self.kills, 'clan': self.clan,
                    'country': self.country, 'inventory': self.inventory,
                    'archenemy': self.archenemy,
                    'superpower': self.superpower})

    @property
    def enemy(self):
        ''' enemy '''
        return self.archenemy

    def add_enemy(self, rival):
        ''' add_enemy '''
        return self.archenemy.append(rival)

    def del_enemy(self, rival):
        ''' del_enemy '''
        return self.archenemy.remove(rival)

    @property
    def items(self):
        ''' items '''
        return self.inventory

    @items.setter
    def items(self, item):
        self.inventory = self.inventory.append(item)

    def additem(self, item):
        ''' additem '''
        return self.inventory.append(item)

    def drop_item(self, item):
        ''' drop_item '''
        return self.inventory.remove(item)

    def del_item_n(self, n):
        ''' del_item_n '''
        del self.inventory[n]

    @property
    def kill(self):
        ''' kill '''
        return f"{self.name}: {self.kills} kills total"

    @kill.setter
    def kill(self, kill):
        self.kills = kill

    @kill.getter
    def kill(self):
        ''' kill.getter '''
        return self.kill

    def add_kill(self, killno):
        ''' add_kill '''
        self.kills += killno

    @property
    def healthstat(self):
        ''' healthstat '''
        return self.health

    def inc_health(self, h):
        ''' inc_health '''
        if self.health + h >= 100:
            print(f"{self.name} -> Healthy enough now!: 100")
            self.health = 100
        else:
            self.health += h

    def dec_health(self, h):
        ''' dec_health '''
        if self.health - h <= 0:
            print(f"{self.name} -> Need health to be alive!: 0!")
            self.alive = 0
            self.health = 0
        else:
            self.health -= h

    @staticmethod
    def set_level(self, amount):
        ''' set_level '''
        self.level = amount

    def add_win(self, win):
        ''' add_win '''
        self.wins += win

    def add_loss(self, loss):
        ''' add_loss '''
        self.losses += loss


# read json file
def read_json_data(filename, raw=False):
    ''' read_json_data '''
    try:
        data = json.load(open(filename))
    except FileNotFoundError:
        return []
    else:
        if raw:
            return data["heros"]
        return [Hero(**hero) for hero in data["heros"]]


def main():
    ''' main '''
    #  ## Hero class default
    #  hero0 = Hero()
    #
    #  print(f"Hero : {hero0!s}")
    #  print(f"Hero name: {hero0.name}")
    #  print(f"Hero items: {hero0.items}")
    #  print(f"Hero stat: {hero0.healthstat}")
    #  print(f"Hero wins: {hero0.wins}")
    #
    #  # generate a Hero object
    #  hero = Hero(name='Thor', ID=1, health=85, level=2,
    #              inventory=['Mjolnir', 'Chariot', 'Bilskirnir'], wins=2, kills=10,
    #              clan="Asgardian", country='Asgard',
    #              archenemy=['Thanos', 'Hella', 'Malekith'])
    #
    #  print(f"Hero name: {hero.name}")
    #  print(f"Hero items: {hero.items}")
    #  print(f"Hero stat: {hero.healthstat}")
    #
    #  hero.add_item('Bifrost')
    #  Hero.set_level(hero, 5)
    #  print(f"Hero {hero.name} items: {hero.items}")
    #  print(f"Hero {hero.name} level: {hero.level}")
    #  print(f"Hero {hero.name} wins: {hero.wins}")
    #
    #  hero.drop_item('Bifrost')
    #  hero.add_win(4)
    #  print(f"Hero {hero.name}, items: {hero.items}")
    #  print(f"Hero {hero.name} wins: {hero.wins}")
    #  print(f"Hero {hero.name}, kill #: {hero.kills}")
    #  print(f"Hero {hero.name}, kill total #: {hero.kills}")
    #  hero.kill = 12
    #  print(f"Hero {hero.name}, kill #: {hero.kills}")
    #  hero.add_kill(5)
    #  print(f"Hero {hero.name}, kill #: {hero.kills}")
    #  print(f"Hero {hero.name}, health: {hero.health}")
    #  hero.inc_health(10)
    #  print(f"Hero {hero.name}, health: {hero.health}")
    #  hero.inc_health(10)
    #  print(f"Hero {hero.name}, health: {hero.health}")
    #  print(f"Hero {hero.name}, alive: {hero.alive}")
    #
    #  hero.add_loss(2)
    #  print(f"Hero {hero.name}, losses: {hero.losses}")
    #
    #  # full object
    #  print(f"Hero {hero!s}")
    #  print(f"Hero {hero!r}")
    #
    #  print(f"Number of heros {Hero.numHeros}")

    #  HEROS = read_json_data("heros.json")
    R_HEROS = read_json_data("heros.json", raw=True)

    #  pprint(HEROS)
    #  pprint(R_HEROS)

    #  ids = sorted(R_HEROS, key=itemgetter('ID'))
    #  print(f"Sorted IDs[0]: {ids[0]['ID']}, {ids[0]['name']}, {ids[0]['archenemy']}")

    for i, h in enumerate(R_HEROS):
        eroe = Hero(**h)
        print(f"{eroe!s}")
        print(f"\nHero ID: {eroe.ID}, name: {eroe.name}, kills: {eroe.kills},\
              health: {eroe.health},\
              inventory: {eroe.inventory}, enemy: {eroe.archenemy}")
        eroe.add_kill(-1)
        eroe.additem('Katana')
        eroe.add_enemy("Galactus")
        print(f"\n{eroe.name}, kills: {eroe.kills}, health: {eroe.health},\
              inventory: {eroe.inventory}, enemy: {eroe.archenemy}")
        eroe.del_item_n(-1)
        print(f"\n{eroe.name}, kills: {eroe.kills}, health: {eroe.health},\
            inventory: {eroe.inventory}")
        print(f"\nTotal generated heros: {Hero.numHeros}")


# MAIN
if __name__ == "__main__":
    main()
