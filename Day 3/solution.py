# Open file and strip of new lines.
with open('../../Day 3/input.txt', 'r') as file:
    data = [line.strip('\n') for line in file.readlines()]

#Part 1 - find duplicates in each pack
duplicates = []
for line in data:
    dup = None
    size = int(len(line)/2)
    pack1 = line[:size]
    pack2 = line[size:]

    for item in pack1:
        if item in pack2:
            dup = item
    duplicates.append(dup)

#Function to return the appraised value of items in a list.
def appraise_value(pack):
    appraised_value = 0
    for item in pack:
        item_value = 0
        if ord(item) > 64 and ord(item) < 91:
            item_value += ord(item) - 38
        elif ord(item) > 96 and ord(item) < 123:
            item_value += ord(item) - 96
        else:
            print("Something went wrong")
        appraised_value += item_value
    return appraised_value

#Part 2
groups = []
group_count = 0
elf_count = 1
for line in data:
    if len(groups) == group_count:
        groups.append([])
    if elf_count < 3:
        groups[group_count].append(line)
        elf_count += 1
    elif elf_count == 3:
        groups[group_count].append(line)
        group_count += 1
        elf_count = 1

badge_sticker = []
for group in groups:
    for char in group[0]:
        if char in group[1] and char in group[2]:
            badge_sticker.append(char)
            break

print(appraise_value(duplicates))
print(appraise_value(badge_sticker))
