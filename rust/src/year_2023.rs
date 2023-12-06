mod day_4;

pub type Solution = fn(&String) -> String;

pub fn get_day(day: &u8) -> Option<(Solution, Solution)> {
    match day {
        4 => Some((day_4::part_1, day_4::part_2)),
        _ => None,
    }
}
