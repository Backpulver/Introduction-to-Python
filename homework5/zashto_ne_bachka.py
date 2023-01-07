"""
[Title/Звание]
RPG Chess

[Description/Обрисовка]
Шах с магически елемент, който позволява преди началото на всяка игра да изберем клас с три уникални 
споспбности под формата на карти на една от шестте вида фигури на полето (представете си много осакатен hearthstone)

[Functionalities/Надарености]
Играчът избира клас преди започването на игра
Класът позволява на играча да получи преднина в играта чрез нови правила за хода си чрез използването на карта
Освен нови правила някои полета и фигури ще получат "ключови думи", които променят хода на играта
Останалите функционалности са същите като на стандратна партия шах
Играта ще може да бъде играна от двама под формата на "couch co-op" или "LAN party"

[Milestones/Възлови точки]
Реализиране на 2d дъска за шах с фигури на нея
Създаване на поне 2 класа, всеки с по три карти, променящи нормалните ходове и полето за игра
Направата на нова система за ходовете вклюваща "mana" и "cooldown" на картите
Функционалности за местене на различните фигури и използване на карти
Опит за балансиране на класовете и техните начини на игра съвместно с класическите правила за шах
UI + открояващи начини за начало и край на игра с меню (пауза механика?)
Завъртане на дъската при смяна на хода или друг начин, който ще улеснява играта на един монитор
Свързване към lobby на lan party

[Estimate in man-hours/Времеоценка в човекочасове]
140

[Usage of technologies/Потребление на технологии]
Pygame/PyKyra
PyOpenGL
"""