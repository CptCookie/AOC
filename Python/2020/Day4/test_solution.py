from .solution import validate_field


def test_byr_validation():
    assert validate_field("byr", "1920")
    assert validate_field("byr", "2002")
    assert validate_field("byr", "2000")
    assert validate_field("byr", "1999")
    assert not validate_field("byr", "2003")
    assert not validate_field("byr", "1919")


def test_iyr_validation():
    assert validate_field("iyr", "2010")
    assert validate_field("iyr", "2020")
    assert not validate_field("iyr", "2000")
    assert not validate_field("iyr", "2025")


def test_ecl_validation():
    assert validate_field("ecl", "brn")
    assert not validate_field("ecl", "wat")


def test_pid_validation():
    assert validate_field("pid", "000000001")
    assert not validate_field("pid", "0123456789")


def test_hcl_validation():
    assert validate_field("hcl", "#123abc")
    assert not validate_field("hcl", "#123abz")
    assert not validate_field("hcl", "123abc")
