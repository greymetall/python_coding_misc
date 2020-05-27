# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

sd.background_color = sd.COLOR_DARK_ORANGE
sd.resolution = (800, 800)


def cell(x, y):
    cell_point = sd.get_point(x, y)
    sd.square(left_bottom=cell_point, side=side, color=color, width=filling_cell)


side = 100
filling_cell = 0
for y in range(0, side * 8 + 1, side):
    for x in range(0, side * 8 + 1, side):
        color = sd.COLOR_DARK_ORANGE if (x + y) % 200 else sd.COLOR_WHITE
        cell(x=x, y=y)

sd.pause()
