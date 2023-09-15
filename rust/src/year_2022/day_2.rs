fn parse_data(data: String) -> Vec<Vec<u32>> {
        data.split("\n")
            .filter(|x| x != &"")
            .map(|row| {
                row.replace("\n", "").split(" ").collect()
            })
            .collect()
    }


fn main() {
    println!("Hello, world!");
}
