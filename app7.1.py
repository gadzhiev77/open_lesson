# Графическое приложение с PyQt6 для расчета ИМТ
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QFrame
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

# Цвета для категорий
CATEGORY_STYLES = {
    "Недостаточная масса": "#3b82f6",
    "Нормальная масса":    "#22c55e",
    "Избыточная масса":    "#f59e0b",
    "Ожирение":            "#ef4444",
}


class BMIApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор ИМТ")
        self.resize(460, 480)

        # ---------- Общие стили окна ----------
        self.setStyleSheet("""
            QWidget {
                background-color: #f5f7fa;
                font-family: 'Segoe UI', Arial, sans-serif;
                color: #1f2937;
            }
            QLabel#title {
                font-size: 26px;
                font-weight: 700;
                color: #1e3a8a;
                padding: 6px 0 2px 0;
            }
            QLabel#subtitle {
                font-size: 13px;
                color: #6b7280;
                padding-bottom: 14px;
            }
            QLabel#field_label {
                font-size: 15px;
                font-weight: 600;
                color: #374151;
            }
            QLineEdit {
                font-size: 18px;
                padding: 12px 14px;
                border: 2px solid #d1d5db;
                border-radius: 10px;
                background: #ffffff;
            }
            QLineEdit:focus {
                border: 2px solid #3b82f6;
                background: #ffffff;
            }
            QPushButton {
                font-size: 17px;
                font-weight: 700;
                color: #ffffff;
                background-color: #2563eb;
                border: none;
                border-radius: 10px;
                padding: 14px;
            }
            QPushButton:hover { background-color: #1d4ed8; }
            QPushButton:pressed { background-color: #1e40af; }
            QLabel#result_bmi {
                font-size: 40px;
                font-weight: 800;
            }
            QLabel#result_category {
                font-size: 16px;
                font-weight: 600;
                padding: 10px 0 4px 0;
            }
            QLabel#error {
                font-size: 15px;
                color: #dc2626;
                font-weight: 600;
            }
            QFrame#result_card {
                background: #ffffff;
                border: 2px solid #e5e7eb;
                border-radius: 14px;
            }
        """)

        # ---------- Заголовок ----------
        title = QLabel("Калькулятор ИМТ")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        subtitle = QLabel("Узнайте свой индекс массы тела за секунду")
        subtitle.setObjectName("subtitle")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # ---------- Поле "Вес" ----------
        self.label_weight = QLabel("Вес (кг)")
        self.label_weight.setObjectName("field_label")
        self.entry_weight = QLineEdit()
        self.entry_weight.setPlaceholderText("Например, 70")

        # ---------- Поле "Рост" ----------
        self.label_height = QLabel("Рост (м)")
        self.label_height.setObjectName("field_label")
        self.entry_height = QLineEdit()
        self.entry_height.setPlaceholderText("Например, 1.75")

        # ---------- Кнопка ----------
        self.btn_calc = QPushButton("Рассчитать")
        self.btn_calc.clicked.connect(self.calculate_bmi)

        # ---------- Карточка результата ----------
        self.result_card = QFrame()
        self.result_card.setObjectName("result_card")
        result_layout = QVBoxLayout(self.result_card)
        result_layout.setContentsMargins(16, 16, 16, 16)
        result_layout.setSpacing(6)

        self.label_result = QLabel("—")
        self.label_result.setObjectName("result_bmi")
        self.label_result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_category = QLabel("")
        self.label_category.setObjectName("result_category")
        self.label_category.setAlignment(Qt.AlignmentFlag.AlignCenter)

        result_layout.addWidget(self.label_result)
        result_layout.addWidget(self.label_category)

        # ---------- Общий layout ----------
        layout = QVBoxLayout()
        layout.setContentsMargins(28, 20, 28, 24)
        layout.setSpacing(10)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(6)

        layout.addWidget(self.label_weight)
        layout.addWidget(self.entry_weight)

        layout.addSpacing(6)
        layout.addWidget(self.label_height)
        layout.addWidget(self.entry_height)

        layout.addSpacing(14)
        layout.addWidget(self.btn_calc)

        layout.addSpacing(16)
        layout.addWidget(self.result_card)

        self.setLayout(layout)

        # Enter в любом поле запускает расчёт
        self.entry_weight.returnPressed.connect(self.calculate_bmi)
        self.entry_height.returnPressed.connect(self.calculate_bmi)

    def calculate_bmi(self):
        try:
            weight = float(self.entry_weight.text().replace(",", "."))
            height = float(self.entry_height.text().replace(",", "."))
        except ValueError:
            self.show_error("Введите корректные числа!")
            return

        if weight <= 0 or height <= 0:
            self.show_error("Вес и рост должны быть положительными.")
            return
        if height > 3:
            self.show_error("Рост в метрах, например 1.75.")
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Недостаточная масса"
        elif bmi < 25.0:
            category = "Нормальная масса"
        elif bmi < 30.0:
            category = "Избыточная масса"
        else:
            category = "Ожирение"

        color = CATEGORY_STYLES[category]

        self.label_result.setText(f"{bmi:.1f}")
        self.label_result.setStyleSheet(f"color: {color};")
        self.label_category.setText(category)
        self.label_category.setStyleSheet(
            f"color: {color}; font-size: 16px; font-weight: 700;"
        )

    def show_error(self, message):
        self.label_result.setText("—")
        self.label_result.setStyleSheet("color: #9ca3af;")
        self.label_category.setText(message)
        self.label_category.setStyleSheet(
            "color: #dc2626; font-size: 15px; font-weight: 600;"
        )


app = QApplication(sys.argv)
window = BMIApp()
window.show()
sys.exit(app.exec())