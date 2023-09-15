pub mod utils;
pub mod year_2015;
pub mod year_2016;
pub mod year_2018;

pub mod solutions {
    use crate::{utils, year_2015, year_2016, year_2018};

    pub fn get_day(year: &u16, day: &u8) -> Option<utils::DaySol> {
        match year {
            2015 => year_2015::get_day(day),
            2016 => year_2016::get_day(day),
            2018 => year_2018::get_day(day),
            _ => None,
        }
    }
}
