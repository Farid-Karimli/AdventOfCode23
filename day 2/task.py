puzzle = open("puzzle.txt", "r")
puzzle = puzzle.read().split("\n")

config = {"red": 12, "green": 13, "blue": 14}

def process_set(s):
    d = {"red": 0, "green": 0, "blue": 0}
    for ball in s:
        ball = ball.strip().split()
        d[ball[1]] = int(ball[0])

    return d.values()

def run_check(red, green, blue):
    if red > config["red"]:
        return False
    if green > config["green"]:
        return False
    if blue > config["blue"]:
        return False
    return True

total = 0

for line in puzzle:
    valid = True
    parts = line.split(":")

    gameid = int(parts[0].split()[1])
    power = 1

    sets = parts[1].split(";")

    max_red, max_green, max_blue = process_set(sets[0].split(","))
    for set in sets:
        set = set.split(",")

    
        red, green, blue = process_set(set)
    
        if red > max_red:
            max_red = red
            
        if green > max_green:
            max_green = green
            
        if blue > max_blue:
            max_blue = blue
            
    power *= max_red
    power *= max_green
    power *= max_blue

    print(power)

    if valid:
        print(gameid,"is valid")
        total += power

print("Total is:")
print(total)

            