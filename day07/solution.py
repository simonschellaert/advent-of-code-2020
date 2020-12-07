from collections import defaultdict


def find_reachable(edges, root):
    stack = [root]
    reachable = set()

    while stack:
        node = stack.pop()
        reachable.add(node)

        for neighbor, _ in edges[node]:
            stack.append(neighbor)

    return reachable


def calculate_reachable_weight(edges, root):
    stack = [(root, 1)]
    total_count, visited = 0, set()

    while stack:
        node, count = stack.pop()
        total_count += count

        for neighbor, subcount in edges[node]:
            stack.append((neighbor, count * subcount))

    return total_count


with open('input.txt') as f:
    # Map every bag to the set of bags that the specified bag can contain.
    contains = defaultdict(set)

    # Map every bag to the set of bags that can contain the specified bag.
    contained_by = defaultdict(set)

    for line in f:
        outer, contents = line.strip('\n.').split(' contain ')
        outer = outer.rstrip('s')

        if contents == 'no other bags':
            continue

        for item in contents.split(','):
            count, inner = item.strip().rstrip('s').split(' ', 1)

            contains[outer].add((inner, int(count)))
            contained_by[inner].add((outer, int(count)))

    # The bags that can eventually contain a shiny gold bag are all the bags that
    # are reachable from a shiny gold bag through the `contained_by` edges.
    predecessors = find_reachable(contained_by, 'shiny gold bag')
    print('Part 1:', len(predecessors) - 1)

    # The number of bags required within a shiny gold bag is the sum of the
    # (recursive) weightsof all the nodes reachable by the `contains` edges.
    weight = calculate_reachable_weight(contains, 'shiny gold bag')
    print('Part 2:', weight - 1)
