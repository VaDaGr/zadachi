from math import pi
def weight(r, h):
    return round((pi*r**2*h) / 1000, 2)

print(weight(6, 29))