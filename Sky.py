class Sky(object):
    def __init__(self, stars, min_h):
        self.stars = [(random(width), random(min_h, height), random(1, 2)) for _ in xrange(stars)]
    
    def draw(self):
        for x, y, r in self.stars:
            ellipse(x, y, r * 2, r * 2)