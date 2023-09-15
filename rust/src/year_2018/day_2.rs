use std::collections::HashMap;

pub fn part_1(input: &String) -> String {
    let ids = parse_input(input);
    let mut maps: Vec<HashMap<char, i32>> = Vec::new();
    let mut twos: i32 = 0;
    let mut threes: i32 = 0;

    for line in ids {
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
    (twos * threes).to_string()
}

pub fn part_2(input: &String) -> String {
    let ids = parse_input(input);

    for (n, line1) in ids.iter().enumerate() {
        for line2 in ids[n..].iter() {
            let comp = compare_lines(*line1, *line2);
            match comp {
                Some(n) => return n,
                None => (),
            }
        }
    }

    String::from("")
}

fn compare_lines(line1: &str, line2: &str) -> Option<String> {
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

fn containes_chars_ntimes(n_appear: i32, map: &HashMap<char, i32>) -> bool {
    let content: Vec<&i32> = map.values().collect();
    content.contains(&&n_appear)
}

fn get_map(line: &str) -> HashMap<char, i32> {
    let mut hash: HashMap<char, i32> = HashMap::new();
    for c in line.chars() {
        let counter = hash.entry(c).or_insert(0);
        *counter += 1;
    }
    hash
}

fn parse_input(puzzle_input: &String) -> Vec<&str> {
    let mut split: Vec<&str> = puzzle_input.split("\n").collect();
    split.pop();
    split
}
