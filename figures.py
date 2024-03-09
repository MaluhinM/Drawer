import turtle


def figure_circle(x):
    turtle.circle(x['radius'])

def figure_snowflake(x):
    turtle.forward(x['distance']*2)
    for i in range(x['repeat']):
        turtle.backward(x['distance'])
        turtle.right(x['angle'])
        turtle.forward(x['distance'])
        turtle.backward(x['distance'])
        turtle.left(x['angle'])
        turtle.backward(x['distance'])
        turtle.right(x['angle'])
        turtle.forward(x['distance']*2)
        turtle.backward(x['distance']*2)
        turtle.right(x['angle'])
        turtle.forward(x['distance'])
        turtle.left(x['angle'])
        turtle.forward(x['distance'])
        turtle.backward(x['distance'])
        turtle.right(x['angle'])
        turtle.forward(x['distance'])
    turtle.backward(x['distance']*2)
