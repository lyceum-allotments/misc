import math
import numpy as np
import matplotlib.pyplot as plt

x = 0.0
y = 0.0
dn_x = 1
dn_y = 0

def setheading(angle):
    global dn_x, dn_y

    dn_x = math.cos(angle * math.pi / 180.)
    dn_y = math.sin(angle * math.pi / 180.)


def forward(distance):
    global x, y
    x += float(distance) * dn_x
    y += float(distance) * dn_y

def position():
    return (x, y)

def setposition(new_x, new_y):
    global x, y
    x = new_x
    y = new_y

def exitonclick():
    return

def hist2d(data, bins):
    data = np.array(data)
    x = data[:,0]
    y = data[:,1]

    plt.hist2d(x, y, bins)
    plt.colorbar()

