from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('registration.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Здесь ты можешь сохранить данные в файл или базу
    data = {
        'Фамилия': request.form.get('last_name'),
        'Имя': request.form.get('first_name'),
        'Отчество': request.form.get('middle_name'),
        'Паспорт': request.form.get('passport'),
        'Email': request.form.get('email'),
        'Телефон': request.form.get('phone'),
        'Организация': request.form.get('organization'),
        'Должность': request.form.get('position'),
        'Комментарий': request.form.get('comment')
    }
    print('Новая регистрация:', data)  # Можно заменить на сохранение

    return ('', 204)  # Успешно, без тела

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
