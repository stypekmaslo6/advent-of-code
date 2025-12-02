import os

dir_path = os.path.dirname(os.path.realpath(__file__))
input_file = "input.txt"

def day1(input, part2):
    dial = 50
    code = 0
    with open(os.path.join(dir_path, input)) as f:
        for cmd in f:
            step = int(cmd[1::])
            tmp = dial
            dial = (dial + step) % 100 if cmd[0] == 'R' else (dial - step) % 100

            if part2:
                code += (tmp + step) // 100 if cmd[0] == 'R' else max(0, 1 + (step - (tmp if tmp > 0 else 100)) // 100)
            else:
                code = code + 1 if dial == 0 else code

    return code
            
print(f"Part 1: {day1(input_file, False)}")
print(f"Part 2: {day1(input_file, True)}")