fn parse_input(input: &String) -> Vec<u16> {
    input
        .split_ascii_whitespace()
        .map(|num| num.parse::<u16>().unwrap())
        .collect()
}
fn is_valid_triangle(triangle: &Vec<u16>) -> bool {
    let max_side = triangle.iter().max().unwrap();
    triangle.iter().sum::<u16>() - max_side > *max_side
}

fn count_valid_trianges(triangles: Vec<u16>) -> usize {
    triangles
        .chunks_exact(3)
        .map(|t| is_valid_triangle(&t.to_vec()))
        .filter(|t| *t)
        .collect::<Vec<bool>>()
        .len()
}

pub fn part_1(input: &String) -> String {
    let triangles = parse_input(input);
    count_valid_trianges(triangles).to_string()
}

pub fn part_2(input: &String) -> String {
    let triangles = parse_input(input);
    let reform_tri: Vec<u16> = vec![
        triangles.iter().skip(0).step_by(3).collect::<Vec<&u16>>(),
        triangles.iter().skip(1).step_by(3).collect(),
        triangles.iter().skip(2).step_by(3).collect(),
    ]
    .iter()
    .flatten()
    .map(|v| **v)
    .collect();

    count_valid_trianges(reform_tri).to_string()
}
