#database
import os

def get_particles():
    """Returns a dictionary of the particles by id."""
    path = os.path.dirname(os.path.abspath(os.path.curdir))
    particles = open(os.path.join(path, 'Saves', 'Particles.txt'), 'r')
    id = 0
    d = {}
    for line in particles:
        particle = eval(line)
        d[id] = particle
        id += 1

    particles.close()
    return d

def set_particles(d):
    """Writes the dictionary of particles to file.
WARNING - WIPES THE FILE FIRST"""
    path = os.path.dirname(os.path.abspath(os.path.curdir))
    particles = open(os.path.join(path, 'Saves', 'Particles.txt'), 'w')
    ids = list(d.keys())
    lines = map(lambda id:str(d[id]), ids)
    string = '\n'.join(lines)
    particles.write(string)
    particles.close()
    return 1
