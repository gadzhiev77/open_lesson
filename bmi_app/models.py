from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class BMIRecord(db.Model):
    __tablename__ = 'bmi_records'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120), nullable=False)
    weight_kg = db.Column(db.Float, nullable=False)
    height_cm = db.Column(db.Float, nullable=False)
    bmi = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(40), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'weight_kg': self.weight_kg,
            'height_cm': self.height_cm,
            'bmi': round(self.bmi, 2),
            'category': self.category,
            'created_at': self.created_at.strftime('%d.%m.%Y %H:%M'),
        }


def calculate_bmi(weight_kg: float, height_cm: float):
    """Возвращает (ИМТ, категория)."""
    height_m = height_cm / 100.0
    bmi = weight_kg / (height_m ** 2)

    if bmi < 16:
        category = 'Выраженный дефицит массы'
    elif bmi < 18.5:
        category = 'Недостаточная масса'
    elif bmi < 25:
        category = 'Норма'
    elif bmi < 30:
        category = 'Избыточная масса'
    elif bmi < 35:
        category = 'Ожирение I степени'
    elif bmi < 40:
        category = 'Ожирение II степени'
    else:
        category = 'Ожирение III степени'

    return bmi, category