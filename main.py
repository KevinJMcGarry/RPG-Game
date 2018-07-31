from classes.game import BColors, Person
from classes.magic import Spell

# Create Black Magic (** using the Spell class **)
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create White Magic (** using the Spell class **)
cure = Spell("Cure", 12, 120, "white")
curea = Spell("Curea", 18, 200, "black")


# Instantiate player and enemy object
player = Person(460, 65, 60, 34, [fire, thunder, blizzard, meteor, cure, curea])
enemy = Person(1200, 65, 45, 25, [])

print(player.magic)  # prints the objects from the self.magic list (these are from the Spell class)
print(player.hp)  # prints the hp instance attribute value from the Person class

running = True
i = 0

print(f'{BColors.FAIL + BColors.BOLD}An Enemy Attacks!{BColors.ENDC}')

# The Battle Loop
while running:
    print("=" * 17)
    player.choose_action()
    choice = int(input('Choose action: '))

    # players attack
    if choice == 1:  # Physical Attack
        attack_damage = player.generate_damage()
        enemy.take_damage(attack_damage)  # inflicting damage on the enemy
        print(f'You attacked for {attack_damage} points of damage')
    elif choice == 2:  # Magic Attack
        player.choose_magic()
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
            print(f'{BColors.OKBLUE}You attacked for {spell_damage} points of damage with your '
                  f'{spell_chosen.name} spell')  # spell.name from variable above ??
    else:
        print("Thanks for playing!!")
        break

    # enemy's attack
    enemy_attack_damage = enemy.generate_damage()
    player.take_damage(enemy_attack_damage)
    print(f'Enemy attacked for {enemy_attack_damage} points of damage')

    # getting everyone's hp on each loop
    print('-' * 30)
    print(f'{BColors.FAIL}Enemy HP: {enemy.get_hp()}/{enemy.get_maxhp()}{BColors.ENDC}')
    print(f'{BColors.OKGREEN}Your HP: {player.get_hp()}/{player.get_maxhp()}{BColors.ENDC}')
    print(f'{BColors.OKGREEN}Your MP: {player.get_mp()}/{player.get_maxmp()}')


    # checking heath points of player and enemies to determine if round is over
    if enemy.get_hp() == 0:
        print(f'{BColors.OKGREEN}You Win!{BColors.ENDC}')
        runing = False
    elif player.get_hp() == 0:
        print(f'{BColors.FAIL}Your enemy has defeated you!{BColors.ENDC}')
        running = False



