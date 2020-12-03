def count_trees(grid, down, right):
    row, col = down, right
    count = 0

    while row < len(grid):
        count += grid[row][col] == '#'
        row, col = row + down, (col + right) % len(grid[0])

    return count


if __name__ == '__main__':
    with open('input.txt') as f:
        grid = [list(row.rstrip()) for row in f]

    print('Part 1:', count_trees(grid, 1, 3))

    count = 1

    for down, right in ((1, 1), (1, 3), (1, 5), (1, 7), (2, 1)):
        count *= count_trees(grid, down, right)

    print('Part 2:', count)
