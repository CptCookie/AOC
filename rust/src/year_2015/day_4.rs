use crate::Solution;
use crypto::digest::Digest;
use crypto::md5::Md5;
use solution_macro::mark_solution;

#[mark_solution(2015, 4)]
struct Day4;

impl Solution for Day4 {
    fn part1(&self, input: &str) -> String {
        find_hash(&input, 5).unwrap().to_string()
    }

    fn part2(&self, input: &str) -> String {
        find_hash(&input, 6).unwrap().to_string()
    }
}

fn find_hash(message: &str, num_leed_zero: u8) -> Option<u64> {
    for n in 0..std::u64::MAX {
        let mut new_message: String = String::from(message);
        new_message.extend(n.to_string().chars());
        let mut hash = Md5::new();
        hash.input_str(&new_message);

        if leeding_zeros(hash.result_str()) == num_leed_zero {
            return Some(n);
        }
    }
    None
}

fn leeding_zeros(string: String) -> u8 {
    let mut counter: u8 = 0;
    for c in string.chars() {
        match c {
            '0' => counter += 1,
            _ => return counter,
        }
    }
    counter
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_find_hash() {
        assert_eq!(find_hash(&String::from("abcdef"), 5), Some(609043));
        assert_eq!(find_hash(&String::from("pqrstuv"), 5), Some(1048970));
    }
}
