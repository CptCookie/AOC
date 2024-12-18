use std::{fs::File, io::Read};

fn parse_input(input: &str) -> (Vec<i32>, Vec<i32>) {
    return input
        .split('\n')
        .filter(|n| n != &"")
        .map(parse_line)
        .unzip();
}

fn parse_line(line: &str) -> (i32, i32) {
    let numbers: Vec<i32> = line
        .split_whitespace()
        .map(|n| n.parse::<i32>().unwrap())
        .collect();
    return (numbers[0], numbers[1]);
}

fn solution_1(numbers: &mut (Vec<i32>, Vec<i32>)) -> i32 {
    let (left, right) = numbers;
    left.sort();
    right.sort();

    left.iter()
        .enumerate()
        .map(|(i, l)| (l - right[i]).abs())
        .sum()
}

fn solution_2((left, right): &(Vec<i32>, Vec<i32>)) -> usize {
    left.iter()
        .map(|l| right.iter().filter(|r| r == &l).count() * (*l as usize))
        .sum()
}

fn main() {
    let mut file = File::open("input.txt").unwrap();
    let mut input: String = String::from("");
    let _ = file.read_to_string(&mut input);
    let mut numbers = parse_input(&input);
    println!("solution 1: {}", solution_1(&mut numbers));
    println!("solution 2: {}", solution_2(&numbers));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solution_1() {
        let mut numbers = (vec![3, 4, 2, 1, 3, 3], vec![4, 3, 5, 3, 9, 3]);
        let result = solution_1(&mut numbers);
        assert!(result == 11, "wrong result {}", result)
    }

    #[test]
    fn test_solution_2() {
        let numbers = (vec![3, 4, 2, 1, 3, 3], vec![4, 3, 5, 3, 9, 3]);
        let result = solution_2(&numbers);
        assert!(result == 31, "wrong result {}", result)
    }
}
