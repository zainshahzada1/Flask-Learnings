from flask import Flask, render_template, request, make_response
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('setcookie.html')


@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userid', user)
        return resp


@app.route('/getcookie')
def get_cookie():
    name = request.cookies.get('userid')
    return '<h1>Hello ' + name + '</h1>'


if __name__ == '__main__':
    app.run(debug=True)
