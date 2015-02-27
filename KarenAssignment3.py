from visual import *
from visual.graph import *

Planet = sphere(pos=(2,3,0),radius = 0.5, color = (0,1,1))
Planet.velocity = vector(1,-1,0)
PlanetMass = 3
Planet.trail = curve(color = Planet.color)

Star = sphere(pos=(0,0,0), radius = 1, color = (1,1,0))
Star.velocity = vector(0,0,0)
StarMass = 5

t = 0
delta = 0.001

while t < 1000:
    Distance = sqrt((Planet.pos.x - Star.pos.x)**2 + (Planet.pos.y - Star.pos.y)**2)
    Force = - (StarMass*PlanetMass)/Distance**2
    Fx = Force * (Planet.pos.x - Star.pos.x)/Distance
    Fy = Force * (Planet.pos.y - Star.pos.y)/Distance
    Ax = Fx/PlanetMass
    Ay = Fy/PlanetMass
    Planet.velocity.x = Planet.velocity.x + Ax*delta
    Planet.velocity.y = Planet.velocity.y + Ay*delta
    Planet.pos.x = Planet.pos.x + Planet.velocity.x*delta
    Planet.pos.y = Planet.pos.y + Planet.velocity.y*delta
    Planet.trail.append(pos=Planet.pos)
    t = t + delta





