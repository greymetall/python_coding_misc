# -*- coding: utf-8 -*-


from random import randint

MAX_BUNCHES = 5
MAX_BUNCHE_SIZE = 10

_holder = {}
_sorted_keys = None


def put_stones():
    """ расположить камни на игровой поверхности """
    global _holder, _sorted_keys
    _holder = {}
    for i in range(1, MAX_BUNCHES + 1):
        _holder[i] = randint(1, MAX_BUNCHE_SIZE)
    _sorted_keys = sorted(_holder.keys())


def take_from_bunch(position, quantity):
    """ взять камни из кучи """
    if position.isdigit() & quantity.isdigit():
        position, quantity = int(position), int(quantity)
        if position in _holder:
            if (0 < quantity <= 3) & (_holder[position] >= quantity):
                _holder[position] -= quantity
                return True
    else:
        return False


def get_bunches():
    """ текущее расположение камней (возвращает список) """
    res = []
    for key in _sorted_keys:
        res.append(_holder[key])
    return res


def is_game_over():
    """ конец игры """
    return sum(_holder.values()) == 0
