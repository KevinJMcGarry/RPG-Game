from classes.game import BColors, Person
import pdb

# magic object is an array of spells that can be used
magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 12, "dmg": 80},
         {"name": "Blizzard", "cost": 10, "dmg": 60}]

# instantiating your player object and an enemy object
player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0

print(f'{BColors.FAIL + BColors.BOLD}An Enemy Attacks!{BColors.ENDC}')

while running:
    print("=" * 17)
    player.choose_action()
    choice = int(input('Choose action: '))

    if choice == 1:
        attack_damage = player.generate_damage()
        enemy.take_damage(attack_damage)  # inflicting damage on the enemy
        print(f'You inflicted {attack_damage} points of damage with your attack')
        print(f'Enemy HP is now {enemy.get_hp()}')
    else:
        player.choose_magic()
        spell_index = int(input('Choose spell: ')) - 1  # starting with 0 index to work with magic list/array
        spell_damage = player.generate_spell_damage(spell_index)
        enemy.take_damage(spell_damage)
        print(f'You inflicted {spell_damage} points of damage with your {magic[spell_index]["name"]} spell. '
              f'Enemy HP is now {enemy.get_hp()}')

    enemy_attack_damage = enemy.generate_damage()
    player.take_damage(enemy_attack_damage)
    print(f'Enemy inflicted {enemy_attack_damage} points of damage. Your total HP left is {player.get_hp()}')


    running = False

