import tkinter as tk

root = tk.Tk()
root.title("Listbox и выбор элемента")

listbox = tk.Listbox(root, width = 50, height = 10)
listbox.pack(padx = 10, pady = 10)

for fruit in ["Apple", "Banana", "Cherry", "Orange", "Mango"]:
    listbox.insert("end", fruit)

def show_selection():
    idx = listbox.curselection()
    if idx:
        print("Вы выбрали:", listbox.get(idx))
    else:
        print("Нет выбора")

button = tk.Button(root, text = "Показать выбор", command = show_selection)
button.pack()

root.mainloop()

