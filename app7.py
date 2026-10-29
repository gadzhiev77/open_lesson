# Графическое приложение с PyQt6 для расчета ИМТ
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class BMIApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор ИМТ")
        layout = QVBoxLayout()

        self.label_weight = QLabel("Вес (кг):")
        self.entry_weight = QLineEdit()
        layout.addWidget(self.label_weight)
        layout.addWidget(self.entry_weight)

        self.label_height = QLabel("Рост (м):")
        self.entry_height = QLineEdit()
        layout.addWidget(self.label_height)
        layout.addWidget(self.entry_height)

        self.btn_calc = QPushButton("Рассчитать")
        self.btn_calc.clicked.connect(self.calculate_bmi)
        layout.addWidget(self.btn_calc)

        self.label_result = QLabel("")
        layout.addWidget(self.label_result)

        self.setLayout(layout)

    def calculate_bmi(self):
        try:
            weight = float(self.entry_weight.text())
            height = float(self.entry_height.text())
            bmi = weight / (height ** 2)
            if bmi < 18.5:
                category = "Недостаточная масса"
            elif bmi < 25.0:
                category = "Нормальная масса"
            elif bmi < 30.0:
                category = "Избыточная масса"
            else:
                category = "Ожирение"
            self.label_result.setText(f"ИМТ = {bmi:.1f} ({category})")
        except ValueError:
            self.label_result.setText("Введите корректные числа!")

app = QApplication([])
window = BMIApp()
window.show()
app.exec()
