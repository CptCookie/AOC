pub mod utils;

use std::fs;
use std::io;
use std::path::Path;

use clap::{arg, command, value_parser, ArgMatches};

use rust::solutions;

const CACHE: &str = "./cache/";

fn main() {
    let args = get_args();

    let year = args.get_one::<u16>("year").unwrap();
    let day = args.get_one::<u8>("day").unwrap();
    let token = args.get_one::<String>("token").unwrap();
    run_aoc(year, day, token);
}

fn run_aoc(year: &u16, day: &u8, token: &String) {
    // let test = build_years();
    let input = get_input(year, day, token);
    if let Some(s) = solutions::get_day(year, day) {
        let part_1 = s.0(&input);
        let part_2 = s.1(&input);
        println!("Solution to AOC {year}-{day}\tpart 1: {part_1}\tpart_2: {part_2}")
    } else {
        println!("No Solution to AOC")
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
    println!("try loading data from cache");
    fs::read_to_string(format!("./cache/{year}-{day}"))
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
    println!("request data from AOC");
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
            arg!([day] "optional day [1..25]").value_parser(value_parser!(u8).range(1..25)), // .required(false)
        )
        .arg(arg!([token] "session Token to fetch inputs from AOC").env("AOC_TOKEN"))
        .get_matches();
}
