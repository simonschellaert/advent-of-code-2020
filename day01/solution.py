def find_two_sum(values, desired_sum):
    seen = set()

    for value in values:
        complement = desired_sum - value

        if complement in seen:
            return complement, value

        seen.add(value)


def find_three_sum(values, desired_sum):
    seen = set()

    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            complement = desired_sum - values[i] - values[j]

            if complement in seen:
                return complement, values[i], values[j]

        seen.add(values[i])


if __name__ == '__main__':
    with open('input.txt') as f:
        expenses = [int(line) for line in f]

    a, b = find_two_sum(expenses, 2020)
    print('Part 1:', a * b)

    a, b, c = find_three_sum(expenses, 2020)
    print('Part 2:', a * b * c)
