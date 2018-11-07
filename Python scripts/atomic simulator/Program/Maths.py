#Random maths functions needed
import math
from Float import Float

def spherical(x,y,z):
    r = math.sqrt(x*x+y*y+z*z)
    theta = math.acos(z/r)
    phi = math.atan2(y/x)
    return r,theta,phi #radius, inclination, azimuth

def cartesian(radius, inclination, azimuth):
    r = abs(radius)
    theta = inclination%math.pi
    phi = azimuth%(math.pi*2)
    x = r*math.sin(theta)*math.cos(phi)
    y = r*math.sin(theta)*math.sin(phi)
    z = r*math.cos(theta)
    return x,y,z


