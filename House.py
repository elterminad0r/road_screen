from stripes import draw_stripe, atan_erp
from collections import deque

def extend_line(x, y, hx, hy, tx):
    return hy + (y - hy) * (tx - hx) / (x - hx)
    
def apply_to(l):
    def to_all(func):
        def f():
            for i in list(l):
                func(i)
        return f
    return to_all

class House(object):
    inst = deque()
    
    def __init__(self, d, w, depth, lx, ly, rx, ry, hx, hy, draw_dist, max_w):
        self.w = w
        self.depth = depth
        self.lx = lx
        self.ly = ly
        self.rx = rx
        self.ry = ry
        self.hx = hx
        self.hy = hy
        self.max_w = max_w
        
        self.draw_dist = draw_dist
        self.offset = draw_dist - d
        
        House.inst.appendleft(self)
    
    @staticmethod
    @apply_to(inst)
    def draw_sides(self):
        d = self.draw_dist - self.offset
        beginShape()
        vertex(*atan_erp(d, self.lx, self.ly, self.hx, self.hy))
        vertex(*atan_erp(d, self.rx, self.ry, self.hx, self.hy))
        vertex(*atan_erp(d, self.rx + self.depth, self.ry, self.hx, self.hy))
        vertex(*atan_erp(d, self.lx + self.depth, self.ly, self.hx, self.hy))
        endShape(CLOSE)
    
    @staticmethod
    @apply_to(inst)
    def update(self):
        self.offset += 0.03
        if self.offset - self.max_w > self.draw_dist:
            self.offset = 0
            House.inst.append(House.inst.popleft())
    
    @staticmethod
    @apply_to(inst)
    def draw(self):
        draw_stripe(self.draw_dist - self.offset, self.w, self.lx, self.ly, self.rx, self.ry, self.hx, self.hy)
