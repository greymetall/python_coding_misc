# -*- coding: utf-8 -*-

# Отрисовка стены с узором. Размер кирпича - 100х50


import simple_draw as sd

sd.background_color = sd.COLOR_DARK_ORANGE
sd.resolution = (1200, 600)


def brick(x, y, height, width, color):
    start_point = sd.get_point(x, y)
    x1 = x + width
    y1 = y + height
    end_point = sd.get_point(x1, y1)
    sd.rectangle(left_bottom=start_point, right_top=end_point, color=color, width=width_line)


brick_height, brick_width = 50, 100
for y in range(0, sd.resolution[1] + 1, brick_height):
    for x in range(-brick_width // 2, sd.resolution[0] + brick_width // 2 + 1, brick_width):
        x_ = x if not y % (2 * brick_height) else x + brick_width // 2
        width_line = 2 if (-x_ + brick_width // 2 + y) % 50 or (-x_ + brick_width // 2 + y) % 150 else 0
        brick(x=x_, y=y, height=brick_height, width=brick_width, color=sd.COLOR_CYAN)

sd.pause()
