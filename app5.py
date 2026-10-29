# Однократный расчет ИМТ (консольное приложение)
# Логика оформлена классом — класс это "шаблон", объединяющий
# данные (вес, рост) и действия над ними (методы).


class BMICalculator:
    """Класс для расчета индекса массы тела."""

    def __init__(self, weight, height):
        # Атрибуты объекта — данные, с которыми работают методы
        self.weight = weight
        self.height = height

    def calculate_bmi(self):
        """Считает ИМТ по формуле вес / рост^2."""
        return self.weight / (self.height ** 2)

    def get_category(self):
        """Определяет категорию по значению ИМТ."""
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Недостаточная масса тела"
        elif bmi < 25.0:
            return "Нормальная масса тела"
        elif bmi < 30.0:
            return "Избыточная масса тела"
        else:
            return "Ожирение"

    def print_result(self):
        """Выводит результат на экран."""
        bmi = self.calculate_bmi()
        print(f"ИМТ = {bmi:.1f}")
        print("Категория:", self.get_category())


def main():
    weight = float(input("Введите вес в килограммах: "))
    height = float(input("Введите рост в метрах: "))

    # Создаём объект класса — экземпляр с конкретными весом и ростом
    calculator = BMICalculator(weight, height)
    calculator.print_result()


main()