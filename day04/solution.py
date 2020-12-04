import re


constraints = {
  'byr': lambda x: 1920 <= int(x) <= 2020,
  'iyr': lambda x:  2010 <= int(x) <= 2020,
  'eyr': lambda x:  2020 <= int(x) <= 2030,
  'hgt': lambda x: (x.endswith('cm') and 150 <= int(x[:-2]) <= 193) or (x.endswith('in') and 59 <= int(x[:-2]) <= 76),
  'hcl': lambda x: re.match('#[0123456789abcdef]{6}', x),
  'ecl': lambda x:  x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
  'pid': lambda x: len(x) == 9
}


def read_passport(filename):
    with open(filename) as f:
        passports = []

        for group in f.read().split('\n\n'):
            passport = {column.split(':')[0]: column.split(':')[1] for line in group.split('\n') for column in line.split(' ') if line}
            passports.append(passport)

    return passports


if __name__ == '__main__':
    passports = read_passport('input.txt')

    fields_present = fields_valid = 0

    for p in passports:
        # Check if every required field is present.
        if not set(constraints.keys()).issubset(p.keys()):
            continue

        fields_present += 1

        # Check if every required field is valid.
        if all(constraints[key](value) for key, value in p.items() if key in constraints):
            fields_valid += 1

    print('Part 1:', fields_present)
    print('Part 2:', fields_valid)
