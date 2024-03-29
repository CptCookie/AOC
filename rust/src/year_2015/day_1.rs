fn floor_sum(steps: &String) -> i32 {
    let mut counter: i32 = 0;
    for step in steps.chars() {
        match step {
            '(' => counter += 1,
            ')' => counter -= 1,
            _ => (),
        }
    }
    counter
}

fn find_floor(steps: &String, target_floor: i32) -> Option<usize> {
    let mut current_floor = 0;
    for (n, step) in steps.chars().enumerate() {
        match step {
            '(' => current_floor += 1,
            ')' => current_floor -= 1,
            _ => (),
        }

        if current_floor == target_floor {
            return Some(n + 1);
        }
    }
    None
}

pub fn part_1(input: &String) -> String {
    floor_sum(input).to_string()
}

pub fn part_2(input: &String) -> String {
    find_floor(input, -1).unwrap().to_string()
}

#[cfg(test)]
mod test {
    use super::find_floor;
    use super::floor_sum;

    #[test]
    fn test_floor_sum() {
        let test_data = String::from("(())");
        assert_eq!(floor_sum(&test_data), 0);

        let test_data = String::from("(()(()(");
        assert_eq!(floor_sum(&test_data), 3);

        let test_data = String::from("))(((((");
        assert_eq!(floor_sum(&test_data), 3);

        let test_data = String::from(")())())");
        assert_eq!(floor_sum(&test_data), -3);
    }

    #[test]
    fn test_find_floor() {
        let test_data = String::from("(())");
        assert_eq!(find_floor(&test_data, -1), None);

        let test_data = String::from(")");
        assert_eq!(find_floor(&test_data, -1), Some(1));

        let test_data = String::from("()())");
        assert_eq!(find_floor(&test_data, -1), Some(5));
    }
}
