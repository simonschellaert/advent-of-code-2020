def calculate_differences(ratings):
    three_diff = one_diff = 0

    for i in range(1, len(ratings)):
        diff = ratings[i] - ratings[i - 1]
        if diff == 3:
            three_diff += 1
        elif diff == 1:
            one_diff += 1

    return one_diff * three_diff


def calculate_combinations_count(ratings):
    count = [0] * len(ratings)
    count[0] = 1

    for i in range(1, len(ratings)):
        j = i - 1

        while j >= 0 and ratings[j] >= ratings[i] - 3:
            count[i] += count[j]
            j -= 1

    return count[-1]


if __name__ == '__main__':
    ratings = [int(line) for line in open('input.txt')]

    ratings += [0, max(ratings) + 3]
    ratings.sort()

    differences = calculate_differences(ratings)
    print('Part 1:', differences)

    combinations = calculate_combinations_count(ratings)
    print('Part 2:', combinations)
