import operator
import numpy as np

class Monkey:
    def __init__(self, items, operation, test, tr, fal) -> None:
        self.items = items
        self.operation = operation
        self.test = test
        self.inspected = 0
        self.true = tr
        self.false = fal
    
    def relieve_worry(self):
        self.items[0] = self.items[0] // 3

    def inspect_item(self):
        x = op_dict[self.operation[0]]
        if self.operation[1] == 'old':
            self.items[0] = x(int(self.items[0]), int(self.items[0]))
        else:
            self.items[0] = x(int(self.items[0]), int(self.operation[1]))
        self.inspected +=1
        # print(self.items[0])

    def throw_test(self):
        if int(self.items[0]) % int(self.test) == 0:
            self.items[0] = self.items[0] % rslt_lcm #Comment out for P1
            return True
        else:
            return False

    def throw_item(self, list, condition):
        if condition is True:
            list[self.true].items.append(self.items[0])
            del self.items[0]
        elif condition is False:
            list[self.false].items.append(self.items[0])
            del self.items[0]



def parse_monkeys(file_data):
    item_list = []
    op = None
    test = None
    tr = None
    fal = None
    for line in file_data:
        if 'Monkey' in line:
            monkeys.append(None)
        if 'Starting ' in line:
            #Splits Text From Numbers, and splits numbers into a list
            item_list = line.strip().split(":")[1].replace(',', '').split()
            # print(item_list)
        if 'Operation:' in line:
            op = line.strip().split('=')[1].split()
            del op[0]
        if 'Test:' in line:
            test = line.strip().split('by ')[1]
            lcm_list.append(int(test))
        if 'true' in line:
            tr = int(line.strip()[-1])
        if 'false' in line:
            fal = int(line.strip()[-1])

        monkeys[-1] = Monkey(item_list, op, test, tr, fal)



with open('./Day11/input.txt', 'r') as f:
    data = f.readlines()

monkeys = []
op_dict = {'+' : operator.add, '-' : operator.sub, '*':operator.mul, '/': operator.truediv}
lcm_list = []
parse_monkeys(data)

gvn_arr = np.array(lcm_list)
rslt_lcm = np.lcm.reduce(gvn_arr)
# print("The lcm of given array elements = ", rslt_lcm)

for round in range(10000):
    for m in monkeys:
        while m.items:
            m.inspect_item()
            # m.relieve_worry() #Comment Out for P2
            m.throw_item(monkeys, m.throw_test())

total_inspections = []
for m in monkeys:
    total_inspections.append(m.inspected)
total_inspections.sort(reverse=True)
print(total_inspections, 'Target: 99, 97, 8, 103')
print(total_inspections[0]*total_inspections[1])
