pub mod year_2015;
pub mod year_2016;
pub mod year_2018;
pub mod year_2019;
pub mod year_2021;
pub mod year_2022;
pub mod year_2023;
mod year_2024;
pub mod year_2025;

use inventory;
use solution_macro::mark_solution;

pub trait Solution: Send + Sync {
    fn part1(&self, input: &str) -> String;
    fn part2(&self, input: &str) -> String;
}

#[derive(Debug)]
pub struct SolutionEntry {
    pub year: u16,
    pub day: u8,
    pub factory: fn() -> Box<dyn Solution>,
}

impl SolutionEntry {
    pub fn solver(&self) -> Box<dyn Solution> {
        (self.factory)()
    }
}

inventory::collect!(SolutionEntry);
