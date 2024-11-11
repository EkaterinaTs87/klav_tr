from tkinter import *
import time


def check(event):
    global i
    if event.char == phraze[i]:
        i += 1
        if i == len(phraze):
            e = time.time() - t
            allow_time = len(phraze)  # время за которое нужно напечатать
            if e <= allow_time:
                label.config(text=f"Вы победили! Ваше время: {e:.2f} секунд.")
            else:
                label.config(text=f"Ваше время: {e:.2f} секунд. Надо уложиться в {allow_time}")

            window.unbind("<KeyPress>")
        else:
            label.config(text=phraze[i])
    else:
        label.config(text=f"Ошибка! Ожидалось буква {phraze[i]}. \n Для продолжения нажмите любую клавишу.")
        window.bind("<KeyPress>", continu)


def continu(event):
    label.config(text=phraze[i])
    window.bind("<KeyPress>", check)


phraze = "helloworld"
i = 0
t = time.time()

window = Tk()
window.title("Клавиатурный тренажер")
window.geometry("900x150")

label = Label(text=phraze[i], font="Arial 29")
label.pack()

window.bind("<KeyPress>", check)

window.mainloop()