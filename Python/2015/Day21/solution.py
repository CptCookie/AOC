import itertools
from .const import WEAPONS, ARMOR, RINGS, BOSS


def all_equipt_combinations():
    weapon_combination = itertools.combinations(WEAPONS, r=1)
    armor_combination = itertools.combinations(ARMOR, r=1)
    ring_combination = itertools.combinations(RINGS, r=2)

    return list(
        itertools.product(
            list(weapon_combination), list(armor_combination), list(ring_combination)
        )
    )


def simulate_combat(player, enemy):
    """simulate the combat between the player and the enemy
    character are given in the format:
    [ healthpoints, attack, defense ]
    """
    # breakpoint()

    player_turn = True
    while player[0] > 0 and enemy[0] > 0:
        if player_turn:
            attack_net = player[1] - enemy[2]
            attack_net = 1 if attack_net <= 0 else attack_net
            enemy[0] -= attack_net
            player_turn = False
        else:
            attack_net = enemy[1] - player[2]
            attack_net = 1 if attack_net <= 0 else attack_net
            player[0] -= attack_net
            player_turn = True
    return enemy[0] <= 0


def cheapest_win():
    winning_costs = []
    for weapon, armor, rings in all_equipt_combinations():
        weapon = weapon[0]
        armor = armor[0]

        attack = weapon[1] + sum([n[1] for n in rings])
        defense = armor[2] + sum([n[2] for n in rings])

        if simulate_combat([100, attack, defense], BOSS.copy()):
            winning_costs.append(weapon[0] + armor[0] + sum(n[0] for n in rings))

    return min(winning_costs)


def expensive_loss():
    loosing_costs = []
    for weapon, armor, rings in all_equipt_combinations():
        weapon = weapon[0]
        armor = armor[0]

        attack = weapon[1] + sum([n[1] for n in rings])
        defense = armor[2] + sum([n[2] for n in rings])

        if not simulate_combat([100, attack, defense], BOSS.copy()):
            loosing_costs.append(weapon[0] + armor[0] + sum(n[0] for n in rings))

    return max(loosing_costs)


def solve(puzzle_input):
    print(f"solution 1: {cheapest_win()}")
    print(f"solution 2: {expensive_loss()}")
