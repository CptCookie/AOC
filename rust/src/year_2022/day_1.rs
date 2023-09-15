fn parse_data(data: &String) -> Vec<Vec<u32>> {
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

fn sum_elf_calories(elfs: Vec<Vec<u32>>) -> Vec<u32> {
    elfs.iter().map(|e| e.iter().sum()).collect()
}

pub fn part_1(input: &String) -> String {
    let puzzle_data = parse_data(input);
    let mut sum_calories: Vec<u32> = sum_elf_calories(puzzle_data);

    sum_calories.sort();
    sum_calories[sum_calories.len() - 1].to_string()
}

pub fn part_2(input: &String) -> String {
    let puzzle_data = parse_data(input);
    let mut sum_calories: Vec<u32> = sum_elf_calories(puzzle_data);
    
    sum_calories.sort();
    sum_calories[sum_calories.len() - 3..].iter().sum::<u32>().to_string()
}

