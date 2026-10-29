# Однократный расчет ИМТ (консольное приложение)
weight = float(input("Введите вес в килограммах: "))
height = float(input("Введите рост в метрах: "))
bmi = weight / (height ** 2)
print(f"ИМТ = {bmi:.1f}")
# Определение категории по ИМТ:
if bmi < 18.5:
    category = "Недостаточная масса тела"
elif bmi < 25.0:
    category = "Нормальная масса тела"
elif bmi < 30.0:
    category = "Избыточная масса тела"
else:
    category = "Ожирение"
print("Категория:", category)
