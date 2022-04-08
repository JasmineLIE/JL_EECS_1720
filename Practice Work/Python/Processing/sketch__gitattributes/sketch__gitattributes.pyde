c, d = None, None

def setup():
  size(800, 800)
  global c, d, x1, y1, x2, y2
  c= color(random(255), random(255), random(255))
  d= color(random(255), random(255), random(255))


def draw():
  global c, d, x1, y1, x2, y2
  for x in range(width): # loop through every x
    for y in range(height):
        p = lerpColor(c, d, 1.0 * x/width + y/width)

        stroke(p)
        line(x, 0, y, width)


def mousePressed():
  global c, d
  c= color(random(255), random(255), random(255))
  d= color(random(255), random(255), random(255))
