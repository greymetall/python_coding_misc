# -*- coding: utf-8 -*-

# Функия отрисовки рандомных смайликов в произвольной точке экрана
# Форма рожицы-смайлика - рандомная
# Смайлы создаются рекурсивно, заполняя всё пространство экрана
# Наложения смайлов друг на друга исключены!)


import simple_draw as sd

sd.resolution = (1200, 600)
sd.background_color = (245, 240, 240)


def smile(point, color):
    # голова смайла
    x = point.x
    y = point.y
    if x < 90:
        x = 90
    elif point.x > 1110:
        x = 1110
    if y < 80:
        y = 80
    elif y > 520:
        y = 520
    # point = sd.get_point(x, y)
    random_delta_x = sd.random_number(50, 90)
    random_delta_y = sd.random_number(40, random_delta_x - 10)
    x_left = x - random_delta_x
    if x_left < 0:
        x_left = 0
    x_right = x + random_delta_x
    if x_right > 1200:
        x_right = 1200
    y_top = y + random_delta_y
    if y_top > 600:
        y_top = 600
    y_bottom = y - random_delta_y
    if y_bottom < 0:
        y_bottom = 0
    left_bottom = sd.get_point(x=x_left, y=y_bottom)
    right_top = sd.get_point(x=x_right, y=y_top)
    color = sd.random_color()

    # отрисовка с условием чтоб смайлы не накладывались друг на друга
    if not dict_used_points:
        dict_used_points.setdefault((0, 0), (0, 0))
    for key, value in dict_used_points.items():
        if0 = (key[0] < left_bottom.x < value[0]) & (key[1] < left_bottom.y < value[1])
        if1 = (left_bottom.x >= value[0]) or (left_bottom.y >= value[1])
        if2 = (right_top.x <= key[0]) or (right_top.y <= key[1])
        if if0 or all([not if1, not if2]):
            return smile(point=sd.random_point(), color=None)

    sd.ellipse(left_bottom, right_top, color=color, width=2)
    dict_used_points.setdefault((left_bottom.x, left_bottom.y), (right_top.x, right_top.y))

    # глаза
    center_left_eye = sd.get_point(x=x_left + sd.random_number(30, 40),
                                   y=y_top - sd.random_number(30, 35))
    radius_left_eye = sd.random_number(7, 10)
    # width_left_eye = sd.random_number(2, 4) * sd.random_number(0, 1)
    center_right_eye = sd.get_point(x=x_right - sd.random_number(30, 40),
                                    y=y_top - sd.random_number(30, 35))
    radius_right_eye = sd.random_number(7, 10)
    # widht_right_eye = sd.random_number(2, 4) * sd.random_number(0, 1)
    sd.circle(center_position=center_left_eye, radius=radius_left_eye, color=color, width=sd.random_number(0, 2))
    sd.circle(center_position=center_right_eye, radius=radius_right_eye, color=color, width=sd.random_number(0, 2))

    # рот
    point1 = sd.get_point(x=x_left + sd.random_number(20, 40),
                          y=y_bottom + sd.random_number(30, 40))
    point2 = sd.get_point(x=x_left + sd.random_number(40, 50),
                          y=y - random_delta_y + sd.random_number(15, 25))
    point3 = sd.get_point(x=x + sd.random_number(-10, 10),
                          y=y_bottom + sd.random_number(20, 30))
    point4 = sd.get_point(x=x_right - sd.random_number(40, 50),
                          y=y_bottom + sd.random_number(15, 25))
    point5 = sd.get_point(x=x_right - sd.random_number(20, 40),
                          y=y_bottom + sd.random_number(30, 45))

    points = [point1, point2, point3, point4, point5]
    random_points_list1 = points[0:sd.random_number(2, 5)]
    random_points_list2 = points[sd.random_number(0, 3):5]
    random_points_list3 = points[::2]
    random_points_list4 = points[1::2]
    random_points_list = sd.choice([random_points_list1, random_points_list2, random_points_list3, random_points_list4])
    closed = sd.choice([True, False])
    sd.lines(point_list=random_points_list, color=color,
             closed=closed, width=sd.random_number(1, 4))


# smile(X=sd.random_number(70,1140), Y=sd.random_number(50,550), color=None)
dict_used_points = dict()

for _ in range(25):
    smile(point=sd.random_point(), color=None)
    # print(dict_used_points)

sd.pause()
