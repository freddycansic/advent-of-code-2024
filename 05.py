from aocd import data

example = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

def is_ordered(update, rules):
    for i, page in enumerate(update):
        for (before, after) in rules:
            if page == before:
                if before in update[:i]:
                    return None
                
            if page == after:
                if before in update[i:]:
                    return None
                
    return middle(update)

def middle(update):
    return update[int(len(update) / 2)]

def parse(data):
    rules, updates = data.split("\n\n", 1)
    rules = [[int(num) for num in rule.split("|")] for rule in rules.split("\n")]
    updates = [[int(num) for num in update.split(",")] for update in updates.split("\n")]
    
    return rules, updates

def part_1(data):
    rules, updates = parse(data)
    
    middles = [is_ordered(update, rules) for update in updates]
    middles = [middle for middle in middles if middle is not None]
    
    return sum(middles)
    
def part_2(data):
    rules, updates = parse(data)
    
    unordered = [update for update in updates if not is_ordered(update, rules)]
    middles = [middle(solve(update, rules)) for update in unordered]
    return sum(middles)

def solve(update, rules):
    
    while not is_ordered(update, rules):
        for i, page in enumerate(update):
            for (before, after) in rules:
                # If the rule is not applicable, continue
                if page != before:
                    continue
                
                # If the rule doesn't occur in this update, continue
                if after not in update[:i]:
                    continue
                
                position = update[:i].index(after)
                
                update[i], update[position] = update[position], update[i]
                # Le bubble sort

    return update

print(part_2(data))