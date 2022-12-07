from .solution import solution_1, solution_2, parse_data

TEST_DATA = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


def test_parse_data():
    dir_tree = parse_data(TEST_DATA)
    assert "//a" in dir_tree
    assert "//a/e" in dir_tree
    assert "//a/e/i" in dir_tree
    assert "//a/f" in dir_tree
    assert "//a/g" in dir_tree
    assert "//a/h.lst" in dir_tree
    assert "//b.txt" in dir_tree
    assert "//c.dat" in dir_tree
    assert "//d" in dir_tree
    assert "//d" in dir_tree
    assert "//d/j" in dir_tree
    assert "//d/d.log" in dir_tree
    assert "//d/d.ext" in dir_tree
    assert "//d/k" in dir_tree


def test_children():
    dir_tree = parse_data(TEST_DATA)

    assert len(dir_tree["/"].children) == 4


def test_size():
    dir_tree = parse_data(TEST_DATA)

    dir_tree["//a/e/i"].size == 584
    dir_tree["//a/e"].size == 584
    dir_tree["//a"].size == 94853
    dir_tree["//d"].size == 24933642
    dir_tree["/"].size == 48381165


def test_solution_1():
    assert solution_1(TEST_DATA) == 95437
