# colors class - the ability to use different colors inside of a terminal
# persons class - create objects for ourselves and enemies

# https://github.com/JosephDelgadillo

import random   # used for generate random values for attack damage


class BColors:
    # these are class attributes, apply to all objects created from this class
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:  # this is our character
    def __init__(self, hp, mp, atk, df, magic_list):
        # hit points, magic points, attack, defense, magic
        # setting each instance variable (self.xxx) to what is passed in as an argument when creating an object
        self.maxhp = hp  # this is the maximum number of health points we can have
        self.hp = hp  # current health point, as we do battle - this will change
        self.maxmp = mp  # maximum magic points our character can have
        self.mp = mp  # how many magic points our character currently has
        self.atkl = atk - 10  # attack power - lower damage range
        self.atkh = atk + 10  # attack power - higher amount of damage (adding 10 to value of argument passed in)
        self.df = df  # defense power
        self.magic = magic_list  # this will be a list objects from the Spells class (see main.py)
        self.actions = ["Attack", "Magic", "Exit Game"]  # these will be displayed each time we have a turn

    def generate_damage(self):  # damage our player generates with an attack
        return random.randrange(self.atkl, self.atkh)  # return damage that is randomly chosen between two ranges

    def take_damage(self, dmg):  # damage taken by either us (the player) or the enemy object
        self.hp -= dmg
        if self.hp < 0:  # if hp is less than 0, then set hp to 0
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    # now creating a few utility classes to get properties

    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost


    # now defining actions we can take - attack or magic
    # if we chose magic, we must then have a way to select the actual spell

    def choose_action(self):
        print(f'{BColors.OKBLUE + BColors.BOLD}-- Actions --{BColors.ENDC}')
        i = 1
        for action in self.actions:
            print(f'{i}: {action}')
            i += 1

    def choose_magic(self):
        print(f'{BColors.OKBLUE + BColors.BOLD}-- Magic --{BColors.ENDC}')
        i = 1
        for spell in self.magic:  # remember, self.magic is a list of objects created from the spell class
            print(f'{i}: {spell.name}, cost: {spell.cost}')
            i += 1
        # each object in the self.magic list contains instance attributes created from the Spell class










