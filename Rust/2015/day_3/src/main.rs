use std::fs;

type Postion = Vec<i32>;

fn main() {
    let puzzle_input = fs::read_to_string("2015-3.txt").unwrap();
    println!("Solution 1: {}", solution_1(&puzzle_input));
    println!("Solution 1: {}", solution_2(&puzzle_input));
}

fn solution_1(puzzle_input: &String) -> usize {
    get_unique(deliver_presents(puzzle_input)).len()
}

fn solution_2(puzzle_input: &String) -> usize {
    let mut santa_move: Vec<char> = Vec::with_capacity(puzzle_input.len() / 2);
    let mut bot_move: Vec<char> = Vec::with_capacity(puzzle_input.len() / 2);

    for (n, c) in puzzle_input.chars().enumerate() {
        match n % 2 {
            0 => santa_move.push(c),
            _ => bot_move.push(c),
        }
    }
    let mut pos: Vec<Postion> = deliver_presents(&santa_move.iter().collect::<String>());
    pos.append(&mut deliver_presents(&bot_move.iter().collect::<String>()));
    get_unique(pos).len()
}

fn deliver_presents(movements: &String) -> Vec<Postion> {
    let mut positions: Vec<Postion> = Vec::with_capacity(movements.len() + 1);
    positions.push(vec![0, 0]);
    for m in movements.chars() {
        let x = positions.last().unwrap()[0];
        let y = positions.last().unwrap()[1];

        match m {
            '^' => positions.push(vec![x, y + 1]),
            '>' => positions.push(vec![x + 1, y]),
            'v' => positions.push(vec![x, y - 1]),
            '<' => positions.push(vec![x - 1, y]),
            _ => (),
        }
    }

    positions
}

fn get_unique(positions: Vec<Postion>) -> Vec<Postion> {
    let mut unique: Vec<Postion> = Vec::new();
    for n in positions.iter() {
        if !unique.contains(n) {
            unique.push(n.clone());
        }
    }
    unique
}

#[cfg(test)]
mod test {
    use crate::*;

    #[test]
    fn test_move() {
        let test_data = String::from("^>v<");
        assert_eq!(
            deliver_presents(&test_data),
            vec![vec![0, 0], vec![0, 1], vec![1, 1], vec![1, 0], vec![0, 0]]
        )
    }

    #[test]
    fn test_unique() {
        assert_eq!(
            get_unique(vec![
                vec![0, 0],
                vec![0, 1],
                vec![0, 1],
                vec![1, 0],
                vec![0, 0]
            ]),
            vec![vec![0, 0], vec![0, 1], vec![1, 0]]
        )
    }
}
