pub mod utils;

use std::fs;
use std::io;
use std::path::Path;

use clap::{arg, command, value_parser, ArgMatches};

use rust::solutions;

const CACHE: &str = "./cache/";
const TOKEN_FILE: &str = "./token";


fn main() {
    let args = get_args();

    let year = args.get_one::<u16>("year").unwrap();
    let day = args.get_one::<u8>("day");
    let token = args.get_one::<String>("token");
    match token {
        Some(t) => run_aoc(year, day, t),
        None => run_aoc(year, day, &load_token_file().unwrap())
    }
}

fn run_aoc(year: &u16, day: Option<&u8>, token: &String) {
    match day {
        Some(d) => try_run_day(year, d, token),
        None => run_year(year, token)
    }
}

fn run_year(year: &u16, token: &String) {
    for day in 1..=25 {
        try_run_day(year, &day, token);
    }
}

fn try_run_day(year: &u16, day: &u8, token: &String) {
    if let Some(s) = solutions::get_day(year, day) {
        let input = get_input(year, day, token);
        println!("Solving Advent of Code {year} Day {day}");
        let part_1 = s.0(&input);
        println!("Solution part 1: {part_1}");
        let part_2 = s.1(&input);
        println!("Solution part 2: {part_2}\n");
    } 
}   

fn get_input(year: &u16, day: &u8, token: &String) -> String {
    match load_input_file(year, day) {
        Ok(x) => x,
        Err(_) => {
            let data = request_input_data(year, day, token).unwrap();
            write_input_file(year, day, &data);
            data
        }
    }
}

fn load_input_file(year: &u16, day: &u8) -> io::Result<String> {
    fs::read_to_string(format!("./cache/{year}-{day}"))
}

fn load_token_file() -> Option<String> {
    if Path::new(TOKEN_FILE).exists(){
        return fs::read_to_string(TOKEN_FILE).ok()
    }
    None
}

fn write_input_file(year: &u16, day: &u8, data: &String) {
    if !Path::new(CACHE).exists() {
        let _ = fs::create_dir("./cache");
    }

    fs::write(format!("./cache/{year}-{day}"), data).unwrap();
}

fn request_input_data(
    year: &u16,
    day: &u8,
    token: &str,
) -> Result<String, Box<dyn std::error::Error>> {
    let url = format!("https://adventofcode.com/{year}/day/{day}/input");
    let client = reqwest::blocking::Client::new();
    let resp = client
        .get(url)
        .header(reqwest::header::COOKIE, format!("session={}", token))
        .send()?;
    Ok(resp.text()?)
}

fn get_args() -> ArgMatches {
    return command!()
        .arg(arg!([year] "year [2016..2023]").value_parser(value_parser!(u16).range(2015..2023)))
        .arg(
            arg!([day] "optional day [1..25]").required(false).value_parser(value_parser!(u8).range(1..25)),
        )
        .arg(arg!([token] "session Token to fetch inputs from AOC").env("AOC_TOKEN"))
        .get_matches();
}
