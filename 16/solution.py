"""
Day 16 Advent of Code 2018
"""
import sys


def main(filename):
    """Parse the input file and output the results."""
    with open(filename) as f:
        parts = f.read().split("\n\n\n\n")

    samples = list(filter(None, parts[0].split("\n")))
    program = list(filter(None, parts[1].split("\n")))
    operations = [addr, addi, mulr, muli, banr, bani,
                  borr, bori, setr, seti, gtir, gtri,
                  gtrr, eqir, eqri, eqrr]
    sample_instructions = parse_samples(samples)
    sum_ops = sum_triplicate_instructions(sample_instructions, operations)
    print(f"Part 1 number of more than 3 possible op codes: {sum_ops}")

    mapping = find_opcode_mapping(sample_instructions, operations)
    registers = execute_program(program, mapping)
    print(f"Part 2 value of first register after executing the program: {registers[0]}")
    return 0


def parse_samples(samples):
    """Parse the sample inputs and outputs."""
    instructions = []
    instruction = []
    for s in samples:
        if s.startswith('Before:'):
            instruction.append(eval(s.split(': ')[1]))
        elif s.startswith('After:'):
            instruction.append(eval(s.split(': ')[1]))
            instructions.append(instruction)
            instruction = []
        else:
            instruction.append(list(map(int, s.split(' '))))
    return instructions


def sum_triplicate_instructions(instructions, operations):
    """Get the total number of all opcodes that could be 3 or more."""
    total = 0
    for (before, instruction, after) in instructions:
        possible_opcodes = find_opcodes(before, instruction, after, operations)
        if len(possible_opcodes) >= 3:
            total += 1
    return total


def find_opcode_mapping(instructions, operations):
    """Find the opcode mapping by eliminating possibilities where the possible opcode is 1."""
    opcode_to_func = {}
    for _ in range(16):
        for (before, instruction, after) in instructions:
            possible_opcodes = find_opcodes(before, instruction, after, operations)
            eliminated_opcodes = [o for o in possible_opcodes if o not in opcode_to_func.values()]
            if len(eliminated_opcodes) == 1 and instruction[0] not in opcode_to_func:
                opcode_to_func[instruction[0]] = eliminated_opcodes[0]
    return opcode_to_func


def execute_program(program, opcode_to_func):
    """Execute the program line by line."""
    registers = [0, 0, 0, 0]
    for instruction in program:
        op, a, b, c = map(int, instruction.split(' '))
        registers = execute_cmd(opcode_to_func[op], registers, a, b, c)
    return registers


def find_opcodes(before, instruction, after, operations):
    """Finds the possible opcodes for a sample."""
    op_code, a, b, c = instruction[:]
    found = []

    for o in operations:
        if execute_cmd(o, before, a, b, c) == after:
            found.append(o)

    return found


def execute_cmd(cmd, registers, a, b, c):
    """Executes a command on the registers."""
    after = registers[:]
    after[c] = cmd(after, a, b)
    return after


def addr(registers, a, b):
    """Addr command."""
    return registers[a] + registers[b]


def addi(registers, a, b):
    """Addi command."""
    return registers[a] + b


def mulr(registers, a, b):
    """Mulr command."""
    return registers[a] * registers[b]


def muli(registers, a, b):
    """Muli command."""
    return registers[a] * b


def banr(registers, a, b):
    """Banr command."""
    return registers[a] & registers[b]


def bani(registers, a, b):
    """Bani command."""
    return registers[a] & b


def borr(registers, a, b):
    """Borr command."""
    return registers[a] | registers[b]


def bori(registers, a, b):
    """Bori command."""
    return registers[a] | b


def setr(registers, a, _):
    """Setr command."""
    return registers[a]


def seti(_, a, __):
    """Seti command."""
    return a


def gtir(registers, a, b):
    """Gtir command."""
    return bool(a > registers[b])


def gtri(registers, a, b):
    """Gtri command."""
    return bool(registers[a] > b)


def gtrr(registers, a, b):
    """Gtrr command."""
    return bool(registers[a] > registers[b])


def eqir(registers, a, b):
    """Eqir command."""
    return bool(a == registers[b])


def eqri(registers, a, b):
    """Eqri command."""
    return bool(registers[a] == b)


def eqrr(registers, a, b):
    """Eqrr command."""
    return bool(registers[a] == registers[b])


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
