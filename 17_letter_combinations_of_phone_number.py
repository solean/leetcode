from typing import List

def letter_combinations(digits: str) -> List[str]:
    if len(digits) == 0:
        return []

    mappings = {
        '1': '',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    combinations = []
    generate_combos(combinations, '', 0, digits, mappings)
    return combinations

def generate_combos(combinations, combination, i, digits, mappings):
    if i == len(digits):
        combinations.append(combination)
    else:
        for ch in mappings[digits[i]]:
            generate_combos(combinations, combination + ch, i + 1, digits, mappings)

