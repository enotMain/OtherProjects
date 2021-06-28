from numpy import *
from matplotlib . pyplot import *
from mpl_toolkits . mplot3d import Axes3D

x = arange(-3, 3, 0.1)
y = arange(-3, 3, 0.1)

X, Y = meshgrid(x, y)

Z = sqrt(X**2 + Y**2)

contourf(X, Y, Z)
savefig('23_contour.png')

fig = figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z, color='red')
savefig('23_3D.png')

show ()