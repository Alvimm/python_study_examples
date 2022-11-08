from tkinter import Tk, Label, Button


def click_func():
    print("Button pressed")


main_window = Tk()
text = Label(master=main_window, text="My window displayed")
text.pack()

btn = Button(master=main_window, text='Click', command=click_func)
btn.pack()

main_window.mainloop()
