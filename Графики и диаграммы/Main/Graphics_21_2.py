from numpy import *
from matplotlib.pyplot import *

t = arange(-1, 1, 0.01)

w = 2 * pi
y = sin(w * t)
subplot(3, 3, 1)
grid(True)
title('w = 2pi')
plot(t, y, color='cyan')

w += pi
y = sin(w * t)
subplot(3, 3, 2)
grid(True)
title('w = 3pi')
plot(t, y, color='blue')


w += pi
y = sin(w * t)
subplot(3, 3, 3)
grid(True)
title('w = 4pi')
plot(t, y, color='green')


w += pi
y = sin(w * t)
subplot(3, 3, 4)
grid(True)
title('w = 5pi')
plot(t, y, color='red')


w += pi
y = sin(w * t)
subplot(3, 3, 5)
grid(True)
title('w = 6pi')
plot(t, y, color='orange')


w += pi
y = sin(w * t)
subplot(3, 3, 6)
grid(True)
title('w = 7pi')
plot(t, y, color='yellow')


w += pi
y = sin(w * t)
subplot(3, 3, 7)
grid(True)
title('w = 8pi')
plot(t, y, color='black')


show()