'''
Advent Of Code
Day 05 Solution
'''
import copy #Used to deep copy

with open('./Day05/input.txt', 'r', encoding="utf-8") as file:
    data = file.readlines()
    instructions = []
    cargo = []
    for line in data: # Parse data into instruction list, or cargo list
        temp = []
        if 'move' in line:
            instructions.append(line.strip().split(' '))
        elif '1' in line:
            continue
        else:
            #Spacing to pull only the crate identifier
            for i in range(1, len(line), 4):
                temp.append(line[i])
        if len(temp) > 0:
            cargo.append(temp)

r_cargo = [] # List to rotate cargo

#Bane of my existence - Rotates and reverses cargo list, and filters out if no cargo.
for i in range(len(cargo[0])):
    temp = []
    for x in range(len(cargo)-1, -1, -1):
        if cargo[x][i] != ' ':
            temp.append(cargo[x][i])
    r_cargo.append(temp)

#Parse out words from instructions
for line in instructions:
    line.remove('move')
    line.remove('from')
    line.remove('to')

def read_instruction(ins, string):
    '''
    Function accept a nested list of instructions.
    '''
    result = copy.deepcopy(r_cargo) #Deep copy to prevent modifying in place and ruining part 2 -.-
    for instruction in ins:
        amount_to_move = int(instruction[0])
        origin =  int(instruction[1]) -1
        destination =  int(instruction[2]) -1
        #Calls function based on which part
        if string == 'p1':
            result = move_crate(result, amount_to_move, origin, destination)
        elif string =='p2':
            result = move_stack(result, amount_to_move, origin, destination)
    #Format the answer into a string - just so I can copy and paste the answer in
    ans = ''
    for line in result:
        ans += str(line[-1])
    return ans

def move_crate(cargo, amt, ori, dest):
    '''
    Function Called from Read instruction function
    Moves one crate at a time
    '''
    if amt == 1: #Moving 1 simply pops the origin and appends it to destination
        cargo[dest].append(cargo[ori].pop())
    else: # Modifies span to navigate to appropriate crate and append them to the destination.
        if len(cargo[ori])-1-amt < 0:
            span = None
        else:
            span = len(cargo[ori])-1-amt
        for crate in cargo[ori][-1:span:-1]:
            cargo[dest].append(crate)
        for i in range(amt): #Pops the necessary amount after they've been appended.
            cargo[ori].pop()
    return cargo #Returns the current cargo list to be further modified

def move_stack(cargo, amt, ori, dest):
    '''
    Function called from Read Instruction Function
    Moves an entire stack of cargo at one time
    '''
    if amt == 1: #Moving 1 simply pops the origin and appends it to destination
        cargo[dest].append(cargo[ori].pop())
    else:# Modifies span to navigate to appropriate crates and append them to the destination.
        if len(cargo[ori])-amt < 0:
            span = 0
        else:
            span = len(cargo[ori])-amt
        for crate in range(span, len(cargo[ori])):
            cargo[dest].append(cargo[ori][crate])
        for i in range(amt):
            cargo[ori].pop()
    return cargo

print(f"The top crates for part 1: {read_instruction(instructions, 'p1')}")
print(f"The top crates for part 2: {read_instruction(instructions, 'p2')}")
