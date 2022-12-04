with open("./Day04/input.txt", 'r') as file:
    data = [line.strip() for line in file]

#Function to parse the input text.
def parse_pairs(pair):
    pair_range = []
    split_pair = pair.split(',') # Separates elf pairs
    for elf in split_pair:
        tmp = elf.split('-') #Splits the individual elf assignment so a range can be generated for comparison.
        elf_assignment = []
        for i in range(int(tmp[0]), int(tmp[1])+1):
            elf_assignment.append(i)
        pair_range.append(set(elf_assignment))
    return pair_range

#Checks if either elf assignment is a subset of the other.
def check_subset(pair):
    if pair[0].issubset(pair[1]) or pair[1].issubset(pair[0]):
        return 1
    else:
        return 0

#Checks if there is any overlap by checking if there is any intersection in the sets.
def check_overlap(pair):
    overlap = set(pair[0]) & set(pair[1])
    if len(overlap) > 0:
        return 1
    else:
        return 0

processed_pairs = list(map(parse_pairs, data))
subset_pairs = sum(map(check_subset, processed_pairs))

#Part 1 Solution
print(subset_pairs)

overlaps = list(map(check_overlap, processed_pairs))
#Part 2 Solution
print(sum(overlaps))
