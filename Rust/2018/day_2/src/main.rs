use std::collections::HashMap;

const TOKEN:&str = "53616c7465645f5f381ca9f990b331963bc4c559f548054e919235f4337b05da8d79afdd8cd16584b77c0ee4771218fc";


fn main() {
    let input = read_input("https://adventofcode.com/2018/day/2/input").unwrap();
    println!("Solution 1: {:?}", solution_1(&input));
    println!("Solution 2: {}", solution_2(&input));
    

}

fn solution_2(input: &Vec<String>) -> String {

    for (n,line1) in input.iter().enumerate() {
        for line2 in input[n..].iter() {
            let comp = compare_lines(line1, line2);
            match comp {
                Some(n) => return n,
                None => ()
            }
        }
    }

    String::from("")
}

fn compare_lines(line1: &String, line2: &String) -> Option<String> {
    let line2: Vec<char> = line2.chars().collect();
    let mut unique: Option<usize> = None;

    for (n , line1_char) in line1.chars().enumerate(){
        if line2[n] != line1_char {
            match unique {
                None => unique = Some(n),
                Some (n) => return None
            }
        }
    }

    if unique != None {
        let mut newString = line2.clone();
        newString.remove(unique.unwrap());
        return Some(newString.into_iter().collect())
    } else {
        return None
    }
}

fn solution_1(input: &Vec<String>) -> i32{
    let mut maps: Vec<HashMap<char, i32>> = Vec::new();
    let mut twos: i32 = 0;
    let mut threes: i32 = 0;

    for line in input {
        maps.push(get_hashMap(line))
    }
    
    for map in &maps {
        if containes_n_chars(2, map) {
            twos += 1;
        }

        if containes_n_chars(3, map) {
            threes += 1;
        }
    }
     twos * threes
}

fn containes_n_chars(n_appear: i32, map: &HashMap<char, i32>) -> bool {
    /// Counts how many keys appear n-times in the HashMap
    let mut counter: i32 = 0;
    let content: Vec<&i32> = map.values().collect();
    content.contains(&&n_appear)
}

fn get_hashMap(line: &String) -> HashMap<char, i32>{
    let mut hash:HashMap<char, i32> = HashMap::new();
        for c in line.chars(){
            let counter = hash.entry(c).or_insert(0);
            *counter += 1;
        }
    hash
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
    return Ok(split);
}