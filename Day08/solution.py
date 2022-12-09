
with open('./Day08/input.txt', 'r') as f:
    file = f.readlines()

def parse_data(data):
    '''
    Creates a 2D list and creates tuples
    Tuples represent: Height, Horizontal Vis, Vertical Vis
    '''
    grid = []
    for line in data:
        row = []
        for num in line.strip():
            row.append((num, False, False))
        grid.append(row)
    return grid

def check_vis(tuple_list):
    check_tree_height_lr(tuple_list)
    check_tree_height_rl(tuple_list)
    revlist = reverse_2d_list(tuple_list)
    revlist = check_tree_height_tb(revlist)
    revlist = check_tree_height_bt(revlist)
    revlist = reverse_2d_list(revlist)
    return revlist

def change_row_vis(row):
    for n, t in enumerate(row):
        row[n] = change_vis_h(t)
        row[n] = change_vis_v(row[n])
        
def check_tree_height_lr(tuple_list):
    for i, r in enumerate(tuple_list):
        # print(i, r)
        tallest_so_far = '-'
        if r == tuple_list[0] or r == tuple_list[-1]:
            change_row_vis(r) #Swaps entire row to true
            continue #First/last row is always visible
        for n, t in enumerate(r):
            tallest = max(r)
            prev_tuple = '-'
            if t[0]  > prev_tuple and t[0] > tallest_so_far:
                tallest_so_far = t[0]
                prev_tuple = t[0]
                r[n] = change_vis_h(t)
                if t == tallest:
                    break

def check_tree_height_rl(tuple_list):
    for i, r in enumerate(tuple_list):
        # print(i, r)
        tallest_so_far = '-'
        if r == tuple_list[0] or r == tuple_list[-1]:
            continue # Row already changed
        for n, t in reversed(list(enumerate(r))): # Reversed List
            tallest = max(r)
            prev_tuple = '-'
            if t[0]  > prev_tuple and t[0] > tallest_so_far:
                tallest_so_far = t[0]
                prev_tuple = t[0]
                r[n] = change_vis_h(t)
                if t == tallest:
                    break
        
def check_tree_height_tb(revlist):
    for i, r in enumerate(revlist):
        # print(i, r)
        tallest_so_far = '-'
        for n, t in enumerate(r):
            tallest = max(r)
            prev_tuple = '-'
            if t[0]  > prev_tuple and t[0] > tallest_so_far:
                tallest_so_far = t[0]
                prev_tuple = t[0]
                r[n] = change_vis_v(t)
                if t == tallest:
                    break
    return revlist

def check_tree_height_bt(revlist):
    for i, r in enumerate(revlist):
        # print(i, r)
        tallest_so_far = '-'
        for n, t in reversed(list(enumerate(r))): # Reversed List
            tallest = max(r)
            prev_tuple = '-'
            if t[0]  > prev_tuple and t[0] > tallest_so_far:
                tallest_so_far = t[0]
                prev_tuple = t[0]
                r[n] = change_vis_v(t)
                if t == tallest:
                    break
    return revlist

def reverse_2d_list(tuple_list):
    rev_2d_list = []
    for i, r in enumerate(tuple_list):
        column = []
        for n, t in enumerate(r):
            column.append(tuple_list[n][i])
        rev_2d_list.append(column)
    return rev_2d_list

def change_vis_h(tup):
    return (tup[0], True, tup[2])
def change_vis_v(tup):
    return (tup[0], tup[1], True)

def num_visible(tup_list):
    total_visible = 0
    for _, r in enumerate(tup_list):
        for _, t in enumerate(r):
            if t[1] or t[2] == True:
                total_visible += 1
    return total_visible

def best_view_east(tup_list):
    for i, r in enumerate(tup_list):
        for num, t in enumerate(r):
            height = t[0]
            n,s,e,w = 0,0,0,0
            # If First/Last Row/Column - skip
            if i == 0:
                continue
            if i == len(tup_list)-1:
                continue
            if num == len(r)-1:
                continue
            if num == 0:
                continue

            # Check to East t = current tuple = r[num]
            for x, y in enumerate(r):
                if x == 0:
                    continue
                if num + x == len(r):
                    break
                e += 1
                if height > r[num+x][0]:
                    continue
                else:
                    break
                
            # print(f'Return val E: {e}')

def best_view_west(tup_list):
    for i, r in enumerate(tup_list):
        for num, t in reversed(list(enumerate(r))):
            w = 0
            height = t[0]
            if i == 0:
                continue
            if i == len(tup_list)-1:
                continue
            if num == len(r)-1:
                continue
            if num == 0:
                continue

            # Check to East t = current tuple = r[num]
            for x, y in enumerate(r):
                print(f'I: {i}, Num: {num}, X: {x}, Height: {height} TH: {r[num-x-1][0]}\nT:{t}, Y:{y}\n{r}')
                # if x == 0:
                #     continue
                # if num + x == len(r):
                #     break
                w += 1
                if height > r[num-x-1][0]:
                    continue
                else:
                    break

def look_at_view(cd):
    view_n, view_e, view_s, view_w = 0,0,0,0
    traversal = c
    if c.e == None or c.w == None or c.s == None or c.n == None:
        return 0
    while True:
        view_n +=1
        if traversal.n.height >= c.height:
            break
        traversal = traversal.n
        if traversal.n == None :
            break
    traversal = c
    while True:
        view_e +=1
        if traversal.e.height >= c.height:
            break
        traversal = traversal.e
        if traversal.e == None :
            break
    traversal = c
    while True:
        view_s +=1
        if traversal.s.height >= c.height:
            break
        traversal = traversal.s
        if traversal.s == None :
            break
    traversal = c
    while True:
        view_w +=1
        if traversal.w.height >= c.height:
            break
        traversal = traversal.w
        if traversal.w == None :
            break
    traversal = c
    return (view_n*view_e*view_s*view_w)

tree_grid = parse_data(file)
vis_list = check_vis(tree_grid)

#Part 1
print(num_visible(vis_list))

#Part 2
coord_list = []
for i, r in enumerate(vis_list):
    for n, t in enumerate(r):
        coord = (str(i) +','+ str(n))
        coord_list.append(coord)


class Grid():
    def __init__(self, name, height) -> None:
        self.name = name
        self.height = height
        self.n = None
        self.s = None
        self.e = None
        self.w = None

coord_count = 0
for i, r in enumerate(vis_list):
    for n, t in enumerate(r):
        coord_list[coord_count] = Grid(coord_list[coord_count], t[0])
        coord_count+=1

coord_count = -1
for i,r in enumerate(vis_list):
    for n, t in enumerate(r):
        coord_count +=1
        c = coord_list[coord_count]
        # print(i, c.name)
        #East:
        if coord_count+1 <= len(vis_list)*len(r)-1 and n != len(vis_list)-1:
            c.e = coord_list[coord_count+1]
        #West:
        if coord_count-1 >= 0 and n != 0:
            c.w = coord_list[coord_count-1]
        #North
        if coord_count-len(r) >= 0:
            c.n = coord_list[coord_count-len(r)]
        #South
        if coord_count+len(r) <= len(vis_list)*len(r)-1:
            c.s = coord_list[coord_count+len(r)]
        # try:
        #     print(c.name, c.s.height, c.height)
        # except AttributeError as err:
        #     print(c.name, err)

coord_count = -1
best_view = []
for i, r in enumerate(vis_list):
    for n, t in enumerate(r):
        coord_count+=1
        c = coord_list[coord_count]
        best_view.append(look_at_view(c))


print(max(best_view))
    

