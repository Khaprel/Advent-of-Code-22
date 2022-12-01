#Parse Input
calories = [] #Create 
with open("input.txt", 'r') as fp:
    elf = 0
    for line in fp.readlines():
        cals = line.strip('\n')
        if cals == '':
            calories.append(elf)
            elf = 0
        else:
            elf += int(cals)
    calories.append(elf)

#Part 1
print(max(calories))

#Part 2
calories.sort()
print(sum(calories[:-4:-1]))
