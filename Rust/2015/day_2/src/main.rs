use std::fs;

fn main() {
    let puzzle_input = fs::read_to_string("2015-2.txt").unwrap();
    let puzzle_data = parse_data(puzzle_input);
    println!("Solution 1: {}", solution_1(&puzzle_data));
    println!("Solution 2: {}", solution_2(&puzzle_data));
}

fn solution_1(puzzle_data: &Vec<Vec<u16>>) -> u32 {
    puzzle_data
        .iter()
        .map(|package| calc_wrapping_paper(package) as u32)
        .sum()
}

fn solution_2(puzzle_data: &Vec<Vec<u16>>) -> u32 {
    puzzle_data
        .iter()
        .map(|package| calc_ribbon(package) as u32)
        .sum()
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

fn parse_data(data: String) -> Vec<Vec<u16>> {
    let lines: Vec<&str> = data.split("\n").filter(|x| x != &"").collect();
    let elements: Vec<Vec<u16>> = lines
        .iter()
        .map(|line| line.split("x").map(|e| e.parse::<u16>().unwrap()).collect())
        .collect();
    elements
}

#[cfg(test)]
mod test {
    use crate::calc_ribbon;
    use crate::calc_wrapping_paper;
    use crate::parse_data;
    use crate::solution_1;
    use crate::solution_2;

    #[test]
    fn test_parse_data() {
        let data = parse_data(String::from("1x2x24\n3x5x6\n"));
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
        let data = vec![vec![2, 3, 4], vec![1, 1, 10]];
        assert_eq!(solution_1(data), 101)
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
        let data = vec![vec![2, 3, 4], vec![1, 1, 10]];
        assert_eq!(solution_2(data), 48)
    }
}
