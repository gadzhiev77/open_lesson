from flask import Flask, render_template, request

app = Flask(__name__)


def calculate_bmi(weight, height):
    """Расчёт индекса массы тела"""
    if height <= 0:
        return None
    return weight / (height ** 2)


def get_diagnosis(bmi):
    """Определение диагноза по значению ИМТ"""
    if bmi is None:
        return "Некорректные данные"
    elif bmi <= 16:
        return "Выраженный дефицит массы тела"
    elif bmi < 18.5:
        return "Недостаточная (дефицит) масса тела"
    elif bmi < 25:
        return "Норма"
    elif bmi < 30:
        return "Избыточная масса тела (предожирение)"
    elif bmi < 35:
        return "Ожирение первой степени"
    elif bmi < 40:
        return "Ожирение второй степени"
    else:
        return "Ожирение третьей степени (морбидное)"


@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    diagnosis = None
    weight = ''
    height = ''
    error = None

    if request.method == 'POST':
        try:
            weight = float(request.form.get('weight', 0))
            height = float(request.form.get('height', 0))

            if weight <= 0 or height <= 0:
                error = "Введите положительные значения веса и роста"
            else:
                bmi = calculate_bmi(weight, height)
                diagnosis = get_diagnosis(bmi)
                bmi = round(bmi, 2)
        except ValueError:
            error = "Пожалуйста, введите корректные числовые значения"

    return render_template('index.html',
                           bmi=bmi,
                           diagnosis=diagnosis,
                           weight=weight,
                           height=height,
                           error=error)


if __name__ == '__main__':
    app.run(debug=True)
