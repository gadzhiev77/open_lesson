# Несколько расчетов ИМТ (цикл while)
print("Введите 0 в весе для выхода")
while True:
    weight = float(input("Вес в кг: "))
    if weight == 0:
        break
    height = float(input("Рост в метрах: "))
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Недостаточная масса"
    elif bmi < 25.0:
        category = "Нормальная масса"
    elif bmi < 30.0:
        category = "Избыточная масса"
    else:
        category = "Ожирение"
    print(f"ИМТ = {bmi:.1f} ({category})")
print("Программа завершена.")
