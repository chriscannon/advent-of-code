"""
Calculate Santa's fabric overlap
"""

FABRIC = []
for x in range(1000):
    row = []
    for y in range(1000):
        row.append(".")
    FABRIC.append(row)

INPUT_FILE = open("3/input.txt", "r")
for line in INPUT_FILE:
    id_postition_size = line.split("@")
    f_id = int(id_postition_size[0].strip().strip('#'))
    position_size = id_postition_size[1].strip().split(":")
    left, top = [int(x) for x in position_size[0].split(",")]
    width, height = [int(x) for x in position_size[1].strip().split("x")]

    for i in range(height):
        for j in range(width):
            current = FABRIC[top-1+i][left-1+j]
            if current == ".":
                FABRIC[top-1+i][left-1+j] = f_id
            else:
                FABRIC[top-1+i][left-1+j] = "X"
INPUT_FILE.close()

INPUT_FILE = open("3/input.txt", "r")
for line in INPUT_FILE:
    id_postition_size = line.split("@")
    f_id = int(id_postition_size[0].strip().strip('#'))
    position_size = id_postition_size[1].strip().split(":")
    left, top = [int(x) for x in position_size[0].split(",")]
    width, height = [int(x) for x in position_size[1].strip().split("x")]

    found_x = False
    for i in range(height):
        for j in range(width):
            current = FABRIC[top-1+i][left-1+j]
            if current == "X":
                found_x = True

    if found_x is False:
        print("Non-overlapping ID: {}".format(f_id))
        break
INPUT_FILE.close()
