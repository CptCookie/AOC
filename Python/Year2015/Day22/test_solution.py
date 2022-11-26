from .solution import (
    DRAIN,
    MAGIC_MISSILE,
    POISEN,
    RECHARGE,
    SHIELD,
    Character,
    Warrior,
    Wizzard,
    MAGIC_DMG,
    play_wizard,
)


def test_Charakter_take_damage():
    char = Character(100, 3)
    char.take_damage(5)

    assert char.health == 98


def test_Charakter_take_damage_magic():
    char = Character(100, 3)
    char.take_damage(5, dmg_type=MAGIC_DMG)

    assert char.health == 95


def test_double_effect():
    trainee = Wizzard(100, 300)
    trainee.add_effect(SHIELD, 2)
    trainee.add_effect(SHIELD, 33)
    assert trainee.effects[SHIELD] == 33


def test_effect_poisen():
    char = Character(100, 7)
    char.add_effect(POISEN, 6)

    for n in range(6):
        char.tick()
        assert char.health == 100 - (n + 1) * 3

    assert char.effects[POISEN] == 0


def test_effect_shield():
    char = Character(1, 7)
    char.add_effect(SHIELD, 6)

    for n in range(5):
        char.tick()
        assert char.armor == 7
        assert char.effects[SHIELD] == 6 - (n + 1)

    char.tick()
    assert char.armor == 0
    assert char.effects[SHIELD] == 0


def test_recharge():
    char = Character(100, 7)
    char.add_effect(RECHARGE, 6)

    for n in range(6):
        char.tick()
        assert char.mana == (n + 1) * 101
        assert len(char.effects) == 1

    assert char.effects[RECHARGE] == 0


def test_strike():
    dummy = Character(100, 0)
    trainee = Warrior(100, 0, 8)

    trainee.strike(dummy)
    assert dummy.health == 92


def test_mana_drain():
    trainee = Wizzard(100, 0)
    exception_hit = False

    try:
        trainee.shield()
    except AttributeError:
        exception_hit = True

    assert exception_hit


def test_missile():
    dummy = Character(100, 5)
    trainee = Wizzard(100, 53)
    trainee.magic_missile(dummy)
    assert dummy.health == 96


def test_health_drain():
    dummy = Character(100, 5)
    trainee = Wizzard(100, 73)
    trainee.drain(dummy)
    assert dummy.health == 98
    assert trainee.health == 102


def test_shield():
    trainee = Wizzard(100, 113)
    trainee.shield()
    assert trainee.armor == 7
    assert trainee.effects[SHIELD] == 6


def test_recharge():
    trainee = Wizzard(100, 229)
    trainee.recharge()
    assert trainee.effects[RECHARGE] == 5


def test_play():
    actions = [POISEN, MAGIC_MISSILE]
    player = Wizzard(10, 250)
    boss = Warrior(13, 0, 8)

    play_wizard(player, boss, actions)

    assert not boss.is_alive()
    assert player.is_alive()
    assert player.mana_spend == 226


def test_play_bigger():
    actions = [RECHARGE, SHIELD, DRAIN, POISEN, MAGIC_MISSILE]
    player = Wizzard(10, 250)
    boss = Warrior(14, 0, 8)

    play_wizard(player, boss, actions)

    assert not boss.is_alive()
    assert player.is_alive()
    assert player.health == 1
    assert player.mana_spend == 641
    assert player.effects[RECHARGE] == 0
    assert player.effects[SHIELD] == 0
