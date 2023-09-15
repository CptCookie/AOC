use std::fs;

#[derive(PartialEq)]
enum Direction {
    Forward,
    Up,
    Down,
}
struct Command {
    dir: Direction,
    dist: i32,
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

fn solution_1(cmds: &Vec<Command>) -> i32 {
    let forward: i32 = cmds
        .iter()
        .filter(|cmd| cmd.dir == Direction::Forward)
        .map(|cmd| cmd.dist)
        .sum();

    let vertical: i32 = cmds
        .iter()
        .map(|cmd| match cmd.dir {
            Direction::Up => -cmd.dist,
            Direction::Down => cmd.dist,
            _ => 0,
        })
        .sum();
    forward * vertical
}

fn solution_2(cmds: &Vec<Command>) -> i32 {
    let mut horizontal: i32 = 0;
    let mut vertical = 0;
    let mut aim: i32 = 0;

    for cmd in cmds.iter() {
        match cmd.dir {
            Direction::Forward => {
                horizontal += cmd.dist;
                vertical += aim * cmd.dist;
            }
            Direction::Down => aim += cmd.dist,
            Direction::Up => aim -= cmd.dist,
            _ => (),
        }
    }
    horizontal * vertical
}

fn main() {
    let puzzle_input = fs::read_to_string("input.txt").unwrap();
    let puzzle_data = parse_data(&puzzle_input);

    println!("solution 1: {}", solution_1(&puzzle_data));
    println!("solution 2: {}", solution_2(&puzzle_data));
}

fn parse_data(data: &String) -> Vec<Command> {
    data.split("\n")
        .filter(|x| x != &"")
        .map(|e| Command::from_line(e))
        .collect()
}

#[cfg(test)]
mod test {
    use crate::*;

    #[test]
    fn test_solution_1(){
        let test_data = String::from("forward 5\ndown 5\nforward 8\nup 3\ndown 8\nforward 2");
        assert_eq!(solution_1(&parse_data(&test_data)), 150)
    }


    #[test]
    fn test_solution_2(){
        let test_data = String::from("forward 5\ndown 5\nforward 8\nup 3\ndown 8\nforward 2");
        assert_eq!(solution_2(&parse_data(&test_data)), 900)
    }

}
