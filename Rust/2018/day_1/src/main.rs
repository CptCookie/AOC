const TOKEN:&str = "53616c7465645f5f381ca9f990b331963bc4c559f548054e919235f4337b05da8d79afdd8cd16584b77c0ee4771218fc";

fn main() {
    let input = read_input("https://adventofcode.com/2018/day/1/input").unwrap();
    println!("The sum of all frequency is: {:#?}", sum_freq(&input));

    assert!(fist_double(vec![3, 3, 4, -2, -4]).unwrap() == 10);
    assert!(fist_double(vec![-6, 3, 8, 5, -6]).unwrap() == 5);
    assert!(fist_double(vec![7, 7, -2, -7, -4]).unwrap() == 14);
    println!("The fist double frequency is: {}", fist_double(input).unwrap())

}

fn fist_double(freq_change: Vec<i32>) -> Option<i32> {
    let mut counter = 0;
    let mut distinct_freq: Vec<i32> = vec![0];

    while counter < 1000 {
        for n in freq_change.iter(){
            let new_freq:i32 = distinct_freq.last().unwrap() + n;
            if distinct_freq.iter().any(|n| *n == new_freq){
                return Some(new_freq)
            } else {
                distinct_freq.push(new_freq)
            }
        }
        counter+=1;
    }
    return None
}

fn sum_freq(freq_change: &Vec<i32>) -> i32  {
    let mut result :i32 = 0;
    freq_change.iter().for_each(|n| result += n);
    result
}

fn read_input(url:&str)-> Result<Vec<i32>, Box<dyn std::error::Error>> {
    let client = reqwest::blocking::Client::new();
    let resp = client.get(url)
                               .header(reqwest::header::COOKIE, format!("session={}", TOKEN))
                               .send()?;
    
    let mut split:Vec<i32> = resp.text()?
                             .split("\n")
                             .map(|n| n.parse::<i32>()
                             .unwrap_or(0))
                             .collect();
    split.pop();
    return Ok(split);
}