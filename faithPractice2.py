from visual import *
from visual.graph import *

start = -20.0
stop = 20.0
step = 0.01

fnc1 = gcurve(color = color.green)

for x in arange (start, stop, step):
    y = x**2 - 2
    fnc1.plot(pos=(x,y))
