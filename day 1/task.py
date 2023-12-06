import re
# pattern for finding a digit word in a string
pattern = r'(?=(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9))'

digit_dict = {'one': 1, 'two': 2, 'three': 3 , 'four': 4, 'five':5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

for n in range(1,10):
    digit_dict[str(n)] = n

puzzle1 = open("input.txt").read().split("\n")
print(puzzle1)

total = 0
i = 0
for s in puzzle1:
    i += 1
    finds = re.findall(pattern, s)
    print(s)
    print(finds)
    num = str(digit_dict[finds[0]]) + str(digit_dict[finds[-1]])
    print(num)

    total += int(num)

print(i)
print(total)