fn calc_fuel(mass: u32) -> u32 {
    return (mass / 3) - 2;
}

pub fn part_1(input: &String) -> String {
    input.split_ascii_whitespace().map(|word| calc_fuel(word.parse::<u32>().unwrap())).sum::<u32>().to_string()
}

pub fn part_2(input: &String) -> String {
    let mass: u32 = input.split_ascii_whitespace().map(|word| word.parse::<u32>().unwrap()).sum();
    let mut add_fuel = calc_fuel(mass);
    let mut sum = add_fuel;
    
    /* Doing simple things in a loop is always better than recursion!
        * 8 is the highest value that divided by 3 and floored is equal to 2
        */
    while add_fuel > 8 {
        add_fuel = calc_fuel(add_fuel);
        sum += add_fuel;
    }
    sum.to_string()
}


