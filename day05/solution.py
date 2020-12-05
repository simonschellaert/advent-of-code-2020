from functools import reduce


if __name__ == '__main__':
    # Convert each boarding pass to a binary number by replacing B and R by 1 and L and F by 0.
    translation = str.maketrans('BRLF', '1100')

    with open('input.txt') as input_file:
        seats = set(int(line.translate(translation), 2) for line in input_file)

    print('Part 1:', max(seats))

    # Find the missing seat.
    all_seats = set(range(min(seats), max(seats) + 1))
    print('Part 2:', next(iter(all_seats - set(seats))))
