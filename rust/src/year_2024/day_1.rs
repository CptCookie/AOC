use crate::Solution;
use solution_macro::mark_solution;

#[mark_solution(2024, 1)]
struct Day1;

impl Solution for Day1 {
    fn part1(&self, input: &str) -> String {
        let (mut left, mut right) = parse_input(&input);
        left.sort();
        right.sort();

        left.iter()
            .enumerate()
            .map(|(i, l)| (l - right[i]).abs())
            .sum::<i32>()
            .to_string()
    }

    fn part2(&self, input: &str) -> String {
        let (mut left, mut right) = parse_input(&input);
        left.sort();
        right.sort();

        left.iter()
            .map(|l| right.iter().filter(|r| r == &l).count() * (*l as usize))
            .sum::<usize>()
            .to_string()
    }
}

fn parse_input(input: &str) -> (Vec<i32>, Vec<i32>) {
    input
        .split('\n')
        .filter(|n| n != &"")
        .map(parse_line)
        .unzip()
}

fn parse_line(line: &str) -> (i32, i32) {
    let numbers: Vec<i32> = line
        .split_whitespace()
        .map(|n| n.parse::<i32>().unwrap())
        .collect();
    (numbers[0], numbers[1])
}
