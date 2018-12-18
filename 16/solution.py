"""
Day 16 Advent of Code 2018
"""
import sys


def main(filename):
    """Parse the input file and output the results."""
    with open(filename) as f:
        instructions = []
        instruction = []
        parts = f.read().split("\n\n\n\n")
        samples = list(filter(None, parts[0].split("\n")))
        program = list(filter(None, parts[1].split("\n")))

        for s in samples:
            if s.startswith('Before:'):
                instruction.append(eval(s.split(': ')[1]))
            elif s.startswith('After:'):
                instruction.append(eval(s.split(': ')[1]))
                instructions.append(instruction)
                instruction = []
            else:
                instruction.append(list(map(int, s.split(' '))))

        total = 0
        for (before, instruction, after) in instructions:
            possible_opcodes = find_opcodes(before, instruction, after)
            if len(possible_opcodes) > 2:
                total += 1

        print(f"Part 1 number of more than 3 possible op codes: {total}")

        opcode_to_func = {}
        for _ in range(16):
            for (before, instruction, after) in instructions:
                possible_opcodes = find_opcodes(before, instruction, after)
                eliminated_opcodes = [o for o in possible_opcodes if o not in opcode_to_func.values()]
                if len(eliminated_opcodes) == 1 and instruction[0] not in opcode_to_func:
                    opcode_to_func[instruction[0]] = eliminated_opcodes[0]

        registers = [0, 0, 0, 0]
        for instruction in program:
            op, a, b, c = map(int, instruction.split(' '))
            registers = opcode_to_func[op](registers, a, b, c)
        print(f"Part 2 value of first register after executing program: {registers[0]}")


def find_opcodes(before, instruction, after):
    op_code, a, b, c = instruction[:]
    found = []

    if addr(before, a, b, c) == after:
        found.append(addr)

    if addi(before, a, b, c) == after:
        found.append(addi)

    if mulr(before, a, b, c) == after:
        found.append(mulr)

    if muli(before, a, b, c) == after:
        found.append(muli)

    if banr(before, a, b, c) == after:
        found.append(banr)

    if bani(before, a, b, c) == after:
        found.append(bani)

    if borr(before, a, b, c) == after:
        found.append(borr)

    if bori(before, a, b, c) == after:
        found.append(bori)

    if setr(before, a, b, c) == after:
        found.append(setr)

    if seti(before, a, b, c) == after:
        found.append(seti)

    if gtir(before, a, b, c) == after:
        found.append(gtir)

    if gtri(before, a, b, c) == after:
        found.append(gtri)

    if gtrr(before, a, b, c) == after:
        found.append(gtrr)

    if eqir(before, a, b, c) == after:
        found.append(eqir)

    if eqri(before, a, b, c) == after:
        found.append(eqri)

    if eqrr(before, a, b, c) == after:
        found.append(eqrr)

    return found


def addr(registers, a, b, c):
    after = registers[::]
    after[c] = after[a] + after[b]
    return after


def addi(registers, a, b, c):
    after = registers[::]
    after[c] = after[a] + b
    return after


def mulr(registers, a, b, c):
    after = registers[::]
    after[c] = after[a] * after[b]
    return after


def muli(registers, a, b, c):
    after = registers[::]
    after[c] = after[a] * b
    return after


def banr(registers, a, b, c):
    after = registers[::]
    after[c] = after[a] & after[b]
    return after


def bani(registers, a, b, c):
    after = registers[::]
    after[c] = after[a] & b
    return after


def borr(registers, a, b, c):
    after = registers[::]
    after[c] = after[a] | after[b]
    return after


def bori(registers, a, b, c):
    after = registers[::]
    after[c] = after[a] | b
    return after


def setr(registers, a, _, c):
    after = registers[::]
    after[c] = after[a]
    return after


def seti(registers, a, _, c):
    after = registers[::]
    after[c] = a
    return after


def gtir(registers, a, b, c):
    after = registers[::]
    after[c] = bool(a > after[b])
    return after


def gtri(registers, a, b, c):
    after = registers[::]
    after[c] = bool(after[a] > b)
    return after


def gtrr(registers, a, b, c):
    after = registers[::]
    after[c] = bool(after[a] > after[b])
    return after


def eqir(registers, a, b, c):
    after = registers[::]
    after[c] = bool(a == after[b])
    return after


def eqri(registers, a, b, c):
    after = registers[::]
    after[c] = bool(after[a] == b)
    return after


def eqrr(registers, a, b, c):
    after = registers[::]
    after[c] = bool(after[a] == after[b])
    return after


if __name__ == '__main__':
    main(sys.argv[1])
