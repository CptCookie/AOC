use std::{collections::HashMap, fmt::Debug};

#[derive(Debug)]
struct Point {
    x: i32,
    y: i32,
}
#[derive(Debug)]
struct Square {
    id: i32,
    root: Point,
    size: Point,
}

struct Fabric {
    fabric: Vec<Vec<i32>>, //linear Vector of 2D Array filled with id that claime that square
}

impl Fabric {
    fn new() -> Fabric {
        let fabric: Vec<Vec<i32>> = vec![vec![]; 1000000];
        Fabric { fabric }
    }

    fn get<'a>(&'a mut self, x: usize, y: usize) -> &'a mut Vec<i32> {
        return self.fabric[y * 1000 + x].as_mut();
    }

    fn count_conflicts(&self) -> i32 {
        let mut counter = 0;
        for n in self.fabric.iter() {
            if n.len() > 1 {
                counter += 1;
            }
        }
        counter
    }

    fn set(&mut self, point: &Point, id: i32) {
        let f_point = self.get(point.x as usize, point.y as usize);
        f_point.push(id);
    }

    fn find_legit_claim(&self) -> HashMap<i32, i32> {
        let mut legit: HashMap<i32, i32> = HashMap::new();
        let mut overlap: HashMap<i32, i32> = HashMap::new();

        for (_, p) in self.fabric.iter().enumerate() {
            // first apperance of this single ID
            if p.len() == 1 && legit.get(&p[0]) == None && overlap.get(&p[0]) == None {
                legit.entry(p[0]).or_insert(1);
            } else if p.len() > 1 {
                for id in p {
                    legit.remove(id);
                    overlap.entry(*id).or_insert(1);
                }
            }
        }

        legit
    }
}

impl Square {
    fn new(input: &str) -> Square {
        let sectors: Vec<String> = input
            .replace("#", "")
            .replace(" @ ", " ")
            .replace(": ", " ")
            .replace(",", " ")
            .replace("x", " ")
            .split_whitespace()
            .map(|n| String::from(n))
            .collect();

        let root = Point {
            x: sectors[1].parse().unwrap(),
            y: sectors[2].parse().unwrap(),
        };
        let size = Point {
            x: sectors[3].parse().unwrap(),
            y: sectors[4].parse().unwrap(),
        };
        let id: i32 = sectors[0].parse().unwrap();
        Square { id, root, size }
    }

    fn get_all_coord(&self) -> Vec<Point> {
        let mut points: Vec<Point> = Vec::new();
        for x in (self.root.x)..=(self.root.x + self.size.x - 1) {
            for y in (self.root.y)..=(self.root.y + self.size.y - 1) {
                points.push(Point { x, y })
            }
        }

        return points;
    }
}

pub fn part_1(input: &String) -> String {
    // calculates the solution of AOC2018 day 3 part 1
    let data = parse_input(input);
    let mut claims: Vec<Square> = Vec::new();
    let mut fabric: Fabric = Fabric::new();

    for n in data.iter() {
        claims.push(Square::new(n));
    }

    for claim in claims.iter() {
        let points = claim.get_all_coord();

        for p in points.iter() {
            fabric.set(p, claim.id)
        }
    }

    fabric.count_conflicts().to_string()
}

pub fn part_2(input: &String) -> String {
    // calculates the solution of AOC2018 day 3 part 1
    let data = parse_input(input);
    let mut claims: Vec<Square> = Vec::new();
    let mut fabric: Fabric = Fabric::new();

    for n in data.iter() {
        claims.push(Square::new(n));
    }

    for claim in claims.iter() {
        let points = claim.get_all_coord();

        for p in points.iter() {
            fabric.set(p, claim.id)
        }
    }

    format!("{:?}", fabric.find_legit_claim())
}

fn parse_input(input: &String) -> Vec<&str> {
    input.split("\n").filter(|l| l.len() > 0).collect()
}
