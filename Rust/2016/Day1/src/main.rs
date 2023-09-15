use regex::Regex;
use std::{collections::HashSet, fs};

fn parse(input: &str) -> Vec<(&str, i16)> {
    let pattern = Regex::new(r#"([RL])(\d+)"#).unwrap();
    pattern
        .captures_iter(input)
        .map(|c| c.extract())
        .map(|(_, [dir, dist])| (dir, dist.parse().unwrap()))
        .collect()
}

fn solution_1(directions: &Vec<(&str, i16)>) -> i16 {
    let moves: Vec<(i16, i16)> = vec![(0, 1), (1, 0), (0, -1), (-1, 0)];
    let mut dir = 0; 
    let mut c_pos = (0, 0);

    for (d, l) in directions.iter() {
        match d {
            &"R" => dir = (dir + 1) % 4,
            &"L" => dir = (4 + dir - 1) % 4,
            _ => (),
        }

        let (dx, dy) = moves[dir];
        c_pos = (c_pos.0 + *l * dx, c_pos.1 + *l * dy);
    }

    c_pos.0.abs() + c_pos.1.abs()
}

fn solution_2(directions: &Vec<(&str, i16)>) -> Option<i16> {
    let moves: Vec<(i16, i16)> = vec![(0, 1), (1, 0), (0, -1), (-1, 0)];

    let mut visited = HashSet::with_capacity(directions.len()/2);
    let mut c_pos = (0, 0);
    let mut dir = 0;

    for (d, l) in directions.iter() {
        match d {
            &"R" => dir = (dir + 1) % 4,
            &"L" => dir = (4 + dir - 1) % 4,
            _ => (),
        }

        let (dx, dy) = moves[dir];

        for _ in 0..*l {
            c_pos = (c_pos.0 + 1 * dx, c_pos.1 + 1 * dy);

            if visited.contains(&c_pos) {
                return Some(c_pos.0.abs() + c_pos.1.abs());
            }
            visited.insert(c_pos);
        }
    }

    None
}

fn main() {
    use std::time::Instant;
    
    let input_data = fs::read_to_string("input.txt").expect("Error on reading the file");
    let input = parse(&input_data);
    
    let mut now = Instant::now();
    println!("{:?} took: {:.2?}", solution_1(&input), now.elapsed());
    now = Instant::now();
    println!("{:?} took: {:.2?}", solution_2(&input), now.elapsed());
}
