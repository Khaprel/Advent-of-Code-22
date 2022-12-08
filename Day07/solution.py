'''Opens and parses data from terminal,
creating a file heiarchy to determine which folder to delete'''
with open('./Day07/input.txt', 'r', encoding='utf-8') as file:
    dir_data = file.readlines()

def parse_directory(data):
    '''Parses data into dictionary and totals size of files'''
    system = {}
    cur_dir = [''] #List of directory path
    for line in data:
        if '$ ls' in line:
            continue
        elif '$ cd ..' in line: #Removes the last directory in the path
            cur_dir.pop()
            # print(cur_dir)
        elif '$ cd /' in line: #Clears the directory and returns to root
            cur_dir.clear()
            cur_dir.append('root')
        elif '$ cd' in line: #Adds the current directory to the new path and appends to directory
            cur_dir.append(str(cur_dir[-1]) + '/' + str(line.strip().split(' ')[2]))
            # print(line.strip().split(' ')[2])
        elif 'dir ' in line: #Creates a directory with a value of 0
            path = tuple(cur_dir[-1].split('/'))
            system.update({path: system.get(path, 0)})
        else: #Creates/adds size of contents to directory
            # print(line.strip(), tuple(cur_dir[-1].split('/')))
            size = line.strip().split(' ')[0]
            path = tuple(cur_dir[-1].split('/'))
            try:
                size = int(size)
                system.update({path: system.get(path, 0)+size})
            except TypeError as err:
                print("Unexpected input: ", err)
    return system

def add_dir_val(dic):
    '''Sums up the total values for each directory'''
    totals = {}
    for k, val in dic.items():
        totals[k] = totals.get(k, 0)+val
    return totals

def add_child_val_to_parent(dic):
    '''Modifies dic in place to add the size of the child directory to the parent directory'''
    for k, val in dic.items():
        if len(k) > 1:
            cap = k[0:(len(k)-1)]
            dic.update({cap:dic.get(cap)+val})
            while len(cap) > 1:
                cap = cap[0:(len(cap)-1)]
                dic.update({cap:dic.get(cap)+val})

def sum_xsize_dir(num, dic):
    '''Returns the sum of directories <= num'''
    acc = 0
    for data in dic.values():
        if int(data) <= num:
            acc += data
    return acc


filesystem = parse_directory(dir_data)

file_totals = add_dir_val(filesystem)

add_child_val_to_parent(file_totals)

print(f'The sum of directories of at most 100000: {sum_xsize_dir(100000, file_totals)}')


#Part 2
def min_req_delete():
    '''Creates a list of directories large enough, and returns the minium'''
    delete_list = []
    for data in file_totals.values():
        # print(unused_space, update_space, update_space-unused_space)
        if int(data) > needed_space:
            delete_list.append(data)
    return min(delete_list)

used_space = file_totals[('root',)]
TOTALSPACE = 70000000
UPDATE_SPACE = 30000000
unused_space = TOTALSPACE - used_space
needed_space = UPDATE_SPACE - unused_space

print(f'The smallest directory that would free enough space is: {min_req_delete()}')
