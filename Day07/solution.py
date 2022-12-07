with open('./Day07/input.txt', 'r') as file:
    data = file.readlines()

filesystem = {}
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
    elif '$ cd' in line: #Adds the current directory string to the new path and appends to directory list
        cur_dir.append(str(cur_dir[-1]) + '/' + str(line.strip().split(' ')[2]))
        # print(line.strip().split(' ')[2])
    elif 'dir ' in line: #Creates a directory with a value of 0
        path = tuple(cur_dir[-1].split('/'))
        filesystem.update({path: filesystem.get(path, 0)})
    else: #Creates/adds size of contents to directory
        # print(line.strip(), tuple(cur_dir[-1].split('/')))
        size = line.strip().split(' ')[0]
        path = tuple(cur_dir[-1].split('/'))
        try:
            size = int(size)
            filesystem.update({path: filesystem.get(path, 0)+size})
        except TypeError as err:
            print("Unexpected input: ", err)

file_totals = {}
# print(filesystem)
for k, v in filesystem.items():
    #Adds the total values for each directory
    file_totals[k] = file_totals.get(k, 0)+v

for k, v in file_totals.items():
    # print(f'{k} | {v}')
    if len(k) > 1:
        cap = k[0:(len(k)-1)]
        # print(f'K = {k}, V = {v}')
        # print(f'Cap: {cap} File: {file_totals.get(cap)} V:{v}')
        try:
            file_totals.update({cap:file_totals.get(cap)+v})
        except TypeError as err:
            print("Error: ", err)
        while len(cap) > 1:
            cap = cap[0:(len(cap)-1)]
            file_totals.update({cap:file_totals.get(cap)+v})

acc = 0
for data in file_totals.values():
    # Adds the total of files that are <= 100000
    if int(data) <= 100000:
        acc += data
print(f'The sum of directories of at most 100000: {acc}')


#Part 2
used_space = file_totals[('root',)]

totalspace = 70000000
update_space = 30000000
unused_space = totalspace - used_space
needed_space = update_space - unused_space

delete_list = []
for data in file_totals.values():
    # print(unused_space, update_space, update_space-unused_space)
    if int(data) > needed_space:
        delete_list.append(data)

print(f'The smallest directory that would free enough space is: {min(delete_list)}')
