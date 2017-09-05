from Sky import Sky
from House import House, extend_line
from headlights import draw_headlights
from stripes import draw_stripes, STRIPE_LENGTH

DRAW_DIST = 20
MAX_W = 6

def setup():
    global sky, stripe_offset
    size(800, 800, P2D)
    sky = Sky(100, height / 2 + 3)
    stripe_offset = 0
    
    ext_y_l = extend_line(width / 2 + 200, 0, width / 2, height / 2, width)
    house_dst = 0
    while house_dst + MAX_W < DRAW_DIST:
        house_dst += random(1, 2)
        w = random(3, MAX_W)
        ext_y_h = extend_line(width / 2 + 200, random(400, 700), width / 2, height / 2, width)
        House(house_dst, w, random(500, 600), width, ext_y_l, width, ext_y_h, width / 2, height / 2, DRAW_DIST, MAX_W)
        house_dst += w

    ext_y_l = extend_line(width / 2 - 200, 0, width / 2, height / 2, 0)
    house_dst = 0
    while house_dst + MAX_W < DRAW_DIST:
        house_dst += random(1, 2)
        w = random(3, MAX_W)
        ext_y_h = extend_line(width / 2 - 200, random(400, 700), width / 2, height / 2, 0)
        House(house_dst, w, -random(500, 600), 0, ext_y_l, 0, ext_y_h, width / 2, height / 2, DRAW_DIST, MAX_W)
        house_dst += w

def draw():
    global stripe_offset
    background(0)
    
    draw_headlights(150, 100)
    
    stripe_offset += 0.03
    if stripe_offset > STRIPE_LENGTH * 2:
        stripe_offset = 0
        
    translate(0, height)
    scale(1, -1)
    
    stroke(255)
    line(0, height / 2, width, height / 2)
    line(width / 2 - 200, 0, width / 2, height / 2)
    line(width / 2 + 200, 0, width / 2, height / 2)
    
    noStroke()
    fill(255)
    sky.draw()
    
    House.update()
    fill(0)
    stroke(255)
    House.draw_sides()
    House.draw()
    
    fill(255)
    noStroke()
    draw_stripes(width / 2 - 15, 0,
                 width / 2 + 15, 0,
                 width / 2, height / 2,
                 stripe_offset, DRAW_DIST)