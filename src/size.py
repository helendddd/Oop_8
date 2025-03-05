#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk


def resize_text():
    """
    Изменяет размеры текстового поля на основе значений,
    введенных в однострочные поля.
    """
    try:
        width = int(entry_width.get())  # Получаем ширину
        height = int(entry_height.get())  # Получаем высоту
        text.config(width=width, height=height)  # Применяем новые размеры
    except ValueError:
        # Если введены некорректные значения, ничего не делаем
        pass


def on_focus_in(event):
    """
    Обработчик события получения фокуса.
    """
    text.config(bg="white")


def on_focus_out(event):
    """
    Обработчик события потери фокуса.
    """
    text.config(bg="lightgrey")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Изменение размера текстового поля")

    frame = tk.Frame(root)
    frame.pack(pady=10)

    label_width = tk.Label(frame, text="Ширина:")
    label_width.pack()
    entry_width = tk.Entry(frame, width=10)
    entry_width.pack(pady=5)

    label_height = tk.Label(frame, text="Высота:")
    label_height.pack()
    entry_height = tk.Entry(frame, width=10)
    entry_height.pack(pady=5)

    button_resize = tk.Button(frame, text="Изменить", command=resize_text)
    button_resize.pack(pady=10)

    text = tk.Text(root, bg="lightgrey", wrap=tk.WORD)
    text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    text.bind("<FocusIn>", on_focus_in)
    text.bind("<FocusOut>", on_focus_out)

    root.bind("<Return>", lambda event: resize_text())

    root.mainloop()
