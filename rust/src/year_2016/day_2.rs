use std::fs;

fn get_next_pos(
    current_pos: (usize, usize),
    direction: char,
    keypad: &Vec<Vec<char>>,
) -> (usize, usize) {
    let mut next_pos = current_pos;
    match direction {
        'L' if current_pos.0 > 0 => next_pos.0 -= 1,
        'U' if current_pos.1 > 0 => next_pos.1 -= 1,
        'R' if current_pos.0 < keypad.len() - 1 => next_pos.0 += 1,
        'D' if current_pos.1 < keypad[0].len() - 1 => next_pos.1 += 1,
        _ => return current_pos
    }

    if keypad[next_pos.1][next_pos.0] != 'X' {
        next_pos
    } else {
        current_pos
    }
}

fn get_code(keypad: &Vec<Vec<char>>, start: (usize, usize), instructions: &Vec<&str>) -> String {
    let mut code: Vec<char> = vec![];
    let mut pos = start;

    for line in instructions.iter() {
        line.chars()
            .for_each(|d| pos = get_next_pos(pos, d, keypad));
        code.push(keypad[pos.1][pos.0]);
    }

    code.iter().collect()
}

fn solution_1(instructions: &Vec<&str>) -> String {
    let keypad = vec![
        vec!['1', '2', '3'],
        vec!['4', '5', '6'],
        vec!['7', '8', '9'],
    ];
    let start = (1, 1);
    let code = get_code(&keypad, start, instructions);
    code
}

fn solution_2(instructions: &Vec<&str>) -> String {
    let keypad = vec![
        vec!['X', 'X', '1', 'X', 'X'],
        vec!['X', '2', '3', '4', 'X'],
        vec!['5', '6', '7', '8', '9'],
        vec!['X', 'A', 'B', 'C', 'X'],
        vec!['X', 'X', 'D', 'X', 'X'],
    ];
    let start = (1, 1);
    let code = get_code(&keypad, start, instructions);
    code
}

fn parse_data(input: &String) -> Vec<&str> {
    input.split_terminator("\n").collect()
}

fn main() {
    use std::time::Instant;

    let input_data = fs::read_to_string("input.txt").expect("Error on reading the file");
    let instructions = parse_data(&input_data);

    let mut now = Instant::now();
    println! {"solution 1 {:?} took: {:.2?}", solution_1(&instructions),  now.elapsed()}
    now = Instant::now();
    println! {"solution 2 {:?} took: {:.2?}", solution_2(&instructions),  now.elapsed()}
}
