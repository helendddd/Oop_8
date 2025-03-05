#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk


def move_to_cart():
    selected_items = listbox_goods.curselection()
    for index in reversed(selected_items):
        item = listbox_goods.get(index)
        listbox_cart.insert(tk.END, item)
        listbox_goods.delete(index)


def move_back_to_goods():
    selected_items = listbox_cart.curselection()
    for index in reversed(selected_items):
        item = listbox_cart.get(index)
        listbox_goods.insert(tk.END, item)
        listbox_cart.delete(index)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Список товаров и покупок")

    frame = tk.Frame(root)
    frame.pack(pady=10)

    listbox_goods = tk.Listbox(
        frame,
        selectmode=tk.MULTIPLE,
        width=20,
        height=10
        )
    listbox_goods.pack(side=tk.LEFT, padx=10)

    goods = [
        "apple",
        "bananas",
        "carrot",
        "bread",
        "butter",
        "meat",
        "potato",
        "pineapple",
        "tomato",
        "milk"]
    for item in goods:
        listbox_goods.insert(tk.END, item)

    frame_buttons = tk.Frame(frame)
    frame_buttons.pack(side=tk.LEFT, padx=10)

    button_to_cart = tk.Button(
        frame_buttons,
        text=">>>",
        command=move_to_cart
        )
    button_to_cart.pack(side=tk.TOP, pady=5)

    button_to_goods = tk.Button(
        frame_buttons,
        text="<<<",
        command=move_back_to_goods
        )
    button_to_goods.pack(side=tk.TOP, pady=5)

    listbox_cart = tk.Listbox(
        frame,
        selectmode=tk.MULTIPLE,
        width=20,
        height=10
        )
    listbox_cart.pack(side=tk.LEFT, padx=10)

    root.mainloop()
