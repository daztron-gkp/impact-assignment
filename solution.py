from itertools import product
from typing import List


def all_ways_to_attend_classes(days: int) -> list:
    options = ["P", "A"]
    # P denotes Present and A denotes absent
    # which are the available options for a day
    ways = [''.join(x) for x in product(options, repeat=days)]
    return ways


def invalid_ways_to_attend(total_ways: List[str]) -> list:
    # four or more consecutive leaves (denoted by A)
    # are considered to be ineligible for attending graduation
    return [x for x in total_ways if "AAAA" in x]


def solution_for_days(days: int) -> str:
    all_ways = all_ways_to_attend_classes(days)
    ineligible_ways = invalid_ways_to_attend(all_ways)

    remaining_ways = [x for x in all_ways if x not in ineligible_ways]
    numerator = len([x for x in remaining_ways if x[-1] == 'A'])
    return f"{str(numerator)}/{str(len(all_ways) - len(ineligible_ways))}"
