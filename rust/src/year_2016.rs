use crate::utils;

mod day_1;
mod day_2;

pub fn get_day(day: &u8) -> Option<utils::DaySol> {
    match day {
        1 => Some((day_1::part_1, day_1::part_2)),
        2 => Some((day_2::part_1, day_2::part_2)),
        _ => None,
    }
}
