from turtle import *


# Круг
def figure_circle(x): circle(x['radius'])

# Снежинка
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

# Квадрат
def figure_square(x):
	for i in range(x['repeat']):
		forward(x['distance'])
		left(x['angle'])

# Квадрат с перемещением вперед
def figure_SHIFTsquare(x):
	for i in range(x['repeat']):
		forward(x['distance'])
		left(x['angle'])
	forward(x['distance'])
