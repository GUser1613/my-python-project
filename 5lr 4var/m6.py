import tkinter as tk
from tkinter.ttk import Progressbar

root = tk.Tk()
root.title("Progressbar")


progress = Progressbar(root, length = 300)
progress.pack(pady = 20)

def load(i = 0):
    if i <= 100:
        progress['value'] = i
        root.after(50, load, i + 5)

button = tk.Button(root, text = "Начать загрузку", command = load)
button.pack(pady = 20)

root.mainloop()