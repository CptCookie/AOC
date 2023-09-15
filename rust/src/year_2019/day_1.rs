fn parse_input(input: &String) -> Vec<u32> {
    input
        .split_ascii_whitespace()
        .map(|word| word.parse::<u32>().unwrap())
        .collect()
}

fn fuel_per_mass(mass: &u32) -> u32 {
    return (mass / 3) - 2;
}

fn fuel_fuel_per_mass(mass: &u32) -> u32 {
    let mut mass_fuel = fuel_per_mass(mass);
    let mut sum_fuel = mass_fuel;

    while mass_fuel > 8 {
        mass_fuel = fuel_per_mass(&mass_fuel);
        sum_fuel += mass_fuel;
    }

    sum_fuel
}

fn complete_fuel(masses: &Vec<u32>, fuel_fuel: bool) -> u32 {
    masses
        .iter()
        .map(|m| match fuel_fuel {
            true => fuel_fuel_per_mass(&m),
            false => fuel_per_mass(&m),
        })
        .sum()
}

pub fn part_1(input: &String) -> String {
    complete_fuel(&parse_input(input), false).to_string()
}

pub fn part_2(input: &String) -> String {
    complete_fuel(&parse_input(input), true).to_string()
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_part_2() {
        assert_eq!(part_2(&"1969".to_string()), 966.to_string());
        assert_eq!(part_2(&"100756".to_string()), 50346.to_string());
        assert_eq!(
            part_2(&"1969\n100756".to_string()),
            (966 + 50346).to_string()
        );
    }
}
