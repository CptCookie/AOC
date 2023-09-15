pub fn part_1(input: &String) -> String {
    let data = parse_data(input);
    does_increment(&data, 1).to_string()
}

pub fn part_2(input: &String) -> String {
    let data = parse_data(input);
    does_increment(&data, 3).to_string()
}

fn does_increment(deep_scan: &Vec<u16>, window: usize) -> usize {
    deep_scan
        .iter()
        .zip(deep_scan.iter().skip(window))
        .filter(|(first, second)| first < second)
        .count()
}

fn parse_data(data: &String) -> Vec<u16> {
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
