from numpy import *
from matplotlib.pyplot import *

t = arange(-7, 7, 0.2)
y = 4 * sin(pi * t + pi / 8) - 1
plot(t, y, ':o', color='red')
savefig('19.png')
show()