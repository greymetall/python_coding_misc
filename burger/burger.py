# -*- coding: utf-8 -*-

# Создаём рецепт двойного чизбургера. В нем определить функции добавления ингредиентов:
#  - булочка
#  - котлета
#  - огурчик
#  - помидорчик
#  - майонез
#  - сыр


import my_burger

print('Рецепт приготовления двойного чизбургера таков:')
print('')
my_burger.bun()
print('И разрежем её вдоль')
my_burger.cutlet()
my_burger.cucumber()
my_burger.tomato()
my_burger.maionnaise()
my_burger.cheese()
print('\n=====Вот и получился двойной чизбургер!!!=====')
