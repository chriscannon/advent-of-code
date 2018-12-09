f = open('input.txt', 'r')

ids = []
for l in f:
    ids.append(l.strip())

identical_ids = []
for i in range(len(ids)):
    current_id = ids[i]
    for j in range(len(ids)):
        diff = 0
        if j == i:
            continue
        check_id = ids[j]
        for t, c in enumerate(check_id):
            if c != current_id[t]:
                diff += 1
        if diff == 1:
            identical_ids.append([current_id, check_id])

common_letters = ""
for i, c in enumerate(identical_ids[0][0]):
    if c == identical_ids[0][1][i]:
        common_letters += c
print("Common letters among identical IDs: {}".format(common_letters))