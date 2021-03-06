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
    def __init__(self, name, hp, mp, atk, df, magic_list, items):
        # hit points, magic points, attack, defense, magic, items(inventory)
        # setting each instance variable (self.xxx) to what is passed in as an argument when creating an object
        self.name = name
        self.maxhp = hp  # this is the maximum number of health points we can have
        self.hp = hp  # current health point, as we do battle - this will change
        self.maxmp = mp  # maximum magic points our character can have
        self.mp = mp  # how many magic points our character currently has
        self.atkl = atk - 10  # attack power - lower damage range
        self.atkh = atk + 10  # attack power - higher amount of damage (adding 10 to value of argument passed in)
        self.df = df  # defense power
        self.magic = magic_list  # this will be a list objects from the Spells class (see main.py)
        self.items = items
        self.actions = ["Attack", "Magic", "Items", "Exit Game"]  # these will be displayed each time we have a turn

    def generate_damage(self):  # damage our player generates with an attack
        return random.randrange(self.atkl, self.atkh)  # return damage that is randomly chosen between two ranges

    def take_damage(self, dmg):  # damage taken by either us (the player) or the enemy object
        self.hp -= dmg
        if self.hp < 0:  # if hp is less than 0, then set hp to 0
            self.hp = 0
        return self.hp

    def heal(self, dmg):  # Healing Magic method (using dmg value for amount of healing added to health points)
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
        print(f'\n{BColors.BOLD}{self.name}{BColors.ENDC}')
        print(f'{BColors.OKBLUE + BColors.BOLD}-- Actions --{BColors.ENDC}')
        i = 1
        for action in self.actions:
            print(f'{i}. {action}')
            i += 1

    def choose_magic(self):
        print(f'\n{BColors.OKBLUE + BColors.BOLD}-- Magic --{BColors.ENDC}')
        i = 1
        for spell in self.magic:  # remember, self.magic is a list of objects created from the Spell class
            print(f'{i}. {spell.name}, cost: {spell.cost}')
            i += 1
        # each object in the self.magic list contains instance attributes created from the Spell class

    def choose_item(self):
        print(f'\n{BColors.OKBLUE + BColors.BOLD}-- Items --{BColors.ENDC}')
        i = 1
        for item in self.items:  # remember, self.item is a list of objects created from the Item class
            print(f'{i}. {item["item_name"].name} : {item["item_name"].description} (x{item["quantity"]})')
            i += 1
        # self.items is a list of dicts pairs passed in for the items argument. see (player_items) in main.py for list
        # each dict contains a key called "item". when the key is referenced it returns the actual item object
        # eg - potion, elixir, superpotion, etc.
        # each of these are an actual object created from the Item class, so each object contains its own attributes
        # two of those attributes that we are referencing are name and description

    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 2  # going to have a 50 character bar (players are 25 character bars)

        while bar_ticks > 0:
            hp_bar += "█"  # fill up the hp bar with bar ticks until bar_ticks == 0
            bar_ticks -= 1  # counter for filling up hp_bar with bar blocks

        while len(hp_bar) < 50:
            hp_bar += " "  # adding whitespace to the beginning of the current hp for alignment

        hp_string = f"{self.hp}/{self.maxhp}"
        current_hp = ""  # empty string that will be populated with updated hp_string variable from below

        if len(hp_string) < 11:  # total max hp xxxx/xxxx (including / character). Making sure xxxx/xxxx == 9, if not
            # then our current hp has fallen below 4 digits
            decreased = 11 - len(hp_string)  # determining if the current hp falls below 4 digits
            while decreased > 0:
                current_hp += " "  # adding a white space character to keep everything in alignment when current hp
                # drops to 3 digits or below
                decreased -= 1  # removing the decreased count until it reaches 0
            current_hp += hp_string
        else:
            current_hp = hp_string  # if length of hp_string == 9, assign hp_string to current_hp

        print("                        __________________________________________________ ")
        print(f"{self.name}    {current_hp}  |{BColors.FAIL}{hp_bar}{BColors.ENDC}|")


    def get_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 4  # a green bar block representing a percentage of HP

        # (self.hp / self.maxhp) * 100 = % of hp you have left.
        # Divide this percentage by 4 (as there are 25 ticks/bars in hp), gives you the number of bars to represent
        # this percentage. This is because 25 bars x 4 = 100%

        mp_bar = ""
        mp_ticks = (self.mp / self.maxmp) * 100 / 10  # there are only 10 slots for bars so (10 x 10) = 100%

        while bar_ticks > 0:
            hp_bar += "█"  # fill up the hp bar with bar ticks until bar_ticks == 0
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "  # adding whitespace to the beginning of the current hp for alignment

        while mp_ticks > 0:
            mp_bar += "█"  # fill up the mp bar with bar ticks until bar_ticks == 0
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "  # adding whitespace to the beginning of the current mp for alignment

        # this section of code is for handling the current hp/maxhp number
        # so that when current hp falls to 3 digits or less, the current hp number shifts inward to stay in alignment
        # this will keep the entire light (graph bars etc.) in alignment

        hp_string = f"{self.hp}/{self.maxhp}"
        current_hp = ""  # empty string that will be populated with updated hp_string variable from below

        if len(hp_string) < 9:  # total max hp xxxx/xxxx (including / character). Making sure xxxx/xxxx == 9, if not
            # then our current hp has fallen below 4 digits
            decreased = 9 - len(hp_string)  # determining if the current hp falls below 4 digits
            while decreased > 0:
                current_hp += " "  # adding a white space character to keep everything in alignment when current hp
                                  # drops to 3 digits or below
                decreased -= 1  # removing the decreased count until it reaches 0
            current_hp += hp_string
        else:
            current_hp = hp_string  # if length of hp_string == 9, assign hp_string to current_hp

        # this section performs the same calculations for the mp bar to make sure it stays in alignment if the current
        # mp drops to 2 digits or less

        mp_string = f"{self.mp}/{self.maxmp}"
        current_mp = ""  # empty string that will be populated with updated mp_string variable from below

        if len(mp_string) < 7:  # this tells us that our current_mp has dropped below 3 digits
            decreased = 7 - len(mp_string)
            while decreased > 0:  # while the current_mp isn't full digits (3)
                current_mp += " "
                decreased -= 1

            current_mp += mp_string
        else:
            current_mp = mp_string

        print("                        _________________________              __________ ")
        print(f"{self.name}    {current_hp}  |{BColors.OKGREEN}{hp_bar}{BColors.ENDC}|"
              f"    {current_mp} |{BColors.OKBLUE}{mp_bar}{BColors.ENDC}|")




