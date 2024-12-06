use itertools::Itertools;
use std::iter::zip;

advent_of_code::solution!(1);

pub fn part_one(input: &str) -> Option<u32> {
    let mut lines = input.clone().trim().split("\n").map(String::from).collect::<Vec<String>>();
    let (mut first, mut second): (Vec<u32>, Vec<u32>) = lines.iter_mut().map(|line| line.split_once("   ").unwrap()).map(|(x, y)| (str::parse::<u32>(x).unwrap(), str::parse::<u32>(y).unwrap())).unzip();

    first.sort();
    second.sort();

    Some(zip(first, second).map(|(x, y)| x.abs_diff(y)).sum())
}

pub fn part_two(input: &str) -> Option<u32> {
    let lines = input.clone().trim().split("\n").map(String::from).collect::<Vec<String>>();
    let (first, second): (Vec<u32>, Vec<u32>) = lines.iter().map(|line| line.split_once("   ").unwrap()).map(|(x, y)| (str::parse::<u32>(x).unwrap(), str::parse::<u32>(y).unwrap())).unzip();

    let first_counts = first.into_iter().counts();
    let second_counts = second.into_iter().counts();

    Some(first_counts.into_iter().map(|(item, count)| count as u32 * item * *second_counts.get(&item).unwrap_or(&0) as u32).sum())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, None);
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, None);
    }
}
