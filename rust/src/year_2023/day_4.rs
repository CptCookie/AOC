use crate::Solution;
use solution_macro::mark_solution;
use std::collections::HashSet;

#[mark_solution(2023, 4)]
struct Day4;

impl Solution for Day4 {
    fn part1(&self, input: &str) -> String {
        let mut card_value = 0;
        for (win_nums, own_nums) in parse_input(input).iter() {
            let matches = win_nums.intersection(own_nums).count();
            if matches > 0 {
                card_value += 1 << (matches - 1);
            }
        }

        format!("{}", card_value)
    }

    fn part2(&self, input: &str) -> String {
        let cards = parse_input(input);
        let mut card_count = vec![1; cards.len()];

        for (i, (win_nums, own_nums)) in cards.iter().enumerate() {
            let matches = win_nums.intersection(own_nums).count();
            for n in 0..matches {
                card_count[i + 1 + n] += card_count[i]
            }
        }
        format!("{}", card_count.iter().sum::<usize>())
    }
}

fn parse_input(input: &str) -> Vec<(HashSet<u32>, HashSet<u32>)> {
    let mut cards = Vec::new();

    for line in input.lines() {
        let card = line.split(": ").nth(1).unwrap();

        let win_nums: HashSet<u32> = card
            .split(" | ")
            .nth(0)
            .unwrap()
            .split_ascii_whitespace()
            .map(|n| n.parse::<u32>().unwrap())
            .collect();

        let own_nums: HashSet<u32> = card
            .split(" | ")
            .nth(1)
            .unwrap()
            .split_ascii_whitespace()
            .map(|n| n.parse::<u32>().unwrap())
            .collect();

        cards.push((win_nums, own_nums))
    }
    cards
}
