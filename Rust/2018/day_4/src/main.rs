use std::collections::HashMap;

const TOKEN:&str = "53616c7465645f5f381ca9f990b331963bc4c559f548054e919235f4337b05da8d79afdd8cd16584b77c0ee4771218fc";


fn main() {
    println!("{:#?}", read_input("https://adventofcode.com/2018/day/4/input").unwrap());
}

fn read_input(url:&str)-> Result<Vec<String>, Box<dyn std::error::Error>> {
    let client = reqwest::blocking::Client::new();
    let resp = client.get(url)
                     .header(reqwest::header::COOKIE, format!("session={}", TOKEN))
                     .send()?;
    
    let mut split:Vec<String> = resp.text()?
                             .split("\n")
                             .map(|n| String::from(n))
                             .collect();
    split.pop();
    split.sort();
    return Ok(split);
}