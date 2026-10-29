# Однократный расчет ИМТ (консольное приложение)
# Каждый шаг оформлен отдельной функцией — так проще понять,
# что функция это именованный блок кода, который можно вызвать.


def get_weight():
    """Запрашивает вес у пользователя и возвращает число."""
    return float(input("Введите вес в килограммах: "))


def get_height():
    """Запрашивает рост у пользователя и возвращает число."""
    return float(input("Введите рост в метрах: "))


def calculate_bmi(weight, height):
    """Считает ИМТ по формуле вес / рост^2."""
    return weight / (height ** 2)


def get_category(bmi):
    """Определяет категорию по значению ИМТ."""
    if bmi < 18.5:
        return "Недостаточная масса тела"
    elif bmi < 25.0:
        return "Нормальная масса тела"
    elif bmi < 30.0:
        return "Избыточная масса тела"
    else:
        return "Ожирение"


def print_result(bmi, category):
    """Выводит результат на экран."""
    print(f"ИМТ = {bmi:.1f}")
    print("Категория:", category)


def main():
    """Главная функция: связывает все шаги вместе."""
    weight = get_weight()
    height = get_height()
    bmi = calculate_bmi(weight, height)
    category = get_category(bmi)
    print_result(bmi, category)


main()