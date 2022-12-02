#Parse Input
elf_calories = [] #Create empty list to push elf calorie totals to.
with open("input.txt", 'r') as fp:
    elf = 0 #Running Total of calories held by elf
    for line in fp.readlines():
        cals = line.strip('\n') #Remove the newline from the text file
        if cals == '': #Indicates a new elf, pushing the current elf total to the elf_calories list, and resetting the elf total to 0.
            elf_calories.append(elf)
            elf = 0
        else:       #Indicates same elf, adding current calorie count to running total for the elf.
            elf += int(cals) 
    elf_calories.append(elf)

#Part 1
print(f'The elf with the most calories is carrying: {max(elf_calories)} calories.') #Print highest calorie total for the elves.

#Part 2
elf_calories.sort()
print(f'The 3 elves with the most calories are carrying a total of {sum(elf_calories[:-4:-1])} calories.') # Sorts the calories, lowest to highest. Then returns the sum of the last(read highest) 3 elves.

#Because my daughter wanted to know how many elves there were.
print(f'There are a total of {len(elf_calories)} elves.')
