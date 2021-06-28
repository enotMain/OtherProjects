from numpy import *
from matplotlib.pyplot import *

t = arange(-1, 1, 0.2)

w = 2 * pi
y = sin(w * t)
plot(t, y, ':o', color='cyan')

w += pi
y = sin(w * t)
plot(t, y, ':o', color='blue')

w += pi
y = sin(w * t)
plot(t, y, ':o', color='green')

w += pi
y = sin(w * t)
plot(t, y, ':o', color='red')

w += pi
y = sin(w * t)
plot(t, y, ':o', color='orange')

w += pi
y = sin(w * t)
plot(t, y, ':o', color='yellow')

w += pi
y = sin(w * t)
plot(t, y, ':o', color='brown')

show()