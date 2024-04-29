import tkinter as tk
from tkinter import messagebox

def solve_quadratic():
    
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите числовые значения для a, b и c.")
        return
    
    
    if entry_a.get() == '' or entry_b.get() == '' or entry_c.get() == '':
        messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля.")
        return
    
    
    D = b**2 - 4*a*c
    
    
    if D > 0:
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        result_label.config(text=f"Уравнение имеет два корня: x1 = {x1}, x2 = {x2}")
    elif D == 0:
        x = -b / (2*a)
        result_label.config(text=f"Уравнение имеет один корень: x = {x}")
    else:
        result_label.config(text="Уравнение не имеет действительных корней.")
    
    
    entry_a.config(bg="white")
    entry_b.config(bg="white")
    entry_c.config(bg="white")

def check_entry(event):
   
    try:
        float(event.widget.get())
        event.widget.config(bg="white")
    except ValueError:
        event.widget.config(bg="red")


root = tk.Tk()
root.title("Решение квадратного уравнения")
root.config(bg="lightblue")


entry_a = tk.Entry(root, width=5)
entry_a.grid(row=0, column=0, padx=5, pady=5)
entry_a.bind("<FocusOut>", check_entry)

label_a = tk.Label(root, text="x^2 +", bg="lightblue")
label_a.grid(row=0, column=1, padx=5, pady=5)

entry_b = tk.Entry(root, width=5)
entry_b.grid(row=0, column=2, padx=5, pady=5)
entry_b.bind("<FocusOut>", check_entry)

label_b = tk.Label(root, text="x +", bg="lightblue")
label_b.grid(row=0, column=3, padx=5, pady=5)

entry_c = tk.Entry(root, width=5)
entry_c.grid(row=0, column=4, padx=5, pady=5)
entry_c.bind("<FocusOut>", check_entry)

label_c = tk.Label(root, text=" = 0", bg="lightblue")
label_c.grid(row=0, column=5, padx=5, pady=5)


solve_button = tk.Button(root, text="Решить", command=solve_quadratic, bg="green")
solve_button.grid(row=1, column=0, columnspan=6, padx=5, pady=5)


result_label = tk.Label(root, text="", bg="lightblue")
result_label.grid(row=2, column=0, columnspan=6, padx=5, pady=5)


root.mainloop()
