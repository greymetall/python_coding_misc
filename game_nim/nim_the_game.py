# -*- coding: utf-8 -*-

# Ним — математическая игра, в которой два игрока по очереди берут предметы,
# разложенные на несколько кучек. За один ход может быть взято любое количество предметов
# (большее нуля) из одной кучки. Выигрывает игрок, взявший последний предмет.
# В классическом варианте игры число кучек равняется трём.

# Составить модуль, реализующий функциональность игры.
# Функции управления игрой
#  разложить_камни()
#  взять_из_кучи(NN, KK)
#  положение_камней() - возвращает список [XX, YY, ZZ, ...] - текущее расположение камней
#  есть_конец_игры() - возвращает True если больше ходов сделать нельзя
#
# В текущем модуле реализовать логику работы с пользователем:
#  начало игры,
#  вывод расположения камней
#  ввод первым игроком хода - позицию и кол-во камней
#  вывод расположения камней
#  ввод вторым игроком хода - позицию и кол-во камней
#  вывод расположения камней


from nim_engine import put_stones, get_bunches, is_game_over, take_from_bunch
from termcolor import cprint, colored

put_stones()
user_number = 1
while True:
    cprint('Текущая позиция', color='cyan')
    cprint(get_bunches(), color='green')
    user_color = 'blue' if user_number == 1 else 'magenta'
    cprint('Ход игрока {}'.format(user_number), color=user_color, attrs=['underline'])
    pos = input(colored('Откуда берем?', color=user_color))
    qua = input(colored('Сколько берем?', color=user_color))
    step_successed = take_from_bunch(position=pos, quantity=qua)
    if step_successed:
        user_number = 2 if user_number == 1 else 1
    else:
        cprint('Невозможный ход!', color='red')
    if is_game_over():
        break

cprint('Выиграл игрок номер {}'.format(user_number), color='red', attrs=['bold', 'underline', 'reverse'])
