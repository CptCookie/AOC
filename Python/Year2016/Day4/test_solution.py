from .solution import solution_1, valid_room_name, decrypt_name


def test_valid_room_name():
    assert valid_room_name("aaaaa-bbb-z-y-x", "abxyz") == True
    assert valid_room_name("a-b-c-d-e-f-g-h", "abcde") == True
    assert valid_room_name("not-a-real-room", "oarel") == True
    assert valid_room_name("totally-real-room", "decoy") == False


def test_solution_1():
    test_input = """aaaaa-bbb-z-y-x-123[abxyz]
    a-b-c-d-e-f-g-h-987[abcde]
    not-a-real-room-404[oarel]
    totally-real-room-200[decoy]
    """

    assert solution_1(test_input) == 123 + 987 + 404


def test_decrypt_name():
    assert decrypt_name("qzmt-zixmtkozy-ivhz", 343) == "very encrypted name"
