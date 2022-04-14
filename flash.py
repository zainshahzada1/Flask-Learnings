from flask import Flask, render_template, request, make_response, session, url_for, redirect, flash
app = Flask(__name__)
app.secret_key='random'
n=0
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    global n 
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Username or Password.Please Try Again ......'
        elif  n==1:
            flash('You were Already Succussfully Logged in Before !')
            flash('Logout before logging in Again.')
            return redirect(url_for('index'))
        else:
            n=1
            flash('You Logged In for First Time')
            return redirect(url_for('index',))
    return render_template('flash_login.html',error=error)


if __name__ == '__main__':
    app.run(debug=True)
