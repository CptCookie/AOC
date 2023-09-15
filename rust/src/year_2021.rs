mod day_1;
mod day_2;
mod day_3;

pub type Solution = fn(&String) -> String;

pub fn get_day(day: &u8) -> Option<(Solution, Solution)> {
    match day {
        1 => Some((day_1::part_1, day_1::part_2)),
        2 => Some((day_2::part_1, day_2::part_2)),
        3 => Some((day_3::part_1, day_3::part_2)),
        _ => None,
    }
}
