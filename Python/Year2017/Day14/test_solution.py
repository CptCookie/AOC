from .solution import solution_1, solution_2, mark_cluster, search_clusters


def test_mark_clust():
    test_disc = [
        ["#", "#", ".", "."],
        ["#", ".", "#", "."],
        ["#", ".", ".", "#"],
        [".", "#", ".", "."],
    ]

    expected_disc = [
        [1, 1, ".", "."],
        [1, ".", "#", "."],
        [1, ".", ".", "#"],
        [".", "#", ".", "."],
    ]

    assert mark_cluster(test_disc, (0, 0), number=1) == expected_disc


def test_search_cluster():
    test_disc = [
        ["#", "#", ".", "."],
        ["#", ".", "#", "."],
        ["#", ".", ".", "#"],
        [".", "#", ".", "."],
    ]

    expected_disc = [
        [1, 1, ".", "."],
        [1, ".", 2, "."],
        [1, ".", ".", 3],
        [".", 4, ".", "."],
    ]

    new_disc, found = search_clusters(test_disc)
    assert found == 4
    assert new_disc == expected_disc


def test_solution_1():
    test_input = "flqrgnkx"
    assert solution_1(test_input) == 8108


def test_solution_2():
    test_input = "flqrgnkx"
    assert solution_2(test_input) == 1242
