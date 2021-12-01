use itertools::Itertools;
use std::fs;

fn main() {
    let puzzle_input = fs::read_to_string("input.txt").unwrap();
    let puzzle_data = parse_data(puzzle_input);
    println!("{}", num_single_elements_increase(&puzzle_data));
    println!("{}", num_sum_3_elements_increase(&puzzle_data));
}

fn num_single_elements_increase(deep_scan: &Vec<u16>) -> usize {
    deep_scan
        .iter()
        .tuple_windows()
        .filter(|(first, second)| first < second)
        .count()
}

fn num_sum_3_elements_increase(deep_scan: &Vec<u16>) -> usize {
    deep_scan
        .iter()
        .tuple_windows()
        .map(|(first, second, third)| first + second + third)
        .tuple_windows()
        .filter(|(first, second)| first < second)
        .count()
}

fn parse_data(data: String) -> Vec<u16> {
    data.split("\n")
        .filter(|x| x != &"")
        .map(|e| e.parse::<u16>().unwrap())
        .collect()
}

#[cfg(test)]
mod test {
    use crate::*;

    #[test]
    fn test_single_compare() {
        let test_data: Vec<u16> = vec![199, 200, 208, 210, 200, 207, 240, 269, 260, 263];
        assert_eq!(num_single_elements_increase(&test_data), 7)
    }

    #[test]
    fn test_sum_3_compare() {
        let test_data: Vec<u16> = vec![199, 200, 208, 210, 200, 207, 240, 269, 260, 263];
        assert_eq!(num_sum_3_elements_increase(&test_data), 5)
    }
}
