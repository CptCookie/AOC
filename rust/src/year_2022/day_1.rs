use crate::Solution;
use solution_macro::mark_solution;

#[mark_solution(2022, 1)]
struct Day1;

impl Solution for Day1 {
    fn part1(&self, input: &str) -> String {
        let puzzle_data = parse_data(input);
        let mut sum_calories: Vec<u32> = sum_elf_calories(puzzle_data);

        sum_calories.sort();
        sum_calories[sum_calories.len() - 1].to_string()
    }

    fn part2(&self, input: &str) -> String {
        let puzzle_data = parse_data(input);
        let mut sum_calories: Vec<u32> = sum_elf_calories(puzzle_data);

        sum_calories.sort();
        sum_calories[sum_calories.len() - 3..]
            .iter()
            .sum::<u32>()
            .to_string()
    }
}
fn parse_data(data: &str) -> Vec<Vec<u32>> {
    data.split("\n\n")
        .filter(|x| x != &"")
        .map(|elf| {
            elf.split("\n")
                .filter(|x| x != &"")
                .map(|cal| cal.parse::<u32>().unwrap())
                .collect()
        })
        .collect()
}

fn sum_elf_calories(elfs: Vec<Vec<u32>>) -> Vec<u32> {
    elfs.iter().map(|e| e.iter().sum()).collect()
}
