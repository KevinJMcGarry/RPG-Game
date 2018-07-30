from classes.game import BColors, Person

# magic object is an array of spells that can be used
magic = [{"name": "Fire", "cost": 10, "dmg": 100},
         {"name": "Thunder", "cost": 12, "dmg": 124},
         {"name": "Blizzard", "cost": 10, "dmg": 100}]

# instantiating your player object and an enemy object
player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0

print(f'{BColors.FAIL + BColors.BOLD}An Enemy Attacks!{BColors.ENDC}')

# the battle loop
while running:
    print("=" * 17)
    player.choose_action()
    choice = int(input('Choose action: '))

    # players attack
    if choice == 1:
        attack_damage = player.generate_damage()
        enemy.take_damage(attack_damage)  # inflicting damage on the enemy
        print(f'You attacked for {attack_damage} points of damage')
    else:
        player.choose_magic()
        spell_index = int(input('Choose spell: ')) - 1  # starting with 0 index to work with magic list/array
        spell_damage = player.generate_spell_damage(spell_index)
        enemy.take_damage(spell_damage)
        spell = magic[spell_index]["name"]
        spell_cost = player.get_spell_mp_cost(spell_index)

        current_mp = player.get_mp()  # getting the total magic points the player currently has

        if spell_cost > current_mp:  # handling scenario where you don't have enough mp to cast desired spell
            print(f'{BColors.FAIL}\nYou do not have enough current mp to cast this spell. The current spell requires '
                  f'an additional {spell_cost - current_mp} points{BColors.ENDC}')
            continue  # if you don't have enough mp, loop to beginning to be able to use attack

        player.reduce_mp(spell_cost)  # reduce your magic points for the casted spell
        enemy.take_damage(spell_damage)

        print(f'{BColors.OKBLUE}You attacked for {spell_damage} points of damage with your '
              f'{magic[spell_index]["name"]} spell')

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



