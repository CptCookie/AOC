const TOKEN:&str = "53616c7465645f5f381ca9f990b331963bc4c559f548054e919235f4337b05da8d79afdd8cd16584b77c0ee4771218fc";

fn read_input(url:&str)-> Result<String, Box<dyn std::error::Error>> {
    let client = reqwest::blocking::Client::new();
    let resp = client.get(url)
                     .header(reqwest::header::COOKIE, format!("session={}", TOKEN))
                     .send()?;
    
    let mut split:String = String::from(
                                    resp.text()?
                                    .replace("\n", "")
                                );
    split.pop();
    return Ok(split);
}


fn main() {
    let mut input: String = read_input("https://adventofcode.com/2018/day/5/input").unwrap();
    let mut polymere:Vec<char> = input.chars().collect();
    
    let mut polyCopy = polymere.clone();
    for (i, letter) in polymere[..polymere.len()-1].iter().rev().enumerate() {
        let n = polymere.len() - i;
        if polymere[n].to_lowercase().to_string() == polymere[n-1].to_lowercase().to_string() {
            polymere.remove(*n);
            polymere.remove(*n-1);
        }
    }
}
