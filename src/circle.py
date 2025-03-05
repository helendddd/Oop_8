#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *


def motion(target_x, target_y):
    """
    Постепенно перемещает круг к целевым координатам (target_x, target_y).
    """
    # Получаем текущие координаты круга
    x1, y1, x2, y2 = c.coords(ball)
    current_x = (x1 + x2) / 2  # Центр круга по X
    current_y = (y1 + y2) / 2  # Центр круга по Y

    # Вычисляем разницу между текущими и целевыми координатами
    dx = target_x - current_x
    dy = target_y - current_y

    # Если круг еще не достиг целевой точки
    if abs(dx) > 1 or abs(dy) > 1:
        # Перемещаем круг на небольшое расстояние к целевой точке
        c.move(ball, dx * 0.1, dy * 0.1)
        # Повторяем через 10 мс
        root.after(10, motion, target_x, target_y)


def on_click(event):
    """
    Обрабатывает клик мыши и запускает движение круга к точке клика.
    """
    target_x = event.x  # Координата X клика
    target_y = event.y  # Координата Y клика
    motion(target_x, target_y)  # Запускаем движение круга


if __name__ == "__main__":
    # Создание основного окна
    root = Tk()

    # Создание холста
    c = Canvas(root, width=300, height=200, bg="white")
    c.pack()

    # Создание круга
    ball = c.create_oval(0, 100, 40, 140, fill='green')

    # Привязка события клика мыши к функции on_click
    c.bind("<Button-1>", on_click)

    # Запуск основного цикла обработки событий
    root.mainloop()
