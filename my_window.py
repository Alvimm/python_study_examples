import tkinter as tk
from tkinter import messagebox, PhotoImage

from study import bmi


def click_func():
    print('The button has been clicked')
    index = bmi.calculate_bmi(weight=weight.get(), height=height.get())
    rating = bmi.bmi_rating(index)
    msg = messagebox.showinfo('BMI Rating', rating)


window = tk.Tk()
img = PhotoImage(file="logo.png")
logo = tk.Label(window, image=img)
logo.image = img
logo.grid(row=0, column=0, rowspan=2)
height_label = tk.Label(window, text="Height")
height_label.grid(row=0, column=1)
height = tk.Entry(window)
height.grid(row=0, column=2)
weight_label = tk.Label(window, text="Weight")
weight_label.grid(row=1, column=1)
weight = tk.Entry(window)
weight.grid(row=1, column=2)
btn = tk.Button(window, text="Calculate", command=click_func)
btn.grid(row=2, column=2)
window.mainloop()
