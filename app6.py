# Графическое приложение с Tkinter для расчета ИМТ
import tkinter as tk
from tkinter import messagebox


def get_bmi_category(bmi: float) -> str:
    if bmi < 16.0:
        return "Выраженный дефицит массы"
    elif bmi < 18.5:
        return "Недостаточная масса"
    elif bmi < 25.0:
        return "Нормальная масса"
    elif bmi < 30.0:
        return "Избыточная масса"
    elif bmi < 35.0:
        return "Ожирение I степени"
    elif bmi < 40.0:
        return "Ожирение II степени"
    else:
        return "Ожирение III степени"


def calculate_bmi():
    try:
        weight = float(entry_weight.get().replace(",", "."))
        height = float(entry_height.get().replace(",", "."))
    except ValueError:
        messagebox.showerror("Ошибка", "Введите числовые значения веса и роста.")
        return

    if weight <= 0 or height <= 0:
        messagebox.showerror("Ошибка", "Вес и рост должны быть положительными.")
        return
    if height > 3:
        messagebox.showwarning(
            "Проверьте рост",
            "Рост указан в метрах (например, 1.75), а не в сантиметрах."
        )
        return

    bmi = weight / (height ** 2)
    category = get_bmi_category(bmi)
    label_result.config(text=f"ИМТ = {bmi:.1f} ({category})")


window = tk.Tk()
window.title("Калькулятор ИМТ")
window.geometry("400x320")
window.minsize(360, 300)

window.columnconfigure(0, weight=1)

tk.Label(window, text="Вес (кг):").grid(row=0, column=0, pady=(12, 0))
entry_weight = tk.Entry(window, justify="center")
entry_weight.grid(row=1, column=0, sticky="ew", padx=40)

tk.Label(window, text="Рост (м):").grid(row=2, column=0, pady=(8, 0))
entry_height = tk.Entry(window, justify="center")
entry_height.grid(row=3, column=0, sticky="ew", padx=40)

btn = tk.Button(window, text="Рассчитать", command=calculate_bmi)
btn.grid(row=4, column=0, pady=12)

label_result = tk.Label(window, text="", font=("TkDefaultFont", 12, "bold"))
label_result.grid(row=5, column=0)

window.rowconfigure(6, weight=1)

window.bind("<Return>", lambda e: calculate_bmi())
entry_weight.focus_set()

window.mainloop()