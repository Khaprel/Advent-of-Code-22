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
print(max(elf_calories)) #Print highest calorie total for the elves.

#Part 2
elf_calories.sort()
print(sum(elf_calories[:-4:-1])) # Sorts the calories, lowest to highest. Then returns the sum of the last(read highest) 3 elves.
