from numpy import *
from matplotlib.pyplot import *

t = arange(-1, 1, 0.01)

w = 2 * pi
y = sin(w * t)
plot(t, y, color='cyan', label='w = 2pi')

w += pi
y = sin(w * t)
plot(t, y, color='blue', label='w = 3pi')

w += pi
y = sin(w * t)
plot(t, y, color='green', label='w = 4pi')

w += pi
y = sin(w * t)
plot(t, y, color='red', label='w = 5pi')

w += pi
y = sin(w * t)
plot(t, y, color='orange', label='w = 6pi')

w += pi
y = sin(w * t)
plot(t, y, color='yellow', label='w = 7pi')

w += pi
y = sin(w * t)
plot(t, y, color='brown', label='w = 8pi')

legend(loc='best')
grid(True)
title('y = sin(w * t)')

show()