import math

def parse_input(puzzle_input):
    box_dimension = []
    for box in puzzle_input.split('\n'):
        if box != '':
            box_dimension.append([int(n) for n in box.split('x')])
    return box_dimension

def total_wrapping_paper(puzzle_input:str):
    boxes = parse_input(puzzle_input)
    paper = [paper_needed(n) for n in boxes]
    return sum(paper)

def paper_needed(box: [int]):
    areas = [box[0] * box[1], box[1] * box[2], box[0] * box[2]]
    return min(areas) + sum(areas) * 2

def total_material_needed(puzzle_input, material_func):
    boxes = parse_input(puzzle_input)
    paper = [material_func(n) for n in boxes]
    return sum(paper)

def ribbon_needed(box: [int]):
    return sum(sorted(box)[:-1])*2 + math.prod(box)

def test_wrapping_paper():
    assert paper_needed([2,3,4]) == 58
    assert paper_needed([1,1,10]) == 43

def test_ribbon():
    assert ribbon_needed([2,3,4]) == 34
    assert ribbon_needed([1,1,10]) == 14

def solve(puzzle_input):
    print('testing')
    test_wrapping_paper()
    test_ribbon()

    print('solving')
    print(total_material_needed(puzzle_input, paper_needed))
    print(total_material_needed(puzzle_input, ribbon_needed))