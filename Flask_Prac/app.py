from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/')
def main_page():
    return "This is main Page."


@app.route('/hello')
def hello_world():
    return "Hello world! This is a Flask App"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


@app.route('/do_the_login')
def do_the_login():
    return "do_the_login"


@app.route('/show_the_login_form')
def show_the_login_form():
    return "show_the_login_form"


@app.route('/user/<username>')
def profile(username):
    ans = username + "'s profile"
    return ans


with app.test_request_context():
    print(url_for('main_page'))
    print(url_for('hello_world'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='Akhil Sharma'))
