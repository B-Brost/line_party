""" 
line_party.py
Brianna Brost
10/21/2022
This program creates a random number of points and connects them with lines. The points move around the screen and bounce off the walls. The lines are drawn in a random color and the background is a light blue.
"""
# set up canvas
from random import random, randint
import dudraw
dudraw.set_canvas_size(500, 500)
dudraw.clear(dudraw.WHITE)
# prepare lists
x_points = []
y_points = []
x_speed=[]
y_speed=[]
# make random points
for k in range(10):
    x_points.append(random())
    y_points.append(random())
    x_speed.append(random()*.03)
    y_speed.append(random()*.03)
# entire animation loop
while True:
    # prepare pen
    dudraw.clear_rgb(30,80,200)
    dudraw.set_pen_width(.005)
    dudraw.set_pen_color_rgb(randint(0,255), randint(0,255), randint(0,255))
    # draw lines
    for i in range(9):
        if i < 8:
            dudraw.line(x_points[i], y_points[i], x_points[i+1], y_points[i+1])
        else:
            dudraw.line(x_points[i], y_points[i], x_points[0], y_points[0])
# animate lines
    for j in range(len(x_points)):
        x_points[j]+=x_speed[j]
        y_points[j]+=y_speed[j]
    # bounce
    for j in range(len(x_points)):
        if x_points[j] >= 1 or x_points[j] <= 0:
            x_speed[j] *= -1
        if y_points[j] >= 1 or y_points[j] <= 0:
            y_speed[j] *= -1
    dudraw.show(100)
dudraw.show(float('inf'))

