use std::fs::File;
use std::io;
use std::io::Read;

fn read_input() -> Result<Vec<i32>, io::Error> {
    let mut s: String = String::new();
    File::open("./input.txt")?.read_to_string(&mut s)?;
    let s = s.replace("\n", "");

    let v: Vec<&str> = s.split(",").collect();
    let input = v.iter().map(|x|x.parse().unwrap()).collect();
    Ok(input)
}


fn main(){
    println!("{:#?}", read_input().unwrap())
}