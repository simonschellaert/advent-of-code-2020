neighbor_offsets = {'e': 1j, 'w': -1j, 'se': -1, 'sw': -1 - 1j, 'ne': 1 + 1j, 'nw': 1}


def neighbors(position):
    return {position + offset for offset in neighbor_offsets.values()}


def flip_tiles(lines):
    black = set()

    for line in lines:
        position = 0

        while line:
            for name, offset in neighbor_offsets.items():
                if not line.startswith(name):
                    continue

                position += offset
                line = line[len(name):]

        black ^= set([position])

    return black


def advance(initial, step):
    black = initial

    for _ in range(step):
        new_black = set(black)
        to_check = set(black)

        for position in black:
            to_check |= neighbors(position)

        for position in to_check:
            count = sum(n in black for n in neighbors(position))

            if (position in black and (count == 0 or count > 2)) or \
               (position not in black and count == 2):
                new_black ^= set([position])

        black = new_black

    return black


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [l.strip() for l in f.readlines()]

    initial = flip_tiles(lines)
    print('Part 1:', len(initial))

    final = advance(initial, 100)
    print('Part 2:', len(final))
