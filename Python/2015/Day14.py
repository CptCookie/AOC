def positoning_after(reindeer, time):
    pos = {}
    for r in reindeer:
        circle = int(time / ( r[2] + r[3] ) )
        if time % ( r[2] + r[3] ) > r[2]:
            pos.update({r[0]: (circle + 1) * r[1] * r[2] })
        else:
            pos.update({r[0]: (circle)* r[2] * r[1] + time%(r[2]+r[3])*r[1]})
    return pos

def score_after(reindeer, time):
    scores = {r[0]: 0 for r in reindeer}
    for t in range(1, time+1):
        points = positoning_after(reindeer, t)
        leeding_distance = points[max(points, key=points.get)]
        for n in points:
            if points[n] == leeding_distance:
                scores[n] += 1
    return scores

def test_pos_after():
    reindeer = [
        ['A', 14, 10, 127],
        ['B', 16, 11, 162]
    ]
    assert positoning_after(reindeer, 1000) == {'A': 1120, 'B': 1056}

def test_score_after():
    reindeer = [
        ['A', 14, 10, 127],
        ['B', 16, 11, 162]
    ]
    assert score_after(reindeer, 1000) == {'B': 689, 'A': 312}

def solve(puzzle_input):
    puzzle_input = [n.split(' ') for n in puzzle_input.split('\n') if n != '']
    puzzle_input = [[n[0], int(n[3]), int(n[6]), int(n[-2])] for n in puzzle_input]
    
    print('testing ', end='')
    test_pos_after()
    test_score_after()
    print('done')

    print('solving')
    print(f'solution 1: {positoning_after(puzzle_input, 2503)}')
    print(f'solution 2: {score_after(puzzle_input, 2503)}')