directions = {'N': 1j, 'E': 1, 'S': -1j, 'W': -1}


def navigate_ship(instructions):
    position, direction = 0, 1

    for action, distance in instructions:
        if action in directions:
            position += distance * directions[action]
        elif action == 'L':
            direction *= 1j ** (distance / 90)
        elif action == 'R':
            direction *= (-1j) ** (distance / 90)
        elif action == 'F':
            position += direction * distance

    return position


def navigate_ship_using_waypoint(instructions):
    waypoint_position, ship_position = 10 + 1j, 0

    for action, distance in instructions:
        if action in directions:
            waypoint_position += distance * directions[action]
        elif action == 'L':
            waypoint_position *= 1j ** (distance / 90)
        elif action == 'R':
            waypoint_position *= (-1j) ** (distance / 90)
        elif action == 'F':
            ship_position += waypoint_position * distance

    return ship_position


if __name__ == '__main__':
    with open('input.txt') as f:
        instructions = [(line[0], int(line[1:])) for line in f]

    position = navigate_ship(instructions)
    print('Part 1:', int(abs(position.real) + abs(position.imag)))

    position = navigate_ship_using_waypoint(instructions)
    print('Part 2:', int(abs(position.real) + abs(position.imag)))
