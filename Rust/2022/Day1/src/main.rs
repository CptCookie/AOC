    use std::fs;

    fn parse_data(data: String) -> Vec<Vec<u32>> {
        data.split("\n\n")
            .filter(|x| x != &"")
            .map(|elf| {
                elf.split("\n")
                    .filter(|x| x != &"")
                    .map(|cal| cal.parse::<u32>().unwrap())
                    .collect()
            })
            .collect()
    }

    fn main() {
        let puzzle_input = fs::read_to_string("input.txt").unwrap();
        let puzzle_data = parse_data(puzzle_input);
        let mut sum_calories: Vec<u32> = puzzle_data.iter().map(|e| e.iter().sum()).collect();
        sum_calories.sort();

        println!("solution 1: {}", sum_calories[sum_calories.len() - 1]);
        println!(
            "solution 2: {}",
            sum_calories[sum_calories.len() - 3..].iter().sum::<u32>()
        );
    }
