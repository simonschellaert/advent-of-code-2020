from collections import deque


def find_invalid_number(numbers, pre_length):
    preamble = deque(numbers[:pre_length])

    for number in numbers[pre_length:]:
        # Return if the number can't be formed by adding two numbers in the preamble.
        if all(number != preamble[i] + preamble[j] for i in range(len(preamble)) for j in range(i)):
            return number

        # Delete the oldest number in the preamble and add our new number.
        preamble.popleft()
        preamble.append(number)


def find_weakness(numbers, invalid_number):
    # Maps each prefix sum to the position where it ends.
    prefix_sums = {}

    running_sum = 0

    for end, number in enumerate(numbers):
        running_sum += number
        to_subtract = running_sum - invalid_number

        # Check if there's an existing prefix sum we can substract to get our desired number.
        if to_subtract in prefix_sums:
            contiguous = numbers[prefix_sums[to_subtract] + 1:end + 1]
            return min(contiguous) + max(contiguous)

        prefix_sums[running_sum] = end


if __name__ == '__main__':
    numbers = [int(line) for line in open('input.txt')]

    invalid_number = find_invalid_number(numbers, 25)
    print('Part 1:', invalid_number)

    weakness = find_weakness(numbers, invalid_number)
    print('Part 2:', weakness)
