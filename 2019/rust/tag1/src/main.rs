use std::io::{self, Read};

fn calc_fuel(mass: i64) -> i64 {
    return (mass / 3) - 2;
}

fn main() {
    /* Create empty string with some capacity at the beginning, so as to make less relocations
     * during reading the input
     */
    let mut input = String::with_capacity(4096);
    io::stdin().read_to_string(&mut input).expect("Error reading input");
    
    let mut sum: i64 = 0;
    for word in input.split_ascii_whitespace() {
        let mass: i64 = word.parse().expect("Invalid number Dude");

        let mut additionalFuel = calc_fuel(mass);
        sum += additionalFuel;

        /* Doing simple things in a loop is always better than recursion!
         * 8 is the highest value that divided by 3 and floored is equal to 2
         */
        while additionalFuel > 8 {
            additionalFuel = calc_fuel(additionalFuel);
            sum += additionalFuel;
        }
    }

    println!("{}", sum);
}
