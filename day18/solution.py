def evaluate(line, reverse):
    # Split the given line in tokens and evaluate it.
    tokens = line.strip().replace(')', ' ) ').replace('(', ' ( ').split()
    result, _ = expression(tokens, reverse)
    return result


def expression(tokens, reverse):
    # If running in normal mode, i.e. without operator precendence, an expression
    # consists of one or more terms separated by plus signs or multiplication signs.
    #
    # If running in reverse mode, i.e. with reversed operator precedence, an expression
    # consists of factors separated by multiplication signs. Those factors might then
    # themselves contain one or more terms separated by plus signs, as handled in `factor()`.
    descendant = factor if reverse else term

    # Consume the first term or factor.
    result, tokens = descendant(tokens, reverse)

    while tokens and tokens[0] in '+*':
        op = tokens[0]
        res, tokens = descendant(tokens[1:], reverse)

        assert not reverse or op == '*'
        result = (result * res) if op == '*' else (result + res)

    return result, tokens


def factor(tokens, reverse):
    # Factors are only used in reverse mode. In normal mode, + and * have the same
    # precedence and are both handled in `expression()`.
    assert reverse

    result, tokens = term(tokens, reverse)

    while tokens and tokens[0] == '+':
        op = tokens[0]
        f, tokens = term(tokens[1:], reverse)
        result += f

    return result, tokens


def term(tokens, reverse):
    if tokens[0] == '(':
        # Consume the opening parenthesis, parse the expression, and consume the closing parenthesis.
        exp, tokens = expression(tokens[1:], reverse)
        return exp, tokens[1:]
    else:
        return int(tokens[0]), tokens[1:]


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()

    print('Part 1:', sum(evaluate(line, reverse=False) for line in lines))
    print('Part 2:', sum(evaluate(line, reverse=True) for line in lines))
