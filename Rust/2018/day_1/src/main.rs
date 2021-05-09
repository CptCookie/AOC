use std::collections::HashMap;
use std::fs;

fn main() {
    let puzzle_input = fs::read_to_string("2018-1.txt").unwrap();
    let feq_changes = parse_input(puzzle_input);
    println!("The sum of all frequency is: {:#?}", sum_freq(&feq_changes));
    println!(
        "The fist double frequency is: {}",
        fist_double(feq_changes).unwrap()
    )
}

fn fist_double(freq_change: Vec<i32>) -> Option<i32> {
    let mut counter = 0;
    let mut distinct_freq: HashMap<i32, bool> = HashMap::new();
    let mut current_freq: i32 = 0;

    while counter < 1000 {
        for n in freq_change.iter() {
            let new_freq: i32 = current_freq + n;
            if distinct_freq.contains_key(&new_freq) {
                return Some(new_freq);
            } else {
                distinct_freq.insert(new_freq, true);
                current_freq = new_freq;
            }
        }
        counter += 1;
    }
    return None;
}

fn sum_freq(freq_change: &Vec<i32>) -> i32 {
    freq_change.iter().sum()
}

fn parse_input(puzzle_input: String) -> Vec<i32> {
    let mut split: Vec<i32> = puzzle_input
        .split("\n")
        .map(|n| n.parse::<i32>().unwrap_or(0))
        .collect();
    split.pop();
    split
}

#[cfg(test)]
mod test {
    use super::fist_double;
    use super::sum_freq;

    #[test]
    fn test_double_freq() {
        assert_eq!(fist_double(vec![3, 3, 4, -2, -4]).unwrap(), 10);
        assert_eq!(fist_double(vec![-6, 3, 8, 5, -6]).unwrap(), 5);
        assert_eq!(fist_double(vec![7, 7, -2, -7, -4]).unwrap(), 14);
    }

    #[test]
    fn test_sum_freq() {
        assert_eq!(sum_freq(&vec![1, 1, 1]), 3);
        assert_eq!(sum_freq(&vec![1, 1, -2]), 0);
        assert_eq!(sum_freq(&vec![-1, -2, -3]), -6);
    }
}
