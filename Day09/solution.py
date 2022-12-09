class Rope:
    def __init__(self) -> None:
        self.pos = ['0,0']
        self.x = 0
        self.y = 0

    def update_pos(self):
        self.pos.append(f'{self.x},{self.y}')

    #Logic for unidirectiona movement by lead rope
    def move_r(self):
        self.y += 1
        self.update_pos()
    def move_l(self):
        self.y -= 1
        self.update_pos()
    def move_u(self):
        self.x += 1
        self.update_pos()
    def move_d(self):
        self.x -= 1
        self.update_pos()

    #Logic for diagonal moves // Used for following
    def move_ur(self):
        self.y +=1
        self.x +=1
        self.update_pos()
    def move_dr(self):
        self.y += 1
        self.x -= 1
        self.update_pos()
    def move_ul(self):
        self.x += 1
        self.y -= 1
        self.update_pos()
    def move_dl(self):
        self.x -= 1
        self.y -= 1
        self.update_pos()

    def  follow(self, lead): #Logic for following rope to use.
        if lead.x - self.x > 1 and  lead.y - self.y > 0 or lead.x - self.x > 0 and  lead.y - self.y > 1:
            self.move_ur()
        elif lead.x - self.x > 1 and lead.y - self.y < 0 or lead.x - self.x > 0 and lead.y - self.y < -1:
            self.move_ul()
        elif lead.x - self.x < -1 and  lead.y - self.y > 0 or lead.x - self.x < 0 and  lead.y - self.y > 1:
            self.move_dr()
        elif lead.x - self.x < -1 and lead.y - self.y < 0 or lead.x - self.x < 0 and lead.y - self.y < -1:
            self.move_dl()
        if lead.y - self.y < -1 and lead.x - self.x == 0:
            self.move_l()
        elif lead.y - self.y > 1 and lead.x - self.x == 0:
            self.move_r()
        elif lead.x - self.x < -1 and lead.y - self.y == 0:
            self.move_d()
        elif lead.x - self.x > 1 and lead.y - self.y == 0:
            self.move_u()

with open('./Day09/input.txt', 'r') as f:
    data = f.readlines()

def trace_path(data, ropes):
    r = [Rope() for x in range(ropes)]
    for line in data:
        instruction = line.strip().lower().split()
        for _ in range(int(instruction[1])):
            eval('r[0].move_' + instruction[0] + '()')
            for rope in range(1, ropes):
                eval(f'r[{rope}].follow(r[{rope-1}])')
    finalrope = (eval(f'r[{ropes-1}].pos'))
    return {len(set(finalrope))}

print(f'Part 1: The tail visited {trace_path(data, 2)} unique positions.')
print(f'Part 2: The final tail visited {trace_path(data, 10)} unique positions.')
