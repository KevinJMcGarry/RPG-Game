from classes.game import BColors, Person
from classes.magic import Spell
from classes.inventory import Item
import sys


# Create Black Magic (** using the Spell class **)
fire = Spell("Fire", 25, 600, "black")
thunder = Spell("Thunder", 25, 600, "black")
blizzard = Spell("Blizzard", 25, 600, "black")
meteor = Spell("Meteor", 40, 1200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create White Magic (** using the Spell class **)
cure = Spell("Cure", 25, 620, "white")
curea = Spell("Curea", 32, 1500, "black")


# Create Items that Heal (notice type of either potion or elixer)
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 1000 HP", 1000)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)  # 9999 used to heal to max HP
hielixer = Item("MegaElixer", "elixer", "Fully restores all party member's HP/MP", 9999)  # 9999 used to heal to max HP

# Create Items that cause damage to enemy
grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, quake]  # from the Spell class
player_items = [{"item_name": potion, "quantity": 15}, {"item_name": hipotion, "quantity": 5},
                {"item_name": superpotion, "quantity": 5}, {"item_name": elixer, "quantity": 5},
                {"item_name": hielixer, "quantity": 2}, {"item_name": grenade, "quantity": 5}]  # from the Item class


# Instantiate player and enemy object/s
player1 = Person("Valos  :", 3260, 132, 300, 34, player_spells, player_items)
player2 = Person("Kronos :", 4160, 188, 311, 34, player_spells, player_items)
player3 = Person("Robotos:", 3089, 174, 288, 34, player_spells, player_items)
enemy = Person("Mr Ugh", 5200, 431, 525, 25, [], [])

players = [player1]

# print(player.magic)  # prints the objects from the self.magic list (these are from the Spell class)
# print(player.hp)  # prints the hp instance attribute value from the Person class

running = True
i = 0

print(f'{BColors.FAIL + BColors.BOLD}An Enemy Attacks!{BColors.ENDC}')

# The Battle Loop
while running:
    print("=" * 17)

    print("\n")
    print("NAME        HP                                        MP")

    for player in players:
        player.get_stats()  # the print statements is in the method

    enemy.get_enemy_stats()

    for player in players:
        print("\n")
        player.choose_action()
        choice = int(input('\nChoose action: '))

        # Players Attack
        if choice == 1:  # Physical Attack
            attack_damage = player.generate_damage()
            enemy.take_damage(attack_damage)  # inflicting damage on the enemy
            print(f'\nYou attacked for {attack_damage} points of damage')
        elif choice == 2:  # Magic Attack
            player.choose_magic()  # displays list of magic to chose from
            spell_index = int(input('Choose spell: ')) - 1  # starting with 0 index to work with magic list/array

            spell_chosen = player.magic[spell_index]  # remember, this is an object from the Spell class
            spell_damage = spell_chosen.generate_damage()

            current_mp = player.get_mp()  # getting the total magic points the player currently has

            if spell_chosen.cost > current_mp:  # handling scenario where you don't have enough mp to cast desired spell
                print(f'{BColors.FAIL}\nYou do not have enough current mp to cast this spell. The current spell requires '
                      f'an additional {spell_cost - current_mp} points{BColors.ENDC}')
                continue  # if you don't have enough mp, loop to beginning to be able to use attack

            player.reduce_mp(spell_chosen.cost)  # reduce your magic points for the casted spell

            if spell_chosen.type == "white":
                player.heal(spell_damage)  # not a great name, actually healing, not damaging
                print(f'{BColors.OKBLUE}{spell_chosen.name} heals for {spell_damage} HP{BColors.ENDC}')
            elif spell_chosen.type == "black":
                enemy.take_damage(spell_damage)
                print(f'\n{BColors.OKBLUE}You attacked for {spell_damage} points of damage with your '
                      f'{spell_chosen.name} spell')  # spell.name from variable above
        elif choice == 3:
            player.choose_item()
            item_choice = int(input('Choose Item: ')) - 1

            item = player.items[item_choice]["item_name"]  # choosing an item in a list and then getting the actual object name
            print(f'\nyou have chosen {item.name}')
            print(f'your item type is {item.type}')

            if player.items[item_choice]["quantity"] == 0:  # no quantity left for the item selected
                print(f'{BColors.FAIL}There is no quantity left for Item {item.name}{BColors.ENDC}')
                continue
            player.items[item_choice]["quantity"] -= 1  # deprecating item quantity by 1 each time it is used

            if item.type == "potion":
                player.heal(item.prop)
                print(f'{BColors.OKGREEN}{item.name} heals for {item.prop} HP{BColors.ENDC}')
            elif item.type == "elixer":
                if item.name == "MegaElixer":
                    for i in players:
                        i.hp = i.maxhp  # fully heal all player's HP
                        i.mp = i.maxmp  # fully heal all player's MP
                else:
                    player.hp = player.maxhp  # fully heal player's HP
                    player.mp = player.maxmp  # fully heal player's MP
                print(f'{BColors.OKGREEN}{item.name} fully restores HP/MP{BColors.ENDC}')
            elif item.type == "attack":
                enemy.take_damage(item.prop)
                print(f'{BColors.FAIL}{item.name} deals {item.prop} points of damage')


        else:
            print("Thanks for playing!!")
            break

    # Enemy's Attack
    enemy_attack_damage = enemy.generate_damage()
    player1.take_damage(enemy_attack_damage)  # we are always player 1
    print(f'Enemy attacked for {enemy_attack_damage} points of damage\n')

    # getting everyone's hp on each loop
    print('-' * 30)
    print(f'{BColors.FAIL}Enemy HP: {enemy.get_hp()}/{enemy.get_maxhp()}{BColors.ENDC}')

    # checking heath points of player and enemies to determine if round is over
    if enemy.get_hp() == 0:
        print(f'{BColors.OKGREEN}You Win!{BColors.ENDC}')
        runing = False
    elif player.get_hp() == 0:
        print(f'{BColors.FAIL}Your enemy has defeated you!{BColors.ENDC}')
        running = False



