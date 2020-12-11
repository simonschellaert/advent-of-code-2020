import copy
import itertools


def advance_to_equilibrium(grid, neighbors_generator, occupancy_threshold):
    old_grid = None

    while old_grid != grid:
        old_grid = grid
        grid = copy.deepcopy(grid)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                neighbors = neighbors_generator(old_grid, row, col)

                if old_grid[row][col] == 'L' and all(n != '#' for n in neighbors):
                    grid[row][col] = '#'

                if old_grid[row][col] == '#' and sum(n == '#' for n in neighbors) >= occupancy_threshold:
                    grid[row][col] = 'L'

    return grid


def generate_neighbors_visible(grid, row, col):
    neighbors = []

    # Find the first visible seat in each of the 8 directions.
    for d_r, d_c in itertools.product((-1, 0, 1), repeat=2):
        if not d_r and not d_c:
            continue

        r, c = row + d_r, col + d_c

        while 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            if grid[r][c] in '#L':
                neighbors.append(grid[r][c])
                break

            r, c = r + d_r, c + d_c

    return neighbors


def generate_neighbors_adjacent(grid, row, col):
    return [grid[row + r][col + c] for r, c in itertools.product((-1, 0, 1), repeat=2) if (r or c) and 0 <= row + r < len(grid) and 0 <= col + c < len(grid[0])]


if __name__ == '__main__':
    initial = [list(line.rstrip()) for line in open('input.txt')]

    equilibrium = advance_to_equilibrium(initial, generate_neighbors_adjacent, 4)
    occupied_seats = sum(row.count('#') for row in equilibrium)
    print('Part 1:', occupied_seats)

    equilibrium = advance_to_equilibrium(initial, generate_neighbors_visible, 5)
    occupied_seats = sum(row.count('#') for row in equilibrium)
    print('Part 2:', occupied_seats)
