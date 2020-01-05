from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def index():
    return render_template('home.jinja2')

@app.route('/auth', methods=['GET', 'POST'])
def auth():
    return render_template('auth.jinja2')


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.jinja2')


@app.route('/new.jinja2', methods=['POST'])
def new_post():
    return ''

@app.route("/teste")
def teste():
    return '<h1>Página de teste!!!</h1>'



if __name__ == '__main__':
    app.run(debug=True, port=3000)