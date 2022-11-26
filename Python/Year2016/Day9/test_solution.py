from .solution import decompressed_length


def test_decompress_no_seq():
    assert decompressed_length("ADVENT") == len("ADVENT")


def test_decompress_1x5():
    assert decompressed_length("A(1x5)BC") == len("ABBBBBC")


def test_decompress_3x3():
    assert decompressed_length("(3x3)XYZ") == len("XYZXYZXYZ")


def test_decompress_double():
    assert decompressed_length("A(2x2)BCD(2x2)EFG") == len("ABCBCDEFEFG")


def test_decpress_ignore_overlap():
    assert decompressed_length("(6x1)(1x3)A") == len("(1x3)A")


def test_decpress_recursive():
    assert decompressed_length("(6x1)(1x3)A", recursive=True) == len("AAA")


def test_decpress_ignore_overlap_2():
    assert decompressed_length("X(8x2)(3x3)ABCY") == len("X(3x3)ABC(3x3)ABCY")


def test_decpress_recursive_2():
    assert decompressed_length("X(8x2)(3x3)ABCY", recursive=True) == len(
        "XABCABCABCABCABCABCY"
    )
