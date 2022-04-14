from flask import Flask, render_template, request, make_response, session, url_for, redirect, flash
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'File Saved Successfully'


if __name__ == '__main__':
    app.run(debug=True)
