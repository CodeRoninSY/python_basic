#!/usr/bin/env python
''' hero_class.py
Class examples; Perl6 translated to Python
'''


class Hero():
    ''' Hero Class '''
    inventory = ['Golden Fleece']
    name = "Hercules"
    health = 100
    level = 1

    def __init__(self, name=name, health=health, inventory=inventory,
                 level=level):
        self.name = name
        self.inventory = inventory
        self.health = health
        self.level = level

    def items(self):
        return self.inventory

    def additem(self, item):
        return self.inventory.append(item)

    def healthstat(self):
        return self.health

    @staticmethod
    def set_level(self, amount):
        self.level = amount


hero = Hero()

#  print(f"Hero : {hero}")
print(f"Hero name: {hero.name}")
print(f"Hero items: {hero.items()}")
print(f"Hero stat: {hero.healthstat()}")

hero = Hero(name='Thor', health=85, level=2,
            inventory=['Mjolnir', 'Chariot', 'Bilskirnir'])

#  print(f"Hero : {hero}")
print(f"Hero name: {hero.name}")
print(f"Hero items: {hero.items()}")
print(f"Hero stat: {hero.healthstat()}")

hero.additem('Bifrost')
Hero.set_level(hero, 5)
print(f"Hero items: {hero.items()}")
print(f"Hero level: {hero.level}")
