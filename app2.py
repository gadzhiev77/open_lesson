# Несколько расчетов ИМТ (цикл for)
n = int(input("Сколько человек: "))
for i in range(n):
    print(f"\nРасчет {i+1}:")
    weight = float(input("  Вес в кг: "))
    height = float(input("  Рост в метрах: "))
    bmi = weight / (height ** 2)
    print(f"  ИМТ = {bmi:.1f}", end=" ")
    if bmi < 18.5:
        category = "Недостаточная масса"
    elif bmi < 25.0:
        category = "Нормальная масса"
    elif bmi < 30.0:
        category = "Избыточная масса"
    else:
        category = "Ожирение"
    print(f"({category})")
