mod day_1;

pub type Solution = fn(&String) -> String;

pub fn get_day(day: &u8) -> Option<(Solution, Solution)> {
    match day {
        // 1 => Some((day_1::part_1, day_1::part_2)),
        _ => None,
    }
}
