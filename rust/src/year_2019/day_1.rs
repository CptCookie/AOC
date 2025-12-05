use crate::Solution;
use solution_macro::mark_solution;

#[mark_solution(2019, 1)]
struct Day1;

impl Solution for Day1 {
    fn part1(&self, input: &str) -> String {
        complete_fuel(&parse_input(input), false).to_string()
    }

    fn part2(&self, input: &str) -> String {
        complete_fuel(&parse_input(input), true).to_string()
    }
}

fn parse_input(input: &str) -> Vec<u32> {
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

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_part_2() {
        assert_eq!(Day1 {}.part2(&"1969".to_string()), 966.to_string());
        assert_eq!(Day1 {}.part2(&"100756".to_string()), 50346.to_string());
        assert_eq!(
            Day1 {}.part2(&"1969\n100756".to_string()),
            (966 + 50346).to_string()
        );
    }
}
