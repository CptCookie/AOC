import re
from types import new_class


NORMAL_DMG = "0"
MAGIC_DMG = "1"

MAGIC_MISSILE = "missile"
DRAIN = "drain"
POISEN = "poisen"
RECHARGE = "recharge"
SHIELD = "shield"

MOVES = [MAGIC_MISSILE, DRAIN, POISEN, RECHARGE, SHIELD]


def mana_drain(mana):
    def wrapper(fun):
        def inner(character, *args, **kwargs):
            if character.mana < mana:
                raise AttributeError("Mana to Low")
            else:
                character.mana -= mana
                character.mana_spend += mana
                return fun(character, *args, **kwargs)

        return inner

    return wrapper


class Character:
    def __init__(self, health: int, armor: int):
        self.health = health
        self.armor = armor
        self.effects = {}

    def take_damage(self, damage: int, dmg_type=NORMAL_DMG):
        if dmg_type == NORMAL_DMG:
            self.health -= max(1, damage - self.armor)
        else:
            self.health -= damage

    def is_alive(self):
        return self.health > 0

    def add_effect(self, effect, time):
        if effect not in self.effects or self.effects[effect] < time:
            self.effects[effect] = time

    def tick(self):
        for effect in self.effects:
            time_left = self.effects[effect]
            if time_left == 1 and effect == SHIELD:
                self.armor -= 7

            if time_left > 0 and effect == RECHARGE:
                self.mana += 101

            if time_left > 0 and effect == POISEN:
                self.health -= 3

            if time_left > 0:
                self.effects[effect] -= 1


class Warrior(Character):
    def __init__(self, health: int, armor: int, attack: int):
        super().__init__(health, armor)
        self.attack = attack

    def strike(self, character: Character):
        character.take_damage(self.attack)


class Wizzard(Character):
    def __init__(self, health: int, mana: int):
        super().__init__(health, 0)
        self.mana = mana
        self.mana_spend = 0

    @mana_drain(53)
    def magic_missile(self, target: Character):
        target.take_damage(4, dmg_type=MAGIC_DMG)

    @mana_drain(73)
    def drain(self, target: Character):
        target.take_damage(2, dmg_type=MAGIC_DMG)
        self.health += 2

    @mana_drain(113)
    def shield(self, *args, **kwargs):
        self.add_effect(SHIELD, 6)
        self.armor += 7

    @mana_drain(173)
    def poisen(self, target: Character):
        target.add_effect(POISEN, 6)

    @mana_drain(229)
    def recharge(self):
        self.add_effect(RECHARGE, 5)


def play_wizard(wizzard: Wizzard, warrior: Warrior, actions, hard_core=False):
    for a in actions:
        if hard_core:
            wizzard.health -= 1
            if not wizzard.is_alive:
                return

        if a == MAGIC_MISSILE:
            wizzard.magic_missile(warrior)
        if a == DRAIN:
            wizzard.drain(warrior)
        if a == POISEN:
            wizzard.poisen(warrior)
        if a == SHIELD:
            wizzard.shield()
        if a == RECHARGE:
            wizzard.recharge()

        warrior.tick()
        wizzard.tick()

        if not (wizzard.is_alive() and warrior.is_alive()):
            return

        warrior.strike(wizzard)
        wizzard.tick()
        warrior.tick()

        if not (wizzard.is_alive() and warrior.is_alive()):
            return
    return


def find_win_least_mana(warrior_health, warrior_attack, hard_core=False):
    plays = [[m] for m in MOVES]
    least_mana = None

    while plays:
        new_plays = []
        for p in plays:
            warrior = Warrior(int(warrior_health), 0, int(warrior_attack))
            wizzard = Wizzard(50, 500)

            try:
                play_wizard(wizzard, warrior, p, hard_core)
            except AttributeError:
                continue

            if not warrior.is_alive() and (
                least_mana is None or wizzard.mana_spend < least_mana
            ):
                least_mana = wizzard.mana_spend
            elif (
                wizzard.is_alive()
                and warrior.is_alive()
                and (least_mana is None or wizzard.mana_spend < least_mana)
            ):
                new_plays.extend(get_sensable_new_moves(wizzard, warrior, p))
        plays = new_plays
    return least_mana


def get_sensable_new_moves(wizzard: Wizzard, warrior: Warrior, current_move):
    new_moves = []

    if wizzard.health <= max(warrior.attack - wizzard.armor, 1) and wizzard.mana > 73:
        new_moves.append(current_move + [DRAIN])

    if wizzard.mana > 53:
        new_moves.append(current_move + [MAGIC_MISSILE])

    if (
        SHIELD not in wizzard.effects or wizzard.effects[SHIELD] == 0
    ) and wizzard.mana > 113:
        new_moves.append(current_move + [SHIELD])

    if (
        RECHARGE not in wizzard.effects or wizzard.effects[RECHARGE] == 0
    ) and wizzard.mana > 229:
        new_moves.append(current_move + [RECHARGE])

    if (
        POISEN not in warrior.effects or warrior.effects[POISEN] == 0
    ) and wizzard.mana > 173:
        new_moves.append(current_move + [POISEN])

    return new_moves


def solution_1(puzzle_input):
    boss_health, boss_attack = re.search(
        r"Hit Points: (\d+)|Damage: (\d+)", puzzle_input
    ).groups()
    return find_win_least_mana(71, 10)


def solution_2(puzzle_input):
    return find_win_least_mana(71, 10, hard_core=True)
