# Every parameterized instruction maps a state, represented by a tuple (ip, acc), to a new state.
opcodes = {
    'nop': lambda arg, ip, acc: (ip + 1, acc),
    'acc': lambda arg, ip, acc: (ip + 1, acc + arg),
    'jmp': lambda arg, ip, acc: (ip + arg, acc)
}


def run_program(program):
    visited = set()
    ip = acc = 0

    while ip < len(program):
        if ip in visited:
            return False, acc

        visited.add(ip)

        op, arg = program[ip]
        ip, acc = opcodes[op](arg, ip, acc)

    return True, acc


if __name__ == '__main__':
    with open('input.txt') as f:
        program = [(opcode, int(argument)) for line in f for (opcode, argument) in (line.rstrip().split(' '),)]

    _, result = run_program(program)
    print('Part 1:', result)

    for i, (opcode, argument) in enumerate(program):
        # Replace this `jmp` by a `nop` or vice-versa and test if the resulting program halts.
        if opcode == 'nop':
            program[i] = 'jmp', argument
        elif opcode == 'jmp':
            program[i] = 'nop', argument

        halts, result = run_program(program)
        if halts:
            print('Part 2:', result)
            break

        # Restore the modified instruction to what it originally was.
        program[i] = opcode, argument
