use itertools::Itertools;

advent_of_code::solution!(2);

pub fn is_safe(levels: &[i32]) -> bool {
    let diffs = levels.windows(2).map(|pair| pair[1] - pair[0]).collect_vec();

    let is_same_sign = diffs.iter().all(|&x| x.is_negative()) || diffs.iter().all(|&x| x.is_positive());

    if !is_same_sign {
        return false;
    }

    let is_abs_safe = diffs.iter().all(|&diff| diff.abs() <= 3);

    is_abs_safe
}

pub fn part_one(input: &str) -> Option<u32> {
    let lines = input.trim().split("\n").map(String::from);
    let nums = lines.map(|line| line.split_whitespace().map(str::parse::<i32>).map(Result::unwrap).collect_vec()).collect_vec();

    let safe = nums.iter().filter(|line| is_safe(line)).count();

    Some(safe as u32)
}

pub fn part_two(input: &str) -> Option<u32> {
    let lines = input.trim().split("\n").map(String::from);
    let nums = lines.map(|line| line.split_whitespace().map(str::parse::<i32>).map(Result::unwrap).collect_vec()).collect_vec();

    let unsafes = nums.iter().filter(|line| !is_safe(line)).collect_vec();

    let mut total_safe = nums.len() - unsafes.len();

    // Idc
    for unsafe_nums in unsafes {
        for i in 0..unsafe_nums.len() {
            let mut check = unsafe_nums.clone();
            check.remove(i);

            if is_safe(&check) {
                total_safe += 1;
                break;
            }
        }
    }

    Some(total_safe as u32)
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
