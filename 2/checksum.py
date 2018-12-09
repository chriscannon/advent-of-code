f = open('input.txt', 'r')

two_count = 0
three_count = 0
for l in f:
    chars = {}
    for c in l.strip():
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1

    check_two = True
    check_three = True
    for k, v in chars.items():
        if v == 2 and check_two:
            two_count += 1
            check_two = False
        elif v == 3 and check_three:
            three_count += 1
            check_three = False

print("Checksum: {}".format(two_count * three_count))
