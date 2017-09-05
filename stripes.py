STRIPE_LENGTH = 0.5

def _atan_erp(d, x, y, hx, hy):
    total_length = dist(x, y, hx, hy)
    distance = atan(d) / HALF_PI
    return lerp(x, hx, distance), lerp(y, hy, distance)

atan_memo = {}

def atan_erp(*args):
    if args in atan_memo:
        return atan_memo[args]
    else:
        res = _atan_erp(*args)
        atan_memo[args] = res
        return res

def draw_stripe(d, length_, lx, ly, rx, ry, hx, hy):
    beginShape()
    vertex(*atan_erp(d, lx, ly, hx, hy))
    vertex(*atan_erp(d + length_, lx, ly, hx, hy))
    vertex(*atan_erp(d + length_, rx, ry, hx, hy))
    vertex(*atan_erp(d, rx, ry, hx, hy))
    endShape(CLOSE)

def draw_stripes(lx, ly, rx, ry, hx, hy, offset, draw_dist):
    for d in xrange(0, draw_dist, int(STRIPE_LENGTH * 2)):
        draw_stripe(d - offset, STRIPE_LENGTH, lx, ly, rx, ry, hx, hy)

#TODO kaleidoscope random