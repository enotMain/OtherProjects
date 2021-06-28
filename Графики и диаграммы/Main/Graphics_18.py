from numpy import *
from matplotlib.pyplot import *

x = arange(-10, 10, 0.1)
y = 4 * sin(pi * x + pi / 8) - 1
plot(x, y)
show()