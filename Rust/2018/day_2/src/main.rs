use std::collections::HashMap;
use std::fs;

fn main() {
    let puzzle_input: String = fs::read_to_string("2018-2.txt").unwrap();
    let ids = parse_input(puzzle_input);
    println!("Solution 1: {:?}", solution_1(&ids));
    println!("Solution 2: {}", solution_2(&ids));
}

fn solution_2(input: &Vec<String>) -> String {
    for (n, line1) in input.iter().enumerate() {
        for line2 in input[n..].iter() {
            let comp = compare_lines(line1, line2);
            match comp {
                Some(n) => return n,
                None => (),
            }
        }
    }

    String::from("")
}

fn compare_lines(line1: &String, line2: &String) -> Option<String> {
    let line2: Vec<char> = line2.chars().collect();
    let mut unique: Option<usize> = None;

    for (n, line1_char) in line1.chars().enumerate() {
        if line2[n] != line1_char {
            match unique {
                None => unique = Some(n),
                Some(_n) => return None,
            }
        }
    }

    if unique != None {
        let mut new_string = line2.clone();
        new_string.remove(unique.unwrap());
        return Some(new_string.into_iter().collect());
    } else {
        return None;
    }
}

fn solution_1(input: &Vec<String>) -> i32 {
    let mut maps: Vec<HashMap<char, i32>> = Vec::new();
    let mut twos: i32 = 0;
    let mut threes: i32 = 0;

    for line in input {
        maps.push(get_map(line))
    }

    for map in &maps {
        if containes_chars_ntimes(2, map) {
            twos += 1;
        }

        if containes_chars_ntimes(3, map) {
            threes += 1;
        }
    }
    twos * threes
}

fn containes_chars_ntimes(n_appear: i32, map: &HashMap<char, i32>) -> bool {
    let content: Vec<&i32> = map.values().collect();
    content.contains(&&n_appear)
}

fn get_map(line: &String) -> HashMap<char, i32> {
    let mut hash: HashMap<char, i32> = HashMap::new();
    for c in line.chars() {
        let counter = hash.entry(c).or_insert(0);
        *counter += 1;
    }
    hash
}

fn parse_input(puzzle_input: String) -> Vec<String> {
    let mut split: Vec<String> = puzzle_input.split("\n").map(|n| String::from(n)).collect();
    split.pop();
    split
}
