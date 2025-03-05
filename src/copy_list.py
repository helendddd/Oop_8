#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk


def add_to_list(event=None):
    """
    Добавляет текст из текстового поля в список.
    """
    text = entry.get()  # Получаем текст из текстового поля
    if text:  # Если текст не пустой
        listbox.insert(tk.END, text)  # Добавляем текст в список
        entry.delete(0, tk.END)  # Очищаем текстовое поле


def copy_to_entry(event):
    """
    Копирует текст из списка в текстовое поле при двойном клике.
    """
    selected_index = listbox.curselection()  # Получаем индекс элемента
    if selected_index:  # Если элемент выбран
        text = listbox.get(selected_index)  # Получаем текст элемента
        entry.delete(0, tk.END)  # Очищаем текстовое поле
        entry.insert(0, text)  # Вставляем текст в текстовое поле


if __name__ == "__main__":
    # Создание основного окна
    root = tk.Tk()
    root.title("Текст и список")

    # Однострочное текстовое поле
    entry = tk.Entry(root, width=30)
    entry.pack(pady=10)

    # Привязка клавиши Enter к добавлению текста в список
    entry.bind("<Return>", add_to_list)

    # Список (Listbox)
    listbox = tk.Listbox(root, width=30)
    listbox.pack(pady=10)

    # Привязка двойного клика к копированию текста в текстовое поле
    listbox.bind("<Double-Button-1>", copy_to_entry)

    # Запуск основного цикла обработки событий
    root.mainloop()
