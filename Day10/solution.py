class CPU():
    def __init__(self) -> None:
        self.signal_strength = []
        self.cycle = 1
        self.x = 1

    def read_instruction(self, instruction, crt):
        if instruction == 'noop':
            self.cycle_check(instruction, crt)
            self.cycle += 1
            return
        else:
            self.cycle_check(instruction, crt)
            self.cycle += 1
            self.cycle_check(instruction, crt)
            self.cycle += 1
            self.x += int(instruction.split(' ')[1])

    def cycle_check(self, ins, crt):
        sprite = [self.x-1, self.x, self.x+1]
        crt.draw(sprite)
        if self.cycle < 221:
            if (self.cycle - 20) % 40 == 0:
                self.signal_strength.append(self.cycle * self.x)
                # print(self.cycle, self.x, ins)

class CRT():
    def __init__(self) -> None:
        self.display = ''
        self.pos = 0
    
    def draw(self, sprt):
        if self.pos in sprt:
            self.display += '#'
        else:
            self.display += '.'
        if self.pos == 39:
            self.pos = 0
        else:
            self.pos +=1
        


cpu = CPU()
screen = CRT()

with open('./Day10/input.txt', 'r') as f:
    data = f.readlines()
    for line in data:
        cpu.read_instruction(line.strip(), screen)

print(f'The sum of the signal strength is: {sum(cpu.signal_strength)}')

print(screen.display[0:39])
print(screen.display[40:79])
print(screen.display[80:119])
print(screen.display[120:159])
print(screen.display[160:199])
print(screen.display[200:239])
