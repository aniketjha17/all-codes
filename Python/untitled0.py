# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 09:43:56 2018

@author: Aniket-Jha
"""

import turtle
t = turtle.Pen()
turtle.bgcolor("tomato")
t.speed(0)
#list color
colors = ["red", "yellow", "blue", "green"]
for x in range(350):
    t.pencolor( colors[ x % 4] )
    t.forward(2*x)
    t.left(100)