import tkinter as tk

time_ms = 0
running = False

def update():
    global time_ms
    if running:
        time_ms += 10

        minutes = time_ms // 60000
        seconds = (time_ms // 1000) % 60
        millis = (time_ms % 1000) // 10

        label.config(text=f"{minutes:02d}:{seconds:02d}:{millis:02d}")
        root.after(10, update)

def start():
    global running
    if not running:   
        running = True
        update()

def pause():
    global running
    running = False

def reset():
    global running, time_ms
    running = False
    time_ms = 0
    label.config(text="00:00:00")
    

root = tk.Tk()
root.title("Секундомер")

label = tk.Label(root, text="00:00:00", font=("Arial", 30))
label.pack(pady=10)

tk.Button(root, text="Старт", width=10, command=start).pack()
tk.Button(root, text="Пауза", width=10, command=pause).pack()
tk.Button(root, text="Сброс", width=10, command=reset).pack()

root.mainloop()