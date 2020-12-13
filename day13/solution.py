import functools
import math
import operator


def find_earliest_departure(busses, timestamp):
    next_departure, bus = min((b * math.ceil(timestamp / b), b) for b in busses if b)
    return (next_departure - timestamp) * bus


def find_perfect_timestamp(busses):
    M = functools.reduce(operator.mul, (b for b in busses if b), 1)
    result = 0

    # Solve the equations using the Chinese Remainder Theorem.
    for i, bus in enumerate(busses):
        if not bus:
            continue

        b_i = M // bus
        b_i_inv = pow(b_i, bus - 2, bus)
        result -= i * b_i * b_i_inv

    return result % M


if __name__ == '__main__':
    with open('input.txt') as f:
        timestamp = int(next(f))
        busses = [int(b) if b != 'x' else None for b in next(f).split(',')]

    earliest_departure = find_earliest_departure(busses, timestamp)
    print('Part 1:', earliest_departure)

    perfect_timestamp = find_perfect_timestamp(busses)
    print('Part 2:', perfect_timestamp)
