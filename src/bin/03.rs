use regex::Regex;

advent_of_code::solution!(3);

pub fn part_one(input: &str) -> Option<u32> {
    let multiply_pairs = Regex::new(r"mul\((?<x>\d+),(?<y>\d+)\)").unwrap();
    let values = multiply_pairs.captures_iter(input);

    Some(values.map(|pair| (pair["x"].parse::<u32>().unwrap(), pair["y"].parse::<u32>().unwrap())).map(|(x, y)| x * y).sum())
}

pub fn part_two(input: &str) -> Option<u32> {
    let ignore_instructions = Regex::new(r"don't\(\)[\s\S]*?do\(\)").unwrap();
    let ignore_end = Regex::new(r"don't\(\)[\s\S]*").unwrap();

    let sanitised_instructions = ignore_instructions.replace_all(input, "");
    let sanitised_instructions = ignore_end.replace(&*sanitised_instructions, "");

    part_one(&*sanitised_instructions)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(161));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(48));
    }
}
