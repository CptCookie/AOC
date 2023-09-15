use std::fs;

fn common_bit_at(binarys: &Vec<&str>, index: usize, most_common: bool) -> char {
    let one_count = binarys
        .iter()
        .filter(|bin| bin.chars().nth(index).unwrap() == '1')
        .count();
    match (one_count * 2 >= binarys.len(), most_common) {
        (cnt, mc) if cnt ^ mc => '0',
        _ => '1',
    }
}

fn filter_by_common_bit(binarys: &Vec<&str>, most_common: bool) -> Option<i32> {
    let mut filtered_binarys = binarys.to_vec();

    for index in 0..binarys[0].len() {
        let common_bit = common_bit_at(&filtered_binarys, index, most_common);

        filtered_binarys = filtered_binarys
            .iter()
            .filter(|e| e.chars().nth(index).unwrap() == common_bit)
            .map(|e| *e)
            .collect();

        if filtered_binarys.len() == 1 {
            return Some(i32::from_str_radix(filtered_binarys[0], 2).unwrap());
        }
    }
    return None;
}

fn solution_1(binarys: &Vec<&str>) -> i32 {
    let mut bin_solution: Vec<char> = vec![];
    for index in 0..binarys[0].len() {
        bin_solution.push(common_bit_at(binarys, index, true))
    }

    let gamma = i32::from_str_radix(&bin_solution.iter().collect::<String>(), 2).unwrap();
    let epsilon = i32::from_str_radix(
        &bin_solution
            .iter()
            .map(|e| match *e {
                '1' => '0',
                _ => '1',
            })
            .collect::<String>(),
        2,
    )
    .unwrap();

    return gamma * epsilon;
}

fn solution_2(binarys: &Vec<&str>) -> i32 {
    let gamma = filter_by_common_bit(&binarys, true).unwrap();
    let epsilon = filter_by_common_bit(&binarys, false).unwrap();
    return gamma * epsilon;
}

fn main() {
    let puzzle_input = fs::read_to_string("input.txt").unwrap();
    let puzzle_data: Vec<&str> = puzzle_input.split("\r\n").filter(|x| x != &"").collect();

    println!("solution 1: {}", solution_1(&puzzle_data));
    println!("solution 2: {}", solution_2(&puzzle_data));
}

#[cfg(test)]
mod test {

    use crate::*;

    #[test]
    fn test_solution_1() {
        let test_data: Vec<&str> = vec![
            "00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000",
            "11001", "00010", "01010",
        ];
        assert_eq!(solution_1(&test_data), 198)
    }

    #[test]
    fn test_solution_2() {
        let test_data: Vec<&str> = vec![
            "00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000",
            "11001", "00010", "01010",
        ];
        assert_eq!(filter_by_common_bit(&test_data, true), Some(23));
        assert_eq!(filter_by_common_bit(&test_data, false), Some(10));
        assert_eq!(solution_2(&test_data), 230)
    }
}
