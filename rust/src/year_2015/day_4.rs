use crypto::digest::Digest;
use crypto::md5::Md5;

pub fn part_1(input: &String) -> String {
    find_hash(&input, 5).unwrap().to_string()
}

pub fn part_2(input: &String) -> String {
    find_hash(&input, 6).unwrap().to_string()
}

fn find_hash(message: &String, num_leed_zero: u8) -> Option<u64> {
    for n in 0..std::u64::MAX {
        let mut new_message: String = message.clone();
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
    fn tesf_find_hash() {
        assert_eq!(find_hash(&String::from("abcdef"), 5), Some(609043));
        assert_eq!(find_hash(&String::from("pqrstuv"), 5), Some(1048970));
    }
}
