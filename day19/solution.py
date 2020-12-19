from functools import reduce
from typing import Dict, List, Set, Union


# Every rule maps a rule id to a set of one or more alternatives. Each alternative in turn
# is either a string to match literally, or a sequence of rule ids to match one after another.
RuleBook = Dict[int, Set[Union[List[int], str]]]


def match(rule_id: int, string: str, rules: RuleBook) -> List[str]:
    matches = []

    for pattern in rules[rule_id]:
        if isinstance(pattern, str) and string.startswith(pattern):
            matches += [string[len(pattern):]]
        elif isinstance(pattern, tuple):
            pattern_matches = [string]

            for subpattern in pattern:
                pattern_matches = [new_match for cur_match in pattern_matches for new_match in match(subpattern, cur_match, rules)]

            matches += pattern_matches

    return matches


def count_matching_messages(messages: List[str], rules: RuleBook) -> int:
    count = 0

    for message in messages:
        count += any(r == '' for r in match(0, message, rules))

    return count


if __name__ == '__main__':
    with open('input.txt') as f:
        rule_descriptions, messages = [part.split('\n') for part in f.read().split('\n\n')]

        rules = {}

        for rule in rule_descriptions:
            rule_id, context = rule.split(':')

            if '"' in context:
                rules[int(rule_id)] = {context.strip().strip('"')}
            else:
                rules[int(rule_id)] = {tuple(int(subrule) for subrule in alternation.strip().split(' ')) for alternation in context.split('|')}

    print('Part 1:', count_matching_messages(messages, rules))

    rules[8] = {(42, ), (42, 8)}
    rules[11] = {(42, 31), (42, 11, 31)}

    print('Part 2:', count_matching_messages(messages, rules))
