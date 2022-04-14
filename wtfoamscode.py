from flask_wtf import FlaskForm
from wtforms import validators 
from wtforms import TextField, TextAreaField, SubmitField, RadioField,IntegerField
class ContactForm(FlaskForm):
    Name=TextField('Name of Student',[validators.Required('Please Enter Your Name!')])
    Gender=RadioField('Gender', choices=[('M','Male'),('F','Female')])
    Address=TextAreaField('Address')
    Email = TextField('Email', [validators.Required('Please Enter Email ....')])
    Age=IntegerField('Age')
    Language=RadioField('Languages',choices=[('cpp'),('py')])
    Submit=SubmitField('Submit')



