from flask import Flask, render_template, request, flash, redirect
from wtfoamscode import ContactForm
app = Flask(__name__)
app.secret_key = 'random'


@app.route('/', methods=['POST', 'GET'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All Fields are Required Should be Corrected...')
            return render_template('contact_form.html', form=form)
        else:
            return render_template('form_success.html')
    if request.method == 'GET':
        return render_template('contact_form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
