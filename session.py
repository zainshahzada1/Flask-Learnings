from flask import Flask, render_template, request, make_response,session,url_for,redirect
app = Flask(__name__)
app.secret_key='random'
@app.route('/')
def index():
    if 'username' in session:
        username=session['username']
        return '<h1>You Logged  in as '+username.capitalize()+'</h1><br>'+'<a href="/logout">Click Here to Logout</a>'
    else:
        return '<h1>You are not Logged in</h1>'+'<br>'+'<a href="/login">Click Here To Login<a>'


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('session.html')

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)
