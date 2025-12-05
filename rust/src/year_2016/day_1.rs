use crate::Solution;
use regex::Regex;
use solution_macro::mark_solution;
use std::collections::HashSet;

#[mark_solution(2016, 1)]
struct Day1;

impl Solution for Day1 {
    fn part1(&self, input: &str) -> String {
        let directions = parse(input);
        let moves: Vec<(i16, i16)> = vec![(0, 1), (1, 0), (0, -1), (-1, 0)];
        let mut dir = 0;
        let mut c_pos = (0, 0);

        for (d, l) in directions.iter() {
            match d {
                &"R" => dir = (dir + 1) % 4,
                &"L" => dir = (4 + dir - 1) % 4,
                _ => (),
            }

            let (dx, dy) = moves[dir];
            c_pos = (c_pos.0 + *l * dx, c_pos.1 + *l * dy);
        }

        format!("{}", c_pos.0.abs() + c_pos.1.abs())
    }
    fn part2(&self, input: &str) -> String {
        let directions = parse(input);
        let moves: Vec<(i16, i16)> = vec![(0, 1), (1, 0), (0, -1), (-1, 0)];

        let mut visited = HashSet::with_capacity(directions.len() / 2);
        let mut c_pos = (0, 0);
        let mut dir = 0;

        for (d, l) in directions.iter() {
            match d {
                &"R" => dir = (dir + 1) % 4,
                &"L" => dir = (4 + dir - 1) % 4,
                _ => (),
            }

            let (dx, dy) = moves[dir];

            for _ in 0..*l {
                c_pos = (c_pos.0 + 1 * dx, c_pos.1 + 1 * dy);

                if visited.contains(&c_pos) {
                    return format!("{}", c_pos.0.abs() + c_pos.1.abs());
                }
                visited.insert(c_pos);
            }
        }

        panic!("NOTHING!")
    }
}

fn parse(input: &str) -> Vec<(&str, i16)> {
    let pattern = Regex::new(r#"([RL])(\d+)"#).unwrap();
    pattern
        .captures_iter(input)
        .map(|c| c.extract())
        .map(|(_, [dir, dist])| (dir, dist.parse().unwrap()))
        .collect()
}
