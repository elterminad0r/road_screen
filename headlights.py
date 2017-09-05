def coord_to_pix(x, y):
    return y * width + x

def draw_headlights(d, b):
    loadPixels()
    for x in range(width / 2 - d, width / 2 + d):
        for y in range(height - d, height):
            l_d = dist(x, y, width / 2, height)
            if l_d < d:
                c = color(map(l_d, 0, d, b, 0))
                pixels[coord_to_pix(x, y)] = c
    updatePixels()