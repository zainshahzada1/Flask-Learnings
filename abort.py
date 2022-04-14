from flask import Flask, render_template, request, make_response, session, url_for, redirect,abort
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('redirect_login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['name'] == 'admin':
            return redirect('/seccess')
        else:
            abort(404)
    else:
        return redirect(url_for('index'))


@app.route('/seccess')
def seccess():
    return 'Logged in Successfully'


if __name__ == '__main__':
    app.run(debug=True)
