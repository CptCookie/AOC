use crate::Solution;
use solution_macro::mark_solution;

#[mark_solution(2021, 2)]
struct Day2;

impl Solution for Day2 {
    fn part1(&self, input: &str) -> String {
        let cmds = parse_input(input);
        let forward: i64 = cmds
            .iter()
            .filter(|cmd| cmd.dir == Direction::Forward)
            .map(|cmd| cmd.dist)
            .sum();

        let vertical: i64 = cmds
            .iter()
            .map(|cmd| match cmd.dir {
                Direction::Up => -cmd.dist,
                Direction::Down => cmd.dist,
                _ => 0,
            })
            .sum();
        (forward * vertical).to_string()
    }

    fn part2(&self, input: &str) -> String {
        let cmds = parse_input(input);
        let mut horizontal: i64 = 0;
        let mut vertical = 0;
        let mut aim: i64 = 0;

        for cmd in cmds.iter() {
            match cmd.dir {
                Direction::Forward => {
                    horizontal += cmd.dist;
                    vertical += aim * cmd.dist;
                }
                Direction::Down => aim += cmd.dist,
                Direction::Up => aim -= cmd.dist,
            }
        }
        (horizontal * vertical).to_string()
    }
}
#[derive(PartialEq)]
enum Direction {
    Forward,
    Up,
    Down,
}
struct Command {
    dir: Direction,
    dist: i64,
}

impl Command {
    fn from_line(line: &str) -> Command {
        let split: Vec<&str> = line.split_whitespace().collect();
        Command {
            dir: Direction::from_string(split[0]).unwrap(),
            dist: split[1].parse().unwrap(),
        }
    }
}

impl Direction {
    // inspired by u/nowardic
    fn from_string(string: &str) -> Result<Direction, &str> {
        match string {
            "forward" => Ok(Direction::Forward),
            "up" => Ok(Direction::Up),
            "down" => Ok(Direction::Down),
            _ => Err("Unkown Direction"),
        }
    }
}

fn parse_input(data: &str) -> Vec<Command> {
    data.split("\n")
        .filter(|x| x != &"")
        .map(|e| Command::from_line(e))
        .collect()
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_solution_1() {
        let test_data = String::from("forward 5\ndown 5\nforward 8\nup 3\ndown 8\nforward 2");
        assert_eq!(Day2 {}.part1(&test_data), 150.to_string())
    }

    #[test]
    fn test_solution_2() {
        let test_data = String::from("forward 5\ndown 5\nforward 8\nup 3\ndown 8\nforward 2");
        assert_eq!(Day2 {}.part2(&test_data), 900.to_string())
    }
}
