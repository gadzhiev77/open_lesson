from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, BMIRecord, calculate_bmi

app = Flask(__name__)
app.config['SECRET_KEY'] = 'change-me-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bmi.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    """Главная: форма + список записей (с поиском)."""
    query = request.args.get('q', '').strip()
    if query:
        records = BMIRecord.query.filter(
            BMIRecord.full_name.ilike(f'%{query}%')
        ).order_by(BMIRecord.created_at.desc()).all()
    else:
        records = BMIRecord.query.order_by(BMIRecord.created_at.desc()).all()

    return render_template('index.html', records=records, query=query)


@app.route('/add', methods=['POST'])
def add_record():
    """Добавление новой записи с расчётом ИМТ."""
    full_name = request.form.get('full_name', '').strip()
    weight_str = request.form.get('weight', '').strip()
    height_str = request.form.get('height', '').strip()

    # Валидация
    if not full_name:
        flash('Введите фамилию и инициалы.', 'danger')
        return redirect(url_for('index'))

    try:
        weight = float(weight_str.replace(',', '.'))
        height = float(height_str.replace(',', '.'))
    except ValueError:
        flash('Вес и рост должны быть числами.', 'danger')
        return redirect(url_for('index'))

    if not (10 <= weight <= 400):
        flash('Вес должен быть в пределах 10–400 кг.', 'danger')
        return redirect(url_for('index'))

    if not (50 <= height <= 250):
        flash('Рост должен быть в пределах 50–250 см.', 'danger')
        return redirect(url_for('index'))

    bmi, category = calculate_bmi(weight, height)

    record = BMIRecord(
        full_name=full_name,
        weight_kg=weight,
        height_cm=height,
        bmi=bmi,
        category=category,
    )
    db.session.add(record)
    db.session.commit()

    flash(f'Запись добавлена. ИМТ = {bmi:.2f} ({category})', 'success')
    return redirect(url_for('index'))


@app.route('/delete/<int:record_id>', methods=['POST'])
def delete_record(record_id):
    """Удаление записи."""
    record = BMIRecord.query.get_or_404(record_id)
    db.session.delete(record)
    db.session.commit()
    flash('Запись удалена.', 'info')
    return redirect(url_for('index'))


@app.route('/edit/<int:record_id>', methods=['GET', 'POST'])
def edit_record(record_id):
    """Редактирование веса/роста с пересчётом ИМТ."""
    record = BMIRecord.query.get_or_404(record_id)

    if request.method == 'POST':
        try:
            weight = float(request.form['weight'].replace(',', '.'))
            height = float(request.form['height'].replace(',', '.'))
        except (ValueError, KeyError):
            flash('Некорректные данные.', 'danger')
            return redirect(url_for('edit_record', record_id=record_id))

        if not (10 <= weight <= 400) or not (50 <= height <= 250):
            flash('Значения веса/роста вне допустимого диапазона.', 'danger')
            return redirect(url_for('edit_record', record_id=record_id))

        bmi, category = calculate_bmi(weight, height)
        record.full_name = request.form.get('full_name', record.full_name).strip()
        record.weight_kg = weight
        record.height_cm = height
        record.bmi = bmi
        record.category = category

        db.session.commit()
        flash('Запись обновлена.', 'success')
        return redirect(url_for('index'))

    return render_template('edit.html', record=record)


@app.route('/delete_all', methods=['POST'])
def delete_all():
    """Очистка всей базы (доп. функция)."""
    BMIRecord.query.delete()
    db.session.commit()
    flash('Все записи удалены.', 'info')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)