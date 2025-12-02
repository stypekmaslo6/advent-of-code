import os

dir_path = os.path.dirname(os.path.realpath(__file__))
input_file = "input.txt"

def day2(input, part2):
    id_list = open(os.path.join(dir_path, input)).read().split(',')
    code = 0
    for id_range in id_list:
        start, end = map(int, id_range.split('-'))
        for id_num in range(start, end + 1):
            id_str = str(id_num)
            has_double = False
            has_at_least_one_double = False

            if part2:
                for i in range(1, len(id_str)):
                    if len(id_str) % i == 0:
                        chunks = [id_str[j:j+i] for j in range(0, len(id_str), i)]
                        if all(x == chunks[0] for x in chunks):
                            has_at_least_one_double = True
                if has_at_least_one_double:
                    code += id_num
            else:
                if len(id_str) % 2 == 0:
                    if id_str[:len(id_str)//2] == id_str[len(id_str)//2:]:
                        has_double = True

                if has_double:
                    code += id_num
    return code
            
print(f"Part 1: {day2(input_file, False)}")
print(f"Part 2: {day2(input_file, True)}")