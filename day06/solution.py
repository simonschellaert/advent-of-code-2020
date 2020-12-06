if __name__ == '__main__':
    with open('input.txt') as f:
        count_any = count_all = 0

        for group in f.read().split('\n\n'):
            forms = [set(p) for p in group.split('\n') if p]

            # Count the questions for which anyone answered yes in this group.
            count_any += len(set.union(*forms))

            # Count the questions for which everyone answered yes in this group.
            count_all += len(set.intersection(*forms))

        print('Part 1:', count_any)
        print('Part 2:', count_all)
