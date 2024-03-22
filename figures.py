from turtle import *


def figure_circle(x):
    circle(x['radius'])

def figure_snowflake(x):
    forward(x['distance']*2)
    for i in range(x['repeat']):
        backward(x['distance'])
        right(x['angle'])
        forward(x['distance'])
        backward(x['distance'])
        left(x['angle'])
        backward(x['distance'])
        right(x['angle'])
        forward(x['distance']*2)
        backward(x['distance']*2)
        right(x['angle'])
        forward(x['distance'])
        left(x['angle'])
        forward(x['distance'])
        backward(x['distance'])
        right(x['angle'])
        forward(x['distance'])
    backward(x['distance']*2)
