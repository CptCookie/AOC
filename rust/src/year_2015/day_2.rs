use crate::Solution;
use solution_macro::mark_solution;

#[mark_solution(2015, 2)]
struct Day2;

impl Solution for Day2 {
    fn part1(&self, input: &str) -> String {
        parse_data(input)
            .iter()
            .map(|package| calc_wrapping_paper(package) as u32)
            .sum::<u32>()
            .to_string()
    }

    fn part2(&self, input: &str) -> String {
        parse_data(input)
            .iter()
            .map(|package| calc_ribbon(package) as u32)
            .sum::<u32>()
            .to_string()
    }
}

fn calc_wrapping_paper(size: &Vec<u16>) -> u16 {
    let areas = vec![size[0] * size[1], size[0] * size[2], size[1] * size[2]];
    2 * areas.iter().sum::<u16>() + areas.iter().min().unwrap()
}

fn calc_ribbon(size: &Vec<u16>) -> u16 {
    let mut sorted_sizes = size.clone();
    sorted_sizes.sort();
    let ribbon = 2 * sorted_sizes[0] + 2 * sorted_sizes[1];
    let bow: u16 = size.iter().product();
    bow + ribbon
}

fn parse_data(data: &str) -> Vec<Vec<u16>> {
    let lines: Vec<&str> = data.split("\n").filter(|x| x != &"").collect();
    let elements: Vec<Vec<u16>> = lines
        .iter()
        .map(|line| line.split("x").map(|e| e.parse::<u16>().unwrap()).collect())
        .collect();
    elements
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_parse_data() {
        let data = parse_data(&String::from("1x2x24\n3x5x6\n"));
        assert_eq!(data, vec![vec![1, 2, 24], vec![3, 5, 6]])
    }

    #[test]
    fn test_wrapping_paper() {
        let data = vec![2, 3, 4];
        assert_eq!(calc_wrapping_paper(&data), 58);

        let data = vec![1, 1, 10];
        assert_eq!(calc_wrapping_paper(&data), 43);
    }

    #[test]
    fn test_warp_package() {
        let data = String::from("2x3x4\n1x1x10\n");
        assert_eq!(Day2 {}.part1(&data), String::from("101"))
    }

    #[test]
    fn test_ribbon() {
        let data = vec![4, 3, 2];
        assert_eq!(calc_ribbon(&data), 34);

        let data = vec![10, 1, 1];
        assert_eq!(calc_ribbon(&data), 14);
    }

    #[test]
    fn test_ribbon_package() {
        let data = String::from("2x3x4\n1x1x10\n");
        assert_eq!(Day2 {}.part2(&data), String::from("48"))
    }
}
