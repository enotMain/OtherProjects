from numpy import *
from matplotlib.pyplot import *

t = arange(-1, 1, 0.01)

w = 2 * pi
y = sin(w * t)
figure(1)
plot(t, y, color='cyan')
grid(True)
title('w = 2pi')
savefig('21_3_1.png')

w += pi
y = sin(w * t)
figure(2)
plot(t, y, color='blue')
grid(True)
title('w = 3pi')
savefig('21_3_2.png')

w += pi
y = sin(w * t)
figure(3)
plot(t, y, color='green')
grid(True)
title('w = 4pi')
savefig('21_3_3.png')

w += pi
y = sin(w * t)
figure(4)
plot(t, y, color='red')
grid(True)
title('w = 5pi')
savefig('21_3_4.png')

w += pi
y = sin(w * t)
figure(5)
plot(t, y, color='orange')
grid(True)
title('w = 6pi')
savefig('21_3_5.png')

w += pi
y = sin(w * t)
figure(6)
plot(t, y, color='yellow')
grid(True)
title('w = 7pi')
savefig('21_3_6.png')

w += pi
y = sin(w * t)
figure(7)
plot(t, y, color='brown')
grid(True)
title('w = 8pi')
savefig('21_3_7.png')

show()