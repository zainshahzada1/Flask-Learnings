from flask import Flask
from flask_mail import Mail, Message
app = Flask(__name__)

mail = Mail(app)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yousniper99@gmail.com'
app.config['MAIL_PASSWORD'] = 'zainshahzadaGmail'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route("/")
def index():
    msg = Message('Hello', sender='yousniper99@gmail.com',
                  recipients=['zainulabideen.jutt1@gmail.com'])
    msg.body = 'Hello, Flask! This is a Simple message from Flask'
    mail.send(msg)
    return 'Message has been sent successfully'


if __name__ == '__main__':
    app.run(debug=True)
