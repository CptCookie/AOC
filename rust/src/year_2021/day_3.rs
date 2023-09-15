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

pub fn part_1(input: &String) -> String {
    let binarys = parse_input(input);
    let mut bin_solution: Vec<char> = vec![];
    for index in 0..binarys[0].len() {
        bin_solution.push(common_bit_at(&binarys, index, true))
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

    return (gamma * epsilon).to_string();
}

pub fn part_2(input: &String) -> String {
    let binarys = parse_input(input);
    let gamma = filter_by_common_bit(&binarys, true).unwrap();
    let epsilon = filter_by_common_bit(&binarys, false).unwrap();
    (gamma * epsilon).to_string()
}

fn parse_input(input: &String) -> Vec<&str> {
    input
        .split_ascii_whitespace()
        .filter(|x| x != &"")
        .collect()
}

#[cfg(test)]
mod test {

    use super::*;

    #[test]
    fn test_solution_1() {
        let test_data = String::from(
            "00100\n11110\n10110\n10111\n10101\n01111\n00111\n11100\n10000\n11001\n00010\n01010\n",
        );
        assert_eq!(part_1(&test_data), 198.to_string())
    }

    #[test]
    fn test_solution_2() {
        let test_data = String::from(
            "00100\n11110\n10110\n10111\n10101\n01111\n00111\n11100\n10000\n11001\n00010\n01010\n",
        );
        assert_eq!(part_2(&test_data), 230.to_string())
    }
}
