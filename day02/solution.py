import re


if __name__ == '__main__':
    with open('input.txt') as input_file:
        policies = [(int(a), int(b), c, d) for line in input_file for a, b, c, d in (re.split('-|: | ', line),)]

    # Determine the number of passwords with between `lower` and `upper` occurences of the specified letter.
    valid = sum(lower <= sum(x == letter for x in password) <= upper \
                for lower, upper, letter, password in policies)
    print('Part 1:', valid)

    # Determine the number of passwords with the specified letter at either position `i` or at position `j`
    valid = sum(max(i, j) <= len(password) and (password[i - 1] == letter) ^ (password[j - 1] == letter) \
                for i, j, letter, password in policies)
    print('Part 2:', valid)
