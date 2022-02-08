from flask import Flask, render_template, request, url_for
import time


app = Flask(__name__)
server_start_time = time.time()
'''
@app.route('/base')
def base():
    return render_template('base.html')
'''

@app.route('/')
def start():
    return render_template('start.html', base="base.html")


@app.route('/home')
def hello():
    return """
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h1>Hello</h1>
    <hr>
    <h2><a href=status>status hir</a></h2>
    <h3><a href=/get_messages>messages hir</a></h3>
  </body>
</html>
"""

users = [
    {'username': 'Kira', 'password':'0000'},
    {'username': 'Anton', 'password':'0001'}
]

@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    login_ok = False
    for user in users:
        if user['username'] == username:
            if user['password'] == password:
                login_ok = True
                break
    return {'ok': login_ok}





@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/day-<num>')
def day(num):
    return render_template(f'day-{num}.html')


@app.route('/status')
def staatus():
    return """
<html>
  <head>
    <title>status Page</title>
  </head>
  <body>
    <h1>Status</h1>
    <hr>
    <h2><a href=status/time_>time hir</a></h2><h2>
  </body>
</html>
"""


@app.route('/status/time_')
def time_():
    return {
        "current-time": time.ctime(time.time())
    }


messages = [
    {'username': 'Иван М', 'text': 'Проивет!', 'timestamp': time.time()},
    {'username': 'Миша', 'text': 'И тебе проивет!', 'timestamp': time.time()},
    {'username': 'Миша', 'text': 'классный месc.', 'timestamp': time.time()},
]


@app.route('/get_messages')
def get_messages():
    return {
        'messages': messages
    }


@app.route('/send_messages', methods=['GET', 'POST'])
def send_messages():
    username = request.json['username']
    text = request.json['text']

    messages.append(
        {
            'username':username,
            'text':text,
            'timestamp': time.time()
        }
    )
    return {
        'ok':True
    }


if __name__ == '__main__':
    app.run(debug=True)
