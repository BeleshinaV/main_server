'''
flash() - на стороне сервера
get_flashed_messages() - в шаблоне

flash() -> session -> get_flashed_messages() -> шаблон
'''

from flask import Flask, render_template, url_for, request, flash


app = Flask(__name__)
app.config['SECRET.KEY'] = 'dfkjhbvrituniuibufd'
users = [
    {'username': 'Beleshina', 'password': '12345', 'is_admin': True},
    {'username': 'Student', 'password': '1060', 'is_admin': False},
]


@app.route('/')
def begin():
    return f"""
Ссылка на <a href='/base'>базовую</a> страницу<br>
Ссылка на <a href='/start'>стартовую</a> страницу<br>
Ссылка на <a href={url_for('index')}>index</a> страницу<br>
Ссылка на <a href={url_for('form')}>страницу с формой</a><br>
Ссылка на <a href={url_for('login')}>страницу авторизации</a><br>
"""



@app.route('/index')
def index():
    username = 'Beleshina'
    return render_template('index.html', username=username)


@app.route('/days/day-<num>')
def day(num):
    return render_template(f'day-{num}.html')


@app.route('/photo-<num>')
def photo(num):
    return render_template(f'photo-{num}.html')


@app.route('/base')
def base():
    return render_template('base.html')


@app.route('/start')
def start():
    return render_template('start.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # валидация даннных
        if len(request.form['fullname']) < 5 and not request.form['fullname'].isalpha():
            flash('Ошибка в имени. Сообщение не отправлено!', category='error')
        else:
            flash('Сообщение принято!', category='success')      
        for item in request.form:
            print(item, request.form[item])
    return render_template('form.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        for user in users:
            if request.form['username'] == user['username']:
                if request.form['password'] == user['password']:
                    return redirect(f"/profile/{user['username']}")
                else:
                    flash('Неправильный пароль', category='error')
                    break
            else:
                flash('Неправильный логин', category='error')
         flash('Такого пользователя не существует', category='error')
        
     return render_template('login.html')

        
      
@app.route('/profile/<username>')
def profile(username):
    for user in users:
        if user['username'] == username:
            if 'logged_in' in session:
                if session['logged_in'] == usernime:
                    return render_template('profile.html', username=username)
                else:
                    abort(403)
            flash('Вам туда нельзя. Зарегистрируйтесь!', category='error')
            return redirect(url_for('login'))
    abort(404)


if __name__ == '__main__':
    app.run(debug=True)
