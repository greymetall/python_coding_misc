# -*- coding: utf-8 -*-

# Задание:
# Представьте себе замкнутую по окружности железную дорогу.
# По ней едет поезд, последний вагон которого скреплён с первым так,
# что внутри можно свободно перемещаться между вагонами.
# Вы оказались в одном случайном вагоне и ваша задача — подсчитать их общее количество.
# В каждом вагоне можно включать или выключать свет, но начальное положение переключателей
# случайное и заранее неизвестно. Все вагоны внутри выглядят строго одинаково, окна закрыты так, что невозможно
# посмотреть наружу, движение поезда равномерное. Помечать вагоны как-либо, кроме включения или выключения света,
# нельзя. Количество вагонов конечно (не верьте заголовку).
# Алгоритм решения:
# Предложим один из возможных вариантов решения. Вам нужно включить свет в начальном вагоне, в котором вы находитесь,
# если он ещё не горит. Затем пойти в одну любую сторону до тех пор, пока не встретите вагон с работающим освещением,
# при этом обязательно считать пройденные вагоны. Выключаете в найденном вагоне свет и идёте обратно к начальному.
# Если в нём свет всё ещё горит, то повторяете операцию. Если же нет, значит вы прошли полный круг и знаете ответ.
# Код решения:


def train_gen():
    # this function generates a crazy-train with a random number of wagons
    from random import randint, choice
    global n
    n = randint(3, 1000)
    print(f'количество вагонов задано рандомно и равно {n}, но мы пока не знаем этого и попробуем вычислить...')
    train = {}
    for wagon in range(1, n + 2):
        train[wagon] = choice([True, False])
    train[1] = True
    print('зажгли свет в 1 вагоне')
    train[n + 1] = train[1]  # n + 1 вагон - это несуществующий вагон, который является на самом деле 1 вагоном
    print('наш поезд выглядит так: цифра - № вагона, True - свет в вагоне горит, False - свет не горит:')
    print(train)
    print(f'где {n + 1} вагон - это и есть 1 вагон, т.к. поезд замкнут в кольцо')
    print(locals())
    return train


def train_scan(train):
    # this function scans ours crazy-train according to the algorithm and calculates how many wagons it includes
    current_wagon = 2
    print('сейчас я в 1 вагоне')
    print(f'иду в {current_wagon} вагон')
    while True:
        while not train[current_wagon]:
            current_wagon += 1
            print(f'тут темно, значит иду в вагон {current_wagon}')
        else:
            print(f'ага, в вагоне {current_wagon} светло!')
            train[current_wagon] = False
            print(f'выключаю свет в вагоне {current_wagon} и иду назад')
            if train[current_wagon] == train[n + 1]:  # если текущий вагон = n + 1 , то
                train[1] = train[current_wagon]  # приравниваем к первому, т.к. последний замыкающий вагон n + 1
                # - это и есть 1 вагон
            go_back = current_wagon
            while go_back != 1:
                if not train[go_back]:
                    print(f'в вагоне {go_back} свет не горит, значит')
                    go_back -= 1
                    print(f'иду обратно в вагон {go_back}')
                    continue
                else:
                    print('что-то тут не так...')
            else:
                if train[go_back]:
                    print(f'в вагоне {go_back} горит свет, отсюда начинали. Повторяем операцию')
                    continue
                else:
                    print(f'ага! свет в 1 вагоне погас! А мы его погасили в вагоне {current_wagon}. '
                          f'Значит {current_wagon} вагон - это и есть 1 вагон!')
                    break
    total_wagons = current_wagon - 1
    print(f'всего вагонов насчитали: {total_wagons}, а теперь сравним: {n} - столько вагонов '
          f'на самом деле было в поезде')
    if total_wagons == n:
        print(f'Ура! {total_wagons} = {n}!!!\n'
              f'========= искомое количество вагонов в поезде: {total_wagons} =========')
    return total_wagons


train = train_gen()
train_scan(train)
