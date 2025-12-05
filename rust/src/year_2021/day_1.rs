use crate::Solution;
use solution_macro::mark_solution;

#[mark_solution(2021, 1)]
struct Day1;

impl Solution for Day1 {
    fn part1(&self, input: &str) -> String {
        let data = parse_data(input);
        does_increment(&data, 1).to_string()
    }

    fn part2(&self, input: &str) -> String {
        let data = parse_data(input);
        does_increment(&data, 3).to_string()
    }
}

fn does_increment(deep_scan: &Vec<u16>, window: usize) -> usize {
    deep_scan
        .iter()
        .zip(deep_scan.iter().skip(window))
        .filter(|(first, second)| first < second)
        .count()
}

fn parse_data(data: &str) -> Vec<u16> {
    data.split("\n")
        .filter(|x| x != &"")
        .map(|e| e.parse::<u16>().unwrap())
        .collect()
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_single_compare() {
        let test_data: Vec<u16> = vec![199, 200, 208, 210, 200, 207, 240, 269, 260, 263];
        assert_eq!(does_increment(&test_data, 1), 7)
    }

    #[test]
    fn test_sum_3_compare() {
        let test_data: Vec<u16> = vec![199, 200, 208, 210, 200, 207, 240, 269, 260, 263];
        assert_eq!(does_increment(&test_data, 3), 5)
    }
}
