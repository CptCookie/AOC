pub mod utils;
pub mod year_2015;
pub mod year_2016;
pub mod year_2018;
pub mod year_2019;
pub mod year_2021;
pub mod year_2022;
pub mod year_2023;

pub mod solutions {
    use crate::{
        utils, year_2015, year_2016, year_2018, year_2019, year_2021, year_2022, year_2023,
    };

    pub fn get_day(year: &u32, day: &u8) -> Option<utils::DaySol> {
        match year {
            2015 => year_2015::get_day(day),
            2016 => year_2016::get_day(day),
            2018 => year_2018::get_day(day),
            2019 => year_2019::get_day(day),
            2021 => year_2021::get_day(day),
            2022 => year_2022::get_day(day),
            2023 => year_2023::get_day(day),
            _ => None,
        }
    }
}
